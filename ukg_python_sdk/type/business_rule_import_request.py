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


class RequiredBusinessRuleImportRequest(TypedDict):
    pass

class OptionalBusinessRuleImportRequest(TypedDict, total=False):
    # The XML Serialized transaction
    transaction: str

    # An optionally provided unique file name
    uniqueFileName: str

class BusinessRuleImportRequest(RequiredBusinessRuleImportRequest, OptionalBusinessRuleImportRequest):
    pass
