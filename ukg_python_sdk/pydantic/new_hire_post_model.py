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

from ukg_python_sdk.pydantic.new_hire_post_model_compensation import NewHirePostModelCompensation
from ukg_python_sdk.pydantic.new_hire_post_model_contact_information import NewHirePostModelContactInformation
from ukg_python_sdk.pydantic.new_hire_post_model_job import NewHirePostModelJob
from ukg_python_sdk.pydantic.new_hire_post_model_mentor import NewHirePostModelMentor
from ukg_python_sdk.pydantic.new_hire_post_model_organization_levels import NewHirePostModelOrganizationLevels

class NewHirePostModel(BaseModel):
    contact_information: typing.Optional[NewHirePostModelContactInformation] = Field(None, alias='contactInformation')

    job: typing.Optional[NewHirePostModelJob] = Field(None, alias='job')

    organization_levels: typing.Optional[NewHirePostModelOrganizationLevels] = Field(None, alias='organizationLevels')

    compensation: typing.Optional[NewHirePostModelCompensation] = Field(None, alias='compensation')

    # External user identifier of the onboarding owner
    onboarding_owner_id: typing.Optional[str] = Field(None, alias='onboardingOwnerId')

    # Hire date of the new hire
    hire_date: typing.Optional[datetime] = Field(None, alias='hireDate')

    # Orientation date of the new hire
    orientation_date: typing.Optional[datetime] = Field(None, alias='orientationDate')

    # Start date of the new hire
    start_date: typing.Optional[datetime] = Field(None, alias='startDate')

    # Reason why the new hire start date is 4 or more business days in the past
    past_start_date_reason: typing.Optional[str] = Field(None, alias='pastStartDateReason')

    mentor: typing.Optional[NewHirePostModelMentor] = Field(None, alias='mentor')

    # Personal message for the new hire
    personal_message: typing.Optional[str] = Field(None, alias='personalMessage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
