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


class EmployeeEmploymentDetails(BaseModel):
    company_i_d: typing.Optional[str] = Field(None, alias='companyID')

    employee_i_d: typing.Optional[str] = Field(None, alias='employeeID')

    primary_job_code: typing.Optional[str] = Field(None, alias='primaryJobCode')

    job_title: typing.Optional[str] = Field(None, alias='jobTitle')

    full_time_or_part_time_code: typing.Optional[str] = Field(None, alias='fullTimeOrPartTimeCode')

    primary_work_location_code: typing.Optional[str] = Field(None, alias='primaryWorkLocationCode')

    primary_project_code: typing.Optional[str] = Field(None, alias='primaryProjectCode')

    deduction_group_code: typing.Optional[str] = Field(None, alias='deductionGroupCode')

    earning_group_code: typing.Optional[str] = Field(None, alias='earningGroupCode')

    employee_type_code: typing.Optional[str] = Field(None, alias='employeeTypeCode')

    employee_status_code: typing.Optional[str] = Field(None, alias='employeeStatusCode')

    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    supervisor_id: typing.Optional[str] = Field(None, alias='supervisorId')

    original_hire_date: typing.Optional[str] = Field(None, alias='originalHireDate')

    last_hire_date: typing.Optional[str] = Field(None, alias='lastHireDate')

    date_of_termination: typing.Optional[str] = Field(None, alias='dateOfTermination')

    date_of_retirement: typing.Optional[str] = Field(None, alias='dateOfRetirement')

    date_time_created: typing.Optional[str] = Field(None, alias='dateTimeCreated')

    date_time_changed: typing.Optional[str] = Field(None, alias='dateTimeChanged')

    date_last_pay_date_paid: typing.Optional[str] = Field(None, alias='dateLastPayDatePaid')

    pay_group: typing.Optional[str] = Field(None, alias='payGroup')

    is_home_company: typing.Optional[str] = Field(None, alias='isHomeCompany')

    page: typing.Optional[int] = Field(None, alias='page')

    per__page: typing.Optional[int] = Field(None, alias='per_Page')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
