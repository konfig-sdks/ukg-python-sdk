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


class RequiredOrgLevels(TypedDict):
    # Organization Level Description.
    description: str

    # Organization Code, one half of the unique identifier.
    code: str

    # Organazation Level, one half of unique identifier. Cannot be updated.
    level: typing.Union[int, float]

class OptionalOrgLevels(TypedDict, total=False):
    # Organizational budget group.
    budgetGroup: str

    # Current year to date budget for full time employee.
    currentYearBudgetFTE: typing.Union[int, float]

    # Current year to date budget for salary.
    currentYearBudgetSalary: typing.Union[int, float]

    # General Ledger Segment. Alpha-numeric and special characters allowed.
    glSegment: str

    # Last year Budget for full time employee.
    lastYearBudgetFTE: typing.Union[int, float]

    # Last year Budget salary.
    lastYearBudgetSalary: typing.Union[int, float]

    # Organization description. Cannot be updated.
    levelDescription: str

    # The reporting category code.
    reportingCategory: str

    # The organization level status.
    isActive: bool

class OrgLevels(RequiredOrgLevels, OptionalOrgLevels):
    pass
