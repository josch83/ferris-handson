import sys
import datetime
import inspect as sys_inspect
from decimal import Decimal

from sqlalchemy import (
    inspect,
    Column,
    Integer,
    ForeignKey,
    DateTime,
    Numeric,
    Enum,
    Boolean,
    String,
    MetaData,
    UniqueConstraint,
    Unicode,
)
from sqlalchemy.orm import DeclarativeBase, declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
import sqlalchemy.types as types
from sqlalchemy.sql.ddl import CreateSchema, DropSchema
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import FernetEngine

from ferris import (
    db,
    session,
    engine,
    minio_client,
    mycryptkey,
)


"""  # #####################################################
     Password type for the SQLA Model, correctly translated
     into the right openapi type specification
     {type: 'string', format: 'password'}
"""  # #####################################################


class Encrypted(StringEncryptedType):
    def __init__(self):
        super().__init__(Unicode, mycryptkey, FernetEngine)


"""  # #####################################################
     The following 2 types have special meaning for the API/UI generation:
     password is masked in the UI
     hidden is not exposed via API
"""  # #####################################################


class Password(Encrypted): pass


class Hidden(Encrypted): pass


# This gives only one MetaFata for all models we load, but we want different MeetaData for each model
# Base = declarative_base() # The pure SQLAlchemy way

class Base(DeclarativeBase):
    __abstract__ = True
    metadata = MetaData()

"""  # #####################################################
     Base Class for API generator
"""  # #####################################################


class BaseAPI:
    # Should this class have an API or not.
    __generate_api__ = True
    # Which template file to use to generate the controller
    __generator_template__ = "controller_template"
    # Additional end-points for operations on the entity, dict of name: method-name
    __operations__ = dict()
    # Used for json fields, to specify the jason objects
    __special_types__ = dict()
    # Which backref related entities should be there as list of ID's
    __related__ = dict()
    #  Which backref related entities should be there as complete objects
    __embedded__ = dict()
    # Which fields are read only, i.e. returned by the server, but must not be used in create/update
    __read_only_fields__ = list()
    # computed fields (read-only) and their types.
    __virtual_fields__ = dict()
    # a dictionary to map attribute names to their display names, default is the attr name itself
    __fields_with_name__ = dict()
    # a list of optional fields, must not contain DB required fields
    __optional__ = list()
    # a list of required fields, must contain every DB required field
    __required__ = list()
    # a list of read only fields, must not contain
    __readonly__ = list()
    # __optional__, __required__ and  __readonly__ must be pairwise disjoint
    # if all three are (), the DB settings for required and readonly (e.g. auto increment) are used
    # a dict with attr and values,
    # - used as filter on views attr_1 == val_1 and ... and attr_n == val_n
    # - used as value assertions on inserts
    __filter_condition__ = dict()
    # use this to set the api name, e.g. in case a table has multiple api's, default is to use the table name
    __api_name__ = None
    # operation names and description, must be a method of the object
    __operations__ = dict()

    @classmethod
    def all_related(cls) -> dict:
        """
        add inherited __related__ from superclasses
        """
        r = dict()
        for c in reversed(sys_inspect.getmro(cls)):
            if issubclass(c, BaseAPI):
                r.update(c.__related__)
        return r

    @classmethod
    def all_embedded(cls) -> dict:
        """
        add inherited __embedded__ from superclasses
        """
        r = dict()
        for c in reversed(sys_inspect.getmro(cls)):
            if issubclass(c, BaseAPI):
                r.update(c.__embedded__)
        return r

    def to_dict(self, exclude=None):
        """
        Make a dict (JSON) out of an SQLA-Object for sending
        """
        dict_result = dict()
        for column in inspect(self).mapper.columns:
            if column.key != exclude:
                if isinstance(column.type, Numeric) and isinstance(
                        getattr(self, column.key), Decimal
                ):
                    dict_result[column.key] = getattr(self, column.key).to_eng_string()
                else:
                    dict_result[column.key] = getattr(self, column.key)
        for k in self.__virtual_fields__:
            if callable(getattr(self, k)):  # virtual fields from methods
                dict_result[k] = getattr(self, k)()
            else: # virtual fields from properties
                dict_result[k] = getattr(self, k)
        for k in self.all_related():
            dict_result[k] = [v.id for v in getattr(self, k)]
        for k in self.all_embedded():
            backref_col = getattr(self.__class__, k).expression.right.name
            dict_result[k] = [v.to_dict(exclude=backref_col) for v in getattr(self, k)]
        return dict_result

    @classmethod
    def get_apiclass(cls, class_or_name):
        if sys_inspect.isclass(class_or_name):
            return class_or_name
        for c in cls. all_subclasses():
            if c.__name__ == class_or_name:
                return c
        raise NameError(f'No API class with name {class_or_name} found.')

    @classmethod
    def all_subclasses(cls):
        return set(cls.__subclasses__()).union(
            [s for c in cls.__subclasses__() for s in c.all_subclasses()])

    def from_dict(self, obj_dict):
        """
        make an SQLA-Object out of an received dict (JSON)
        """
        for column in inspect(self).mapper.columns:
            try:
                if isinstance(column.type, Numeric) and isinstance(
                        obj_dict[column.key], str
                ):
                    setattr(self, column.key, Decimal(obj_dict[column.key]))
                else:
                    setattr(self, column.key, obj_dict[column.key])
            except KeyError:
                pass
        # for key, value in obj_dict.items():
        #     setattr(self, key, value)
        for k, cn in self.all_related().items():
            api_class = BaseAPI.get_apiclass(cn)
            dl = []
            for n in obj_dict.get(k, []):
                rel_obj = db.session.query(api_class).filter_by(id=n).first()
                if not rel_obj:
                    raise LookupError(
                        f"Error: No '{api_class.__name__}' found with id='{n}'"
                    )
                dl.append(rel_obj)
            if obj_dict.get(k):
                setattr(self, k, dl)
        for k, cn in self.all_embedded().items():
            api_class = BaseAPI.get_apiclass(cn)
            dl = []
            for d in obj_dict[k]:
                dl.append(api_class().from_dict(d))
            setattr(self, k, dl)
        # pprint(self.to_dict())
        return self

    @hybrid_method
    def id_has_access(self, utag):
        """
        Record Level Access, default allow it
        """
        return True

    @id_has_access.expression
    def id_has_access(cls, utag):
        return True

    def valid_object_create(self):
        """
        check validity of self object, called by insert controller
        redefine on demand
        Should raise ValueError('Explanation') for invalid objects
        """
        return True

    def valid_object_update(self):
        """
        check validity of self object, called by update controller
        redefine on demand
        Should raise ValueError('Explanation') for invalid objects
        """
        return True

    @hybrid_property
    def modifiable(self):
        """
        Called before update and delete
        Check if the current DB records is modifiable or not (e.g. not a successfully executed transaction)
        """
        return True

    def set_writer(self, user):
        # Avoid error on non-audit classes
        pass

# #####################################################
#   Extension of API generator Base Class with Audit fields
# #####################################################


class AuditAPIbyString(BaseAPI):
    __read_only_fields__ = [
        "created_by",
        "created_on",
        "changed_by",
        "changed_on",
    ]
    created_on = Column(
        DateTime,
        default=datetime.datetime.now,
        nullable=False,
        comment="Timestamp on which the record was created, automatically filled by the API",
    )
    changed_on = Column(
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False,
        comment="Timestamp on which the record was last changed, automatically filled by the API",
    )
    created_by = Column(
        String,
        default=lambda ctx: ctx.current_parameters.get("changed_by"),
        nullable=False,
        comment="User name/email of the user who inserted the record via API",
    )
    changed_by = Column(
        String,
        nullable=False,
        comment="User name/email of the user who last changed the record via API",
    )

    def set_writer(self, user_token):
        # changed_by = user_token["email"]
        self.changed_by = user_token["preferred_username"]
        self.changed_on = datetime.datetime.now()


class AuditAPIbyID(BaseAPI):
    __read_only_fields__ = [
        "created_by_id",
        "created_on",
        "changed_by_id",
        "changed_on",
    ]
    created_on = Column(
        DateTime,
        default=datetime.datetime.now,
        nullable=False,
        comment="Timestamp on which the record was created, automatically filled by the API",
    )
    changed_on = Column(
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False,
        comment="Timestamp on which the record was last changed, automatically filled by the API",
    )

    @declared_attr
    def created_by_id(cls):
        return Column(
            Integer,
            ForeignKey("None.id"),
            # on insert take the same value as changed_by_id
            default=lambda ctx: ctx.current_parameters.get("changed_by_id"),
            nullable=False,
            comment="User ID of the user who inserted the record via API",
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "None",
            primaryjoin="%s.created_by_id == None.id" % cls.__name__,
            enable_typechecks=False,
        )

    @declared_attr
    def changed_by_id(cls):
        return Column(
            Integer,
            ForeignKey("None.id"),
            nullable=False,
            comment="User ID of the user who last changed the record via API",
        )

    @declared_attr
    def changed_by(cls):
        return relationship(
            "None",
            primaryjoin="%s.changed_by_id == None.id" % cls.__name__,
            enable_typechecks=False,
        )

    def set_writer(self, user_token):
        with db.engine.connect() as con:
            uid = con.execute(text('select id from public.None where email = :email'),
                        {"email": user_token["email"]}).first()
        if not uid:
            print('No user with email', user_token["email"], 'found', flush=True)
            raise ValueError(f'Illegal user for update/create, no user with email = {user_token["email"]} found in the DB')
        self.changed_by_id, = uid
        self.changed_on = datetime.datetime.now()


AuditAPI = AuditAPIbyString


# #####################################################
#  Pre defined JSON Types with special interpretations
# #####################################################

# openapi component spec for minio files
minio_file_structure = {
    "type": "object",
    "title": "minio_file_link",
    "description": "It represents a link to a minio file on minio.ferris.ai",
    "properties": {
        "bucket": {
            "type": "string",
            "title": "bucket",
            "description": "It represents the bucket in the storage",
        },
        "filepath": {
            "type": "string",
            "title": "filepath",
            "description": "It represents the filepath (including prefix)",
        },
    },
}

# openapi component spec for list of minio files
minio_file_list = {
    "type": "array",
    "items": {
        "type": "object",
        "title": "minio_file_link",
        "description": "It represents a link to a minio file on minio.ferris.ai",
        "properties": {
            "url": {
                "type": "string",
                "title": "url",
                "description": "It represents theURL of the server",
            },
            "description": {
                "type": "string",
                "title": "description",
                "description": "It represents the description",
            },
        },
    }
}


def minio_build_url(file_link):
    """
    Helper to build valid minio URLs out of file_structures
    """
    if file_link is None:
        return "No file link exists for this item"
    bucket_name = file_link.get("bucket", None)
    filepath = file_link.get("filepath", None)

    # Decide to return empty string or meaningful message that could be used in UI
    if bucket_name is None:
        return "Non existing bucket"
    if filepath is None:
        return "Non existing filepath"

    # Check an object exists in the bucket
    try:
        minio_client.stat_object(bucket_name, filepath)
    except:  # most probably not found
        return f"The file {filepath} was not found in our storage. Please upload it before working with it!"

    presigned_url = minio_external_client.presigned_get_object(
        bucket_name,
        filepath,
        expires=datetime.timedelta(seconds=10800),
    )

    return presigned_url


def git_build_url(git_ssh_url, file):
    if git_ssh_url and file:
        [host, repo] = git_ssh_url.split("@")[1].split(":")
        repo = repo.split(".")[0]
        return f"https://{host}/{repo}/tree/main/{file}"
    else:
        return None



# #####################################################
#  Role Access Rights Dummies
# #####################################################

# Cannot know them before loading them, so just the system given ones
entities = ['address', 'user_account', 'role_rights']
entity_enum = Enum(*entities, name="entities", native_enum=False)

roles = ['admin', 'user']
role_enum = Enum(*roles, name="roles", native_enum=False)

def role_access(ent, user_token, req):
    """
    Checks if the roles of the user have requested access to the entity
    :param ent:
    :type ent: string ENUM entities
    :param user_tag:
    :type user_tag: string
    :param req:
    :type req: string ENUM [can_access, can_read, can_create, can_update]

    """
    user_roles = user_token["roles"]
    rs = db.session.query(RoleRights).filter_by(entity=ent).all()
    for rec in rs:
        if rec.role in user_roles and getattr(rec, req, False):
            return True
    return False

class RoleRights(Base, AuditAPI):
    """
     The table defining the role based access rights.
     (ID based rights are hard-coded)
     """
    __generate_api__ = True

    __tablename__ = "role_rights"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, autoincrement=True, comment='Auto increment ID of the Entity')
    entity = Column(entity_enum)
    role = Column(role_enum)
    can_access = Column(Boolean)
    can_read = Column(Boolean)
    can_create = Column(Boolean)
    can_update = Column(Boolean)
    can_delete = Column(Boolean)
    UniqueConstraint("entity","role")

    def __repr__(self):
        return f"{self.entity} {self.role}"


def init_role_rights():
    for e in entities:
        for r in roles:
            rr = RoleRights()
            rr.entity = e
            rr.role = r
            rr.created_by = 'Initial'
            rr.changed_by = 'Initial'
            rr.can_access = True
            rr.can_read = True
            rr.can_create = r == 'admin'
            rr.can_update = r == 'admin'
            rr.can_delete = r == 'admin'
            session.add(rr)
    session.commit()