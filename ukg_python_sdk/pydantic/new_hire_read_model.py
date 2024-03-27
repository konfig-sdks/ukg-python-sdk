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

from ukg_python_sdk.pydantic.new_hire_read_model_compensation import NewHireReadModelCompensation
from ukg_python_sdk.pydantic.new_hire_read_model_contact_information import NewHireReadModelContactInformation
from ukg_python_sdk.pydantic.new_hire_read_model_job import NewHireReadModelJob
from ukg_python_sdk.pydantic.new_hire_read_model_mentor import NewHireReadModelMentor
from ukg_python_sdk.pydantic.new_hire_read_model_onboarding_owner import NewHireReadModelOnboardingOwner
from ukg_python_sdk.pydantic.new_hire_read_model_organization_levels import NewHireReadModelOrganizationLevels
from ukg_python_sdk.pydantic.new_hire_read_model_provisioning import NewHireReadModelProvisioning

class NewHireReadModel(BaseModel):
    # Unique identifier of the new hire
    id: typing.Optional[str] = Field(None, alias='id')

    contact_information: typing.Optional[NewHireReadModelContactInformation] = Field(None, alias='contactInformation')

    job: typing.Optional[NewHireReadModelJob] = Field(None, alias='job')

    organization_levels: typing.Optional[NewHireReadModelOrganizationLevels] = Field(None, alias='organizationLevels')

    compensation: typing.Optional[NewHireReadModelCompensation] = Field(None, alias='compensation')

    onboarding_owner: typing.Optional[NewHireReadModelOnboardingOwner] = Field(None, alias='onboardingOwner')

    # Hire date of the new hire
    hire_date: typing.Optional[datetime] = Field(None, alias='hireDate')

    # Orientation date of the new hire
    orientation_date: typing.Optional[datetime] = Field(None, alias='orientationDate')

    # Start date of the new hire
    start_date: typing.Optional[datetime] = Field(None, alias='startDate')

    # Reason why the new hire start date is 4 or more business days in the past
    past_start_date_reason: typing.Optional[str] = Field(None, alias='pastStartDateReason')

    mentor: typing.Optional[NewHireReadModelMentor] = Field(None, alias='mentor')

    # Personalized welcome message for the new hire
    personal_message: typing.Optional[str] = Field(None, alias='personalMessage')

    provisioning: typing.Optional[NewHireReadModelProvisioning] = Field(None, alias='provisioning')

    # The status of the new hire in onboarding
    onboarding_status: typing.Optional[str] = Field(None, alias='onboardingStatus')

    # Identity user identifier of the new hire
    identity_user_id: typing.Optional[str] = Field(None, alias='identityUserId')

    # External user identifier of the new hire
    external_user_id: typing.Optional[str] = Field(None, alias='externalUserId')

    # Employee number of the new hire
    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    # Date that the new hire was processed
    sent_to_process_hire_date: typing.Optional[datetime] = Field(None, alias='sentToProcessHireDate')

    # Launch date of the new hire
    launched_on: typing.Optional[datetime] = Field(None, alias='launchedOn')

    # Creation date of the new hire
    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    # Last updated date of the new hire
    updated_at: typing.Optional[datetime] = Field(None, alias='updatedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
