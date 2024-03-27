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


class RequiredNewHiresGetById200ResponseOrganizationLevelsItem(TypedDict):
    pass

class OptionalNewHiresGetById200ResponseOrganizationLevelsItem(TypedDict, total=False):
    # Description of a organization that the new hire is associated with.
    description: str

    # Identifier of the organization level
    id: str

    # Level of the organization level
    level: str

    # Unique code of a organization that the new hire is associated with
    code: str

class NewHiresGetById200ResponseOrganizationLevelsItem(RequiredNewHiresGetById200ResponseOrganizationLevelsItem, OptionalNewHiresGetById200ResponseOrganizationLevelsItem):
    pass
