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


class NewHireReadModelMentorName(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Name of the mentor
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def prefix() -> typing.Type['NewHireReadModelMentorNamePrefix']:
                return NewHireReadModelMentorNamePrefix
            first = schemas.StrSchema
            middle = schemas.StrSchema
            last = schemas.StrSchema
            formerLast = schemas.StrSchema
        
            @staticmethod
            def suffix() -> typing.Type['NewHireReadModelMentorNameSuffix']:
                return NewHireReadModelMentorNameSuffix
            preferredFirst = schemas.StrSchema
            __annotations__ = {
                "prefix": prefix,
                "first": first,
                "middle": middle,
                "last": last,
                "formerLast": formerLast,
                "suffix": suffix,
                "preferredFirst": preferredFirst,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefix"]) -> 'NewHireReadModelMentorNamePrefix': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middle"]) -> MetaOapg.properties.middle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["formerLast"]) -> MetaOapg.properties.formerLast: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> 'NewHireReadModelMentorNameSuffix': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferredFirst"]) -> MetaOapg.properties.preferredFirst: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["prefix", "first", "middle", "last", "formerLast", "suffix", "preferredFirst", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefix"]) -> typing.Union['NewHireReadModelMentorNamePrefix', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> typing.Union[MetaOapg.properties.first, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middle"]) -> typing.Union[MetaOapg.properties.middle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> typing.Union[MetaOapg.properties.last, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["formerLast"]) -> typing.Union[MetaOapg.properties.formerLast, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suffix"]) -> typing.Union['NewHireReadModelMentorNameSuffix', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferredFirst"]) -> typing.Union[MetaOapg.properties.preferredFirst, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["prefix", "first", "middle", "last", "formerLast", "suffix", "preferredFirst", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        prefix: typing.Union['NewHireReadModelMentorNamePrefix', schemas.Unset] = schemas.unset,
        first: typing.Union[MetaOapg.properties.first, str, schemas.Unset] = schemas.unset,
        middle: typing.Union[MetaOapg.properties.middle, str, schemas.Unset] = schemas.unset,
        last: typing.Union[MetaOapg.properties.last, str, schemas.Unset] = schemas.unset,
        formerLast: typing.Union[MetaOapg.properties.formerLast, str, schemas.Unset] = schemas.unset,
        suffix: typing.Union['NewHireReadModelMentorNameSuffix', schemas.Unset] = schemas.unset,
        preferredFirst: typing.Union[MetaOapg.properties.preferredFirst, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHireReadModelMentorName':
        return super().__new__(
            cls,
            *args,
            prefix=prefix,
            first=first,
            middle=middle,
            last=last,
            formerLast=formerLast,
            suffix=suffix,
            preferredFirst=preferredFirst,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.new_hire_read_model_mentor_name_prefix import NewHireReadModelMentorNamePrefix
from ukg_python_sdk.model.new_hire_read_model_mentor_name_suffix import NewHireReadModelMentorNameSuffix
