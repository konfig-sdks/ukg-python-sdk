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


class WorkSummaryDto(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            empId = schemas.Int64Schema
            workDate = schemas.DateTimeSchema
            wrkMins = schemas.Int64Schema
            authorized = schemas.BoolSchema
            overtime = schemas.BoolSchema
            absent = schemas.BoolSchema
            absentTimeCode = schemas.StrSchema
            authorizedMessage = schemas.StrSchema
            comments = schemas.StrSchema
        
            @staticmethod
            def clocks() -> typing.Type['WorkSummaryClocksDto']:
                return WorkSummaryClocksDto
            
            
            class workDetails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WorkDetailDto']:
                        return WorkDetailDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['WorkDetailDto'], typing.List['WorkDetailDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'workDetails':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WorkDetailDto':
                    return super().__getitem__(i)
        
            @staticmethod
            def exceptions() -> typing.Type['WorkSummaryDtoExceptions']:
                return WorkSummaryDtoExceptions
            wrksMessages = schemas.StrSchema
            readOnly = schemas.BoolSchema
            readOnlyReason = schemas.StrSchema
            daily = schemas.BoolSchema
            flag1 = schemas.StrSchema
            flag2 = schemas.StrSchema
            flag3 = schemas.StrSchema
            flag4 = schemas.StrSchema
            flag5 = schemas.StrSchema
            udf1 = schemas.StrSchema
            udf2 = schemas.StrSchema
            udf3 = schemas.StrSchema
            udf4 = schemas.StrSchema
            udf5 = schemas.StrSchema
            udf6 = schemas.StrSchema
            udf7 = schemas.StrSchema
            udf8 = schemas.StrSchema
            udf9 = schemas.StrSchema
            udf10 = schemas.StrSchema
        
            @staticmethod
            def payGroup() -> typing.Type['PayGroupDto']:
                return PayGroupDto
        
            @staticmethod
            def calcGroup() -> typing.Type['CalcGroupDto']:
                return CalcGroupDto
            __annotations__ = {
                "id": id,
                "empId": empId,
                "workDate": workDate,
                "wrkMins": wrkMins,
                "authorized": authorized,
                "overtime": overtime,
                "absent": absent,
                "absentTimeCode": absentTimeCode,
                "authorizedMessage": authorizedMessage,
                "comments": comments,
                "clocks": clocks,
                "workDetails": workDetails,
                "exceptions": exceptions,
                "wrksMessages": wrksMessages,
                "readOnly": readOnly,
                "readOnlyReason": readOnlyReason,
                "daily": daily,
                "flag1": flag1,
                "flag2": flag2,
                "flag3": flag3,
                "flag4": flag4,
                "flag5": flag5,
                "udf1": udf1,
                "udf2": udf2,
                "udf3": udf3,
                "udf4": udf4,
                "udf5": udf5,
                "udf6": udf6,
                "udf7": udf7,
                "udf8": udf8,
                "udf9": udf9,
                "udf10": udf10,
                "payGroup": payGroup,
                "calcGroup": calcGroup,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["empId"]) -> MetaOapg.properties.empId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workDate"]) -> MetaOapg.properties.workDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wrkMins"]) -> MetaOapg.properties.wrkMins: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorized"]) -> MetaOapg.properties.authorized: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overtime"]) -> MetaOapg.properties.overtime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["absent"]) -> MetaOapg.properties.absent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["absentTimeCode"]) -> MetaOapg.properties.absentTimeCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorizedMessage"]) -> MetaOapg.properties.authorizedMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clocks"]) -> 'WorkSummaryClocksDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workDetails"]) -> MetaOapg.properties.workDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exceptions"]) -> 'WorkSummaryDtoExceptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wrksMessages"]) -> MetaOapg.properties.wrksMessages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnly"]) -> MetaOapg.properties.readOnly: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnlyReason"]) -> MetaOapg.properties.readOnlyReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daily"]) -> MetaOapg.properties.daily: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flag1"]) -> MetaOapg.properties.flag1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flag2"]) -> MetaOapg.properties.flag2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flag3"]) -> MetaOapg.properties.flag3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flag4"]) -> MetaOapg.properties.flag4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flag5"]) -> MetaOapg.properties.flag5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf1"]) -> MetaOapg.properties.udf1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf2"]) -> MetaOapg.properties.udf2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf3"]) -> MetaOapg.properties.udf3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf4"]) -> MetaOapg.properties.udf4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf5"]) -> MetaOapg.properties.udf5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf6"]) -> MetaOapg.properties.udf6: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf7"]) -> MetaOapg.properties.udf7: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf8"]) -> MetaOapg.properties.udf8: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf9"]) -> MetaOapg.properties.udf9: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["udf10"]) -> MetaOapg.properties.udf10: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payGroup"]) -> 'PayGroupDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calcGroup"]) -> 'CalcGroupDto': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "empId", "workDate", "wrkMins", "authorized", "overtime", "absent", "absentTimeCode", "authorizedMessage", "comments", "clocks", "workDetails", "exceptions", "wrksMessages", "readOnly", "readOnlyReason", "daily", "flag1", "flag2", "flag3", "flag4", "flag5", "udf1", "udf2", "udf3", "udf4", "udf5", "udf6", "udf7", "udf8", "udf9", "udf10", "payGroup", "calcGroup", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["empId"]) -> typing.Union[MetaOapg.properties.empId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workDate"]) -> typing.Union[MetaOapg.properties.workDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wrkMins"]) -> typing.Union[MetaOapg.properties.wrkMins, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorized"]) -> typing.Union[MetaOapg.properties.authorized, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overtime"]) -> typing.Union[MetaOapg.properties.overtime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["absent"]) -> typing.Union[MetaOapg.properties.absent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["absentTimeCode"]) -> typing.Union[MetaOapg.properties.absentTimeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorizedMessage"]) -> typing.Union[MetaOapg.properties.authorizedMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clocks"]) -> typing.Union['WorkSummaryClocksDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workDetails"]) -> typing.Union[MetaOapg.properties.workDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exceptions"]) -> typing.Union['WorkSummaryDtoExceptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wrksMessages"]) -> typing.Union[MetaOapg.properties.wrksMessages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnly"]) -> typing.Union[MetaOapg.properties.readOnly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnlyReason"]) -> typing.Union[MetaOapg.properties.readOnlyReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daily"]) -> typing.Union[MetaOapg.properties.daily, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flag1"]) -> typing.Union[MetaOapg.properties.flag1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flag2"]) -> typing.Union[MetaOapg.properties.flag2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flag3"]) -> typing.Union[MetaOapg.properties.flag3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flag4"]) -> typing.Union[MetaOapg.properties.flag4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flag5"]) -> typing.Union[MetaOapg.properties.flag5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf1"]) -> typing.Union[MetaOapg.properties.udf1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf2"]) -> typing.Union[MetaOapg.properties.udf2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf3"]) -> typing.Union[MetaOapg.properties.udf3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf4"]) -> typing.Union[MetaOapg.properties.udf4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf5"]) -> typing.Union[MetaOapg.properties.udf5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf6"]) -> typing.Union[MetaOapg.properties.udf6, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf7"]) -> typing.Union[MetaOapg.properties.udf7, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf8"]) -> typing.Union[MetaOapg.properties.udf8, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf9"]) -> typing.Union[MetaOapg.properties.udf9, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["udf10"]) -> typing.Union[MetaOapg.properties.udf10, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payGroup"]) -> typing.Union['PayGroupDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calcGroup"]) -> typing.Union['CalcGroupDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "empId", "workDate", "wrkMins", "authorized", "overtime", "absent", "absentTimeCode", "authorizedMessage", "comments", "clocks", "workDetails", "exceptions", "wrksMessages", "readOnly", "readOnlyReason", "daily", "flag1", "flag2", "flag3", "flag4", "flag5", "udf1", "udf2", "udf3", "udf4", "udf5", "udf6", "udf7", "udf8", "udf9", "udf10", "payGroup", "calcGroup", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        empId: typing.Union[MetaOapg.properties.empId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        workDate: typing.Union[MetaOapg.properties.workDate, str, datetime, schemas.Unset] = schemas.unset,
        wrkMins: typing.Union[MetaOapg.properties.wrkMins, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        authorized: typing.Union[MetaOapg.properties.authorized, bool, schemas.Unset] = schemas.unset,
        overtime: typing.Union[MetaOapg.properties.overtime, bool, schemas.Unset] = schemas.unset,
        absent: typing.Union[MetaOapg.properties.absent, bool, schemas.Unset] = schemas.unset,
        absentTimeCode: typing.Union[MetaOapg.properties.absentTimeCode, str, schemas.Unset] = schemas.unset,
        authorizedMessage: typing.Union[MetaOapg.properties.authorizedMessage, str, schemas.Unset] = schemas.unset,
        comments: typing.Union[MetaOapg.properties.comments, str, schemas.Unset] = schemas.unset,
        clocks: typing.Union['WorkSummaryClocksDto', schemas.Unset] = schemas.unset,
        workDetails: typing.Union[MetaOapg.properties.workDetails, list, tuple, schemas.Unset] = schemas.unset,
        exceptions: typing.Union['WorkSummaryDtoExceptions', schemas.Unset] = schemas.unset,
        wrksMessages: typing.Union[MetaOapg.properties.wrksMessages, str, schemas.Unset] = schemas.unset,
        readOnly: typing.Union[MetaOapg.properties.readOnly, bool, schemas.Unset] = schemas.unset,
        readOnlyReason: typing.Union[MetaOapg.properties.readOnlyReason, str, schemas.Unset] = schemas.unset,
        daily: typing.Union[MetaOapg.properties.daily, bool, schemas.Unset] = schemas.unset,
        flag1: typing.Union[MetaOapg.properties.flag1, str, schemas.Unset] = schemas.unset,
        flag2: typing.Union[MetaOapg.properties.flag2, str, schemas.Unset] = schemas.unset,
        flag3: typing.Union[MetaOapg.properties.flag3, str, schemas.Unset] = schemas.unset,
        flag4: typing.Union[MetaOapg.properties.flag4, str, schemas.Unset] = schemas.unset,
        flag5: typing.Union[MetaOapg.properties.flag5, str, schemas.Unset] = schemas.unset,
        udf1: typing.Union[MetaOapg.properties.udf1, str, schemas.Unset] = schemas.unset,
        udf2: typing.Union[MetaOapg.properties.udf2, str, schemas.Unset] = schemas.unset,
        udf3: typing.Union[MetaOapg.properties.udf3, str, schemas.Unset] = schemas.unset,
        udf4: typing.Union[MetaOapg.properties.udf4, str, schemas.Unset] = schemas.unset,
        udf5: typing.Union[MetaOapg.properties.udf5, str, schemas.Unset] = schemas.unset,
        udf6: typing.Union[MetaOapg.properties.udf6, str, schemas.Unset] = schemas.unset,
        udf7: typing.Union[MetaOapg.properties.udf7, str, schemas.Unset] = schemas.unset,
        udf8: typing.Union[MetaOapg.properties.udf8, str, schemas.Unset] = schemas.unset,
        udf9: typing.Union[MetaOapg.properties.udf9, str, schemas.Unset] = schemas.unset,
        udf10: typing.Union[MetaOapg.properties.udf10, str, schemas.Unset] = schemas.unset,
        payGroup: typing.Union['PayGroupDto', schemas.Unset] = schemas.unset,
        calcGroup: typing.Union['CalcGroupDto', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkSummaryDto':
        return super().__new__(
            cls,
            *args,
            id=id,
            empId=empId,
            workDate=workDate,
            wrkMins=wrkMins,
            authorized=authorized,
            overtime=overtime,
            absent=absent,
            absentTimeCode=absentTimeCode,
            authorizedMessage=authorizedMessage,
            comments=comments,
            clocks=clocks,
            workDetails=workDetails,
            exceptions=exceptions,
            wrksMessages=wrksMessages,
            readOnly=readOnly,
            readOnlyReason=readOnlyReason,
            daily=daily,
            flag1=flag1,
            flag2=flag2,
            flag3=flag3,
            flag4=flag4,
            flag5=flag5,
            udf1=udf1,
            udf2=udf2,
            udf3=udf3,
            udf4=udf4,
            udf5=udf5,
            udf6=udf6,
            udf7=udf7,
            udf8=udf8,
            udf9=udf9,
            udf10=udf10,
            payGroup=payGroup,
            calcGroup=calcGroup,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.calc_group_dto import CalcGroupDto
from ukg_python_sdk.model.pay_group_dto import PayGroupDto
from ukg_python_sdk.model.work_detail_dto import WorkDetailDto
from ukg_python_sdk.model.work_summary_clocks_dto import WorkSummaryClocksDto
from ukg_python_sdk.model.work_summary_dto_exceptions import WorkSummaryDtoExceptions
