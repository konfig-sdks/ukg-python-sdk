# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.payroll_v1_earnings_history_base_elements.get import GetInsRate
from ukg_python_sdk.apis.tags.earnings_history_api_raw import EarningsHistoryApiRaw


class EarningsHistoryApi(
    GetInsRate,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EarningsHistoryApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EarningsHistoryApiRaw(api_client)
