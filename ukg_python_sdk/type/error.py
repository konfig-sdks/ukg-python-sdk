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

from ukg_python_sdk.type.error_errors import ErrorErrors
from ukg_python_sdk.type.error_modelstate import ErrorModelstate

class RequiredError(TypedDict):
    pass

class OptionalError(TypedDict, total=False):
    title: str

    type: str

    errorCount: typing.Union[int, float]

    errors: ErrorErrors

    detail: str

    code: int

    message: str

    modelstate: ErrorModelstate

class Error(RequiredError, OptionalError):
    pass
