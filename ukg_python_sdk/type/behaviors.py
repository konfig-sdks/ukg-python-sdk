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


class RequiredBehaviors(TypedDict):
    pass

class OptionalBehaviors(TypedDict, total=False):
    # The behavior description in all available languages.
    description: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The id of one of pre-defined behaviors.
    id: str

    created_at: str

    updated_at: str

    # The behavior name in all available languages.
    name: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    is_archived: bool

class Behaviors(RequiredBehaviors, OptionalBehaviors):
    pass
