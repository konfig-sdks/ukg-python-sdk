# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.personnel_v1_empl_multiple_jobs.get import ListDetails
from ukg_python_sdk.apis.tags.employee_multiple_jobs_opp_api_raw import EmployeeMultipleJobsOPPApiRaw


class EmployeeMultipleJobsOPPApi(
    ListDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EmployeeMultipleJobsOPPApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EmployeeMultipleJobsOPPApiRaw(api_client)
