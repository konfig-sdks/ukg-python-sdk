# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.hours_worked.post import AddTimeEntriesRaw
from ukg_python_sdk.paths.time_pending_clock_transactions.get import GetPendingTransactionsRaw
from ukg_python_sdk.paths.time_clock_transactions.get import GetProcessedTransactionsRaw
from ukg_python_sdk.paths.time_work_summaries.get import GetWorkSummariesRaw
from ukg_python_sdk.paths.time_work_summary.get import GetWorkSummaryByIdRaw


class TimeApiRaw(
    AddTimeEntriesRaw,
    GetPendingTransactionsRaw,
    GetProcessedTransactionsRaw,
    GetWorkSummariesRaw,
    GetWorkSummaryByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
