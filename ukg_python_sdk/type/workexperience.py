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

from ukg_python_sdk.type.workexperience_from import WorkexperienceFrom
from ukg_python_sdk.type.workexperience_to import WorkexperienceTo

RequiredWorkexperience = TypedDict("RequiredWorkexperience", {
    })

OptionalWorkexperience = TypedDict("OptionalWorkexperience", {
    # The job description. Maximum of 2000 characters.
    "description": str,

    # The id of the candidate’s work experience record. 
    "id": str,

    # The job title of the experience. Maximum of 100 characters.
    "job_title": str,

    # The company name of the experience. Maximum of 100 characters.
    "company": str,

    # The job location. Maximum of 20 characters.
    "location": str,

    "from": WorkexperienceFrom,

    "to": WorkexperienceTo,
    }, total=False)

class Workexperience(RequiredWorkexperience, OptionalWorkexperience):
    pass
