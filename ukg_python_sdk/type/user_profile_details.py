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


class RequiredUserProfileDetails(TypedDict):
    pass

class OptionalUserProfileDetails(TypedDict, total=False):
    employeeId: str

    companyId: str

    firstName: str

    lastName: str

    personId: str

    email: str

    workPhone: str

    userStatus: str

    userId: int

    userName: str

    roleId: int

    roleName: str

    roleDescription: str

    integrationUserKey: str

    filterCompanyId: str

    filterDeductionGroupCode: str

    filterEmployeeType: str

    filterStatus: str

    filterFullTimeOrPartTime: str

    filterJobCode: str

    filterLocationCode: str

    filterOrganizationLevel1: str

    filterOrganizationLevel2: str

    filterOrganizationLevel3: str

    filterOrganizationLevel4: str

    filterPayGroupCode: str

    filterProjectCode: str

    filterSalaryOrHourly: str

    filterShiftCode: str

    filterSupervisorID: str

    filterTaxCalculationGroupID: str

    masterCompany: str

    masterCompanyId: str

    homeCompany: str

    homeCompanyId: str

class UserProfileDetails(RequiredUserProfileDetails, OptionalUserProfileDetails):
    pass
