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

from ukg_python_sdk.type.new_hires_get_by_id_response_compensation_currency import NewHiresGetByIdResponseCompensationCurrency
from ukg_python_sdk.type.new_hires_get_by_id_response_compensation_rate_per import NewHiresGetByIdResponseCompensationRatePer

class RequiredNewHiresGetByIdResponseCompensation(TypedDict):
    pass

class OptionalNewHiresGetByIdResponseCompensation(TypedDict, total=False):
    # Whether the new hire is full time
    isFullTime: bool

    # Whether the new hire is salaried
    isSalaried: bool

    # Work hours of the new hire
    workHours: typing.Union[int, float]

    # Weekly hours of the new hire
    weeklyHours: typing.Union[int, float]

    # Currency type of the new hire's pay
    currencyType: str

    currency: NewHiresGetByIdResponseCompensationCurrency

    # Pay rate of the new hire
    payRate: typing.Union[int, float]

    ratePer: NewHiresGetByIdResponseCompensationRatePer

class NewHiresGetByIdResponseCompensation(RequiredNewHiresGetByIdResponseCompensation, OptionalNewHiresGetByIdResponseCompensation):
    pass
