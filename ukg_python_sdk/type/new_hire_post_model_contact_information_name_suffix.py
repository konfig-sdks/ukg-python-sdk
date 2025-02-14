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


class RequiredNewHirePostModelContactInformationNameSuffix(TypedDict):
    pass

class OptionalNewHirePostModelContactInformationNameSuffix(TypedDict, total=False):
    # Unique identifier of the suffix
    id: str

    # UltiPro suffix code
    code: str

class NewHirePostModelContactInformationNameSuffix(RequiredNewHirePostModelContactInformationNameSuffix, OptionalNewHirePostModelContactInformationNameSuffix):
    pass
