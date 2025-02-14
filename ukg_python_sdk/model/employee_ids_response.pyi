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


class EmployeeIdsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            type = schemas.StrSchema
            detail = schemas.StrSchema
            errorCount = schemas.NumberSchema
        
            @staticmethod
            def multistatus() -> typing.Type['EmployeeIdsResponseMultistatus']:
                return EmployeeIdsResponseMultistatus
            __annotations__ = {
                "title": title,
                "type": type,
                "detail": detail,
                "errorCount": errorCount,
                "multistatus": multistatus,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorCount"]) -> MetaOapg.properties.errorCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multistatus"]) -> 'EmployeeIdsResponseMultistatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "type", "detail", "errorCount", "multistatus", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> typing.Union[MetaOapg.properties.detail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorCount"]) -> typing.Union[MetaOapg.properties.errorCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multistatus"]) -> typing.Union['EmployeeIdsResponseMultistatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "type", "detail", "errorCount", "multistatus", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        detail: typing.Union[MetaOapg.properties.detail, str, schemas.Unset] = schemas.unset,
        errorCount: typing.Union[MetaOapg.properties.errorCount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        multistatus: typing.Union['EmployeeIdsResponseMultistatus', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeIdsResponse':
        return super().__new__(
            cls,
            *args,
            title=title,
            type=type,
            detail=detail,
            errorCount=errorCount,
            multistatus=multistatus,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.employee_ids_response_multistatus import EmployeeIdsResponseMultistatus
