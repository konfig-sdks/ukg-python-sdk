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

from ukg_python_sdk.pydantic.clock_transaction_type_dto import ClockTransactionTypeDto

class ClockTransactionDto(BaseModel):
    type: typing.Optional[ClockTransactionTypeDto] = Field(None, alias='type')

    time: typing.Optional[datetime] = Field(None, alias='time')

    data: typing.Optional[str] = Field(None, alias='data')

    # GPS data
    location: typing.Optional[str] = Field(None, alias='location')

    # Clock extra data
    ext_data: typing.Optional[str] = Field(None, alias='extData')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
