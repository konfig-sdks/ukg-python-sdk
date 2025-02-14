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


class NewHiresCreateSingleNewHireResponseCompensation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Compensation of the new hire
    """


    class MetaOapg:
        
        class properties:
            isFullTime = schemas.BoolSchema
            isSalaried = schemas.BoolSchema
            workHours = schemas.NumberSchema
            weeklyHours = schemas.NumberSchema
            currencyType = schemas.StrSchema
        
            @staticmethod
            def currency() -> typing.Type['NewHiresCreateSingleNewHireResponseCompensationCurrency']:
                return NewHiresCreateSingleNewHireResponseCompensationCurrency
            payRate = schemas.NumberSchema
        
            @staticmethod
            def ratePer() -> typing.Type['NewHiresCreateSingleNewHireResponseCompensationRatePer']:
                return NewHiresCreateSingleNewHireResponseCompensationRatePer
            __annotations__ = {
                "isFullTime": isFullTime,
                "isSalaried": isSalaried,
                "workHours": workHours,
                "weeklyHours": weeklyHours,
                "currencyType": currencyType,
                "currency": currency,
                "payRate": payRate,
                "ratePer": ratePer,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isFullTime"]) -> MetaOapg.properties.isFullTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSalaried"]) -> MetaOapg.properties.isSalaried: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workHours"]) -> MetaOapg.properties.workHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weeklyHours"]) -> MetaOapg.properties.weeklyHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyType"]) -> MetaOapg.properties.currencyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'NewHiresCreateSingleNewHireResponseCompensationCurrency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payRate"]) -> MetaOapg.properties.payRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratePer"]) -> 'NewHiresCreateSingleNewHireResponseCompensationRatePer': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isFullTime", "isSalaried", "workHours", "weeklyHours", "currencyType", "currency", "payRate", "ratePer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isFullTime"]) -> typing.Union[MetaOapg.properties.isFullTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSalaried"]) -> typing.Union[MetaOapg.properties.isSalaried, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workHours"]) -> typing.Union[MetaOapg.properties.workHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weeklyHours"]) -> typing.Union[MetaOapg.properties.weeklyHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyType"]) -> typing.Union[MetaOapg.properties.currencyType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union['NewHiresCreateSingleNewHireResponseCompensationCurrency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payRate"]) -> typing.Union[MetaOapg.properties.payRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratePer"]) -> typing.Union['NewHiresCreateSingleNewHireResponseCompensationRatePer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isFullTime", "isSalaried", "workHours", "weeklyHours", "currencyType", "currency", "payRate", "ratePer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isFullTime: typing.Union[MetaOapg.properties.isFullTime, bool, schemas.Unset] = schemas.unset,
        isSalaried: typing.Union[MetaOapg.properties.isSalaried, bool, schemas.Unset] = schemas.unset,
        workHours: typing.Union[MetaOapg.properties.workHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        weeklyHours: typing.Union[MetaOapg.properties.weeklyHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currencyType: typing.Union[MetaOapg.properties.currencyType, str, schemas.Unset] = schemas.unset,
        currency: typing.Union['NewHiresCreateSingleNewHireResponseCompensationCurrency', schemas.Unset] = schemas.unset,
        payRate: typing.Union[MetaOapg.properties.payRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ratePer: typing.Union['NewHiresCreateSingleNewHireResponseCompensationRatePer', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHiresCreateSingleNewHireResponseCompensation':
        return super().__new__(
            cls,
            *args,
            isFullTime=isFullTime,
            isSalaried=isSalaried,
            workHours=workHours,
            weeklyHours=weeklyHours,
            currencyType=currencyType,
            currency=currency,
            payRate=payRate,
            ratePer=ratePer,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.new_hires_create_single_new_hire_response_compensation_currency import NewHiresCreateSingleNewHireResponseCompensationCurrency
from ukg_python_sdk.model.new_hires_create_single_new_hire_response_compensation_rate_per import NewHiresCreateSingleNewHireResponseCompensationRatePer
