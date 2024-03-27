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

from ukg_python_sdk.type.skill_skill_name import SkillSkillName

class RequiredSkillSkill(TypedDict):
    pass

class OptionalSkillSkill(TypedDict, total=False):
    # The id of a standard skill.
    id: str

    name: SkillSkillName

class SkillSkill(RequiredSkillSkill, OptionalSkillSkill):
    pass
