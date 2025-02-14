# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.locations_code.get import GetConfigurationRaw
from ukg_python_sdk.paths.locations.get import GetConfigurationsRaw


class LocationsApiRaw(
    GetConfigurationRaw,
    GetConfigurationsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
