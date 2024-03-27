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


class EducationsFrom(BaseModel):
    # A value between 1 and 12 of the month when the education started.
    month: typing.Optional[str] = Field(None, alias='month')

    # An integer no less than 100 years ago and no greater than the to.year.
    year: typing.Optional[str] = Field(None, alias='year')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
