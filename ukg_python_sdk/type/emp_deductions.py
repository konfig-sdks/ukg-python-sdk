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


class RequiredEmpDeductions(TypedDict):
    pass

class OptionalEmpDeductions(TypedDict, total=False):
    arrearsAmt: typing.Union[int, float]

    benefitAmount: typing.Union[int, float]

    benefitAmountCalcRule: str

    benefitAmountRateOrPercent: typing.Union[int, float]

    benefitOption: str

    benefitStartDate: datetime

    benefitStatus: str

    benefitStatusDate: datetime

    benefitStopDate: datetime

    companyID: str

    customAmount1: typing.Union[int, float]

    customAmount2: typing.Union[int, float]

    customDate: datetime

    dateSuspendedFrom: datetime

    dateSuspendedTo: datetime

    datetimeChanged: datetime

    datetimeCreated: datetime

    declinedByCarrier: str

    declinedByCarrierDate: datetime

    declinedByCarrierReason: str

    deductionCode: str

    effectiveRecordID: str

    contactID: str

    memberOrCaseNumber: str

    employeeAmount: typing.Union[int, float]

    employeeCalcRateOrPct: typing.Union[int, float]

    employeeCalcRule: str

    employeeCauseNumber: str

    employeeDedLastPaid: datetime

    employeeEligibilityDate: datetime

    employeeFiscalYTDAmt: typing.Union[int, float]

    employeeGoalAmt: typing.Union[int, float]

    employeeGoalToDateAmt: typing.Union[int, float]

    employeeID: str

    employeeLastAmount: typing.Union[int, float]

    employeeMonthToDateAmount: typing.Union[int, float]

    employeeQuarterToDateAmount: typing.Union[int, float]

    employeeYearToDateAmount: typing.Union[int, float]

    evidenceOfInsurabilityDate: datetime

    evidenceOfInsurabilityDesiredAmt: typing.Union[int, float]

    evidenceOfInsurabilityDesiredCalcRateOrPct: typing.Union[int, float]

    employerAmount: typing.Union[int, float]

    employerCalcRateOrPct: typing.Union[int, float]

    employerCalcRule: str

    employerFiscalYearToDateAmount: typing.Union[int, float]

    employerLastAmount: typing.Union[int, float]

    employerMonthToDateAmount: typing.Union[int, float]

    employerQuarterToDateAmount: typing.Union[int, float]

    employerYearToDateAmount: typing.Union[int, float]

    interestAmount: typing.Union[int, float]

    isDeductionOffset: bool

    medicalIndicator: bool

    needEvidenceOfInsurability: bool

    notes: str

    primaryCarePhysician: str

    primaryCarePhysicianId: str

    priorEmployeeAmount: typing.Union[int, float]

    priorEmployeeGoalAmount: typing.Union[int, float]

    priorEmployeeYearToDateAmount: typing.Union[int, float]

    priorEmployerYearToDateAmount: typing.Union[int, float]

    deductionStartDate: datetime

    deductionStopDate: datetime

    systemID: str

    waiveReason: str

    isHomeCompany: bool

    isWaived: bool

    includeInAdditionalCheck: bool

    includeInManualCheck: bool

    employeePerCapAmount: typing.Union[int, float]

    employeePerCapPercent: typing.Union[int, float]

    employeePerCapCalcRule: str

    employeeId: str

    companyId: str

    dedCode: str

    benStatus: str

    endDateTime: datetime

    page: int

    per_Page: int

class EmpDeductions(RequiredEmpDeductions, OptionalEmpDeductions):
    pass
