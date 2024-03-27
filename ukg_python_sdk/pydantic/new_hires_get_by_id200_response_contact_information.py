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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from ukg_python_sdk.pydantic.new_hires_get_by_id200_response_contact_information_address import NewHiresGetById200ResponseContactInformationAddress
from ukg_python_sdk.pydantic.new_hires_get_by_id200_response_contact_information_name import NewHiresGetById200ResponseContactInformationName

class NewHiresGetById200ResponseContactInformation(BaseModel):
    name: typing.Optional[NewHiresGetById200ResponseContactInformationName] = Field(None, alias='name')

    # Email address of the new hire
    email_address: typing.Optional[str] = Field(None, alias='emailAddress')

    # Primary phone number of the new hire
    primary_phone: typing.Optional[str] = Field(None, alias='primaryPhone')

    # Secondary phone number of the new hire
    secondary_phone: typing.Optional[str] = Field(None, alias='secondaryPhone')

    address: typing.Optional[NewHiresGetById200ResponseContactInformationAddress] = Field(None, alias='address')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
