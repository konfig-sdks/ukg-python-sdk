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


class ApplicationJobBoard(BaseModel):
    # The id of the job board on which the opportunity has been published to.
    id: typing.Optional[str] = Field(None, alias='id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
