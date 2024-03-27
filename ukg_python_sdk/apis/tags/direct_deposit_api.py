# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.payroll_v1_companies_company_id_direct_deposit.get import ListDirectDepositDetailsByCompany
from ukg_python_sdk.paths.payroll_v1_direct_deposit.get import ListEmployeeDirectDepositDetails
from ukg_python_sdk.apis.tags.direct_deposit_api_raw import DirectDepositApiRaw


class DirectDepositApi(
    ListDirectDepositDetailsByCompany,
    ListEmployeeDirectDepositDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DirectDepositApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DirectDepositApiRaw(api_client)
