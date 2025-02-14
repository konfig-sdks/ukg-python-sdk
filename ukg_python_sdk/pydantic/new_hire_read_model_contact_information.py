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

from ukg_python_sdk.pydantic.new_hire_read_model_contact_information_address import NewHireReadModelContactInformationAddress
from ukg_python_sdk.pydantic.new_hire_read_model_contact_information_name import NewHireReadModelContactInformationName

class NewHireReadModelContactInformation(BaseModel):
    name: typing.Optional[NewHireReadModelContactInformationName] = Field(None, alias='name')

    # Email address of the new hire
    email_address: typing.Optional[str] = Field(None, alias='emailAddress')

    # Primary phone number of the new hire
    primary_phone: typing.Optional[str] = Field(None, alias='primaryPhone')

    # Secondary phone number of the new hire
    secondary_phone: typing.Optional[str] = Field(None, alias='secondaryPhone')

    address: typing.Optional[NewHireReadModelContactInformationAddress] = Field(None, alias='address')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
