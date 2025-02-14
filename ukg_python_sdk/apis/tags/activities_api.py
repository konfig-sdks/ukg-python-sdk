# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.simpleschedule_activities.get import GetAll
from ukg_python_sdk.apis.tags.activities_api_raw import ActivitiesApiRaw


class ActivitiesApi(
    GetAll,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ActivitiesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ActivitiesApiRaw(api_client)
