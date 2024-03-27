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


class EmployeeMultipleJobs(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            annualPayRate = schemas.NumberSchema
            companyId = schemas.StrSchema
            dateInJob = schemas.DateTimeSchema
            employeeId = schemas.StrSchema
            hourlyPayRate = schemas.NumberSchema
            isPrimaryJob = schemas.BoolSchema
            jobCode = schemas.StrSchema
            jobIsInActive = schemas.BoolSchema
            otherRate1 = schemas.NumberSchema
            otherRate2 = schemas.NumberSchema
            otherRate3 = schemas.NumberSchema
            otherRate4 = schemas.NumberSchema
            piecePayRate = schemas.NumberSchema
            __annotations__ = {
                "annualPayRate": annualPayRate,
                "companyId": companyId,
                "dateInJob": dateInJob,
                "employeeId": employeeId,
                "hourlyPayRate": hourlyPayRate,
                "isPrimaryJob": isPrimaryJob,
                "jobCode": jobCode,
                "jobIsInActive": jobIsInActive,
                "otherRate1": otherRate1,
                "otherRate2": otherRate2,
                "otherRate3": otherRate3,
                "otherRate4": otherRate4,
                "piecePayRate": piecePayRate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualPayRate"]) -> MetaOapg.properties.annualPayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateInJob"]) -> MetaOapg.properties.dateInJob: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourlyPayRate"]) -> MetaOapg.properties.hourlyPayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPrimaryJob"]) -> MetaOapg.properties.isPrimaryJob: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobCode"]) -> MetaOapg.properties.jobCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobIsInActive"]) -> MetaOapg.properties.jobIsInActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRate1"]) -> MetaOapg.properties.otherRate1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRate2"]) -> MetaOapg.properties.otherRate2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRate3"]) -> MetaOapg.properties.otherRate3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRate4"]) -> MetaOapg.properties.otherRate4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["piecePayRate"]) -> MetaOapg.properties.piecePayRate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["annualPayRate", "companyId", "dateInJob", "employeeId", "hourlyPayRate", "isPrimaryJob", "jobCode", "jobIsInActive", "otherRate1", "otherRate2", "otherRate3", "otherRate4", "piecePayRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualPayRate"]) -> typing.Union[MetaOapg.properties.annualPayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateInJob"]) -> typing.Union[MetaOapg.properties.dateInJob, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourlyPayRate"]) -> typing.Union[MetaOapg.properties.hourlyPayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPrimaryJob"]) -> typing.Union[MetaOapg.properties.isPrimaryJob, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobCode"]) -> typing.Union[MetaOapg.properties.jobCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobIsInActive"]) -> typing.Union[MetaOapg.properties.jobIsInActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRate1"]) -> typing.Union[MetaOapg.properties.otherRate1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRate2"]) -> typing.Union[MetaOapg.properties.otherRate2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRate3"]) -> typing.Union[MetaOapg.properties.otherRate3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRate4"]) -> typing.Union[MetaOapg.properties.otherRate4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["piecePayRate"]) -> typing.Union[MetaOapg.properties.piecePayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["annualPayRate", "companyId", "dateInJob", "employeeId", "hourlyPayRate", "isPrimaryJob", "jobCode", "jobIsInActive", "otherRate1", "otherRate2", "otherRate3", "otherRate4", "piecePayRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        annualPayRate: typing.Union[MetaOapg.properties.annualPayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, schemas.Unset] = schemas.unset,
        dateInJob: typing.Union[MetaOapg.properties.dateInJob, str, datetime, schemas.Unset] = schemas.unset,
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, schemas.Unset] = schemas.unset,
        hourlyPayRate: typing.Union[MetaOapg.properties.hourlyPayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        isPrimaryJob: typing.Union[MetaOapg.properties.isPrimaryJob, bool, schemas.Unset] = schemas.unset,
        jobCode: typing.Union[MetaOapg.properties.jobCode, str, schemas.Unset] = schemas.unset,
        jobIsInActive: typing.Union[MetaOapg.properties.jobIsInActive, bool, schemas.Unset] = schemas.unset,
        otherRate1: typing.Union[MetaOapg.properties.otherRate1, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        otherRate2: typing.Union[MetaOapg.properties.otherRate2, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        otherRate3: typing.Union[MetaOapg.properties.otherRate3, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        otherRate4: typing.Union[MetaOapg.properties.otherRate4, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        piecePayRate: typing.Union[MetaOapg.properties.piecePayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeMultipleJobs':
        return super().__new__(
            cls,
            *args,
            annualPayRate=annualPayRate,
            companyId=companyId,
            dateInJob=dateInJob,
            employeeId=employeeId,
            hourlyPayRate=hourlyPayRate,
            isPrimaryJob=isPrimaryJob,
            jobCode=jobCode,
            jobIsInActive=jobIsInActive,
            otherRate1=otherRate1,
            otherRate2=otherRate2,
            otherRate3=otherRate3,
            otherRate4=otherRate4,
            piecePayRate=piecePayRate,
            _configuration=_configuration,
            **kwargs,
        )
