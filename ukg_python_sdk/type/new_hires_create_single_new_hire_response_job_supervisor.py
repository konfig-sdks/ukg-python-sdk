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

from ukg_python_sdk.type.new_hires_create_single_new_hire_response_job_supervisor_name import NewHiresCreateSingleNewHireResponseJobSupervisorName

class RequiredNewHiresCreateSingleNewHireResponseJobSupervisor(TypedDict):
    pass

class OptionalNewHiresCreateSingleNewHireResponseJobSupervisor(TypedDict, total=False):
    # Id of the supervisor
    id: str

    name: NewHiresCreateSingleNewHireResponseJobSupervisorName

    # The email of the supervisor
    email: str

    # The external user id of the supervisor
    externalUserId: str

class NewHiresCreateSingleNewHireResponseJobSupervisor(RequiredNewHiresCreateSingleNewHireResponseJobSupervisor, OptionalNewHiresCreateSingleNewHireResponseJobSupervisor):
    pass
