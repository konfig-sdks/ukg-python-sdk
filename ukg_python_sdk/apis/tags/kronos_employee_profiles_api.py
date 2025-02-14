# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.personnel_v1_integration_kronos_employee_profiles.get import GetList
from ukg_python_sdk.apis.tags.kronos_employee_profiles_api_raw import KronosEmployeeProfilesApiRaw


class KronosEmployeeProfilesApi(
    GetList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: KronosEmployeeProfilesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = KronosEmployeeProfilesApiRaw(api_client)
