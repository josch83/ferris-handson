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

class Address(object):
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
        'changed_by': 'str',
        'changed_on': 'datetime',
        'created_by': 'str',
        'created_on': 'datetime',
        'email_address': 'str',
        'id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'changed_by': 'changed_by',
        'changed_on': 'changed_on',
        'created_by': 'created_by',
        'created_on': 'created_on',
        'email_address': 'email_address',
        'id': 'id',
        'user_id': 'user_id'
    }

    def __init__(self, changed_by=None, changed_on=None, created_by=None, created_on=None, email_address=None, id=None, user_id=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._changed_by = None
        self._changed_on = None
        self._created_by = None
        self._created_on = None
        self._email_address = None
        self._id = None
        self._user_id = None
        self.discriminator = None
        if changed_by is not None:
            self.changed_by = changed_by
        if changed_on is not None:
            self.changed_on = changed_on
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        self.email_address = email_address
        if id is not None:
            self.id = id
        self.user_id = user_id

    @property
    def changed_by(self):
        """Gets the changed_by of this Address.  # noqa: E501

        User name/email of the user who last changed the record via API  # noqa: E501

        :return: The changed_by of this Address.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this Address.

        User name/email of the user who last changed the record via API  # noqa: E501

        :param changed_by: The changed_by of this Address.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def changed_on(self):
        """Gets the changed_on of this Address.  # noqa: E501

        Timestamp on which the record was last changed, automatically filled by the API  # noqa: E501

        :return: The changed_on of this Address.  # noqa: E501
        :rtype: datetime
        """
        return self._changed_on

    @changed_on.setter
    def changed_on(self, changed_on):
        """Sets the changed_on of this Address.

        Timestamp on which the record was last changed, automatically filled by the API  # noqa: E501

        :param changed_on: The changed_on of this Address.  # noqa: E501
        :type: datetime
        """

        self._changed_on = changed_on

    @property
    def created_by(self):
        """Gets the created_by of this Address.  # noqa: E501

        User name/email of the user who inserted the record via API  # noqa: E501

        :return: The created_by of this Address.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Address.

        User name/email of the user who inserted the record via API  # noqa: E501

        :param created_by: The created_by of this Address.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this Address.  # noqa: E501

        Timestamp on which the record was created, automatically filled by the API  # noqa: E501

        :return: The created_on of this Address.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Address.

        Timestamp on which the record was created, automatically filled by the API  # noqa: E501

        :param created_on: The created_on of this Address.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def email_address(self):
        """Gets the email_address of this Address.  # noqa: E501

        to be documented  # noqa: E501

        :return: The email_address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Address.

        to be documented  # noqa: E501

        :param email_address: The email_address of this Address.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def id(self):
        """Gets the id of this Address.  # noqa: E501

        to be documented  # noqa: E501

        :return: The id of this Address.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Address.

        to be documented  # noqa: E501

        :param id: The id of this Address.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this Address.  # noqa: E501

        to be documented  # noqa: E501

        :return: The user_id of this Address.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Address.

        to be documented  # noqa: E501

        :param user_id: The user_id of this Address.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
