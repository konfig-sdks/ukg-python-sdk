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

from ukg_python_sdk.type.creator_background_check_integration import CreatorBackgroundCheckIntegration
from ukg_python_sdk.type.creator_contact_info import CreatorContactInfo
from ukg_python_sdk.type.creator_name import CreatorName
from ukg_python_sdk.type.creator_preferred_locale import CreatorPreferredLocale
from ukg_python_sdk.type.creator_roles import CreatorRoles
from ukg_python_sdk.type.hyperlinks import Hyperlinks
from ukg_python_sdk.type.links import Links

class RequiredCreator(TypedDict):
    pass

class OptionalCreator(TypedDict, total=False):
    # The id of the recruiter who created the background check order.
    id: str

    # The recruiter id in the core HR system.
    person_id: str

    # The date of this user creation date.
    created_at: str

    # The alternative user id that can be used in third-party vendors’ integrations. Returned only for users with the “recruiter”, “hiring-manager”, or “recruiting-administrator” role.
    integration_user_id: str

    # A flag indicating whether the recruiter is an internal employee. 
    is_internal: bool

    # A flag indicating whether the recruiter is an active employee. Can only be specified when is_internal is true.
    is_active: bool

    preferred_locale: CreatorPreferredLocale

    name: CreatorName

    contact_info: CreatorContactInfo

    roles: CreatorRoles

    hyperlinks: typing.List[Hyperlinks]

    updated_at: str

    links: typing.List[Links]

    background_check_integration: CreatorBackgroundCheckIntegration

class Creator(RequiredCreator, OptionalCreator):
    pass
