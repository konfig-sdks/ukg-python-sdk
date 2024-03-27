# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.personnel_v1_user_profile_details.get import GetAllDetails
from ukg_python_sdk.apis.tags.user_profile_details_api_raw import UserProfileDetailsApiRaw


class UserProfileDetailsApi(
    GetAllDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UserProfileDetailsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UserProfileDetailsApiRaw(api_client)
