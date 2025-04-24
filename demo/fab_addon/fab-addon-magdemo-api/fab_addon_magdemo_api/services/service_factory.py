# File auto generated, DO NOT edit because it will be smashed

from enum import Enum
from typing import Type, Union

from .address_service import AddressService
from .user_account_service import UserAccountService
from .role_rights_service import RoleRightsService


class services_available(Enum):
    ADDRESS = "address"
    USER_ACCOUNT = "user_account"
    ROLE_RIGHTS = "role_rights"


def ServiceFactory(*, service: services_available) -> Union[
    
    Type[AddressService],
    Type[UserAccountService],
    Type[RoleRightsService],
    
]:  # named argument, we want to be esplicit!

    services_allowed = [
    
        "address",
        "user_account",
        "role_rights",
    ]

    # if service not in services_allowed and service is not None:
    #     raise ValueError(f"Not allowed value for service param. You assigned: {service}.\nAllowed values are: {services_allowed}")

    # if service is None:
    #     raise TypeError(f"service parameter must not be None. Valid choices are {services_allowed}")

    services = {
        "address": AddressService,
        "user_account": UserAccountService,
        "role_rights": RoleRightsService,
    }
    # Now we return the class, not the instance of the class
    return services[service.value]
