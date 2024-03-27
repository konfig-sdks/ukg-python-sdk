# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.hours_worked.post import AddTimeEntries
from ukg_python_sdk.paths.time_pending_clock_transactions.get import GetPendingTransactions
from ukg_python_sdk.paths.time_clock_transactions.get import GetProcessedTransactions
from ukg_python_sdk.paths.time_work_summaries.get import GetWorkSummaries
from ukg_python_sdk.paths.time_work_summary.get import GetWorkSummaryById
from ukg_python_sdk.apis.tags.time_api_raw import TimeApiRaw


class TimeApi(
    AddTimeEntries,
    GetPendingTransactions,
    GetProcessedTransactions,
    GetWorkSummaries,
    GetWorkSummaryById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TimeApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TimeApiRaw(api_client)
