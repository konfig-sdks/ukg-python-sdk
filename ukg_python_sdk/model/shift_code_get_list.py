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


class ShiftCodeGetList(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            shiftCode = schemas.StrSchema
            shiftCodeDescription = schemas.StrSchema
            __annotations__ = {
                "shiftCode": shiftCode,
                "shiftCodeDescription": shiftCodeDescription,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftCode"]) -> MetaOapg.properties.shiftCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftCodeDescription"]) -> MetaOapg.properties.shiftCodeDescription: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["shiftCode", "shiftCodeDescription", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftCode"]) -> typing.Union[MetaOapg.properties.shiftCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftCodeDescription"]) -> typing.Union[MetaOapg.properties.shiftCodeDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["shiftCode", "shiftCodeDescription", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        shiftCode: typing.Union[MetaOapg.properties.shiftCode, str, schemas.Unset] = schemas.unset,
        shiftCodeDescription: typing.Union[MetaOapg.properties.shiftCodeDescription, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShiftCodeGetList':
        return super().__new__(
            cls,
            *args,
            shiftCode=shiftCode,
            shiftCodeDescription=shiftCodeDescription,
            _configuration=_configuration,
            **kwargs,
        )
