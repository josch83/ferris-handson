# coding: utf-8

"""
    ferris.ai None jsctzi

    API definition for ferris.ai None jsctzi  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@ferris.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jsctzi_api_client.api_client import ApiClient


class RoleRightsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_role_rights(self, body, **kwargs):  # noqa: E501
        """Create a new role_rights  # noqa: E501

        Create a new role_rights with new id and provided data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_rights(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RoleRights body: (required)
        :return: NewRoleRights
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_role_rights_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_role_rights_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_role_rights_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new role_rights  # noqa: E501

        Create a new role_rights with new id and provided data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_rights_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RoleRights body: (required)
        :return: NewRoleRights
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_role_rights" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_role_rights`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/role_rights', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NewRoleRights',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_role_rights_by_id(self, oid, **kwargs):  # noqa: E501
        """Get a role_rights by ID  # noqa: E501

        Get a role_rights by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_rights_by_id(oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int oid: role_rights ID (required)
        :return: RoleRights
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_rights_by_id_with_http_info(oid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_role_rights_by_id_with_http_info(oid, **kwargs)  # noqa: E501
            return data

    def get_role_rights_by_id_with_http_info(self, oid, **kwargs):  # noqa: E501
        """Get a role_rights by ID  # noqa: E501

        Get a role_rights by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_rights_by_id_with_http_info(oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int oid: role_rights ID (required)
        :return: RoleRights
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role_rights_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'oid' is set
        if ('oid' not in params or
                params['oid'] is None):
            raise ValueError("Missing the required parameter `oid` when calling `get_role_rights_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'oid' in params:
            path_params['oid'] = params['oid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/role_rights/{oid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RoleRights',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_role_rightss(self, **kwargs):  # noqa: E501
        """Get all role_rights IDs  # noqa: E501

        Get all role_rights IDs and names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_rightss(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Offset for start of  returned records
        :param int limit: Limit the amount of returned records
        :param str order_by: Column used for sorting. The format is [+|-]<column_name>
        :param list[str] list_fields: Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name>
        :param bool equal_can_access: Search for role_rightss, where can_access == input
        :param bool not_can_access: Search for role_rightss, where can_access != input
        :param bool isnull_can_access: Search for role_rightss, where can_access isNull input
        :param bool equal_can_create: Search for role_rightss, where can_create == input
        :param bool not_can_create: Search for role_rightss, where can_create != input
        :param bool isnull_can_create: Search for role_rightss, where can_create isNull input
        :param bool equal_can_delete: Search for role_rightss, where can_delete == input
        :param bool not_can_delete: Search for role_rightss, where can_delete != input
        :param bool isnull_can_delete: Search for role_rightss, where can_delete isNull input
        :param bool equal_can_read: Search for role_rightss, where can_read == input
        :param bool not_can_read: Search for role_rightss, where can_read != input
        :param bool isnull_can_read: Search for role_rightss, where can_read isNull input
        :param bool equal_can_update: Search for role_rightss, where can_update == input
        :param bool not_can_update: Search for role_rightss, where can_update != input
        :param bool isnull_can_update: Search for role_rightss, where can_update isNull input
        :param str changed_by: Search for role_rightss, where changed_by like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_changed_by: Search for role_rightss, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_changed_by: Search for role_rightss, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_changed_by: Search for role_rightss, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str gte_changed_on: Search for role_rightss, where changed_on >= input
        :param str lte_changed_on: Search for role_rightss, where changed_on <= input
        :param str created_by: Search for role_rightss, where created_by like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_created_by: Search for role_rightss, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_created_by: Search for role_rightss, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_created_by: Search for role_rightss, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str gte_created_on: Search for role_rightss, where created_on >= input
        :param str lte_created_on: Search for role_rightss, where created_on <= input
        :param str entity: Search for role_rightss, where entity like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_entity: Search for role_rightss, where entity notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_entity: Search for role_rightss, where entity ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_entity: Search for role_rightss, where entity notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param bool isnull_entity: Search for role_rightss, where entity isNull input
        :param int equal_id: Search for role_rightss, where id == input
        :param int not_id: Search for role_rightss, where id != input
        :param list[int] in_list_id: Search for role_rightss, where id in input
        :param int gte_id: Search for role_rightss, where id >= input
        :param int lte_id: Search for role_rightss, where id <= input
        :param str equal_role: Search for role_rightss, where role == input
        :param str not_role: Search for role_rightss, where role != input
        :param list[str] in_list_role: Search for role_rightss, where role in input
        :param bool isnull_role: Search for role_rightss, where role isNull input
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_rightss_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_role_rightss_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_role_rightss_with_http_info(self, **kwargs):  # noqa: E501
        """Get all role_rights IDs  # noqa: E501

        Get all role_rights IDs and names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_rightss_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Offset for start of  returned records
        :param int limit: Limit the amount of returned records
        :param str order_by: Column used for sorting. The format is [+|-]<column_name>
        :param list[str] list_fields: Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name>
        :param bool equal_can_access: Search for role_rightss, where can_access == input
        :param bool not_can_access: Search for role_rightss, where can_access != input
        :param bool isnull_can_access: Search for role_rightss, where can_access isNull input
        :param bool equal_can_create: Search for role_rightss, where can_create == input
        :param bool not_can_create: Search for role_rightss, where can_create != input
        :param bool isnull_can_create: Search for role_rightss, where can_create isNull input
        :param bool equal_can_delete: Search for role_rightss, where can_delete == input
        :param bool not_can_delete: Search for role_rightss, where can_delete != input
        :param bool isnull_can_delete: Search for role_rightss, where can_delete isNull input
        :param bool equal_can_read: Search for role_rightss, where can_read == input
        :param bool not_can_read: Search for role_rightss, where can_read != input
        :param bool isnull_can_read: Search for role_rightss, where can_read isNull input
        :param bool equal_can_update: Search for role_rightss, where can_update == input
        :param bool not_can_update: Search for role_rightss, where can_update != input
        :param bool isnull_can_update: Search for role_rightss, where can_update isNull input
        :param str changed_by: Search for role_rightss, where changed_by like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_changed_by: Search for role_rightss, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_changed_by: Search for role_rightss, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_changed_by: Search for role_rightss, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str gte_changed_on: Search for role_rightss, where changed_on >= input
        :param str lte_changed_on: Search for role_rightss, where changed_on <= input
        :param str created_by: Search for role_rightss, where created_by like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_created_by: Search for role_rightss, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_created_by: Search for role_rightss, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_created_by: Search for role_rightss, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str gte_created_on: Search for role_rightss, where created_on >= input
        :param str lte_created_on: Search for role_rightss, where created_on <= input
        :param str entity: Search for role_rightss, where entity like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_entity: Search for role_rightss, where entity notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_entity: Search for role_rightss, where entity ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_entity: Search for role_rightss, where entity notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param bool isnull_entity: Search for role_rightss, where entity isNull input
        :param int equal_id: Search for role_rightss, where id == input
        :param int not_id: Search for role_rightss, where id != input
        :param list[int] in_list_id: Search for role_rightss, where id in input
        :param int gte_id: Search for role_rightss, where id >= input
        :param int lte_id: Search for role_rightss, where id <= input
        :param str equal_role: Search for role_rightss, where role == input
        :param str not_role: Search for role_rightss, where role != input
        :param list[str] in_list_role: Search for role_rightss, where role in input
        :param bool isnull_role: Search for role_rightss, where role isNull input
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'order_by', 'list_fields', 'equal_can_access', 'not_can_access', 'isnull_can_access', 'equal_can_create', 'not_can_create', 'isnull_can_create', 'equal_can_delete', 'not_can_delete', 'isnull_can_delete', 'equal_can_read', 'not_can_read', 'isnull_can_read', 'equal_can_update', 'not_can_update', 'isnull_can_update', 'changed_by', 'not_changed_by', 'ilike_changed_by', 'notilike_changed_by', 'gte_changed_on', 'lte_changed_on', 'created_by', 'not_created_by', 'ilike_created_by', 'notilike_created_by', 'gte_created_on', 'lte_created_on', 'entity', 'not_entity', 'ilike_entity', 'notilike_entity', 'isnull_entity', 'equal_id', 'not_id', 'in_list_id', 'gte_id', 'lte_id', 'equal_role', 'not_role', 'in_list_role', 'isnull_role']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role_rightss" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('OFFSET', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('LIMIT', params['limit']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('ORDER_BY', params['order_by']))  # noqa: E501
        if 'list_fields' in params:
            query_params.append(('LIST_FIELDS', params['list_fields']))  # noqa: E501
            collection_formats['LIST_FIELDS'] = 'multi'  # noqa: E501
        if 'equal_can_access' in params:
            query_params.append(('equal_can_access', params['equal_can_access']))  # noqa: E501
        if 'not_can_access' in params:
            query_params.append(('not_can_access', params['not_can_access']))  # noqa: E501
        if 'isnull_can_access' in params:
            query_params.append(('isnull_can_access', params['isnull_can_access']))  # noqa: E501
        if 'equal_can_create' in params:
            query_params.append(('equal_can_create', params['equal_can_create']))  # noqa: E501
        if 'not_can_create' in params:
            query_params.append(('not_can_create', params['not_can_create']))  # noqa: E501
        if 'isnull_can_create' in params:
            query_params.append(('isnull_can_create', params['isnull_can_create']))  # noqa: E501
        if 'equal_can_delete' in params:
            query_params.append(('equal_can_delete', params['equal_can_delete']))  # noqa: E501
        if 'not_can_delete' in params:
            query_params.append(('not_can_delete', params['not_can_delete']))  # noqa: E501
        if 'isnull_can_delete' in params:
            query_params.append(('isnull_can_delete', params['isnull_can_delete']))  # noqa: E501
        if 'equal_can_read' in params:
            query_params.append(('equal_can_read', params['equal_can_read']))  # noqa: E501
        if 'not_can_read' in params:
            query_params.append(('not_can_read', params['not_can_read']))  # noqa: E501
        if 'isnull_can_read' in params:
            query_params.append(('isnull_can_read', params['isnull_can_read']))  # noqa: E501
        if 'equal_can_update' in params:
            query_params.append(('equal_can_update', params['equal_can_update']))  # noqa: E501
        if 'not_can_update' in params:
            query_params.append(('not_can_update', params['not_can_update']))  # noqa: E501
        if 'isnull_can_update' in params:
            query_params.append(('isnull_can_update', params['isnull_can_update']))  # noqa: E501
        if 'changed_by' in params:
            query_params.append(('changed_by', params['changed_by']))  # noqa: E501
        if 'not_changed_by' in params:
            query_params.append(('not_changed_by', params['not_changed_by']))  # noqa: E501
        if 'ilike_changed_by' in params:
            query_params.append(('ilike_changed_by', params['ilike_changed_by']))  # noqa: E501
        if 'notilike_changed_by' in params:
            query_params.append(('notilike_changed_by', params['notilike_changed_by']))  # noqa: E501
        if 'gte_changed_on' in params:
            query_params.append(('gte_changed_on', params['gte_changed_on']))  # noqa: E501
        if 'lte_changed_on' in params:
            query_params.append(('lte_changed_on', params['lte_changed_on']))  # noqa: E501
        if 'created_by' in params:
            query_params.append(('created_by', params['created_by']))  # noqa: E501
        if 'not_created_by' in params:
            query_params.append(('not_created_by', params['not_created_by']))  # noqa: E501
        if 'ilike_created_by' in params:
            query_params.append(('ilike_created_by', params['ilike_created_by']))  # noqa: E501
        if 'notilike_created_by' in params:
            query_params.append(('notilike_created_by', params['notilike_created_by']))  # noqa: E501
        if 'gte_created_on' in params:
            query_params.append(('gte_created_on', params['gte_created_on']))  # noqa: E501
        if 'lte_created_on' in params:
            query_params.append(('lte_created_on', params['lte_created_on']))  # noqa: E501
        if 'entity' in params:
            query_params.append(('entity', params['entity']))  # noqa: E501
        if 'not_entity' in params:
            query_params.append(('not_entity', params['not_entity']))  # noqa: E501
        if 'ilike_entity' in params:
            query_params.append(('ilike_entity', params['ilike_entity']))  # noqa: E501
        if 'notilike_entity' in params:
            query_params.append(('notilike_entity', params['notilike_entity']))  # noqa: E501
        if 'isnull_entity' in params:
            query_params.append(('isnull_entity', params['isnull_entity']))  # noqa: E501
        if 'equal_id' in params:
            query_params.append(('equal_id', params['equal_id']))  # noqa: E501
        if 'not_id' in params:
            query_params.append(('not_id', params['not_id']))  # noqa: E501
        if 'in_list_id' in params:
            query_params.append(('in_list_id', params['in_list_id']))  # noqa: E501
            collection_formats['in_list_id'] = 'multi'  # noqa: E501
        if 'gte_id' in params:
            query_params.append(('gte_id', params['gte_id']))  # noqa: E501
        if 'lte_id' in params:
            query_params.append(('lte_id', params['lte_id']))  # noqa: E501
        if 'equal_role' in params:
            query_params.append(('equal_role', params['equal_role']))  # noqa: E501
        if 'not_role' in params:
            query_params.append(('not_role', params['not_role']))  # noqa: E501
        if 'in_list_role' in params:
            query_params.append(('in_list_role', params['in_list_role']))  # noqa: E501
            collection_formats['in_list_role'] = 'multi'  # noqa: E501
        if 'isnull_role' in params:
            query_params.append(('isnull_role', params['isnull_role']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/role_rights', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_role_rights_by_id(self, body, oid, **kwargs):  # noqa: E501
        """Update the role_rights  # noqa: E501

        Update the role_rights with the provided data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_role_rights_by_id(body, oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RoleRights body: (required)
        :param int oid: role_rights ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_role_rights_by_id_with_http_info(body, oid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_role_rights_by_id_with_http_info(body, oid, **kwargs)  # noqa: E501
            return data

    def update_role_rights_by_id_with_http_info(self, body, oid, **kwargs):  # noqa: E501
        """Update the role_rights  # noqa: E501

        Update the role_rights with the provided data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_role_rights_by_id_with_http_info(body, oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RoleRights body: (required)
        :param int oid: role_rights ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'oid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_role_rights_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_role_rights_by_id`")  # noqa: E501
        # verify the required parameter 'oid' is set
        if ('oid' not in params or
                params['oid'] is None):
            raise ValueError("Missing the required parameter `oid` when calling `update_role_rights_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'oid' in params:
            path_params['oid'] = params['oid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sso_auth']  # noqa: E501

        return self.api_client.call_api(
            '/role_rights/{oid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
