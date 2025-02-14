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


class RequiredOpportunityDescriptionBrief(TypedDict):
    pass

class OptionalOpportunityDescriptionBrief(TypedDict, total=False):
    externel: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    internal: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OpportunityDescriptionBrief(RequiredOpportunityDescriptionBrief, OptionalOpportunityDescriptionBrief):
    pass
