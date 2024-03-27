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


class NewHiresGetById200ResponseContactInformation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contact information of the new hire
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def name() -> typing.Type['NewHiresGetById200ResponseContactInformationName']:
                return NewHiresGetById200ResponseContactInformationName
            emailAddress = schemas.StrSchema
            primaryPhone = schemas.StrSchema
            secondaryPhone = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['NewHiresGetById200ResponseContactInformationAddress']:
                return NewHiresGetById200ResponseContactInformationAddress
            __annotations__ = {
                "name": name,
                "emailAddress": emailAddress,
                "primaryPhone": primaryPhone,
                "secondaryPhone": secondaryPhone,
                "address": address,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'NewHiresGetById200ResponseContactInformationName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailAddress"]) -> MetaOapg.properties.emailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryPhone"]) -> MetaOapg.properties.primaryPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondaryPhone"]) -> MetaOapg.properties.secondaryPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'NewHiresGetById200ResponseContactInformationAddress': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "emailAddress", "primaryPhone", "secondaryPhone", "address", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['NewHiresGetById200ResponseContactInformationName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailAddress"]) -> typing.Union[MetaOapg.properties.emailAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryPhone"]) -> typing.Union[MetaOapg.properties.primaryPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondaryPhone"]) -> typing.Union[MetaOapg.properties.secondaryPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['NewHiresGetById200ResponseContactInformationAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "emailAddress", "primaryPhone", "secondaryPhone", "address", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union['NewHiresGetById200ResponseContactInformationName', schemas.Unset] = schemas.unset,
        emailAddress: typing.Union[MetaOapg.properties.emailAddress, str, schemas.Unset] = schemas.unset,
        primaryPhone: typing.Union[MetaOapg.properties.primaryPhone, str, schemas.Unset] = schemas.unset,
        secondaryPhone: typing.Union[MetaOapg.properties.secondaryPhone, str, schemas.Unset] = schemas.unset,
        address: typing.Union['NewHiresGetById200ResponseContactInformationAddress', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHiresGetById200ResponseContactInformation':
        return super().__new__(
            cls,
            *args,
            name=name,
            emailAddress=emailAddress,
            primaryPhone=primaryPhone,
            secondaryPhone=secondaryPhone,
            address=address,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.new_hires_get_by_id200_response_contact_information_address import NewHiresGetById200ResponseContactInformationAddress
from ukg_python_sdk.model.new_hires_get_by_id200_response_contact_information_name import NewHiresGetById200ResponseContactInformationName
