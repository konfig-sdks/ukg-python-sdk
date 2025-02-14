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


class RequiredEmployeeEducationModel(TypedDict):
    pass

class OptionalEmployeeEducationModel(TypedDict, total=False):
    employeeId: str

    systemId: str

    school: str

    educationLevel: str

    educationMajor: str

    educationMinor: str

    gpa: str

    beginDate: datetime

    endDate: datetime

    isGraduate: bool

    isHighestLevel: bool

    employeeNumber: str

    country: str

class EmployeeEducationModel(RequiredEmployeeEducationModel, OptionalEmployeeEducationModel):
    pass
