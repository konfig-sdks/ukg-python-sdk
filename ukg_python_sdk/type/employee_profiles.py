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


class RequiredEmployeeProfiles(TypedDict):
    pass

class OptionalEmployeeProfiles(TypedDict, total=False):
    description: str

    profileValue: str

    profileType: str

    product: str

    module: str

    companyId: str

    employeeId: str

    lastModifiedDate: datetime

    isCleared: bool

    isDateEffective: bool

    effectiveDate: datetime

    recordId: typing.Union[int, float]

    changeRecordID: typing.Union[int, float]

    isPrimary: bool

    isPrimaryEffectiveDate: datetime

    originalHireDate: datetime

class EmployeeProfiles(RequiredEmployeeProfiles, OptionalEmployeeProfiles):
    pass
