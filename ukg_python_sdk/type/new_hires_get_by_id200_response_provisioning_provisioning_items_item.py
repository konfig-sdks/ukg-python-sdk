# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from ukg_python_sdk.type.new_hires_get_by_id200_response_provisioning_provisioning_items_item_selected_option import NewHiresGetById200ResponseProvisioningProvisioningItemsItemSelectedOption

class RequiredNewHiresGetById200ResponseProvisioningProvisioningItemsItem(TypedDict):
    pass

class OptionalNewHiresGetById200ResponseProvisioningProvisioningItemsItem(TypedDict, total=False):
    # Id of the provisioning item
    id: str

    # Category of the provisioning item
    name: str

    # Recipient of the provisioning item
    recipient: str

    selectedOption: NewHiresGetById200ResponseProvisioningProvisioningItemsItemSelectedOption

    # Comment on the provisioning item
    comments: str

class NewHiresGetById200ResponseProvisioningProvisioningItemsItem(RequiredNewHiresGetById200ResponseProvisioningProvisioningItemsItem, OptionalNewHiresGetById200ResponseProvisioningProvisioningItemsItem):
    pass
