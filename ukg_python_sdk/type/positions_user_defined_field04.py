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


class RequiredPositionsUserDefinedField04(TypedDict):
    pass

class OptionalPositionsUserDefinedField04(TypedDict, total=False):
    isNull: bool

    Value: typing.Union[int, float]

class PositionsUserDefinedField04(RequiredPositionsUserDefinedField04, OptionalPositionsUserDefinedField04):
    pass
