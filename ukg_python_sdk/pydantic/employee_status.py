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


class EmployeeStatus(BaseModel):
    as_of_date: typing.Optional[datetime] = Field(None, alias='asOfDate')

    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    trigger_termination: typing.Optional[bool] = Field(None, alias='triggerTermination')

    status: typing.Optional[str] = Field(None, alias='status')

    status_start_date: typing.Optional[datetime] = Field(None, alias='statusStartDate')

    status_reason: typing.Optional[str] = Field(None, alias='statusReason')

    status_reason_desc: typing.Optional[str] = Field(None, alias='statusReasonDesc')

    is_primary: typing.Optional[bool] = Field(None, alias='isPrimary')

    is_primary_effective_date: typing.Optional[datetime] = Field(None, alias='isPrimaryEffectiveDate')

    original_hire_date: typing.Optional[datetime] = Field(None, alias='originalHireDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
