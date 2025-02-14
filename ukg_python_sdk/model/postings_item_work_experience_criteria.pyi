# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ukg_python_sdk import schemas  # noqa: F401


class PostingsItemWorkExperienceCriteria(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PostingsItemWorkExperienceCriteriaItem']:
            return PostingsItemWorkExperienceCriteriaItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['PostingsItemWorkExperienceCriteriaItem'], typing.List['PostingsItemWorkExperienceCriteriaItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PostingsItemWorkExperienceCriteria':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PostingsItemWorkExperienceCriteriaItem':
        return super().__getitem__(i)

from ukg_python_sdk.model.postings_item_work_experience_criteria_item import PostingsItemWorkExperienceCriteriaItem
