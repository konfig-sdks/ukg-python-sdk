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


class NewHiresCreateSingleNewHireRequestContactInformationName(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Name of the new hire
    """


    class MetaOapg:
        required = {
            "last",
            "first",
        }
        
        class properties:
            
            
            class first(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class last(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
        
            @staticmethod
            def prefix() -> typing.Type['NewHiresCreateSingleNewHireRequestContactInformationNamePrefix']:
                return NewHiresCreateSingleNewHireRequestContactInformationNamePrefix
            
            
            class middle(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
            class formerLast(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
        
            @staticmethod
            def suffix() -> typing.Type['NewHiresCreateSingleNewHireRequestContactInformationNameSuffix']:
                return NewHiresCreateSingleNewHireRequestContactInformationNameSuffix
            
            
            class preferredFirst(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            __annotations__ = {
                "first": first,
                "last": last,
                "prefix": prefix,
                "middle": middle,
                "formerLast": formerLast,
                "suffix": suffix,
                "preferredFirst": preferredFirst,
            }
    
    last: MetaOapg.properties.last
    first: MetaOapg.properties.first
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefix"]) -> 'NewHiresCreateSingleNewHireRequestContactInformationNamePrefix': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middle"]) -> MetaOapg.properties.middle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["formerLast"]) -> MetaOapg.properties.formerLast: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> 'NewHiresCreateSingleNewHireRequestContactInformationNameSuffix': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferredFirst"]) -> MetaOapg.properties.preferredFirst: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first", "last", "prefix", "middle", "formerLast", "suffix", "preferredFirst", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefix"]) -> typing.Union['NewHiresCreateSingleNewHireRequestContactInformationNamePrefix', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middle"]) -> typing.Union[MetaOapg.properties.middle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["formerLast"]) -> typing.Union[MetaOapg.properties.formerLast, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suffix"]) -> typing.Union['NewHiresCreateSingleNewHireRequestContactInformationNameSuffix', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferredFirst"]) -> typing.Union[MetaOapg.properties.preferredFirst, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first", "last", "prefix", "middle", "formerLast", "suffix", "preferredFirst", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        last: typing.Union[MetaOapg.properties.last, str, ],
        first: typing.Union[MetaOapg.properties.first, str, ],
        prefix: typing.Union['NewHiresCreateSingleNewHireRequestContactInformationNamePrefix', schemas.Unset] = schemas.unset,
        middle: typing.Union[MetaOapg.properties.middle, str, schemas.Unset] = schemas.unset,
        formerLast: typing.Union[MetaOapg.properties.formerLast, str, schemas.Unset] = schemas.unset,
        suffix: typing.Union['NewHiresCreateSingleNewHireRequestContactInformationNameSuffix', schemas.Unset] = schemas.unset,
        preferredFirst: typing.Union[MetaOapg.properties.preferredFirst, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHiresCreateSingleNewHireRequestContactInformationName':
        return super().__new__(
            cls,
            *args,
            last=last,
            first=first,
            prefix=prefix,
            middle=middle,
            formerLast=formerLast,
            suffix=suffix,
            preferredFirst=preferredFirst,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.new_hires_create_single_new_hire_request_contact_information_name_prefix import NewHiresCreateSingleNewHireRequestContactInformationNamePrefix
from ukg_python_sdk.model.new_hires_create_single_new_hire_request_contact_information_name_suffix import NewHiresCreateSingleNewHireRequestContactInformationNameSuffix
