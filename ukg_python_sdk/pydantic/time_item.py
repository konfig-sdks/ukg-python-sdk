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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class TimeItem(BaseModel):
    # The date the hours were worked
    date_worked: datetime = Field(alias='dateWorked')

    # The number of hours worked
    hours_worked: typing.Union[int, float] = Field(alias='hoursWorked')

    # The UltiPro EmployeeNumber, either this value OR the EEID MUST be specified
    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    # The UltiPro EEID, either this value OR the EmployeeNumber MUST be specified
    ee_id: typing.Optional[str] = Field(None, alias='eeId')

    # The UltiPro CompanyCode, either this value OR the CoID MUST be specified
    company_code: typing.Optional[str] = Field(None, alias='companyCode')

    # The UltiPro CoID, either this value OR the CompanyCode MUST be specified
    co_id: typing.Optional[str] = Field(None, alias='coId')

    # This value should be NULL from the originator
    id: typing.Optional[typing.Union[int, float]] = Field(None, alias='id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
