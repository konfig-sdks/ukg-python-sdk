# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.award_type.post import CreateConfiguration
from ukg_python_sdk.paths.award_type.get import GetAllConfigurations
from ukg_python_sdk.paths.award_type_code.put import UpdateConfiguration
from ukg_python_sdk.apis.tags.award_type_api_raw import AwardTypeApiRaw


class AwardTypeApi(
    CreateConfiguration,
    GetAllConfigurations,
    UpdateConfiguration,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AwardTypeApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AwardTypeApiRaw(api_client)
