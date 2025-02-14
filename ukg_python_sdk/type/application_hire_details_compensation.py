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

from ukg_python_sdk.type.application_hire_details_compensation_currency import ApplicationHireDetailsCompensationCurrency

class RequiredApplicationHireDetailsCompensation(TypedDict):
    pass

class OptionalApplicationHireDetailsCompensation(TypedDict, total=False):
    # The flag indicating whether the applicant is full-time or part-time.
    is_fulltime: str

    # The hours per week of the applicant Must not be less than 0 or greater than 999999999.99 
    hours_per_week: str

    # Whether the applicant is salary or hourly
    is_salaried: str

    # The USD pay rate for the applicant If supplied, must not be less than 0, greater than 99999999999999.9999, or have a decimal with more than 4 digits 
    pay_rate: str

    currency: ApplicationHireDetailsCompensationCurrency

class ApplicationHireDetailsCompensation(RequiredApplicationHireDetailsCompensation, OptionalApplicationHireDetailsCompensation):
    pass
