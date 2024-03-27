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


class PtoPlans(BaseModel):
    # Employee Identifier
    employee_id: str = Field(alias='employeeId')

    # Company Identifier
    company_id: str = Field(alias='companyId')

    # PTO Plan Identifier
    pto_plan: str = Field(alias='ptoPlan')

    # Amount of hours earned for PTO
    earned: typing.Optional[typing.Union[int, float]] = Field(None, alias='earned')

    # Amount of hours taken for PTO
    taken: typing.Optional[typing.Union[int, float]] = Field(None, alias='taken')

    # Balance of PTO hours
    pending_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='pendingBalance')

    # Date in which PTO is earned through, format should be YYYY-MM-DD
    earned_through_date: typing.Optional[str] = Field(None, alias='earnedThroughDate')

    # Date in which the PTO reset's, format should be YYYY-MM-DD
    reset: typing.Optional[str] = Field(None, alias='reset')

    # Date to be used if pending rules are relevant, format should be YYYY-MM-DD
    pending_move_date: typing.Optional[str] = Field(None, alias='pendingMoveDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
