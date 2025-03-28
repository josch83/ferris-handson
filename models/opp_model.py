import io
import zipfile
from datetime import timedelta

import yaml
# This must be imported here, other import it from here

from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    ForeignKey,
    DATE,
    DateTime,
    JSON,
    Boolean,
    Table,
    Identity,
    func, UniqueConstraint,
)
from sqlalchemy import inspect
from sqlalchemy.orm import relationship
from sqlalchemy.sql import or_
from sqlalchemy import event

from .api_classes import (
    AuditAPI,
    Base,
    engine,
    session,
    minio_file_structure,
    minio_file_list,
    minio_client,
    minio_external_client,
    minio_build_url,
    role_access,
    RoleRights,
    roles,
    entities,
    init_role_rights,
)

"""  # #####################################################
     Enum Definitions
"""  # #####################################################

access_level = ("Public", "User", "Expert", "Client", "Partner")
access_level_enum = Enum(*access_level, name="access_level", native_enum=False)

entity_types = ["Taggable Entity", "Contact"]
entity_type_enum = Enum(*entity_types, name="entity_types", native_enum=False)

organization_type = ("Legal Entity", "Non-Profit", "Virtual", "Group", "others")
organization_type_enum = Enum(
    *organization_type, name="organization_type", native_enum=False
)

record_status = (
    "active",
    "in use",
    "blocked",
    "archived",
)
record_status_enum = Enum(*record_status, name="record_status", native_enum=False)

user_status = {
    "requested",
    "approved",
    "denied",
    "deactivated",
}
user_status_enum = Enum(*user_status, name="user_status", native_enum=False)

onboarding_flags = ("active", "planned", "sunset", "prohibited")
onboarding_flag_enum = Enum(
    *onboarding_flags, name="onboarding_flags", native_enum=False
)

high_risk_country_flags = ("standard risk", "high risk", "prohibited")
high_risk_country_flag_enum = Enum(
    *high_risk_country_flags, name="high_risk_country_flags", native_enum=False
)

# #####################################################
#     Sub Structure components
# #####################################################

# openapi component spec for address
address = {
    "type": "object",
    "properties": {
        "line1": {"type": "string", "x-nullable": True},
        "line2": {"type": "string", "x-nullable": True},
        "zip_code": {"type": "string", "x-nullable": True},
        "city": {"type": "string", "x-nullable": True},
        "state": {"type": "string", "x-nullable": True},
        "country": {"type": "string", "x-nullable": True},
    },
}

# openapi component spec for list of URL's
url_list = {"type": "array", "items": {"type": "string"}}

"""  # #####################################################
     ORM Model of the DB Schema
"""  # #####################################################

tagging_table = Table(
    "tagging",
    Base.metadata,
    Column("tag_id", String, ForeignKey("tag.id"), primary_key=True),
    # Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
    Column("entity_id", Integer, ForeignKey("taggable_entity.id"), primary_key=True),
)


class Tag(AuditAPI, Base):
    __tablename__ = "tag"
    __related__ = {"tagged_entities": "TaggableEntity"}
    # id = Column(Integer, primary_key=True, autoincrement=True)
    # description = Column(String, unique=True)
    id = Column(String, primary_key=True)
    tagged_entities = relationship(
        "TaggableEntity", secondary=tagging_table, back_populates="tags"
    )

    def __repr__(self):
        return self.description


class TaggableEntity(AuditAPI, Base):
    __generate_api__ = False
    __tablename__ = "taggable_entity"
    __related__ = {"tags": "Tag"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    entity_type = Column(entity_type_enum, nullable=False)
    tags = relationship(
        "Tag", secondary=tagging_table, back_populates="tagged_entities"
    )
    __mapper_args__ = {"polymorphic_identity": "Taggable Entity", "polymorphic_on": entity_type}


class Country(AuditAPI, Base):
    """
    List of countries to server as Reference
    """
    __tablename__ = "country"
    id = Column(String, primary_key=True)  # country_iso3
    country_iso = Column(String)
    name_short = Column(String)
    name_long = Column(String)
    eu_member = Column(Boolean)
    sepa_member = Column(Boolean)
    un_member = Column(Boolean)
    onboarding_flag = Column(onboarding_flag_enum)
    high_risk_country_flag = Column(high_risk_country_flag_enum)
    valid_from = Column(DATE)

    def __repr__(self):
        return f"{self.id} {self.name_short}"


org_contact_rel_table = Table(
    "org_contact_rel",
    Base.metadata,
    Column("organization_id", Integer, ForeignKey("organization.id"), primary_key=True),
    Column("contact_id", Integer, ForeignKey("contact.id"), primary_key=True)
)


class Organization(AuditAPI, Base):
    __generate_api__ = True
    __tablename__ = "organization"
    __virtual_fields__ = {
        "contact_count": "integer",
    }
    id = Column(Integer, primary_key=True, autoincrement=True)

    industry = Column(String, nullable=False, comment="Industry the organization belongs to")
    name = Column(String, nullable=False, comment="Name of Organization")
    country_id = Column(
        String, ForeignKey("country.id"), nullable=False, comment="ID of Country"
    )
    no_employees = Column(
        Integer,
        nullable=True,
        comment="Number of Employees / Members the Organization has",
        default=None,
    )
    org_url = Column(String, nullable=False, comment="URL of Organization")
    li_org_url = Column(String, nullable=False, comment="URL of Organization's LinkedIn Profile")
    org_description = Column(String, nullable=False, comment="Short Description of Organization")
    source = Column(String, nullable=False, comment="Source of Organization")
    apollo_id = Column(String, nullable=False, comment="Apollo ID of Organisation / Account")
    __table_args__ = (UniqueConstraint("source", "apollo_id", name="external_unique_organization_key"),)
    contacts = relationship("Contact", secondary="org_contact_rel", back_populates="organizations")

    def contact_count(self):
        return len(self.contacts)

    def __repr__(self):
        return f"{self.id}|{self.name}"


class Contact(TaggableEntity):
    __generate_api__ = {"find", "create", "read", "update", "delete"}
    __tablename__ = "contact"

    id = Column(
        Integer,
        ForeignKey("taggable_entity.id"),
        primary_key=True,
        comment="ID of Contact / Person",
    )
    first_name = Column(String, nullable=False, comment="First Name of Contact")
    last_name = Column(String, nullable=False, comment="Last Name / Given Name of Contact")
    title = Column(String, nullable=False, comment="Professional Title of Contact")
    email = Column(String, nullable=False, comment="Email Address of Contact")
    company = Column(String, nullable=False, comment="Company Name of Contact")
    industry = Column(String, nullable=False, comment="Industry the contact belongs to")
    city = Column(String, nullable=False, comment="City / Location of Contact")
    country_id = Column(
        String, ForeignKey("country.id"), nullable=False, comment="ID of Country"
    )
    con_org_url = Column(String, nullable=False, comment="URL of Organization (according to Contact)")
    con_li_org_url = Column(String, nullable=False,
                            comment="URL of Organization's LinkedIn Profile (according to Contact)")
    contact_url = Column(String, nullable=False, comment="URL of Contact's LinkedIn Profile")
    source = Column(String, nullable=False, comment="Source of Organization")
    org_apollo_id = Column(String, nullable=False, comment="Apollo ID of Organisation / Account")
    con_apollo_id = Column(String, nullable=False, comment="Apollo ID of Contact / Person")
    status = Column(
        record_status_enum,
        nullable=False,
        comment="Status of the contact record in terms of usage",
    )
    organizations = relationship("Organization", secondary="org_contact_rel", back_populates="contacts")
    __table_args__ = (UniqueConstraint("source", "con_apollo_id", name="external_unique_contact_key"),)

    __mapper_args__ = {"polymorphic_identity": "Contact"}

    def __repr__(self):
        return f"{self.id}|{self.first_name}|{self.last_name}"


class User(AuditAPI, Base):
    __generate_api__ = {"find", "create", "read", "update", "delete"}
    __tablename__ = "user"
    __virtual_fields__ = {
        "user_profile_url": "string",
    }
    __special_types__ = {
        "profile": minio_file_structure
    }
    id = Column(Integer, Identity(start=100), primary_key=True, comment="ID of user")
    status = Column(
        user_status_enum,
        default="requested",
        comment="Status of the User",
    )
    username = Column(
        String,
        nullable=False,
        unique=True,
        comment="Account name of user for loging this app",
    )
    profile = Column(JSON)
    email = Column(String, nullable=False, unique=True, comment="Email of user")

    def __repr__(self):
        return self.email

    def user_profile_url(self):
        return minio_build_url(self.profile)

    def valid_object_create(self):
        found = (
                session.query(User.username, User.email)
                .filter(
                    or_(
                        func.lower(User.username) == func.lower(self.username),
                        func.lower(User.email) == func.lower(self.email),
                    )
                )
                .first()
                is not None
        )
        print(found, flush=True)
        print(f"User found: {found}", flush=True)
        if found:
            raise ValueError(f"Not possible: email or username are registered.")
        else:
            return True


# Create only tables, not already in the DB,
# if you changed your model you need to drop it first
# Base.metadata.drop_all(engine)
# it only drops tables in the metadata from the DB,
# tables in the DB and not in the metadata aren't affected

#  Create the schema in the DB
Base.metadata.create_all(engine)

# Do a simple query for error checking by sqla
session.query(User).first()

# Initialize the role_rights table with basic rights (read to all roles, write to 'admin')
# if it is empty
# if not session.query(RoleRights).all():
#    init_role_rights()
