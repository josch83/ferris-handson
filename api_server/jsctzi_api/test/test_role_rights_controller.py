# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from jsctzi_api.models.new_role_rights import NewRoleRights  # noqa: E501
from jsctzi_api.models.role_rights import RoleRights  # noqa: E501
from jsctzi_api.test import BaseTestCase


class TestRoleRightsController(BaseTestCase):
    """RoleRightsController integration test stubs"""

    def test_create_role_rights(self):
        """Test case for create_role_rights

        Create a new role_rights
        """
        body = RoleRights()
        response = self.client.open(
            '/role_rights',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_role_rights_by_id(self):
        """Test case for get_role_rights_by_id

        Get a role_rights by ID
        """
        response = self.client.open(
            '/role_rights/{oid}'.format(oid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_role_rightss(self):
        """Test case for get_role_rightss

        Get all role_rights IDs
        """
        query_string = [('offset', 2),
                        ('limit', 2),
                        ('order_by', 'order_by_example'),
                        ('list_fields', 'list_fields_example'),
                        ('equal_can_access', true),
                        ('not_can_access', true),
                        ('isnull_can_access', true),
                        ('equal_can_create', true),
                        ('not_can_create', true),
                        ('isnull_can_create', true),
                        ('equal_can_delete', true),
                        ('not_can_delete', true),
                        ('isnull_can_delete', true),
                        ('equal_can_read', true),
                        ('not_can_read', true),
                        ('isnull_can_read', true),
                        ('equal_can_update', true),
                        ('not_can_update', true),
                        ('isnull_can_update', true),
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
                        ('entity', 'entity_example'),
                        ('not_entity', 'not_entity_example'),
                        ('ilike_entity', 'ilike_entity_example'),
                        ('notilike_entity', 'notilike_entity_example'),
                        ('isnull_entity', true),
                        ('equal_id', 56),
                        ('not_id', 56),
                        ('in_list_id', 56),
                        ('gte_id', 56),
                        ('lte_id', 56),
                        ('equal_role', 'equal_role_example'),
                        ('not_role', 'not_role_example'),
                        ('in_list_role', 'in_list_role_example'),
                        ('isnull_role', true)]
        response = self.client.open(
            '/role_rights',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_role_rights_by_id(self):
        """Test case for update_role_rights_by_id

        Update the role_rights
        """
        body = RoleRights()
        response = self.client.open(
            '/role_rights/{oid}'.format(oid=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
