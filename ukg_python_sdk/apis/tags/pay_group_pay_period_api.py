# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.payroll_v1_paygroup_payperiods.get import GetPayGroupPayPeriod
from ukg_python_sdk.apis.tags.pay_group_pay_period_api_raw import PayGroupPayPeriodApiRaw


class PayGroupPayPeriodApi(
    GetPayGroupPayPeriod,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PayGroupPayPeriodApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PayGroupPayPeriodApiRaw(api_client)
