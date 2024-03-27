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


class RequiredCreatorPreferredLocale(TypedDict):
    pass

class OptionalCreatorPreferredLocale(TypedDict, total=False):
    # The id of the recruiter’s preferred language.
    id: str

    # The preferred language code:  en-US  en-GB  fr-CA  es-ES  pt-BR  de-DE  zh-CN 
    code: str

class CreatorPreferredLocale(RequiredCreatorPreferredLocale, OptionalCreatorPreferredLocale):
    pass
