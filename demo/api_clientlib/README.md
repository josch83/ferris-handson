# magdemo-api-client
API definition for ferris.ai Ferris Demo Project for MAG Hands On

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.2
- Package version: 0.0.2
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [http://ferris.ai/](http://ferris.ai/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import magdemo_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import magdemo_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = magdemo_api_client.AddressApi(magdemo_api_client.ApiClient(configuration))
body = magdemo_api_client.Address() # Address | 

try:
    # Create a new address
    api_response = api_instance.create_address(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->create_address: %s\n" % e)

# Configure API key authorization: sso_auth
configuration = magdemo_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = magdemo_api_client.AddressApi(magdemo_api_client.ApiClient(configuration))
oid = 56 # int | address ID

try:
    # Get a address by ID
    api_response = api_instance.get_address_by_id(oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->get_address_by_id: %s\n" % e)

# Configure API key authorization: sso_auth
configuration = magdemo_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = magdemo_api_client.AddressApi(magdemo_api_client.ApiClient(configuration))
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

# Configure API key authorization: sso_auth
configuration = magdemo_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = magdemo_api_client.AddressApi(magdemo_api_client.ApiClient(configuration))
body = magdemo_api_client.Address() # Address | 
oid = 56 # int | address ID

try:
    # Update the address
    api_instance.update_address_by_id(body, oid)
except ApiException as e:
    print("Exception when calling AddressApi->update_address_by_id: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressApi* | [**create_address**](docs/AddressApi.md#create_address) | **POST** /address | Create a new address
*AddressApi* | [**get_address_by_id**](docs/AddressApi.md#get_address_by_id) | **GET** /address/{oid} | Get a address by ID
*AddressApi* | [**get_addresss**](docs/AddressApi.md#get_addresss) | **GET** /address | Get all address IDs
*AddressApi* | [**update_address_by_id**](docs/AddressApi.md#update_address_by_id) | **PUT** /address/{oid} | Update the address
*RoleRightsApi* | [**create_role_rights**](docs/RoleRightsApi.md#create_role_rights) | **POST** /role_rights | Create a new role_rights
*RoleRightsApi* | [**get_role_rights_by_id**](docs/RoleRightsApi.md#get_role_rights_by_id) | **GET** /role_rights/{oid} | Get a role_rights by ID
*RoleRightsApi* | [**get_role_rightss**](docs/RoleRightsApi.md#get_role_rightss) | **GET** /role_rights | Get all role_rights IDs
*RoleRightsApi* | [**update_role_rights_by_id**](docs/RoleRightsApi.md#update_role_rights_by_id) | **PUT** /role_rights/{oid} | Update the role_rights
*UserAccountApi* | [**create_user_account**](docs/UserAccountApi.md#create_user_account) | **POST** /user_account | Create a new user_account
*UserAccountApi* | [**get_user_account_by_id**](docs/UserAccountApi.md#get_user_account_by_id) | **GET** /user_account/{oid} | Get a user_account by ID
*UserAccountApi* | [**get_user_accounts**](docs/UserAccountApi.md#get_user_accounts) | **GET** /user_account | Get all user_account IDs
*UserAccountApi* | [**update_user_account_by_id**](docs/UserAccountApi.md#update_user_account_by_id) | **PUT** /user_account/{oid} | Update the user_account

## Documentation For Models

 - [Address](docs/Address.md)
 - [NewAddress](docs/NewAddress.md)
 - [NewRoleRights](docs/NewRoleRights.md)
 - [NewUserAccount](docs/NewUserAccount.md)
 - [RoleRights](docs/RoleRights.md)
 - [UserAccount](docs/UserAccount.md)

## Documentation For Authorization


## sso_auth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

Ferris Solutions

info@ferris.ai

