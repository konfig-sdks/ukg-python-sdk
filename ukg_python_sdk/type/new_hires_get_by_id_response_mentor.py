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

from ukg_python_sdk.type.new_hires_get_by_id_response_mentor_name import NewHiresGetByIdResponseMentorName

class RequiredNewHiresGetByIdResponseMentor(TypedDict):
    pass

class OptionalNewHiresGetByIdResponseMentor(TypedDict, total=False):
    # Description of the mentor
    description: str

    # Id of the mentor
    id: str

    # External user identifier of the mentor
    externalUserId: str

    # Email of the mentor
    email: str

    name: NewHiresGetByIdResponseMentorName

class NewHiresGetByIdResponseMentor(RequiredNewHiresGetByIdResponseMentor, OptionalNewHiresGetByIdResponseMentor):
    pass
