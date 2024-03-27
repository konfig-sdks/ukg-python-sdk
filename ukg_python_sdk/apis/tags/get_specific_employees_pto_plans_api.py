# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.personnel_v1_companies_company_id_employees_employee_id_pto_plans.get import Info
from ukg_python_sdk.apis.tags.get_specific_employees_pto_plans_api_raw import GetSpecificEmployeesPTOPlansApiRaw


class GetSpecificEmployeesPTOPlansApi(
    Info,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GetSpecificEmployeesPTOPlansApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GetSpecificEmployeesPTOPlansApiRaw(api_client)
