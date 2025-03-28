# coding: utf-8

"""
    ferris.ai ipt JSC & TZI

    API definition for ferris.ai ipt JSC & TZI  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@ferris.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from josch83_api_client.api_client import ApiClient


class AddressApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_address(self, body, **kwargs):  # noqa: E501
        """Create a new address  # noqa: E501

        Create a new address with new id and provided data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_address(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Address body: (required)
        :return: NewAddress
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_address_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_address_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_address_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new address  # noqa: E501

        Create a new address with new id and provided data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_address_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Address body: (required)
        :return: NewAddress
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
                    " to method create_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_address`")  # noqa: E501

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
            '/address', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NewAddress',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_by_id(self, oid, **kwargs):  # noqa: E501
        """Get a address by ID  # noqa: E501

        Get a address by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_by_id(oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int oid: address ID (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_by_id_with_http_info(oid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_by_id_with_http_info(oid, **kwargs)  # noqa: E501
            return data

    def get_address_by_id_with_http_info(self, oid, **kwargs):  # noqa: E501
        """Get a address by ID  # noqa: E501

        Get a address by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_by_id_with_http_info(oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int oid: address ID (required)
        :return: Address
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
                    " to method get_address_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'oid' is set
        if ('oid' not in params or
                params['oid'] is None):
            raise ValueError("Missing the required parameter `oid` when calling `get_address_by_id`")  # noqa: E501

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
            '/address/{oid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Address',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_addresss(self, **kwargs):  # noqa: E501
        """Get all address IDs  # noqa: E501

        Get all address IDs and names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_addresss(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Offset for start of  returned records
        :param int limit: Limit the amount of returned records
        :param str order_by: Column used for sorting. The format is [+|-]<column_name>
        :param list[str] list_fields: Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name>
        :param str changed_by: Search for addresss, where changed_by like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_changed_by: Search for addresss, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_changed_by: Search for addresss, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_changed_by: Search for addresss, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str gte_changed_on: Search for addresss, where changed_on >= input
        :param str lte_changed_on: Search for addresss, where changed_on <= input
        :param str created_by: Search for addresss, where created_by like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_created_by: Search for addresss, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_created_by: Search for addresss, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_created_by: Search for addresss, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str gte_created_on: Search for addresss, where created_on >= input
        :param str lte_created_on: Search for addresss, where created_on <= input
        :param str email_address: Search for addresss, where email_address like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_email_address: Search for addresss, where email_address notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_email_address: Search for addresss, where email_address ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_email_address: Search for addresss, where email_address notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param int equal_id: Search for addresss, where id == input
        :param int not_id: Search for addresss, where id != input
        :param list[int] in_list_id: Search for addresss, where id in input
        :param int gte_id: Search for addresss, where id >= input
        :param int lte_id: Search for addresss, where id <= input
        :param int equal_user_id: Search for addresss, where user_id == input
        :param int not_user_id: Search for addresss, where user_id != input
        :param list[int] in_list_user_id: Search for addresss, where user_id in input
        :param int gte_user_id: Search for addresss, where user_id >= input
        :param int lte_user_id: Search for addresss, where user_id <= input
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_addresss_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_addresss_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_addresss_with_http_info(self, **kwargs):  # noqa: E501
        """Get all address IDs  # noqa: E501

        Get all address IDs and names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_addresss_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Offset for start of  returned records
        :param int limit: Limit the amount of returned records
        :param str order_by: Column used for sorting. The format is [+|-]<column_name>
        :param list[str] list_fields: Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name>
        :param str changed_by: Search for addresss, where changed_by like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_changed_by: Search for addresss, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_changed_by: Search for addresss, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_changed_by: Search for addresss, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str gte_changed_on: Search for addresss, where changed_on >= input
        :param str lte_changed_on: Search for addresss, where changed_on <= input
        :param str created_by: Search for addresss, where created_by like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_created_by: Search for addresss, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_created_by: Search for addresss, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_created_by: Search for addresss, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str gte_created_on: Search for addresss, where created_on >= input
        :param str lte_created_on: Search for addresss, where created_on <= input
        :param str email_address: Search for addresss, where email_address like input (place the %-wildcard at start and/or end of the input yourself)
        :param str not_email_address: Search for addresss, where email_address notlike input (place the %-wildcard at start and/or end of the input yourself)
        :param str ilike_email_address: Search for addresss, where email_address ilike input (place the %-wildcard at start and/or end of the input yourself)
        :param str notilike_email_address: Search for addresss, where email_address notilike input (place the %-wildcard at start and/or end of the input yourself)
        :param int equal_id: Search for addresss, where id == input
        :param int not_id: Search for addresss, where id != input
        :param list[int] in_list_id: Search for addresss, where id in input
        :param int gte_id: Search for addresss, where id >= input
        :param int lte_id: Search for addresss, where id <= input
        :param int equal_user_id: Search for addresss, where user_id == input
        :param int not_user_id: Search for addresss, where user_id != input
        :param list[int] in_list_user_id: Search for addresss, where user_id in input
        :param int gte_user_id: Search for addresss, where user_id >= input
        :param int lte_user_id: Search for addresss, where user_id <= input
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'order_by', 'list_fields', 'changed_by', 'not_changed_by', 'ilike_changed_by', 'notilike_changed_by', 'gte_changed_on', 'lte_changed_on', 'created_by', 'not_created_by', 'ilike_created_by', 'notilike_created_by', 'gte_created_on', 'lte_created_on', 'email_address', 'not_email_address', 'ilike_email_address', 'notilike_email_address', 'equal_id', 'not_id', 'in_list_id', 'gte_id', 'lte_id', 'equal_user_id', 'not_user_id', 'in_list_user_id', 'gte_user_id', 'lte_user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_addresss" % key
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
        if 'email_address' in params:
            query_params.append(('email_address', params['email_address']))  # noqa: E501
        if 'not_email_address' in params:
            query_params.append(('not_email_address', params['not_email_address']))  # noqa: E501
        if 'ilike_email_address' in params:
            query_params.append(('ilike_email_address', params['ilike_email_address']))  # noqa: E501
        if 'notilike_email_address' in params:
            query_params.append(('notilike_email_address', params['notilike_email_address']))  # noqa: E501
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
        if 'equal_user_id' in params:
            query_params.append(('equal_user_id', params['equal_user_id']))  # noqa: E501
        if 'not_user_id' in params:
            query_params.append(('not_user_id', params['not_user_id']))  # noqa: E501
        if 'in_list_user_id' in params:
            query_params.append(('in_list_user_id', params['in_list_user_id']))  # noqa: E501
            collection_formats['in_list_user_id'] = 'multi'  # noqa: E501
        if 'gte_user_id' in params:
            query_params.append(('gte_user_id', params['gte_user_id']))  # noqa: E501
        if 'lte_user_id' in params:
            query_params.append(('lte_user_id', params['lte_user_id']))  # noqa: E501

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
            '/address', 'GET',
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

    def update_address_by_id(self, body, oid, **kwargs):  # noqa: E501
        """Update the address  # noqa: E501

        Update the address with the provided data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_address_by_id(body, oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Address body: (required)
        :param int oid: address ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_address_by_id_with_http_info(body, oid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_address_by_id_with_http_info(body, oid, **kwargs)  # noqa: E501
            return data

    def update_address_by_id_with_http_info(self, body, oid, **kwargs):  # noqa: E501
        """Update the address  # noqa: E501

        Update the address with the provided data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_address_by_id_with_http_info(body, oid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Address body: (required)
        :param int oid: address ID (required)
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
                    " to method update_address_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_address_by_id`")  # noqa: E501
        # verify the required parameter 'oid' is set
        if ('oid' not in params or
                params['oid'] is None):
            raise ValueError("Missing the required parameter `oid` when calling `update_address_by_id`")  # noqa: E501

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
            '/address/{oid}', 'PUT',
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
