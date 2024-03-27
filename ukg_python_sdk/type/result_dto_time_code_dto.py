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

from ukg_python_sdk.type.time_code_dto import TimeCodeDto

class RequiredResultDtoTimeCodeDto(TypedDict):
    pass

class OptionalResultDtoTimeCodeDto(TypedDict, total=False):
    entities: typing.List[TimeCodeDto]

    index: int

    requestedCount: int

class ResultDtoTimeCodeDto(RequiredResultDtoTimeCodeDto, OptionalResultDtoTimeCodeDto):
    pass
