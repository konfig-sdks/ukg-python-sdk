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


class EmployeeEducationModel(BaseModel):
    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    system_id: typing.Optional[str] = Field(None, alias='systemId')

    school: typing.Optional[str] = Field(None, alias='school')

    education_level: typing.Optional[str] = Field(None, alias='educationLevel')

    education_major: typing.Optional[str] = Field(None, alias='educationMajor')

    education_minor: typing.Optional[str] = Field(None, alias='educationMinor')

    gpa: typing.Optional[str] = Field(None, alias='gpa')

    begin_date: typing.Optional[datetime] = Field(None, alias='beginDate')

    end_date: typing.Optional[datetime] = Field(None, alias='endDate')

    is_graduate: typing.Optional[bool] = Field(None, alias='isGraduate')

    is_highest_level: typing.Optional[bool] = Field(None, alias='isHighestLevel')

    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    country: typing.Optional[str] = Field(None, alias='country')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
