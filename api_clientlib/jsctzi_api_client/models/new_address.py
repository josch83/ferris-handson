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

class NewAddress(object):
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
        'oid': 'int'
    }

    attribute_map = {
        'oid': 'oid'
    }

    def __init__(self, oid=None):  # noqa: E501
        """NewAddress - a model defined in Swagger"""  # noqa: E501
        self._oid = None
        self.discriminator = None
        if oid is not None:
            self.oid = oid

    @property
    def oid(self):
        """Gets the oid of this NewAddress.  # noqa: E501

        address ID  # noqa: E501

        :return: The oid of this NewAddress.  # noqa: E501
        :rtype: int
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this NewAddress.

        address ID  # noqa: E501

        :param oid: The oid of this NewAddress.  # noqa: E501
        :type: int
        """

        self._oid = oid

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
        if issubclass(NewAddress, dict):
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
        if not isinstance(other, NewAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
