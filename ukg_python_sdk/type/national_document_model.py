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


class RequiredNationalDocumentModel(TypedDict):
    pass

class OptionalNationalDocumentModel(TypedDict, total=False):
    employeeId: str

    nationalDocumentId: str

    contactId: str

    nationalDocumentNumber: str

    nationalDocumentDescription: str

    nationalDocumentTypeCode: str

    nationalDocumentIssuingCountryCode: str

    nationalDocumentIssuingPlace: str

    nationalDocumentIssueDate: datetime

    employeeNumber: str

class NationalDocumentModel(RequiredNationalDocumentModel, OptionalNationalDocumentModel):
    pass
