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


class EmployeePayStatementEarningsModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            amount = schemas.Float32Schema
            amountytd = schemas.Float32Schema
            hours = schemas.Float32Schema
            hoursytd = schemas.Float32Schema
            paycode = schemas.StrSchema
            paydescription = schemas.StrSchema
            payrate = schemas.Float32Schema
            periodend = schemas.DateTimeSchema
            periodstart = schemas.DateTimeSchema
            piececount = schemas.Float32Schema
            piecepayrate = schemas.Float32Schema
            __annotations__ = {
                "amount": amount,
                "amountytd": amountytd,
                "hours": hours,
                "hoursytd": hoursytd,
                "paycode": paycode,
                "paydescription": paydescription,
                "payrate": payrate,
                "periodend": periodend,
                "periodstart": periodstart,
                "piececount": piececount,
                "piecepayrate": piecepayrate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amountytd"]) -> MetaOapg.properties.amountytd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hoursytd"]) -> MetaOapg.properties.hoursytd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paycode"]) -> MetaOapg.properties.paycode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paydescription"]) -> MetaOapg.properties.paydescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payrate"]) -> MetaOapg.properties.payrate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodend"]) -> MetaOapg.properties.periodend: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodstart"]) -> MetaOapg.properties.periodstart: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["piececount"]) -> MetaOapg.properties.piececount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["piecepayrate"]) -> MetaOapg.properties.piecepayrate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "amountytd", "hours", "hoursytd", "paycode", "paydescription", "payrate", "periodend", "periodstart", "piececount", "piecepayrate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amountytd"]) -> typing.Union[MetaOapg.properties.amountytd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> typing.Union[MetaOapg.properties.hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hoursytd"]) -> typing.Union[MetaOapg.properties.hoursytd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paycode"]) -> typing.Union[MetaOapg.properties.paycode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paydescription"]) -> typing.Union[MetaOapg.properties.paydescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payrate"]) -> typing.Union[MetaOapg.properties.payrate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodend"]) -> typing.Union[MetaOapg.properties.periodend, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodstart"]) -> typing.Union[MetaOapg.properties.periodstart, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["piececount"]) -> typing.Union[MetaOapg.properties.piececount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["piecepayrate"]) -> typing.Union[MetaOapg.properties.piecepayrate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "amountytd", "hours", "hoursytd", "paycode", "paydescription", "payrate", "periodend", "periodstart", "piececount", "piecepayrate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        amountytd: typing.Union[MetaOapg.properties.amountytd, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hours: typing.Union[MetaOapg.properties.hours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hoursytd: typing.Union[MetaOapg.properties.hoursytd, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        paycode: typing.Union[MetaOapg.properties.paycode, str, schemas.Unset] = schemas.unset,
        paydescription: typing.Union[MetaOapg.properties.paydescription, str, schemas.Unset] = schemas.unset,
        payrate: typing.Union[MetaOapg.properties.payrate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        periodend: typing.Union[MetaOapg.properties.periodend, str, datetime, schemas.Unset] = schemas.unset,
        periodstart: typing.Union[MetaOapg.properties.periodstart, str, datetime, schemas.Unset] = schemas.unset,
        piececount: typing.Union[MetaOapg.properties.piececount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        piecepayrate: typing.Union[MetaOapg.properties.piecepayrate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeePayStatementEarningsModel':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            amountytd=amountytd,
            hours=hours,
            hoursytd=hoursytd,
            paycode=paycode,
            paydescription=paydescription,
            payrate=payrate,
            periodend=periodend,
            periodstart=periodstart,
            piececount=piececount,
            piecepayrate=piecepayrate,
            _configuration=_configuration,
            **kwargs,
        )
