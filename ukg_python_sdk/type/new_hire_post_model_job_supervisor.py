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


class RequiredNewHirePostModelJobSupervisor(TypedDict):
    pass

class OptionalNewHirePostModelJobSupervisor(TypedDict, total=False):
    # Onboarding employee Id
    id: str

    # Person Id from UltiPro
    code: str

class NewHirePostModelJobSupervisor(RequiredNewHirePostModelJobSupervisor, OptionalNewHirePostModelJobSupervisor):
    pass
