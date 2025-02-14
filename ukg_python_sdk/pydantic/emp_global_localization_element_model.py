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


class EmpGlobalLocalizationElementModel(BaseModel):
    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    field_id: typing.Optional[str] = Field(None, alias='fieldId')

    field_name: typing.Optional[str] = Field(None, alias='fieldName')

    boolean_value: typing.Optional[bool] = Field(None, alias='booleanValue')

    numeric_value: typing.Optional[str] = Field(None, alias='numericValue')

    date_time_value: typing.Optional[str] = Field(None, alias='dateTimeValue')

    string_value: typing.Optional[str] = Field(None, alias='stringValue')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    created: typing.Optional[str] = Field(None, alias='created')

    effective: typing.Optional[str] = Field(None, alias='effective')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
