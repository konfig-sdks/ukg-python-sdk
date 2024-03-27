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


class RequiredEmpEmploymentDetails(TypedDict):
    pass

class OptionalEmpEmploymentDetails(TypedDict, total=False):
    companyID: str

    companyCode: str

    companyName: str

    employeeID: str

    jobDescription: str

    payGroupDescription: str

    primaryJobCode: str

    orgLevel1Code: str

    orgLevel2Code: str

    orgLevel3Code: str

    orgLevel4Code: str

    originalHireDate: datetime

    lastHireDate: datetime

    fullTimeOrPartTimeCode: str

    primaryWorkLocationCode: str

    languageCode: str

    primaryProjectCode: str

    workPhoneNumber: str

    workPhoneExtension: str

    workPhoneCountry: str

    dateInJob: datetime

    dateLastWorked: datetime

    dateOfBenefitSeniority: datetime

    dateOfSeniority: datetime

    deductionGroupCode: str

    earningGroupCode: str

    employeeTypeCode: str

    employeeStatusCode: str

    employeeNumber: str

    jobChangeReasonCode: str

    jobTitle: str

    leaveReasonCode: str

    supervisorID: str

    supervisorFirstName: str

    supervisorLastName: str

    autoAllocate: str

    clockCode: str

    dateLastPayDatePaid: datetime

    dateOfEarlyRetirement: datetime

    dateOfLocalUnion: datetime

    dateOfNationalUnion: datetime

    dateOfRetirement: datetime

    dateOfSuspension: datetime

    dateOfTermination: datetime

    datePaidThru: datetime

    statusStartDate: datetime

    hireSource: str

    isAutoAllocated: str

    isAutopaid: str

    isMultipleJob: str

    jobGroupCode: str

    mailstop: str

    okToRehire: str

    payGroup: str

    payPeriod: str

    plannedLeaveReason: str

    positionCode: str

    salaryOrHourly: str

    scheduledAnnualHrs: typing.Union[int, float]

    scheduledFTE: typing.Union[int, float]

    scheduledWorkHrs: typing.Union[int, float]

    shift: str

    shiftGroup: str

    termReason: str

    terminationReasonDescription: str

    termType: str

    timeclockID: str

    unionLocal: str

    unionNational: str

    weeklyHours: typing.Union[int, float]

    dateTimeCreated: datetime

    dateTimeChanged: datetime

    supervisorEmployeeNumber: str

    supervisorCOID: str

    supervisorCompanyCode: str

    companyGLSegment: str

    locationGLSegment: str

class EmpEmploymentDetails(RequiredEmpEmploymentDetails, OptionalEmpEmploymentDetails):
    pass
