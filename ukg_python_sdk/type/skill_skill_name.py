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


class RequiredSkillSkillName(TypedDict):
    pass

class OptionalSkillSkillName(TypedDict, total=False):
    en_us: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class SkillSkillName(RequiredSkillSkillName, OptionalSkillSkillName):
    pass
