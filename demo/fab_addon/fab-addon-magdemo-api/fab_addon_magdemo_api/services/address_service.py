# File auto generated, DO NOT edit because it will be smashed

import os

import magdemo_api_client
from magdemo_api_client.rest import ApiException


class AddressService:
    def __init__(self, token_passed=None):
        host = os.environ.get("MAGDEMO_API_HOST")
        port = os.environ.get("MAGDEMO_API_PORT")

        uri = f"{host}:{port}/"

        config = magdemo_api_client.Configuration()
        config.host = uri
        if token_passed:
            config.api_key["Authorization"] = token_passed
            config.api_key_prefix["Authorization"] = "Bearer"
        self.address_api_instance = magdemo_api_client.AddressApi(magdemo_api_client.ApiClient(config))

    def get_all_dropdowns(self, **kwargs):
        oids_list = self.address_api_instance.get_addresss(**kwargs)
        return oids_list

    def get_all(self, **kwargs):
        oids_list = self.address_api_instance.get_addresss(**kwargs)
        return [oid.get("id") for oid in oids_list]

    def get(self, oid):
        api_response_dict = None
        try:
            api_response = self.address_api_instance.get_address_by_id(oid)
            api_response_dict = api_response.to_dict()
        except ApiException as api_exception:
            print(f"Exception when calling AddressApi->get_address_by_id: {api_exception}\n")
            raise api_exception
        return api_response_dict

    def add(self, item):
        api_response = None
        try:
            body = item
            api_response = self.address_api_instance.create_address(body)
        except ApiException as api_exception:
            print(f"Exception when calling AddressApi->create_address: {api_exception}\n")
            raise api_exception
        return api_response

    def edit(self, item, oid):
        api_response = None
        try:
            body = item
            api_response = self.address_api_instance.update_address_by_id(
                body, oid
            )
        except ApiException as api_exception:
            print(f"Exception when calling AddressApi->update_address_by_id: {api_exception}\n")
            raise api_exception
        return api_response



