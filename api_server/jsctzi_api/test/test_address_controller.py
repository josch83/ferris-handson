# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jsctzi_api.models.address import Address  # noqa: E501
from jsctzi_api.models.new_address import NewAddress  # noqa: E501
from jsctzi_api.test import BaseTestCase


class TestAddressController(BaseTestCase):
    """AddressController integration test stubs"""

    def test_create_address(self):
        """Test case for create_address

        Create a new address
        """
        body = Address()
        response = self.client.open(
            '/address',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_address_by_id(self):
        """Test case for get_address_by_id

        Get a address by ID
        """
        response = self.client.open(
            '/address/{oid}'.format(oid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_addresss(self):
        """Test case for get_addresss

        Get all address IDs
        """
        query_string = [('offset', 2),
                        ('limit', 2),
                        ('order_by', 'order_by_example'),
                        ('list_fields', 'list_fields_example'),
                        ('changed_by', 'changed_by_example'),
                        ('not_changed_by', 'not_changed_by_example'),
                        ('ilike_changed_by', 'ilike_changed_by_example'),
                        ('notilike_changed_by', 'notilike_changed_by_example'),
                        ('gte_changed_on', 'gte_changed_on_example'),
                        ('lte_changed_on', 'lte_changed_on_example'),
                        ('created_by', 'created_by_example'),
                        ('not_created_by', 'not_created_by_example'),
                        ('ilike_created_by', 'ilike_created_by_example'),
                        ('notilike_created_by', 'notilike_created_by_example'),
                        ('gte_created_on', 'gte_created_on_example'),
                        ('lte_created_on', 'lte_created_on_example'),
                        ('email_address', 'email_address_example'),
                        ('not_email_address', 'not_email_address_example'),
                        ('ilike_email_address', 'ilike_email_address_example'),
                        ('notilike_email_address', 'notilike_email_address_example'),
                        ('equal_id', 56),
                        ('not_id', 56),
                        ('in_list_id', 56),
                        ('gte_id', 56),
                        ('lte_id', 56),
                        ('equal_user_id', 56),
                        ('not_user_id', 56),
                        ('in_list_user_id', 56),
                        ('gte_user_id', 56),
                        ('lte_user_id', 56)]
        response = self.client.open(
            '/address',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_address_by_id(self):
        """Test case for update_address_by_id

        Update the address
        """
        body = Address()
        response = self.client.open(
            '/address/{oid}'.format(oid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
