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

from ukg_python_sdk.pydantic.output_application import OutputApplication
from ukg_python_sdk.pydantic.output_candidate import OutputCandidate
from ukg_python_sdk.pydantic.output_creator import OutputCreator
from ukg_python_sdk.pydantic.output_opportunity import OutputOpportunity

class Output(BaseModel):
    candidate: typing.Optional[OutputCandidate] = Field(None, alias='candidate')

    application: typing.Optional[OutputApplication] = Field(None, alias='application')

    opportunity: typing.Optional[OutputOpportunity] = Field(None, alias='opportunity')

    creator: typing.Optional[OutputCreator] = Field(None, alias='creator')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
