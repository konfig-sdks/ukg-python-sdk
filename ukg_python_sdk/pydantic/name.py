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

from ukg_python_sdk.pydantic.name_prefix import NamePrefix
from ukg_python_sdk.pydantic.name_suffix import NameSuffix

class Name(BaseModel):
    # The candidate’s first name. Maximum of 100 characters.
    first: typing.Optional[str] = Field(None, alias='first')

    # The candidate’s middle name. Maximum of 50 characters.
    middle: typing.Optional[str] = Field(None, alias='middle')

    # The candidate’s last name. Maximum of 100 characters.
    last: typing.Optional[str] = Field(None, alias='last')

    prefix: typing.Optional[NamePrefix] = Field(None, alias='prefix')

    suffix: typing.Optional[NameSuffix] = Field(None, alias='suffix')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
