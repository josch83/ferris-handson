# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from jsctzi_api.models.base_model_ import Model
from jsctzi_api import util


class NewAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, oid: int=None):  # noqa: E501
        """NewAddress - a model defined in Swagger

        :param oid: The oid of this NewAddress.  # noqa: E501
        :type oid: int
        """
        self.swagger_types = {
            'oid': int
        }

        self.attribute_map = {
            'oid': 'oid'
        }
        self._oid = oid

    @classmethod
    def from_dict(cls, dikt) -> 'NewAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The New address of this NewAddress.  # noqa: E501
        :rtype: NewAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def oid(self) -> int:
        """Gets the oid of this NewAddress.

        address ID  # noqa: E501

        :return: The oid of this NewAddress.
        :rtype: int
        """
        return self._oid

    @oid.setter
    def oid(self, oid: int):
        """Sets the oid of this NewAddress.

        address ID  # noqa: E501

        :param oid: The oid of this NewAddress.
        :type oid: int
        """

        self._oid = oid
