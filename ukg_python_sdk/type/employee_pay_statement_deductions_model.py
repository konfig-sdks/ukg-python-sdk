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


class RequiredEmployeePayStatementDeductionsModel(TypedDict):
    pass

class OptionalEmployeePayStatementDeductionsModel(TypedDict, total=False):
    basisamount: typing.Union[int, float]

    deductioncode: str

    deductiondescription: str

    employeeamount: typing.Union[int, float]

    employeeamountytd: typing.Union[int, float]

    employeramount: typing.Union[int, float]

    employeramountytd: typing.Union[int, float]

    pretax: bool

class EmployeePayStatementDeductionsModel(RequiredEmployeePayStatementDeductionsModel, OptionalEmployeePayStatementDeductionsModel):
    pass
