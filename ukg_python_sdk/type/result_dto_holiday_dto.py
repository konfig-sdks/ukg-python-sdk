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

from ukg_python_sdk.type.holiday_dto import HolidayDto

class RequiredResultDtoHolidayDto(TypedDict):
    pass

class OptionalResultDtoHolidayDto(TypedDict, total=False):
    entities: typing.List[HolidayDto]

    index: int

    requestedCount: int

class ResultDtoHolidayDto(RequiredResultDtoHolidayDto, OptionalResultDtoHolidayDto):
    pass
