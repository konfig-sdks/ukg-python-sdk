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

from ukg_python_sdk.pydantic.ultimate_software_foundation_services_api_ulti_pro_personnel_platform_configuration_v2_models_field_data import UltimateSoftwareFoundationServicesApiUltiProPersonnelPlatformConfigurationV2ModelsFieldData

class UltimateSoftwareFoundationServicesApiUltiProPersonnelPlatformConfigurationV2ModelsPcData(BaseModel):
    field_rows: typing.Optional[typing.List[UltimateSoftwareFoundationServicesApiUltiProPersonnelPlatformConfigurationV2ModelsFieldData]] = Field(None, alias='fieldRows')

    class_name: typing.Optional[str] = Field(None, alias='className')

    key_name: typing.Optional[str] = Field(None, alias='keyName')

    key_value: typing.Optional[str] = Field(None, alias='keyValue')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
