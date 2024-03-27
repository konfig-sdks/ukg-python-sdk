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


class NewHiresCreateSingleNewHireRequestContactInformationAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Address of the new hire
    """


    class MetaOapg:
        
        class properties:
            
            
            class line1(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
            class line2(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
            class city(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            
            
            class postalCode(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
            class county(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            stateCode = schemas.StrSchema
            countryCode = schemas.StrSchema
            __annotations__ = {
                "line1": line1,
                "line2": line2,
                "city": city,
                "postalCode": postalCode,
                "county": county,
                "stateCode": stateCode,
                "countryCode": countryCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line1"]) -> MetaOapg.properties.line1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line2"]) -> MetaOapg.properties.line2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCode"]) -> MetaOapg.properties.postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["county"]) -> MetaOapg.properties.county: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateCode"]) -> MetaOapg.properties.stateCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["line1", "line2", "city", "postalCode", "county", "stateCode", "countryCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line1"]) -> typing.Union[MetaOapg.properties.line1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line2"]) -> typing.Union[MetaOapg.properties.line2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCode"]) -> typing.Union[MetaOapg.properties.postalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["county"]) -> typing.Union[MetaOapg.properties.county, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateCode"]) -> typing.Union[MetaOapg.properties.stateCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryCode"]) -> typing.Union[MetaOapg.properties.countryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["line1", "line2", "city", "postalCode", "county", "stateCode", "countryCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        line1: typing.Union[MetaOapg.properties.line1, str, schemas.Unset] = schemas.unset,
        line2: typing.Union[MetaOapg.properties.line2, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        postalCode: typing.Union[MetaOapg.properties.postalCode, str, schemas.Unset] = schemas.unset,
        county: typing.Union[MetaOapg.properties.county, str, schemas.Unset] = schemas.unset,
        stateCode: typing.Union[MetaOapg.properties.stateCode, str, schemas.Unset] = schemas.unset,
        countryCode: typing.Union[MetaOapg.properties.countryCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHiresCreateSingleNewHireRequestContactInformationAddress':
        return super().__new__(
            cls,
            *args,
            line1=line1,
            line2=line2,
            city=city,
            postalCode=postalCode,
            county=county,
            stateCode=stateCode,
            countryCode=countryCode,
            _configuration=_configuration,
            **kwargs,
        )
