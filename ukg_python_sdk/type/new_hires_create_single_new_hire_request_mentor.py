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


class RequiredNewHiresCreateSingleNewHireRequestMentor(TypedDict):
    pass

class OptionalNewHiresCreateSingleNewHireRequestMentor(TypedDict, total=False):
    # Brief description of mentor
    description: str

    # Onboarding employee id
    id: str

    # Person Id from UltiPro
    code: str

class NewHiresCreateSingleNewHireRequestMentor(RequiredNewHiresCreateSingleNewHireRequestMentor, OptionalNewHiresCreateSingleNewHireRequestMentor):
    pass
