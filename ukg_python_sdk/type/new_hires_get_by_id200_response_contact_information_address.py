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

from ukg_python_sdk.type.new_hires_get_by_id200_response_contact_information_address_country import NewHiresGetById200ResponseContactInformationAddressCountry

class RequiredNewHiresGetById200ResponseContactInformationAddress(TypedDict):
    pass

class OptionalNewHiresGetById200ResponseContactInformationAddress(TypedDict, total=False):
    # Line 1 of the address
    line1: str

    # Line 2 of the address
    line2: str

    # City of the address
    city: str

    # Zip/postal code of the address
    postalCode: str

    # County of the address
    county: str

    # State code of the address
    stateCode: str

    # Country code of the address
    countryCode: str

    country: NewHiresGetById200ResponseContactInformationAddressCountry

class NewHiresGetById200ResponseContactInformationAddress(RequiredNewHiresGetById200ResponseContactInformationAddress, OptionalNewHiresGetById200ResponseContactInformationAddress):
    pass
