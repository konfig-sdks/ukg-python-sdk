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

from ukg_python_sdk.pydantic.contact_info_address_country_name import ContactInfoAddressCountryName

class ContactInfoAddressCountry(BaseModel):
    # The id of the country
    id: typing.Optional[str] = Field(None, alias='id')

    # The candidate’s country code (ISO standard).
    code: typing.Optional[str] = Field(None, alias='code')

    name: typing.Optional[ContactInfoAddressCountryName] = Field(None, alias='name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
