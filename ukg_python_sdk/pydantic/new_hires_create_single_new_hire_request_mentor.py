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


class NewHiresCreateSingleNewHireRequestMentor(BaseModel):
    # Brief description of mentor
    description: typing.Optional[str] = Field(None, alias='description')

    # Onboarding employee id
    id: typing.Optional[str] = Field(None, alias='id')

    # Person Id from UltiPro
    code: typing.Optional[str] = Field(None, alias='code')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
