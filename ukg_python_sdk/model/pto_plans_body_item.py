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


class PtoPlansBodyItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "companyId",
            "employeeId",
            "ptoPlan",
        }
        
        class properties:
            employeeId = schemas.StrSchema
            companyId = schemas.StrSchema
            ptoPlan = schemas.StrSchema
            earned = schemas.Float64Schema
            taken = schemas.Float64Schema
            pendingBalance = schemas.Float64Schema
            earnedThroughDate = schemas.StrSchema
            reset = schemas.StrSchema
            pendingMoveDate = schemas.StrSchema
            __annotations__ = {
                "employeeId": employeeId,
                "companyId": companyId,
                "ptoPlan": ptoPlan,
                "earned": earned,
                "taken": taken,
                "pendingBalance": pendingBalance,
                "earnedThroughDate": earnedThroughDate,
                "reset": reset,
                "pendingMoveDate": pendingMoveDate,
            }
    
    companyId: MetaOapg.properties.companyId
    employeeId: MetaOapg.properties.employeeId
    ptoPlan: MetaOapg.properties.ptoPlan
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ptoPlan"]) -> MetaOapg.properties.ptoPlan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earned"]) -> MetaOapg.properties.earned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taken"]) -> MetaOapg.properties.taken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pendingBalance"]) -> MetaOapg.properties.pendingBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earnedThroughDate"]) -> MetaOapg.properties.earnedThroughDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reset"]) -> MetaOapg.properties.reset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pendingMoveDate"]) -> MetaOapg.properties.pendingMoveDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "companyId", "ptoPlan", "earned", "taken", "pendingBalance", "earnedThroughDate", "reset", "pendingMoveDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ptoPlan"]) -> MetaOapg.properties.ptoPlan: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earned"]) -> typing.Union[MetaOapg.properties.earned, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taken"]) -> typing.Union[MetaOapg.properties.taken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pendingBalance"]) -> typing.Union[MetaOapg.properties.pendingBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earnedThroughDate"]) -> typing.Union[MetaOapg.properties.earnedThroughDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reset"]) -> typing.Union[MetaOapg.properties.reset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pendingMoveDate"]) -> typing.Union[MetaOapg.properties.pendingMoveDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "companyId", "ptoPlan", "earned", "taken", "pendingBalance", "earnedThroughDate", "reset", "pendingMoveDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        companyId: typing.Union[MetaOapg.properties.companyId, str, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, ],
        ptoPlan: typing.Union[MetaOapg.properties.ptoPlan, str, ],
        earned: typing.Union[MetaOapg.properties.earned, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        taken: typing.Union[MetaOapg.properties.taken, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pendingBalance: typing.Union[MetaOapg.properties.pendingBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        earnedThroughDate: typing.Union[MetaOapg.properties.earnedThroughDate, str, schemas.Unset] = schemas.unset,
        reset: typing.Union[MetaOapg.properties.reset, str, schemas.Unset] = schemas.unset,
        pendingMoveDate: typing.Union[MetaOapg.properties.pendingMoveDate, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PtoPlansBodyItem':
        return super().__new__(
            cls,
            *args,
            companyId=companyId,
            employeeId=employeeId,
            ptoPlan=ptoPlan,
            earned=earned,
            taken=taken,
            pendingBalance=pendingBalance,
            earnedThroughDate=earnedThroughDate,
            reset=reset,
            pendingMoveDate=pendingMoveDate,
            _configuration=_configuration,
            **kwargs,
        )
