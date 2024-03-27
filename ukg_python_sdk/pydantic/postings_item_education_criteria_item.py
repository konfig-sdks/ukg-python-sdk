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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from ukg_python_sdk.pydantic.postings_item_education_criteria_item_degree import PostingsItemEducationCriteriaItemDegree
from ukg_python_sdk.pydantic.postings_item_education_criteria_item_major import PostingsItemEducationCriteriaItemMajor

class PostingsItemEducationCriteriaItem(BaseModel):
    # Indicates if this education is required for the job.
    is_required: typing.Optional[bool] = Field(None, alias='is_required')

    # Indicates if similar educations will be considered for this job.
    allow_related: typing.Optional[bool] = Field(None, alias='allow_related')

    degree: typing.Optional[PostingsItemEducationCriteriaItemDegree] = Field(None, alias='degree')

    major: typing.Optional[PostingsItemEducationCriteriaItemMajor] = Field(None, alias='major')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
