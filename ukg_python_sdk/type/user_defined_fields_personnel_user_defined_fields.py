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

from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field01 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField01
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field02 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField02
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field03 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField03
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field04 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField04
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field05 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField05
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field06 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField06
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field07 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField07
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field08 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField08
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field09 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField09
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field10 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField10
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field11 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField11
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field12 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField12
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field13 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField13
from ukg_python_sdk.type.user_defined_fields_personnel_user_defined_fields_personnel_ud_field14 import UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField14

class RequiredUserDefinedFieldsPersonnelUserDefinedFields(TypedDict):
    pass

class OptionalUserDefinedFieldsPersonnelUserDefinedFields(TypedDict, total=False):
    personnelUDField01: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField01

    personnelUDField02: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField02

    personnelUDField03: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField03

    personnelUDField04: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField04

    personnelUDField05: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField05

    personnelUDField06: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField06

    personnelUDField07: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField07

    personnelUDField08: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField08

    personnelUDField09: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField09

    personnelUDField10: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField10

    personnelUDField11: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField11

    personnelUDField12: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField12

    personnelUDField13: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField13

    personnelUDField14: UserDefinedFieldsPersonnelUserDefinedFieldsPersonnelUdField14

class UserDefinedFieldsPersonnelUserDefinedFields(RequiredUserDefinedFieldsPersonnelUserDefinedFields, OptionalUserDefinedFieldsPersonnelUserDefinedFields):
    pass
