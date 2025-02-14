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


class RequiredOrgUnitsOrgLevel(TypedDict):
    pass

class OptionalOrgUnitsOrgLevel(TypedDict, total=False):
    # The organizational unit’s level id
    id: str

    # The organizational unit level in the company org structure
    level: str

class OrgUnitsOrgLevel(RequiredOrgUnitsOrgLevel, OptionalOrgUnitsOrgLevel):
    pass
