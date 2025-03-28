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
    func,
    UniqueConstraint,
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
    role_access,
    RoleRights,
    roles,
    entities,
    init_role_rights,
)

"""  # #####################################################
     Enum Definitions
"""  # #####################################################
# Place your enum definitions, e.g. for UI popups here
# access_level = ("Public", "User", "Expert", "Client", "Partner")
# access_level_enum = Enum(*access_level, name="access_level", native_enum=False)

# #####################################################
#     Sub Structure components
# #####################################################

# Put structure definitions for JSON fields here
# openapi component spec for list of URL's
# url_list = {"type": "array", "items": {"type": "string"}}

"""  # #####################################################
     ORM Model of the DB Schema
"""  # #####################################################


# Put your SQL Alchemy ORM here, see the other models for examples


class UserAccount(AuditAPI,Base):
    __tablename__ = "user_account"
    __generate_api__ = True
    __related__ = {'addresses': 'Address'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(AuditAPI, Base):
    __tablename__ = "address"
    __generate_api__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("UserAccount", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


"""  # #####################################################
     BOTTOM of File
     After all model definitions above you can (re-) create 
     the DB in the database
"""  # #####################################################

# Create only tables, not already in the DB,
# if you changed your model you need to drop it first
# Base.metadata.drop_all(engine)
# it only drops tables in the metadata from the DB,
# tables in the DB and not in the metadata aren't affected

#  Create the schema in the DB
Base.metadata.create_all(engine)

# Do a simple query for error checking by sqla
session.query(UserAccount).first()

# Initialize the role_rights table with basic rights (read to all roles, write to 'admin')
# if it is empty
if not session.query(RoleRights).all():
   init_role_rights()
