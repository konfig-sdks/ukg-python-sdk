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


class CompanyPayStatementFilter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "endDate",
            "startDate",
        }
        
        class properties:
            startDate = schemas.DateTimeSchema
            endDate = schemas.DateTimeSchema
            companyId = schemas.StrSchema
            payGroup = schemas.StrSchema
            
            
            class page(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = 1
            
            
            class per_Page(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = 1
            pagesCount = schemas.Int32Schema
            __annotations__ = {
                "startDate": startDate,
                "endDate": endDate,
                "companyId": companyId,
                "payGroup": payGroup,
                "page": page,
                "per_Page": per_Page,
                "pagesCount": pagesCount,
            }
    
    endDate: MetaOapg.properties.endDate
    startDate: MetaOapg.properties.startDate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payGroup"]) -> MetaOapg.properties.payGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_Page"]) -> MetaOapg.properties.per_Page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagesCount"]) -> MetaOapg.properties.pagesCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["startDate", "endDate", "companyId", "payGroup", "page", "per_Page", "pagesCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payGroup"]) -> typing.Union[MetaOapg.properties.payGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_Page"]) -> typing.Union[MetaOapg.properties.per_Page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagesCount"]) -> typing.Union[MetaOapg.properties.pagesCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["startDate", "endDate", "companyId", "payGroup", "page", "per_Page", "pagesCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        endDate: typing.Union[MetaOapg.properties.endDate, str, datetime, ],
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, ],
        companyId: typing.Union[MetaOapg.properties.companyId, str, schemas.Unset] = schemas.unset,
        payGroup: typing.Union[MetaOapg.properties.payGroup, str, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        per_Page: typing.Union[MetaOapg.properties.per_Page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pagesCount: typing.Union[MetaOapg.properties.pagesCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompanyPayStatementFilter':
        return super().__new__(
            cls,
            *args,
            endDate=endDate,
            startDate=startDate,
            companyId=companyId,
            payGroup=payGroup,
            page=page,
            per_Page=per_Page,
            pagesCount=pagesCount,
            _configuration=_configuration,
            **kwargs,
        )
