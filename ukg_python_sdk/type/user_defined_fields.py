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

from ukg_python_sdk.type.user_defined_fields_international_user_defined_fields import UserDefinedFieldsInternationalUserDefinedFields
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields import UserDefinedFieldsPersonnelUserDefinedFields

class RequiredUserDefinedFields(TypedDict):
    pass

class OptionalUserDefinedFields(TypedDict, total=False):
    employeeId: str

    personnelUserDefinedFields: UserDefinedFieldsPersonnelUserDefinedFields

    internationalUserDefinedFields: UserDefinedFieldsInternationalUserDefinedFields

class UserDefinedFields(RequiredUserDefinedFields, OptionalUserDefinedFields):
    pass
