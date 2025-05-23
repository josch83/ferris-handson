# coding: utf-8

"""
    ferris.ai None jsctzi

    API definition for ferris.ai None jsctzi  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@ferris.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import jsctzi_api_client
from jsctzi_api_client.api.address_api import AddressApi  # noqa: E501
from jsctzi_api_client.rest import ApiException


class TestAddressApi(unittest.TestCase):
    """AddressApi unit test stubs"""

    def setUp(self):
        self.api = AddressApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_address(self):
        """Test case for create_address

        Create a new address  # noqa: E501
        """
        pass

    def test_get_address_by_id(self):
        """Test case for get_address_by_id

        Get a address by ID  # noqa: E501
        """
        pass

    def test_get_addresss(self):
        """Test case for get_addresss

        Get all address IDs  # noqa: E501
        """
        pass

    def test_update_address_by_id(self):
        """Test case for update_address_by_id

        Update the address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
