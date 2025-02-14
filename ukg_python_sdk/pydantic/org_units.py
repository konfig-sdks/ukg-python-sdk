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

from ukg_python_sdk.pydantic.org_units_org_level import OrgUnitsOrgLevel

class OrgUnits(BaseModel):
    # The id of organizational unit associated with the position the candidate has been hired for
    id: typing.Optional[str] = Field(None, alias='id')

    # The organizational unit’s code in the core HR system
    code: typing.Optional[str] = Field(None, alias='code')

    org_level: typing.Optional[OrgUnitsOrgLevel] = Field(None, alias='org_level')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
