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


class RequiredContact(TypedDict):
    pass

class OptionalContact(TypedDict, total=False):
    city: str

    countryCode: str

    county: str

    addressIsDifferentFromEmployee: bool

    addressLine1: str

    addressLine2: str

    state: str

    zipCode: str

    cobraExport: bool

    cobraIsActive: bool

    cobraReason: str

    cobraStatus: str

    cobraStatusDate: datetime

    dateOfBirth: datetime

    dateOfCOBRAEvent: datetime

    dateOfCOBRALetter: datetime

    employeeId: str

    gender: str

    importId: str

    isBeneficiary: bool

    isDependent: bool

    isDisabled: bool

    isEmergencyContact: bool

    isSmoker: bool

    isStudent: bool

    marriageDate: datetime

    firstName: str

    formerName: str

    lastName: str

    middleName: str

    nameSuffix: str

    occupation: str

    otherInsurance: str

    homePhoneCountry: str

    homePhoneNumber: str

    otherPhoneNumber: str

    otherPhoneType: str

    preferredPhoneNumber: str

    relationshipCode: str

    relationshipDescription: str

    ssn: str

    contactId: str

    userDefinedField01: str

    workPhoneExtension: str

    workPhoneNumber: str

    cobraNotes: str

    notes: str

    isActive: bool

    statusAsOfDate: datetime

    deathDate: datetime

    divorceDate: datetime

    emailAddress: str

    otherPhoneCountryCode: str

    healthCareId: str

    nationalId: str

    nationalIdExpirationDate: datetime

    personID: str

    addressID: str

    workPhoneId: str

    homePhoneId: str

    otherPhoneId: str

class Contact(RequiredContact, OptionalContact):
    pass
