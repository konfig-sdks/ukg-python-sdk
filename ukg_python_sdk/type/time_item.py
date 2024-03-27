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


class RequiredTimeItem(TypedDict):
    # The date the hours were worked
    dateWorked: datetime

    # The number of hours worked
    hoursWorked: typing.Union[int, float]

class OptionalTimeItem(TypedDict, total=False):
    # The UltiPro EmployeeNumber, either this value OR the EEID MUST be specified
    employeeNumber: str

    # The UltiPro EEID, either this value OR the EmployeeNumber MUST be specified
    eeId: str

    # The UltiPro CompanyCode, either this value OR the CoID MUST be specified
    companyCode: str

    # The UltiPro CoID, either this value OR the CompanyCode MUST be specified
    coId: str

    # This value should be NULL from the originator
    id: typing.Union[int, float]

class TimeItem(RequiredTimeItem, OptionalTimeItem):
    pass
