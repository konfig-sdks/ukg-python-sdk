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


class RequiredNewHiresGetByIdResponseCompensationRatePer(TypedDict):
    pass

class OptionalNewHiresGetByIdResponseCompensationRatePer(TypedDict, total=False):
    # Code of the translatable
    code: str

    # The language that the translatable is in
    name: typing.Dict[str, str]

class NewHiresGetByIdResponseCompensationRatePer(RequiredNewHiresGetByIdResponseCompensationRatePer, OptionalNewHiresGetByIdResponseCompensationRatePer):
    pass
