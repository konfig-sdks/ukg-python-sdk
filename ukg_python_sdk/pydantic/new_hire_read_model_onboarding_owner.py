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

from ukg_python_sdk.pydantic.new_hire_read_model_onboarding_owner_name import NewHireReadModelOnboardingOwnerName

class NewHireReadModelOnboardingOwner(BaseModel):
    # Id of the onboarding owner
    id: typing.Optional[str] = Field(None, alias='id')

    # External user identifier of the onboarding owner
    external_user_id: typing.Optional[str] = Field(None, alias='externalUserId')

    # Email of the onboarding owner
    email: typing.Optional[str] = Field(None, alias='email')

    name: typing.Optional[NewHireReadModelOnboardingOwnerName] = Field(None, alias='name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
