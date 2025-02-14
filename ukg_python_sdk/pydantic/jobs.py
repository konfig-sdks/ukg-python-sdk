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


class Jobs(BaseModel):
    # Job title.
    title: str = Field(alias='title')

    # Job country code.
    country_code: str = Field(alias='countryCode')

    # Job Code, the unique identifier.
    code: str = Field(alias='code')

    # Job family code.
    job_family_code: typing.Optional[str] = Field(None, alias='jobFamilyCode')

    # The job status.
    is_active: typing.Optional[bool] = Field(None, alias='isActive')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
