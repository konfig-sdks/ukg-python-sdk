# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.personnel_v1_pto_plans.post import UltiproRecord
from ukg_python_sdk.apis.tags.pto_plan_post_api_raw import PTOPlanPostApiRaw


class PTOPlanPostApi(
    UltiproRecord,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PTOPlanPostApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PTOPlanPostApiRaw(api_client)
