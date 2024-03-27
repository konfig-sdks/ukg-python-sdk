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

from ukg_python_sdk.type.new_hires_get_by_id_response_compensation import NewHiresGetByIdResponseCompensation
from ukg_python_sdk.type.new_hires_get_by_id_response_contact_information import NewHiresGetByIdResponseContactInformation
from ukg_python_sdk.type.new_hires_get_by_id_response_job import NewHiresGetByIdResponseJob
from ukg_python_sdk.type.new_hires_get_by_id_response_mentor import NewHiresGetByIdResponseMentor
from ukg_python_sdk.type.new_hires_get_by_id_response_onboarding_owner import NewHiresGetByIdResponseOnboardingOwner
from ukg_python_sdk.type.new_hires_get_by_id_response_organization_levels import NewHiresGetByIdResponseOrganizationLevels
from ukg_python_sdk.type.new_hires_get_by_id_response_provisioning import NewHiresGetByIdResponseProvisioning

class RequiredNewHiresGetByIdResponse(TypedDict):
    pass

class OptionalNewHiresGetByIdResponse(TypedDict, total=False):
    # Unique identifier of the new hire
    id: str

    contactInformation: NewHiresGetByIdResponseContactInformation

    job: NewHiresGetByIdResponseJob

    organizationLevels: NewHiresGetByIdResponseOrganizationLevels

    compensation: NewHiresGetByIdResponseCompensation

    onboardingOwner: NewHiresGetByIdResponseOnboardingOwner

    # Hire date of the new hire
    hireDate: datetime

    # Orientation date of the new hire
    orientationDate: datetime

    # Start date of the new hire
    startDate: datetime

    # Reason why the new hire start date is 4 or more business days in the past
    pastStartDateReason: str

    mentor: NewHiresGetByIdResponseMentor

    # Personalized welcome message for the new hire
    personalMessage: str

    provisioning: NewHiresGetByIdResponseProvisioning

    # The status of the new hire in onboarding
    onboardingStatus: str

    # Identity user identifier of the new hire
    identityUserId: str

    # External user identifier of the new hire
    externalUserId: str

    # Employee number of the new hire
    employeeNumber: str

    # Date that the new hire was processed
    sentToProcessHireDate: datetime

    # Launch date of the new hire
    launchedOn: datetime

    # Creation date of the new hire
    createdAt: datetime

    # Last updated date of the new hire
    updatedAt: datetime

class NewHiresGetByIdResponse(RequiredNewHiresGetByIdResponse, OptionalNewHiresGetByIdResponse):
    pass
