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


class EmployeePayStatementRangeFilter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def employeeIdentifier() -> typing.Type['EmployeeIdentifier']:
                return EmployeeIdentifier
            startDate = schemas.DateTimeSchema
            endDate = schemas.DateTimeSchema
            
            
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
                "employeeIdentifier": employeeIdentifier,
                "startDate": startDate,
                "endDate": endDate,
                "page": page,
                "per_Page": per_Page,
                "pagesCount": pagesCount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeIdentifier"]) -> 'EmployeeIdentifier': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_Page"]) -> MetaOapg.properties.per_Page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagesCount"]) -> MetaOapg.properties.pagesCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeIdentifier", "startDate", "endDate", "page", "per_Page", "pagesCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeIdentifier"]) -> typing.Union['EmployeeIdentifier', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_Page"]) -> typing.Union[MetaOapg.properties.per_Page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagesCount"]) -> typing.Union[MetaOapg.properties.pagesCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeIdentifier", "startDate", "endDate", "page", "per_Page", "pagesCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employeeIdentifier: typing.Union['EmployeeIdentifier', schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, datetime, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        per_Page: typing.Union[MetaOapg.properties.per_Page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pagesCount: typing.Union[MetaOapg.properties.pagesCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeePayStatementRangeFilter':
        return super().__new__(
            cls,
            *args,
            employeeIdentifier=employeeIdentifier,
            startDate=startDate,
            endDate=endDate,
            page=page,
            per_Page=per_Page,
            pagesCount=pagesCount,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.employee_identifier import EmployeeIdentifier
