# magdemo_api_client.UserAccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_account**](UserAccountApi.md#create_user_account) | **POST** /user_account | Create a new user_account
[**get_user_account_by_id**](UserAccountApi.md#get_user_account_by_id) | **GET** /user_account/{oid} | Get a user_account by ID
[**get_user_accounts**](UserAccountApi.md#get_user_accounts) | **GET** /user_account | Get all user_account IDs
[**update_user_account_by_id**](UserAccountApi.md#update_user_account_by_id) | **PUT** /user_account/{oid} | Update the user_account

# **create_user_account**
> NewUserAccount create_user_account(body)

Create a new user_account

Create a new user_account with new id and provided data

### Example
```python
from __future__ import print_function
import time
import magdemo_api_client
from magdemo_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = magdemo_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = magdemo_api_client.UserAccountApi(magdemo_api_client.ApiClient(configuration))
body = magdemo_api_client.UserAccount() # UserAccount | 

try:
    # Create a new user_account
    api_response = api_instance.create_user_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountApi->create_user_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccount**](UserAccount.md)|  | 

### Return type

[**NewUserAccount**](NewUserAccount.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_account_by_id**
> UserAccount get_user_account_by_id(oid)

Get a user_account by ID

Get a user_account by ID

### Example
```python
from __future__ import print_function
import time
import magdemo_api_client
from magdemo_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = magdemo_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = magdemo_api_client.UserAccountApi(magdemo_api_client.ApiClient(configuration))
oid = 56 # int | user_account ID

try:
    # Get a user_account by ID
    api_response = api_instance.get_user_account_by_id(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountApi->get_user_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**| user_account ID | 

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_accounts**
> list[object] get_user_accounts(offset=offset, limit=limit, order_by=order_by, list_fields=list_fields, changed_by=changed_by, not_changed_by=not_changed_by, ilike_changed_by=ilike_changed_by, notilike_changed_by=notilike_changed_by, gte_changed_on=gte_changed_on, lte_changed_on=lte_changed_on, created_by=created_by, not_created_by=not_created_by, ilike_created_by=ilike_created_by, notilike_created_by=notilike_created_by, gte_created_on=gte_created_on, lte_created_on=lte_created_on, fullname=fullname, not_fullname=not_fullname, ilike_fullname=ilike_fullname, notilike_fullname=notilike_fullname, isnull_fullname=isnull_fullname, equal_id=equal_id, not_id=not_id, in_list_id=in_list_id, gte_id=gte_id, lte_id=lte_id, name=name, not_name=not_name, ilike_name=ilike_name, notilike_name=notilike_name, isnull_name=isnull_name)

Get all user_account IDs

Get all user_account IDs and names

### Example
```python
from __future__ import print_function
import time
import magdemo_api_client
from magdemo_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = magdemo_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = magdemo_api_client.UserAccountApi(magdemo_api_client.ApiClient(configuration))
offset = 56 # int | Offset for start of  returned records (optional)
limit = 56 # int | Limit the amount of returned records (optional)
order_by = 'order_by_example' # str | Column used for sorting. The format is [+|-]<column_name> (optional)
list_fields = ['list_fields_example'] # list[str] | Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name> (optional)
changed_by = 'changed_by_example' # str | Search for user_accounts, where changed_by like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_changed_by = 'not_changed_by_example' # str | Search for user_accounts, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_changed_by = 'ilike_changed_by_example' # str | Search for user_accounts, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_changed_by = 'notilike_changed_by_example' # str | Search for user_accounts, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
gte_changed_on = 'gte_changed_on_example' # str | Search for user_accounts, where changed_on >= input (optional)
lte_changed_on = 'lte_changed_on_example' # str | Search for user_accounts, where changed_on <= input (optional)
created_by = 'created_by_example' # str | Search for user_accounts, where created_by like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_created_by = 'not_created_by_example' # str | Search for user_accounts, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_created_by = 'ilike_created_by_example' # str | Search for user_accounts, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_created_by = 'notilike_created_by_example' # str | Search for user_accounts, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
gte_created_on = 'gte_created_on_example' # str | Search for user_accounts, where created_on >= input (optional)
lte_created_on = 'lte_created_on_example' # str | Search for user_accounts, where created_on <= input (optional)
fullname = 'fullname_example' # str | Search for user_accounts, where fullname like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_fullname = 'not_fullname_example' # str | Search for user_accounts, where fullname notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_fullname = 'ilike_fullname_example' # str | Search for user_accounts, where fullname ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_fullname = 'notilike_fullname_example' # str | Search for user_accounts, where fullname notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
isnull_fullname = true # bool | Search for user_accounts, where fullname isNull input (optional)
equal_id = 56 # int | Search for user_accounts, where id == input (optional)
not_id = 56 # int | Search for user_accounts, where id != input (optional)
in_list_id = [56] # list[int] | Search for user_accounts, where id in input (optional)
gte_id = 56 # int | Search for user_accounts, where id >= input (optional)
lte_id = 56 # int | Search for user_accounts, where id <= input (optional)
name = 'name_example' # str | Search for user_accounts, where name like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_name = 'not_name_example' # str | Search for user_accounts, where name notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_name = 'ilike_name_example' # str | Search for user_accounts, where name ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_name = 'notilike_name_example' # str | Search for user_accounts, where name notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
isnull_name = true # bool | Search for user_accounts, where name isNull input (optional)

try:
    # Get all user_account IDs
    api_response = api_instance.get_user_accounts(offset=offset, limit=limit, order_by=order_by, list_fields=list_fields, changed_by=changed_by, not_changed_by=not_changed_by, ilike_changed_by=ilike_changed_by, notilike_changed_by=notilike_changed_by, gte_changed_on=gte_changed_on, lte_changed_on=lte_changed_on, created_by=created_by, not_created_by=not_created_by, ilike_created_by=ilike_created_by, notilike_created_by=notilike_created_by, gte_created_on=gte_created_on, lte_created_on=lte_created_on, fullname=fullname, not_fullname=not_fullname, ilike_fullname=ilike_fullname, notilike_fullname=notilike_fullname, isnull_fullname=isnull_fullname, equal_id=equal_id, not_id=not_id, in_list_id=in_list_id, gte_id=gte_id, lte_id=lte_id, name=name, not_name=not_name, ilike_name=ilike_name, notilike_name=notilike_name, isnull_name=isnull_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountApi->get_user_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for start of  returned records | [optional] 
 **limit** | **int**| Limit the amount of returned records | [optional] 
 **order_by** | **str**| Column used for sorting. The format is [+|-]&lt;column_name&gt; | [optional] 
 **list_fields** | [**list[str]**](str.md)| Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name&gt; | [optional] 
 **changed_by** | **str**| Search for user_accounts, where changed_by like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_changed_by** | **str**| Search for user_accounts, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_changed_by** | **str**| Search for user_accounts, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_changed_by** | **str**| Search for user_accounts, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **gte_changed_on** | **str**| Search for user_accounts, where changed_on &gt;&#x3D; input | [optional] 
 **lte_changed_on** | **str**| Search for user_accounts, where changed_on &lt;&#x3D; input | [optional] 
 **created_by** | **str**| Search for user_accounts, where created_by like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_created_by** | **str**| Search for user_accounts, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_created_by** | **str**| Search for user_accounts, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_created_by** | **str**| Search for user_accounts, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **gte_created_on** | **str**| Search for user_accounts, where created_on &gt;&#x3D; input | [optional] 
 **lte_created_on** | **str**| Search for user_accounts, where created_on &lt;&#x3D; input | [optional] 
 **fullname** | **str**| Search for user_accounts, where fullname like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_fullname** | **str**| Search for user_accounts, where fullname notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_fullname** | **str**| Search for user_accounts, where fullname ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_fullname** | **str**| Search for user_accounts, where fullname notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **isnull_fullname** | **bool**| Search for user_accounts, where fullname isNull input | [optional] 
 **equal_id** | **int**| Search for user_accounts, where id &#x3D;&#x3D; input | [optional] 
 **not_id** | **int**| Search for user_accounts, where id !&#x3D; input | [optional] 
 **in_list_id** | [**list[int]**](int.md)| Search for user_accounts, where id in input | [optional] 
 **gte_id** | **int**| Search for user_accounts, where id &gt;&#x3D; input | [optional] 
 **lte_id** | **int**| Search for user_accounts, where id &lt;&#x3D; input | [optional] 
 **name** | **str**| Search for user_accounts, where name like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_name** | **str**| Search for user_accounts, where name notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_name** | **str**| Search for user_accounts, where name ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_name** | **str**| Search for user_accounts, where name notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **isnull_name** | **bool**| Search for user_accounts, where name isNull input | [optional] 

### Return type

**list[object]**

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_account_by_id**
> update_user_account_by_id(body, oid)

Update the user_account

Update the user_account with the provided data

### Example
```python
from __future__ import print_function
import time
import magdemo_api_client
from magdemo_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = magdemo_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = magdemo_api_client.UserAccountApi(magdemo_api_client.ApiClient(configuration))
body = magdemo_api_client.UserAccount() # UserAccount | 
oid = 56 # int | user_account ID

try:
    # Update the user_account
    api_instance.update_user_account_by_id(body, oid)
except ApiException as e:
    print("Exception when calling UserAccountApi->update_user_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAccount**](UserAccount.md)|  | 
 **oid** | **int**| user_account ID | 

### Return type

void (empty response body)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

