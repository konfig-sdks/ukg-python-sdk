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


class Roles(BaseModel):
    rol_default_role: typing.Optional[bool] = Field(None, alias='rolDefaultRole')

    rol_description: typing.Optional[str] = Field(None, alias='rolDescription')

    rol_i_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='rolID')

    rol_name: typing.Optional[str] = Field(None, alias='rolName')

    rol_default_role_terminated: typing.Optional[bool] = Field(None, alias='rolDefaultRoleTerminated')

    rol_b_i: typing.Optional[bool] = Field(None, alias='rolBI')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
