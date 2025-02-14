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

from ukg_python_sdk.type.new_hires_get_by_id_response_job_supervisor_name_prefix import NewHiresGetByIdResponseJobSupervisorNamePrefix
from ukg_python_sdk.type.new_hires_get_by_id_response_job_supervisor_name_suffix import NewHiresGetByIdResponseJobSupervisorNameSuffix

class RequiredNewHiresGetByIdResponseJobSupervisorName(TypedDict):
    pass

class OptionalNewHiresGetByIdResponseJobSupervisorName(TypedDict, total=False):
    prefix: NewHiresGetByIdResponseJobSupervisorNamePrefix

    # First name
    first: str

    # Middle name
    middle: str

    # Last name
    last: str

    # Former last name
    formerLast: str

    suffix: NewHiresGetByIdResponseJobSupervisorNameSuffix

    # Preferred first name
    preferredFirst: str

class NewHiresGetByIdResponseJobSupervisorName(RequiredNewHiresGetByIdResponseJobSupervisorName, OptionalNewHiresGetByIdResponseJobSupervisorName):
    pass
