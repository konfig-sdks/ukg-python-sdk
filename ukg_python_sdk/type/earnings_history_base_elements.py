# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredEarningsHistoryBaseElements(TypedDict):
    pass

class OptionalEarningsHistoryBaseElements(TypedDict, total=False):
    employeeId: str

    companyId: str

    earningCode: str

    employeeNumber: str

    genNumber: str

    periodControl: str

    payGroup: str

    accrualCode: str

    baseAmount: typing.Union[int, float]

    batchID: str

    calculationRule: str

    calculationSequence: str

    currentAmount: typing.Union[int, float]

    currentHours: typing.Union[int, float]

    glBaseSegmentId: str

    glFollowBaseAccountAllocation: str

    grossUp: str

    grossUpTarget: typing.Union[int, float]

    grossUpTaxCalculationMethod: int

    hourlyPayRate: typing.Union[int, float]

    includeInDeferredCompensation: bool

    includeInDeferredCompensationHours: bool

    isVoided: bool

    isVoidingRecord: bool

    jobCode: str

    jobPremiumAmount: typing.Union[int, float]

    jobPremiumRateOrPercent: typing.Union[int, float]

    location: str

    numberOfDays: int

    numberOfGames: int

    payDate: datetime

    payoutRateType: str

    payRate: typing.Union[int, float]

    paySheetID: str

    periodPayRate: typing.Union[int, float]

    pieceCount: typing.Union[int, float]

    piecePayRate: typing.Union[int, float]

    planYear: str

    project: str

    reportCategory: str

    taxCalculationGroupId: str

    taxCategory: str

    timeClockCode: str

    tipCredit: typing.Union[int, float]

    tipGrossReceipts: typing.Union[int, float]

    tipType: str

    useDeductionOffSet: bool

    ytdAmount: typing.Union[int, float]

    ytdShiftAmount: typing.Union[int, float]

class EarningsHistoryBaseElements(RequiredEarningsHistoryBaseElements, OptionalEarningsHistoryBaseElements):
    pass
