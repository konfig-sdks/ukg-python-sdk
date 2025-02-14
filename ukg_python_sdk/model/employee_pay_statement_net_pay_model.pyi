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


class EmployeePayStatementNetPayModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            accountnumber = schemas.StrSchema
            accounttype = schemas.StrSchema
            amount = schemas.Float32Schema
            __annotations__ = {
                "accountnumber": accountnumber,
                "accounttype": accounttype,
                "amount": amount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountnumber"]) -> MetaOapg.properties.accountnumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounttype"]) -> MetaOapg.properties.accounttype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountnumber", "accounttype", "amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountnumber"]) -> typing.Union[MetaOapg.properties.accountnumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounttype"]) -> typing.Union[MetaOapg.properties.accounttype, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountnumber", "accounttype", "amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accountnumber: typing.Union[MetaOapg.properties.accountnumber, str, schemas.Unset] = schemas.unset,
        accounttype: typing.Union[MetaOapg.properties.accounttype, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeePayStatementNetPayModel':
        return super().__new__(
            cls,
            *args,
            accountnumber=accountnumber,
            accounttype=accounttype,
            amount=amount,
            _configuration=_configuration,
            **kwargs,
        )
