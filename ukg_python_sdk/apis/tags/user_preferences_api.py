# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.personnel_v1_user_preferences.get import GetUserPreferencesDetails
from ukg_python_sdk.apis.tags.user_preferences_api_raw import UserPreferencesApiRaw


class UserPreferencesApi(
    GetUserPreferencesDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UserPreferencesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UserPreferencesApiRaw(api_client)
