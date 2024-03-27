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

from ukg_python_sdk.type.application_candidate_name import ApplicationCandidateName

class RequiredApplicationCandidate(TypedDict):
    pass

class OptionalApplicationCandidate(TypedDict, total=False):
    # The id of the candidate who has applied to an opportunity.
    id: str

    # A flag indicating whether the candidate is an internal employee. 
    is_inrernal: bool

    # A flag indicating whether the candidate is an active employee. Can only be specified when is_internal is true.
    is_active: bool

    name: ApplicationCandidateName

class ApplicationCandidate(RequiredApplicationCandidate, OptionalApplicationCandidate):
    pass
