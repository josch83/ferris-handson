# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from magdemo_api.models.new_user_account import NewUserAccount  # noqa: E501
from magdemo_api.models.user_account import UserAccount  # noqa: E501
from magdemo_api.test import BaseTestCase


class TestUserAccountController(BaseTestCase):
    """UserAccountController integration test stubs"""

    def test_create_user_account(self):
        """Test case for create_user_account

        Create a new user_account
        """
        body = UserAccount()
        response = self.client.open(
            '/user_account',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_account_by_id(self):
        """Test case for get_user_account_by_id

        Get a user_account by ID
        """
        response = self.client.open(
            '/user_account/{oid}'.format(oid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_accounts(self):
        """Test case for get_user_accounts

        Get all user_account IDs
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
                        ('fullname', 'fullname_example'),
                        ('not_fullname', 'not_fullname_example'),
                        ('ilike_fullname', 'ilike_fullname_example'),
                        ('notilike_fullname', 'notilike_fullname_example'),
                        ('isnull_fullname', true),
                        ('equal_id', 56),
                        ('not_id', 56),
                        ('in_list_id', 56),
                        ('gte_id', 56),
                        ('lte_id', 56),
                        ('name', 'name_example'),
                        ('not_name', 'not_name_example'),
                        ('ilike_name', 'ilike_name_example'),
                        ('notilike_name', 'notilike_name_example'),
                        ('isnull_name', true)]
        response = self.client.open(
            '/user_account',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_account_by_id(self):
        """Test case for update_user_account_by_id

        Update the user_account
        """
        body = UserAccount()
        response = self.client.open(
            '/user_account/{oid}'.format(oid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
