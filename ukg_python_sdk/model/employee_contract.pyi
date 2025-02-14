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


class EmployeeContract(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            companyId = schemas.StrSchema
            employeeId = schemas.StrSchema
            contractNumber = schemas.StrSchema
            contractTypeCode = schemas.StrSchema
            effectiveDate = schemas.StrSchema
            dateTimeCreated = schemas.StrSchema
            rowLastChanged = schemas.StrSchema
            
            
            class page(
                schemas.Int32Schema
            ):
                pass
            
            
            class per_Page(
                schemas.Int32Schema
            ):
                pass
            pagesCount = schemas.Int32Schema
            __annotations__ = {
                "companyId": companyId,
                "employeeId": employeeId,
                "contractNumber": contractNumber,
                "contractTypeCode": contractTypeCode,
                "effectiveDate": effectiveDate,
                "dateTimeCreated": dateTimeCreated,
                "rowLastChanged": rowLastChanged,
                "page": page,
                "per_Page": per_Page,
                "pagesCount": pagesCount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractNumber"]) -> MetaOapg.properties.contractNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractTypeCode"]) -> MetaOapg.properties.contractTypeCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveDate"]) -> MetaOapg.properties.effectiveDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTimeCreated"]) -> MetaOapg.properties.dateTimeCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rowLastChanged"]) -> MetaOapg.properties.rowLastChanged: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_Page"]) -> MetaOapg.properties.per_Page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagesCount"]) -> MetaOapg.properties.pagesCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["companyId", "employeeId", "contractNumber", "contractTypeCode", "effectiveDate", "dateTimeCreated", "rowLastChanged", "page", "per_Page", "pagesCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractNumber"]) -> typing.Union[MetaOapg.properties.contractNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractTypeCode"]) -> typing.Union[MetaOapg.properties.contractTypeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveDate"]) -> typing.Union[MetaOapg.properties.effectiveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTimeCreated"]) -> typing.Union[MetaOapg.properties.dateTimeCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rowLastChanged"]) -> typing.Union[MetaOapg.properties.rowLastChanged, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_Page"]) -> typing.Union[MetaOapg.properties.per_Page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagesCount"]) -> typing.Union[MetaOapg.properties.pagesCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["companyId", "employeeId", "contractNumber", "contractTypeCode", "effectiveDate", "dateTimeCreated", "rowLastChanged", "page", "per_Page", "pagesCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        companyId: typing.Union[MetaOapg.properties.companyId, str, schemas.Unset] = schemas.unset,
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, schemas.Unset] = schemas.unset,
        contractNumber: typing.Union[MetaOapg.properties.contractNumber, str, schemas.Unset] = schemas.unset,
        contractTypeCode: typing.Union[MetaOapg.properties.contractTypeCode, str, schemas.Unset] = schemas.unset,
        effectiveDate: typing.Union[MetaOapg.properties.effectiveDate, str, schemas.Unset] = schemas.unset,
        dateTimeCreated: typing.Union[MetaOapg.properties.dateTimeCreated, str, schemas.Unset] = schemas.unset,
        rowLastChanged: typing.Union[MetaOapg.properties.rowLastChanged, str, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        per_Page: typing.Union[MetaOapg.properties.per_Page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pagesCount: typing.Union[MetaOapg.properties.pagesCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeContract':
        return super().__new__(
            cls,
            *args,
            companyId=companyId,
            employeeId=employeeId,
            contractNumber=contractNumber,
            contractTypeCode=contractTypeCode,
            effectiveDate=effectiveDate,
            dateTimeCreated=dateTimeCreated,
            rowLastChanged=rowLastChanged,
            page=page,
            per_Page=per_Page,
            pagesCount=pagesCount,
            _configuration=_configuration,
            **kwargs,
        )
