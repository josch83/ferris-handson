from flask_appbuilder.models.filters import FilterRelation
from flask_appbuilder.models.generic import GenericColumn, GenericModel, GenericSession
from flask_appbuilder.models.generic.interface import GenericInterface


class FerrisGenericRelationshipType:
    MANY_TO_ONE = "MANYTOONE"
    MANY_TO_MANY = "MANYTOMANY"
    ONE_TO_ONE = "ONETOONE"


class FerrisGenericColumn(GenericColumn):
    """
    Extended FAB Generic column to support virtual relations between generic models
    """

    def __init__(
        self,
        col_type,
        primary_key=False,
        unique=False,
        nullable=False,
        foreign_key=None,
        foreign_key_class=None,
        relationship_type=None,
        read_only_fk=True,
    ):
        """
        :param col_type: Type of the column (str, int, date...)
        :param primary_key: True if column represents primary key
        :param unique: True if the column must have unique value
        :param nullable: True if column value can be None
        :param foreign_key: True if column represents "foreign key"
        :param foreign_key_class: name of the model class of foreign key
        :param relationship_type: Type of the relationship (FerrisGenericRelationshipType.MANY_TO_ONE, FerrisGenericRelationshipType.MANY_TO_MANY, FerrisGenericRelationshipType.ONE_TO_ONE)
        :param read_only_fk: True if object cannot be modified when rendered as related view
        """

        self.foreign_key = foreign_key
        self.foreign_key_class = foreign_key_class
        self.relationship_type = relationship_type
        self.read_only_fk = read_only_fk

        super().__init__(col_type, primary_key, unique, nullable)


class FerrisGenericModel(GenericModel):
    """
    Extended FAB GenericModel (if needed)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FerrisGenericSession(GenericSession):
    """
    Extended FAB GenericSession
    """

    def get(self, pk):
        """
        Overriden get method to prevent using of FAB session cache
        :param pk: primary key
        :return: instance of GenericModel
        """
        return super(FerrisGenericSession, self).get(pk)


class FilterRelationOneToManyEqual(FilterRelation):
    name = "Relation"
    arg_name = "rel_o_m"

    def apply(self, query, value):
        return query.equal(self.column_name, value)


class FilterRelationManyToManyEqual(FilterRelation):
    name = "Relation as many"
    arg_name = "rel_m_m"

    def apply_item(self, query, value_item):
        """
        Get object by column_name and value_item, then apply filter if object exists
        Query with new filter applied
        """
        class_string_name_related = self.datamodel.obj.properties[self.column_name].foreign_key_class
        import importlib
        from fab_addon_jsctzi_api.utils import convert_to_snake_case
        mod_name = (
            f"fab_addon_jsctzi_api.models.{convert_to_snake_case(class_string_name_related[:-5])}"
        )
        module = importlib.import_module(mod_name)
        class_ = getattr(module, class_string_name_related)
        target_col = None
        if class_string_name_related != "TagModel":
            for col, val in class_.__dict__.items():  # loop through originating model
                if not col.startswith("__"):
                    fkc = getattr(val, "foreign_key_class", None)
                    if fkc is not None:
                        if fkc == self.datamodel.obj._name:
                            target_col = col
                            break
        else:
            target_col = "tagged_entities"
        session_class_name = f"{class_string_name_related[:-5]}Session"
        session_ = getattr(module, session_class_name)
        orig_obj = session_().get(value_item)
        ids_list = getattr(orig_obj, target_col)
        if ids_list:
            return query.contains_related_item("id", ids_list)
        else:
            #print("We do not have ids", flush=True)
            ids_list = [-1]  # No user, sends a query that will give no results
            query.contains_related_item("id", ids_list)
        return query

    def apply(self, query, value):
        if isinstance(value, list):
            for value_item in value:
                query = self.apply_item(query, value_item)
            return query

        return self.apply_item(query, value)


class FerrisGenericInterface(GenericInterface):
    """
    Extended FAB Generic interface to support "relationships" on generic models
    """

    def __init__(self, obj, session=None):
        if not issubclass(obj, FerrisGenericModel):
            raise Exception("Model must be instance of FerrisGenericModel")

        self.FilterRelationOneToManyEqual = FilterRelationOneToManyEqual
        self.FilterRelationManyToManyEqual = FilterRelationManyToManyEqual

        super().__init__(obj, session)

        if self.session:
            self.session.query_class = obj._name

    def get_related_fk(self, model):
        for col_name in vars(self.obj):
            col = getattr(self.obj, col_name)

            if isinstance(col, FerrisGenericColumn) and col.foreign_key and col.foreign_key_class == model.__name__:
                return col_name

    def get_relationship_type(self, fk):
        """
        :param fk: foreign key name for which relationship type should be returned
        :return: type of relationship (one of FerrisGenericRelationshipType values)
        """
        col = self.obj.properties[fk]

        return col.relationship_type

    def is_relation_many_to_one(self, fk):
        col = self.obj.properties[fk]

        if (
            isinstance(col, FerrisGenericColumn)
            and col.foreign_key
            and col.relationship_type == FerrisGenericRelationshipType.MANY_TO_ONE
        ):
            return True

    def is_relation_many_to_many(self, fk):
        col = self.obj.properties[fk]

        if (
            isinstance(col, FerrisGenericColumn)
            and col.foreign_key
            and col.relationship_type == FerrisGenericRelationshipType.MANY_TO_MANY
        ):
            return True

    def is_relation_one_to_one(self, fk):
        col = self.obj.properties[fk]

        if (
            isinstance(col, FerrisGenericColumn)
            and col.foreign_key
            and col.relationship_type == FerrisGenericRelationshipType.ONE_TO_ONE
        ):
            return True

    def is_fk(self, col_name):
        return self.obj.properties[col_name].foreign_key

    def is_read_only_fk(self, col_name):
        return self.is_fk(col_name) and self.obj.properties[col_name].read_only_fk