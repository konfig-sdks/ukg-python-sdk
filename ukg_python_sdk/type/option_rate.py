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


class RequiredOptionRate(TypedDict):
    pass

class OptionalOptionRate(TypedDict, total=False):
    deductionCode: str

    benefitOption: str

    employeeRate: typing.Union[int, float]

    employerRate: typing.Union[int, float]

    effectiveDate: datetime

    payFrequency: str

    rateStopDate: datetime

class OptionRate(RequiredOptionRate, OptionalOptionRate):
    pass
