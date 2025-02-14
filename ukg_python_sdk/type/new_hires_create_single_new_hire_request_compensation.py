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


class RequiredNewHiresCreateSingleNewHireRequestCompensation(TypedDict):
    pass

class OptionalNewHiresCreateSingleNewHireRequestCompensation(TypedDict, total=False):
    # Whether the new hire is full time
    isFullTime: bool

    # Whether the new hire is salaried
    isSalaried: bool

    # Work hours of the new hire
    workHours: typing.Union[int, float]

    # Weekly hours of the new hire. Only applicable for hires not in US/Canadian companies
    weeklyHours: typing.Union[int, float]

    # ISO currency code of the new hire
    currencyCode: str

    # Pay rate of the new hire
    payRate: typing.Union[int, float]

    # Pay period of the new hire. Accepts \"H\" (Hour), \"W\" (Week), \"P\" (Period), \"Y\" (Year)
    ratePer: str

class NewHiresCreateSingleNewHireRequestCompensation(RequiredNewHiresCreateSingleNewHireRequestCompensation, OptionalNewHiresCreateSingleNewHireRequestCompensation):
    pass
