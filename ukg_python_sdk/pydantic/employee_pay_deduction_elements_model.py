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


class EmployeePayDeductionElementsModel(BaseModel):
    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    system_id: typing.Optional[str] = Field(None, alias='systemId')

    pay_deduction_id: typing.Optional[str] = Field(None, alias='payDeductionId')

    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    pay_group: typing.Optional[str] = Field(None, alias='payGroup')

    pay_deduction_name: typing.Optional[str] = Field(None, alias='payDeductionName')

    pay_deduction_description: typing.Optional[str] = Field(None, alias='payDeductionDescription')

    period_start_id: typing.Optional[str] = Field(None, alias='periodStartId')

    period_end_id: typing.Optional[str] = Field(None, alias='periodEndId')

    period_start_name: typing.Optional[str] = Field(None, alias='periodStartName')

    period_end_name: typing.Optional[str] = Field(None, alias='periodEndName')

    start_date: typing.Optional[datetime] = Field(None, alias='startDate')

    end_date: typing.Optional[datetime] = Field(None, alias='endDate')

    project: typing.Optional[str] = Field(None, alias='project')

    task: typing.Optional[str] = Field(None, alias='task')

    recurring: typing.Optional[str] = Field(None, alias='recurring')

    amount: typing.Optional[str] = Field(None, alias='amount')

    notes: typing.Optional[str] = Field(None, alias='notes')

    modified_date: typing.Optional[datetime] = Field(None, alias='modifiedDate')

    country: typing.Optional[str] = Field(None, alias='country')

    payment_or_deduction_indicator: typing.Optional[str] = Field(None, alias='paymentOrDeductionIndicator')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
