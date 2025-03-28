# josch83_api_client.RoleRightsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_rights**](RoleRightsApi.md#create_role_rights) | **POST** /role_rights | Create a new role_rights
[**get_role_rights_by_id**](RoleRightsApi.md#get_role_rights_by_id) | **GET** /role_rights/{oid} | Get a role_rights by ID
[**get_role_rightss**](RoleRightsApi.md#get_role_rightss) | **GET** /role_rights | Get all role_rights IDs
[**update_role_rights_by_id**](RoleRightsApi.md#update_role_rights_by_id) | **PUT** /role_rights/{oid} | Update the role_rights

# **create_role_rights**
> NewRoleRights create_role_rights(body)

Create a new role_rights

Create a new role_rights with new id and provided data

### Example
```python
from __future__ import print_function
import time
import josch83_api_client
from josch83_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = josch83_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = josch83_api_client.RoleRightsApi(josch83_api_client.ApiClient(configuration))
body = josch83_api_client.RoleRights() # RoleRights | 

try:
    # Create a new role_rights
    api_response = api_instance.create_role_rights(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleRightsApi->create_role_rights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleRights**](RoleRights.md)|  | 

### Return type

[**NewRoleRights**](NewRoleRights.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_rights_by_id**
> RoleRights get_role_rights_by_id(oid)

Get a role_rights by ID

Get a role_rights by ID

### Example
```python
from __future__ import print_function
import time
import josch83_api_client
from josch83_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = josch83_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = josch83_api_client.RoleRightsApi(josch83_api_client.ApiClient(configuration))
oid = 56 # int | role_rights ID

try:
    # Get a role_rights by ID
    api_response = api_instance.get_role_rights_by_id(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleRightsApi->get_role_rights_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**| role_rights ID | 

### Return type

[**RoleRights**](RoleRights.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_rightss**
> list[object] get_role_rightss(offset=offset, limit=limit, order_by=order_by, list_fields=list_fields, equal_can_access=equal_can_access, not_can_access=not_can_access, isnull_can_access=isnull_can_access, equal_can_create=equal_can_create, not_can_create=not_can_create, isnull_can_create=isnull_can_create, equal_can_delete=equal_can_delete, not_can_delete=not_can_delete, isnull_can_delete=isnull_can_delete, equal_can_read=equal_can_read, not_can_read=not_can_read, isnull_can_read=isnull_can_read, equal_can_update=equal_can_update, not_can_update=not_can_update, isnull_can_update=isnull_can_update, changed_by=changed_by, not_changed_by=not_changed_by, ilike_changed_by=ilike_changed_by, notilike_changed_by=notilike_changed_by, gte_changed_on=gte_changed_on, lte_changed_on=lte_changed_on, created_by=created_by, not_created_by=not_created_by, ilike_created_by=ilike_created_by, notilike_created_by=notilike_created_by, gte_created_on=gte_created_on, lte_created_on=lte_created_on, entity=entity, not_entity=not_entity, ilike_entity=ilike_entity, notilike_entity=notilike_entity, isnull_entity=isnull_entity, equal_id=equal_id, not_id=not_id, in_list_id=in_list_id, gte_id=gte_id, lte_id=lte_id, equal_role=equal_role, not_role=not_role, in_list_role=in_list_role, isnull_role=isnull_role)

Get all role_rights IDs

Get all role_rights IDs and names

### Example
```python
from __future__ import print_function
import time
import josch83_api_client
from josch83_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = josch83_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = josch83_api_client.RoleRightsApi(josch83_api_client.ApiClient(configuration))
offset = 56 # int | Offset for start of  returned records (optional)
limit = 56 # int | Limit the amount of returned records (optional)
order_by = 'order_by_example' # str | Column used for sorting. The format is [+|-]<column_name> (optional)
list_fields = ['list_fields_example'] # list[str] | Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name> (optional)
equal_can_access = true # bool | Search for role_rightss, where can_access == input (optional)
not_can_access = true # bool | Search for role_rightss, where can_access != input (optional)
isnull_can_access = true # bool | Search for role_rightss, where can_access isNull input (optional)
equal_can_create = true # bool | Search for role_rightss, where can_create == input (optional)
not_can_create = true # bool | Search for role_rightss, where can_create != input (optional)
isnull_can_create = true # bool | Search for role_rightss, where can_create isNull input (optional)
equal_can_delete = true # bool | Search for role_rightss, where can_delete == input (optional)
not_can_delete = true # bool | Search for role_rightss, where can_delete != input (optional)
isnull_can_delete = true # bool | Search for role_rightss, where can_delete isNull input (optional)
equal_can_read = true # bool | Search for role_rightss, where can_read == input (optional)
not_can_read = true # bool | Search for role_rightss, where can_read != input (optional)
isnull_can_read = true # bool | Search for role_rightss, where can_read isNull input (optional)
equal_can_update = true # bool | Search for role_rightss, where can_update == input (optional)
not_can_update = true # bool | Search for role_rightss, where can_update != input (optional)
isnull_can_update = true # bool | Search for role_rightss, where can_update isNull input (optional)
changed_by = 'changed_by_example' # str | Search for role_rightss, where changed_by like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_changed_by = 'not_changed_by_example' # str | Search for role_rightss, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_changed_by = 'ilike_changed_by_example' # str | Search for role_rightss, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_changed_by = 'notilike_changed_by_example' # str | Search for role_rightss, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
gte_changed_on = 'gte_changed_on_example' # str | Search for role_rightss, where changed_on >= input (optional)
lte_changed_on = 'lte_changed_on_example' # str | Search for role_rightss, where changed_on <= input (optional)
created_by = 'created_by_example' # str | Search for role_rightss, where created_by like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_created_by = 'not_created_by_example' # str | Search for role_rightss, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_created_by = 'ilike_created_by_example' # str | Search for role_rightss, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_created_by = 'notilike_created_by_example' # str | Search for role_rightss, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
gte_created_on = 'gte_created_on_example' # str | Search for role_rightss, where created_on >= input (optional)
lte_created_on = 'lte_created_on_example' # str | Search for role_rightss, where created_on <= input (optional)
entity = 'entity_example' # str | Search for role_rightss, where entity like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_entity = 'not_entity_example' # str | Search for role_rightss, where entity notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_entity = 'ilike_entity_example' # str | Search for role_rightss, where entity ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_entity = 'notilike_entity_example' # str | Search for role_rightss, where entity notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
isnull_entity = true # bool | Search for role_rightss, where entity isNull input (optional)
equal_id = 56 # int | Search for role_rightss, where id == input (optional)
not_id = 56 # int | Search for role_rightss, where id != input (optional)
in_list_id = [56] # list[int] | Search for role_rightss, where id in input (optional)
gte_id = 56 # int | Search for role_rightss, where id >= input (optional)
lte_id = 56 # int | Search for role_rightss, where id <= input (optional)
equal_role = 'equal_role_example' # str | Search for role_rightss, where role == input (optional)
not_role = 'not_role_example' # str | Search for role_rightss, where role != input (optional)
in_list_role = ['in_list_role_example'] # list[str] | Search for role_rightss, where role in input (optional)
isnull_role = true # bool | Search for role_rightss, where role isNull input (optional)

try:
    # Get all role_rights IDs
    api_response = api_instance.get_role_rightss(offset=offset, limit=limit, order_by=order_by, list_fields=list_fields, equal_can_access=equal_can_access, not_can_access=not_can_access, isnull_can_access=isnull_can_access, equal_can_create=equal_can_create, not_can_create=not_can_create, isnull_can_create=isnull_can_create, equal_can_delete=equal_can_delete, not_can_delete=not_can_delete, isnull_can_delete=isnull_can_delete, equal_can_read=equal_can_read, not_can_read=not_can_read, isnull_can_read=isnull_can_read, equal_can_update=equal_can_update, not_can_update=not_can_update, isnull_can_update=isnull_can_update, changed_by=changed_by, not_changed_by=not_changed_by, ilike_changed_by=ilike_changed_by, notilike_changed_by=notilike_changed_by, gte_changed_on=gte_changed_on, lte_changed_on=lte_changed_on, created_by=created_by, not_created_by=not_created_by, ilike_created_by=ilike_created_by, notilike_created_by=notilike_created_by, gte_created_on=gte_created_on, lte_created_on=lte_created_on, entity=entity, not_entity=not_entity, ilike_entity=ilike_entity, notilike_entity=notilike_entity, isnull_entity=isnull_entity, equal_id=equal_id, not_id=not_id, in_list_id=in_list_id, gte_id=gte_id, lte_id=lte_id, equal_role=equal_role, not_role=not_role, in_list_role=in_list_role, isnull_role=isnull_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleRightsApi->get_role_rightss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for start of  returned records | [optional] 
 **limit** | **int**| Limit the amount of returned records | [optional] 
 **order_by** | **str**| Column used for sorting. The format is [+|-]&lt;column_name&gt; | [optional] 
 **list_fields** | [**list[str]**](str.md)| Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name&gt; | [optional] 
 **equal_can_access** | **bool**| Search for role_rightss, where can_access &#x3D;&#x3D; input | [optional] 
 **not_can_access** | **bool**| Search for role_rightss, where can_access !&#x3D; input | [optional] 
 **isnull_can_access** | **bool**| Search for role_rightss, where can_access isNull input | [optional] 
 **equal_can_create** | **bool**| Search for role_rightss, where can_create &#x3D;&#x3D; input | [optional] 
 **not_can_create** | **bool**| Search for role_rightss, where can_create !&#x3D; input | [optional] 
 **isnull_can_create** | **bool**| Search for role_rightss, where can_create isNull input | [optional] 
 **equal_can_delete** | **bool**| Search for role_rightss, where can_delete &#x3D;&#x3D; input | [optional] 
 **not_can_delete** | **bool**| Search for role_rightss, where can_delete !&#x3D; input | [optional] 
 **isnull_can_delete** | **bool**| Search for role_rightss, where can_delete isNull input | [optional] 
 **equal_can_read** | **bool**| Search for role_rightss, where can_read &#x3D;&#x3D; input | [optional] 
 **not_can_read** | **bool**| Search for role_rightss, where can_read !&#x3D; input | [optional] 
 **isnull_can_read** | **bool**| Search for role_rightss, where can_read isNull input | [optional] 
 **equal_can_update** | **bool**| Search for role_rightss, where can_update &#x3D;&#x3D; input | [optional] 
 **not_can_update** | **bool**| Search for role_rightss, where can_update !&#x3D; input | [optional] 
 **isnull_can_update** | **bool**| Search for role_rightss, where can_update isNull input | [optional] 
 **changed_by** | **str**| Search for role_rightss, where changed_by like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_changed_by** | **str**| Search for role_rightss, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_changed_by** | **str**| Search for role_rightss, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_changed_by** | **str**| Search for role_rightss, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **gte_changed_on** | **str**| Search for role_rightss, where changed_on &gt;&#x3D; input | [optional] 
 **lte_changed_on** | **str**| Search for role_rightss, where changed_on &lt;&#x3D; input | [optional] 
 **created_by** | **str**| Search for role_rightss, where created_by like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_created_by** | **str**| Search for role_rightss, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_created_by** | **str**| Search for role_rightss, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_created_by** | **str**| Search for role_rightss, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **gte_created_on** | **str**| Search for role_rightss, where created_on &gt;&#x3D; input | [optional] 
 **lte_created_on** | **str**| Search for role_rightss, where created_on &lt;&#x3D; input | [optional] 
 **entity** | **str**| Search for role_rightss, where entity like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_entity** | **str**| Search for role_rightss, where entity notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_entity** | **str**| Search for role_rightss, where entity ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_entity** | **str**| Search for role_rightss, where entity notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **isnull_entity** | **bool**| Search for role_rightss, where entity isNull input | [optional] 
 **equal_id** | **int**| Search for role_rightss, where id &#x3D;&#x3D; input | [optional] 
 **not_id** | **int**| Search for role_rightss, where id !&#x3D; input | [optional] 
 **in_list_id** | [**list[int]**](int.md)| Search for role_rightss, where id in input | [optional] 
 **gte_id** | **int**| Search for role_rightss, where id &gt;&#x3D; input | [optional] 
 **lte_id** | **int**| Search for role_rightss, where id &lt;&#x3D; input | [optional] 
 **equal_role** | **str**| Search for role_rightss, where role &#x3D;&#x3D; input | [optional] 
 **not_role** | **str**| Search for role_rightss, where role !&#x3D; input | [optional] 
 **in_list_role** | [**list[str]**](str.md)| Search for role_rightss, where role in input | [optional] 
 **isnull_role** | **bool**| Search for role_rightss, where role isNull input | [optional] 

### Return type

**list[object]**

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_rights_by_id**
> update_role_rights_by_id(body, oid)

Update the role_rights

Update the role_rights with the provided data

### Example
```python
from __future__ import print_function
import time
import josch83_api_client
from josch83_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = josch83_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = josch83_api_client.RoleRightsApi(josch83_api_client.ApiClient(configuration))
body = josch83_api_client.RoleRights() # RoleRights | 
oid = 56 # int | role_rights ID

try:
    # Update the role_rights
    api_instance.update_role_rights_by_id(body, oid)
except ApiException as e:
    print("Exception when calling RoleRightsApi->update_role_rights_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleRights**](RoleRights.md)|  | 
 **oid** | **int**| role_rights ID | 

### Return type

void (empty response body)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

