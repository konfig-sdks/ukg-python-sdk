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

from ukg_python_sdk.type.background_checks_application import BackgroundChecksApplication
from ukg_python_sdk.type.background_checks_author import BackgroundChecksAuthor
from ukg_python_sdk.type.background_checks_packages import BackgroundChecksPackages
from ukg_python_sdk.type.links import Links

class RequiredBackgroundChecks(TypedDict):
    author: BackgroundChecksAuthor

    application: BackgroundChecksApplication

    # The status of the background check order.
    status: str

    # Thebackground check order number. Maximum of 100 characters.
    order_number: str

    packages: BackgroundChecksPackages

class OptionalBackgroundChecks(TypedDict, total=False):
    links: typing.List[Links]

class BackgroundChecks(RequiredBackgroundChecks, OptionalBackgroundChecks):
    pass
