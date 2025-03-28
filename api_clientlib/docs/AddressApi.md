# jsctzi_api_client.AddressApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](AddressApi.md#create_address) | **POST** /address | Create a new address
[**get_address_by_id**](AddressApi.md#get_address_by_id) | **GET** /address/{oid} | Get a address by ID
[**get_addresss**](AddressApi.md#get_addresss) | **GET** /address | Get all address IDs
[**update_address_by_id**](AddressApi.md#update_address_by_id) | **PUT** /address/{oid} | Update the address

# **create_address**
> NewAddress create_address(body)

Create a new address

Create a new address with new id and provided data

### Example
```python
from __future__ import print_function
import time
import jsctzi_api_client
from jsctzi_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = jsctzi_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = jsctzi_api_client.AddressApi(jsctzi_api_client.ApiClient(configuration))
body = jsctzi_api_client.Address() # Address | 

try:
    # Create a new address
    api_response = api_instance.create_address(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->create_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)|  | 

### Return type

[**NewAddress**](NewAddress.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_by_id**
> Address get_address_by_id(oid)

Get a address by ID

Get a address by ID

### Example
```python
from __future__ import print_function
import time
import jsctzi_api_client
from jsctzi_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = jsctzi_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = jsctzi_api_client.AddressApi(jsctzi_api_client.ApiClient(configuration))
oid = 56 # int | address ID

try:
    # Get a address by ID
    api_response = api_instance.get_address_by_id(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->get_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **int**| address ID | 

### Return type

[**Address**](Address.md)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addresss**
> list[object] get_addresss(offset=offset, limit=limit, order_by=order_by, list_fields=list_fields, changed_by=changed_by, not_changed_by=not_changed_by, ilike_changed_by=ilike_changed_by, notilike_changed_by=notilike_changed_by, gte_changed_on=gte_changed_on, lte_changed_on=lte_changed_on, created_by=created_by, not_created_by=not_created_by, ilike_created_by=ilike_created_by, notilike_created_by=notilike_created_by, gte_created_on=gte_created_on, lte_created_on=lte_created_on, email_address=email_address, not_email_address=not_email_address, ilike_email_address=ilike_email_address, notilike_email_address=notilike_email_address, equal_id=equal_id, not_id=not_id, in_list_id=in_list_id, gte_id=gte_id, lte_id=lte_id, equal_user_id=equal_user_id, not_user_id=not_user_id, in_list_user_id=in_list_user_id, gte_user_id=gte_user_id, lte_user_id=lte_user_id)

Get all address IDs

Get all address IDs and names

### Example
```python
from __future__ import print_function
import time
import jsctzi_api_client
from jsctzi_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = jsctzi_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = jsctzi_api_client.AddressApi(jsctzi_api_client.ApiClient(configuration))
offset = 56 # int | Offset for start of  returned records (optional)
limit = 56 # int | Limit the amount of returned records (optional)
order_by = 'order_by_example' # str | Column used for sorting. The format is [+|-]<column_name> (optional)
list_fields = ['list_fields_example'] # list[str] | Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name> (optional)
changed_by = 'changed_by_example' # str | Search for addresss, where changed_by like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_changed_by = 'not_changed_by_example' # str | Search for addresss, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_changed_by = 'ilike_changed_by_example' # str | Search for addresss, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_changed_by = 'notilike_changed_by_example' # str | Search for addresss, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
gte_changed_on = 'gte_changed_on_example' # str | Search for addresss, where changed_on >= input (optional)
lte_changed_on = 'lte_changed_on_example' # str | Search for addresss, where changed_on <= input (optional)
created_by = 'created_by_example' # str | Search for addresss, where created_by like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_created_by = 'not_created_by_example' # str | Search for addresss, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_created_by = 'ilike_created_by_example' # str | Search for addresss, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_created_by = 'notilike_created_by_example' # str | Search for addresss, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
gte_created_on = 'gte_created_on_example' # str | Search for addresss, where created_on >= input (optional)
lte_created_on = 'lte_created_on_example' # str | Search for addresss, where created_on <= input (optional)
email_address = 'email_address_example' # str | Search for addresss, where email_address like input (place the %-wildcard at start and/or end of the input yourself) (optional)
not_email_address = 'not_email_address_example' # str | Search for addresss, where email_address notlike input (place the %-wildcard at start and/or end of the input yourself) (optional)
ilike_email_address = 'ilike_email_address_example' # str | Search for addresss, where email_address ilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
notilike_email_address = 'notilike_email_address_example' # str | Search for addresss, where email_address notilike input (place the %-wildcard at start and/or end of the input yourself) (optional)
equal_id = 56 # int | Search for addresss, where id == input (optional)
not_id = 56 # int | Search for addresss, where id != input (optional)
in_list_id = [56] # list[int] | Search for addresss, where id in input (optional)
gte_id = 56 # int | Search for addresss, where id >= input (optional)
lte_id = 56 # int | Search for addresss, where id <= input (optional)
equal_user_id = 56 # int | Search for addresss, where user_id == input (optional)
not_user_id = 56 # int | Search for addresss, where user_id != input (optional)
in_list_user_id = [56] # list[int] | Search for addresss, where user_id in input (optional)
gte_user_id = 56 # int | Search for addresss, where user_id >= input (optional)
lte_user_id = 56 # int | Search for addresss, where user_id <= input (optional)

try:
    # Get all address IDs
    api_response = api_instance.get_addresss(offset=offset, limit=limit, order_by=order_by, list_fields=list_fields, changed_by=changed_by, not_changed_by=not_changed_by, ilike_changed_by=ilike_changed_by, notilike_changed_by=notilike_changed_by, gte_changed_on=gte_changed_on, lte_changed_on=lte_changed_on, created_by=created_by, not_created_by=not_created_by, ilike_created_by=ilike_created_by, notilike_created_by=notilike_created_by, gte_created_on=gte_created_on, lte_created_on=lte_created_on, email_address=email_address, not_email_address=not_email_address, ilike_email_address=ilike_email_address, notilike_email_address=notilike_email_address, equal_id=equal_id, not_id=not_id, in_list_id=in_list_id, gte_id=gte_id, lte_id=lte_id, equal_user_id=equal_user_id, not_user_id=not_user_id, in_list_user_id=in_list_user_id, gte_user_id=gte_user_id, lte_user_id=lte_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->get_addresss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for start of  returned records | [optional] 
 **limit** | **int**| Limit the amount of returned records | [optional] 
 **order_by** | **str**| Column used for sorting. The format is [+|-]&lt;column_name&gt; | [optional] 
 **list_fields** | [**list[str]**](str.md)| Specifies the fields to be returned. Default: Empty List, in which case __repr__ is returned as name&gt; | [optional] 
 **changed_by** | **str**| Search for addresss, where changed_by like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_changed_by** | **str**| Search for addresss, where changed_by notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_changed_by** | **str**| Search for addresss, where changed_by ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_changed_by** | **str**| Search for addresss, where changed_by notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **gte_changed_on** | **str**| Search for addresss, where changed_on &gt;&#x3D; input | [optional] 
 **lte_changed_on** | **str**| Search for addresss, where changed_on &lt;&#x3D; input | [optional] 
 **created_by** | **str**| Search for addresss, where created_by like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_created_by** | **str**| Search for addresss, where created_by notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_created_by** | **str**| Search for addresss, where created_by ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_created_by** | **str**| Search for addresss, where created_by notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **gte_created_on** | **str**| Search for addresss, where created_on &gt;&#x3D; input | [optional] 
 **lte_created_on** | **str**| Search for addresss, where created_on &lt;&#x3D; input | [optional] 
 **email_address** | **str**| Search for addresss, where email_address like input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **not_email_address** | **str**| Search for addresss, where email_address notlike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **ilike_email_address** | **str**| Search for addresss, where email_address ilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **notilike_email_address** | **str**| Search for addresss, where email_address notilike input (place the %-wildcard at start and/or end of the input yourself) | [optional] 
 **equal_id** | **int**| Search for addresss, where id &#x3D;&#x3D; input | [optional] 
 **not_id** | **int**| Search for addresss, where id !&#x3D; input | [optional] 
 **in_list_id** | [**list[int]**](int.md)| Search for addresss, where id in input | [optional] 
 **gte_id** | **int**| Search for addresss, where id &gt;&#x3D; input | [optional] 
 **lte_id** | **int**| Search for addresss, where id &lt;&#x3D; input | [optional] 
 **equal_user_id** | **int**| Search for addresss, where user_id &#x3D;&#x3D; input | [optional] 
 **not_user_id** | **int**| Search for addresss, where user_id !&#x3D; input | [optional] 
 **in_list_user_id** | [**list[int]**](int.md)| Search for addresss, where user_id in input | [optional] 
 **gte_user_id** | **int**| Search for addresss, where user_id &gt;&#x3D; input | [optional] 
 **lte_user_id** | **int**| Search for addresss, where user_id &lt;&#x3D; input | [optional] 

### Return type

**list[object]**

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address_by_id**
> update_address_by_id(body, oid)

Update the address

Update the address with the provided data

### Example
```python
from __future__ import print_function
import time
import jsctzi_api_client
from jsctzi_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: sso_auth
configuration = jsctzi_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = jsctzi_api_client.AddressApi(jsctzi_api_client.ApiClient(configuration))
body = jsctzi_api_client.Address() # Address | 
oid = 56 # int | address ID

try:
    # Update the address
    api_instance.update_address_by_id(body, oid)
except ApiException as e:
    print("Exception when calling AddressApi->update_address_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)|  | 
 **oid** | **int**| address ID | 

### Return type

void (empty response body)

### Authorization

[sso_auth](../README.md#sso_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

