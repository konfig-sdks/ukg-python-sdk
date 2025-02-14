# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.personnel_v1_companies_company_id_employees_employee_id_pto_plans_pto_plan.patch import OnePtoPlan
from ukg_python_sdk.apis.tags.pto_plan_patch_api_raw import PTOPlanPatchApiRaw


class PTOPlanPatchApi(
    OnePtoPlan,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PTOPlanPatchApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PTOPlanPatchApiRaw(api_client)
