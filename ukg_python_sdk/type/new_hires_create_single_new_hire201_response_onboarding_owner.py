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

from ukg_python_sdk.type.new_hires_create_single_new_hire201_response_onboarding_owner_name import NewHiresCreateSingleNewHire201ResponseOnboardingOwnerName

class RequiredNewHiresCreateSingleNewHire201ResponseOnboardingOwner(TypedDict):
    pass

class OptionalNewHiresCreateSingleNewHire201ResponseOnboardingOwner(TypedDict, total=False):
    # Id of the onboarding owner
    id: str

    # External user identifier of the onboarding owner
    externalUserId: str

    # Email of the onboarding owner
    email: str

    name: NewHiresCreateSingleNewHire201ResponseOnboardingOwnerName

class NewHiresCreateSingleNewHire201ResponseOnboardingOwner(RequiredNewHiresCreateSingleNewHire201ResponseOnboardingOwner, OptionalNewHiresCreateSingleNewHire201ResponseOnboardingOwner):
    pass
