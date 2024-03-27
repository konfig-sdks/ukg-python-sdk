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


class NewHirePostModelCompensation(BaseModel):
    # Whether the new hire is full time
    is_full_time: typing.Optional[bool] = Field(None, alias='isFullTime')

    # Whether the new hire is salaried
    is_salaried: typing.Optional[bool] = Field(None, alias='isSalaried')

    # Work hours of the new hire
    work_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='workHours')

    # Weekly hours of the new hire. Only applicable for hires not in US/Canadian companies
    weekly_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='weeklyHours')

    # ISO currency code of the new hire
    currency_code: typing.Optional[str] = Field(None, alias='currencyCode')

    # Pay rate of the new hire
    pay_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='payRate')

    # Pay period of the new hire. Accepts \"H\" (Hour), \"W\" (Week), \"P\" (Period), \"Y\" (Year)
    rate_per: typing.Optional[str] = Field(None, alias='ratePer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
