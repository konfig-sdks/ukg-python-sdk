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


class RequiredContactInfoPhone(TypedDict):
    pass

class OptionalContactInfoPhone(TypedDict, total=False):
    # The candidate’s primary phone number. Maximum of 25 characters.
    primary: str

    # The candidate’s secondary phone number. Maximum of 25 characters.
    secondary: str

class ContactInfoPhone(RequiredContactInfoPhone, OptionalContactInfoPhone):
    pass
