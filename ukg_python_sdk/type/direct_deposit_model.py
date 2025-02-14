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


class RequiredDirectDepositModel(TypedDict):
    pass

class OptionalDirectDepositModel(TypedDict, total=False):
    description: str

    account: str

    accountType: str

    amountOrPercent: typing.Union[int, float]

    companyId: str

    directDepositOrPrenote: str

    depositRule: str

    employeeBankId: str

    employeeBankName: str

    employeeBankRoutingNumber: str

    employeeId: str

    firstPrenotePayDate: datetime

    sequenceNumber: str

    employeeInstitutionNumber: str

    countryCode: str

    foreignAccountNumber: str

    foreignAccountNumberType: str

    accountRecordId: str

    dateTimeChanged: datetime

    accountIsInactive: bool

class DirectDepositModel(RequiredDirectDepositModel, OptionalDirectDepositModel):
    pass
