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


class EmployeeMultipleJobs(BaseModel):
    annual_pay_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='annualPayRate')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    date_in_job: typing.Optional[datetime] = Field(None, alias='dateInJob')

    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    hourly_pay_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='hourlyPayRate')

    is_primary_job: typing.Optional[bool] = Field(None, alias='isPrimaryJob')

    job_code: typing.Optional[str] = Field(None, alias='jobCode')

    job_is_in_active: typing.Optional[bool] = Field(None, alias='jobIsInActive')

    other_rate1: typing.Optional[typing.Union[int, float]] = Field(None, alias='otherRate1')

    other_rate2: typing.Optional[typing.Union[int, float]] = Field(None, alias='otherRate2')

    other_rate3: typing.Optional[typing.Union[int, float]] = Field(None, alias='otherRate3')

    other_rate4: typing.Optional[typing.Union[int, float]] = Field(None, alias='otherRate4')

    piece_pay_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='piecePayRate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
