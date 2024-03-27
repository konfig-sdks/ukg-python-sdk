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

from ukg_python_sdk.pydantic.new_hires_create_single_new_hire_response_compensation_currency import NewHiresCreateSingleNewHireResponseCompensationCurrency
from ukg_python_sdk.pydantic.new_hires_create_single_new_hire_response_compensation_rate_per import NewHiresCreateSingleNewHireResponseCompensationRatePer

class NewHiresCreateSingleNewHireResponseCompensation(BaseModel):
    # Whether the new hire is full time
    is_full_time: typing.Optional[bool] = Field(None, alias='isFullTime')

    # Whether the new hire is salaried
    is_salaried: typing.Optional[bool] = Field(None, alias='isSalaried')

    # Work hours of the new hire
    work_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='workHours')

    # Weekly hours of the new hire
    weekly_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='weeklyHours')

    # Currency type of the new hire's pay
    currency_type: typing.Optional[str] = Field(None, alias='currencyType')

    currency: typing.Optional[NewHiresCreateSingleNewHireResponseCompensationCurrency] = Field(None, alias='currency')

    # Pay rate of the new hire
    pay_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='payRate')

    rate_per: typing.Optional[NewHiresCreateSingleNewHireResponseCompensationRatePer] = Field(None, alias='ratePer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
