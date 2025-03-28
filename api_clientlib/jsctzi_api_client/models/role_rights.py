# coding: utf-8

"""
    ferris.ai None jsctzi

    API definition for ferris.ai None jsctzi  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@ferris.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RoleRights(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'can_access': 'bool',
        'can_create': 'bool',
        'can_delete': 'bool',
        'can_read': 'bool',
        'can_update': 'bool',
        'changed_by': 'str',
        'changed_on': 'datetime',
        'created_by': 'str',
        'created_on': 'datetime',
        'entity': 'str',
        'id': 'int',
        'role': 'str'
    }

    attribute_map = {
        'can_access': 'can_access',
        'can_create': 'can_create',
        'can_delete': 'can_delete',
        'can_read': 'can_read',
        'can_update': 'can_update',
        'changed_by': 'changed_by',
        'changed_on': 'changed_on',
        'created_by': 'created_by',
        'created_on': 'created_on',
        'entity': 'entity',
        'id': 'id',
        'role': 'role'
    }

    def __init__(self, can_access=None, can_create=None, can_delete=None, can_read=None, can_update=None, changed_by=None, changed_on=None, created_by=None, created_on=None, entity=None, id=None, role=None):  # noqa: E501
        """RoleRights - a model defined in Swagger"""  # noqa: E501
        self._can_access = None
        self._can_create = None
        self._can_delete = None
        self._can_read = None
        self._can_update = None
        self._changed_by = None
        self._changed_on = None
        self._created_by = None
        self._created_on = None
        self._entity = None
        self._id = None
        self._role = None
        self.discriminator = None
        if can_access is not None:
            self.can_access = can_access
        if can_create is not None:
            self.can_create = can_create
        if can_delete is not None:
            self.can_delete = can_delete
        if can_read is not None:
            self.can_read = can_read
        if can_update is not None:
            self.can_update = can_update
        if changed_by is not None:
            self.changed_by = changed_by
        if changed_on is not None:
            self.changed_on = changed_on
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if entity is not None:
            self.entity = entity
        if id is not None:
            self.id = id
        if role is not None:
            self.role = role

    @property
    def can_access(self):
        """Gets the can_access of this RoleRights.  # noqa: E501

        to be documented  # noqa: E501

        :return: The can_access of this RoleRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_access

    @can_access.setter
    def can_access(self, can_access):
        """Sets the can_access of this RoleRights.

        to be documented  # noqa: E501

        :param can_access: The can_access of this RoleRights.  # noqa: E501
        :type: bool
        """

        self._can_access = can_access

    @property
    def can_create(self):
        """Gets the can_create of this RoleRights.  # noqa: E501

        to be documented  # noqa: E501

        :return: The can_create of this RoleRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_create

    @can_create.setter
    def can_create(self, can_create):
        """Sets the can_create of this RoleRights.

        to be documented  # noqa: E501

        :param can_create: The can_create of this RoleRights.  # noqa: E501
        :type: bool
        """

        self._can_create = can_create

    @property
    def can_delete(self):
        """Gets the can_delete of this RoleRights.  # noqa: E501

        to be documented  # noqa: E501

        :return: The can_delete of this RoleRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this RoleRights.

        to be documented  # noqa: E501

        :param can_delete: The can_delete of this RoleRights.  # noqa: E501
        :type: bool
        """

        self._can_delete = can_delete

    @property
    def can_read(self):
        """Gets the can_read of this RoleRights.  # noqa: E501

        to be documented  # noqa: E501

        :return: The can_read of this RoleRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        """Sets the can_read of this RoleRights.

        to be documented  # noqa: E501

        :param can_read: The can_read of this RoleRights.  # noqa: E501
        :type: bool
        """

        self._can_read = can_read

    @property
    def can_update(self):
        """Gets the can_update of this RoleRights.  # noqa: E501

        to be documented  # noqa: E501

        :return: The can_update of this RoleRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_update

    @can_update.setter
    def can_update(self, can_update):
        """Sets the can_update of this RoleRights.

        to be documented  # noqa: E501

        :param can_update: The can_update of this RoleRights.  # noqa: E501
        :type: bool
        """

        self._can_update = can_update

    @property
    def changed_by(self):
        """Gets the changed_by of this RoleRights.  # noqa: E501

        User name/email of the user who last changed the record via API  # noqa: E501

        :return: The changed_by of this RoleRights.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this RoleRights.

        User name/email of the user who last changed the record via API  # noqa: E501

        :param changed_by: The changed_by of this RoleRights.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def changed_on(self):
        """Gets the changed_on of this RoleRights.  # noqa: E501

        Timestamp on which the record was last changed, automatically filled by the API  # noqa: E501

        :return: The changed_on of this RoleRights.  # noqa: E501
        :rtype: datetime
        """
        return self._changed_on

    @changed_on.setter
    def changed_on(self, changed_on):
        """Sets the changed_on of this RoleRights.

        Timestamp on which the record was last changed, automatically filled by the API  # noqa: E501

        :param changed_on: The changed_on of this RoleRights.  # noqa: E501
        :type: datetime
        """

        self._changed_on = changed_on

    @property
    def created_by(self):
        """Gets the created_by of this RoleRights.  # noqa: E501

        User name/email of the user who inserted the record via API  # noqa: E501

        :return: The created_by of this RoleRights.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RoleRights.

        User name/email of the user who inserted the record via API  # noqa: E501

        :param created_by: The created_by of this RoleRights.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this RoleRights.  # noqa: E501

        Timestamp on which the record was created, automatically filled by the API  # noqa: E501

        :return: The created_on of this RoleRights.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this RoleRights.

        Timestamp on which the record was created, automatically filled by the API  # noqa: E501

        :param created_on: The created_on of this RoleRights.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def entity(self):
        """Gets the entity of this RoleRights.  # noqa: E501

        to be documented  # noqa: E501

        :return: The entity of this RoleRights.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this RoleRights.

        to be documented  # noqa: E501

        :param entity: The entity of this RoleRights.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def id(self):
        """Gets the id of this RoleRights.  # noqa: E501

        Auto increment ID of the Entity  # noqa: E501

        :return: The id of this RoleRights.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleRights.

        Auto increment ID of the Entity  # noqa: E501

        :param id: The id of this RoleRights.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def role(self):
        """Gets the role of this RoleRights.  # noqa: E501

        to be documented  # noqa: E501

        :return: The role of this RoleRights.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RoleRights.

        to be documented  # noqa: E501

        :param role: The role of this RoleRights.  # noqa: E501
        :type: str
        """
        allowed_values = ["admin", "developer"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RoleRights, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RoleRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
