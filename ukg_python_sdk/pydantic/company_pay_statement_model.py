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

from ukg_python_sdk.pydantic.employee_pay_statement_identifier_model import EmployeePayStatementIdentifierModel

class CompanyPayStatementModel(BaseModel):
    employeeidentifier: typing.Optional[EmployeePayStatementIdentifierModel] = Field(None, alias='employeeidentifier')

    payidentifier: typing.Optional[str] = Field(None, alias='payidentifier')

    paydate: typing.Optional[datetime] = Field(None, alias='paydate')

    document: typing.Optional[str] = Field(None, alias='document')

    totalearnings: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalearnings')

    totaldeductions: typing.Optional[typing.Union[int, float]] = Field(None, alias='totaldeductions')

    totaltaxes: typing.Optional[typing.Union[int, float]] = Field(None, alias='totaltaxes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
