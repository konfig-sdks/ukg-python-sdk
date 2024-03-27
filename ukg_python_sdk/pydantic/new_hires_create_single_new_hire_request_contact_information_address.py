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


class NewHiresCreateSingleNewHireRequestContactInformationAddress(BaseModel):
    # Line 1 of the address. maxLength: 100 for US/Canadian address country, 255 otherwise
    line1: typing.Optional[str] = Field(None, alias='line1')

    # Line 2 of the address. maxLength: 100 for US/Canadian address country, 255 otherwise
    line2: typing.Optional[str] = Field(None, alias='line2')

    # City of the address. maxLength: 50 for US/Canadian address country, 255 otherwise
    city: typing.Optional[str] = Field(None, alias='city')

    # Zip/postal code of the address. maxLength: 50 for hires not in US/Canadian address country. If hire's address country is US/Canada, a valid postal code format is expected
    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    # County name of the address. maxLength: 30 for US/Canadian address country, 255 otherwise
    county: typing.Optional[str] = Field(None, alias='county')

    # State code of the address
    state_code: typing.Optional[str] = Field(None, alias='stateCode')

    # ISO country code of the address
    country_code: typing.Optional[str] = Field(None, alias='countryCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
