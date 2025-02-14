# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.personnel_v2_platform_configuration_fields_class_name_class_name.get import GetFieldsData
from ukg_python_sdk.apis.tags.v2_platform_configuration_custom_fields_data_api_raw import V2PlatformConfigurationCustomFieldsDataApiRaw


class V2PlatformConfigurationCustomFieldsDataApi(
    GetFieldsData,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: V2PlatformConfigurationCustomFieldsDataApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = V2PlatformConfigurationCustomFieldsDataApiRaw(api_client)
