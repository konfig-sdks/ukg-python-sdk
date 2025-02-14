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


class PublishScheduleDetailDto(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class scheduleDetails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ScheduleDetailDto']:
                        return ScheduleDetailDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ScheduleDetailDto'], typing.List['ScheduleDetailDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scheduleDetails':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ScheduleDetailDto':
                    return super().__getitem__(i)
            comment = schemas.StrSchema
            __annotations__ = {
                "scheduleDetails": scheduleDetails,
                "comment": comment,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduleDetails"]) -> MetaOapg.properties.scheduleDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["scheduleDetails", "comment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduleDetails"]) -> typing.Union[MetaOapg.properties.scheduleDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scheduleDetails", "comment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scheduleDetails: typing.Union[MetaOapg.properties.scheduleDetails, list, tuple, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PublishScheduleDetailDto':
        return super().__new__(
            cls,
            *args,
            scheduleDetails=scheduleDetails,
            comment=comment,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.schedule_detail_dto import ScheduleDetailDto
