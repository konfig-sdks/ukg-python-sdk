# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.military_era.post import CreateConfigurationUkgProRaw
from ukg_python_sdk.paths.military_era.get import GetConfigurationsRaw
from ukg_python_sdk.paths.military_era_code.put import UpdateConfigurationRaw


class MilitaryEraApiRaw(
    CreateConfigurationUkgProRaw,
    GetConfigurationsRaw,
    UpdateConfigurationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
