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


class RequiredUserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField10(TypedDict):
    pass

class OptionalUserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField10(TypedDict, total=False):
    field: str

    value: typing.Union[int, float]

class UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField10(RequiredUserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField10, OptionalUserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField10):
    pass
