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

from ukg_python_sdk.pydantic.new_hire_read_model_mentor_name import NewHireReadModelMentorName

class NewHireReadModelMentor(BaseModel):
    # Description of the mentor
    description: typing.Optional[str] = Field(None, alias='description')

    # Id of the mentor
    id: typing.Optional[str] = Field(None, alias='id')

    # External user identifier of the mentor
    external_user_id: typing.Optional[str] = Field(None, alias='externalUserId')

    # Email of the mentor
    email: typing.Optional[str] = Field(None, alias='email')

    name: typing.Optional[NewHireReadModelMentorName] = Field(None, alias='name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
