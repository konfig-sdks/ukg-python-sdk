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


class NewHirePostModelContactInformation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contact information for the new hire
    """


    class MetaOapg:
        required = {
            "emailAddress",
        }
        
        class properties:
            
            
            class emailAddress(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 254
        
            @staticmethod
            def name() -> typing.Type['NewHirePostModelContactInformationName']:
                return NewHirePostModelContactInformationName
            
            
            class primaryPhone(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
            class secondaryPhone(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
        
            @staticmethod
            def address() -> typing.Type['NewHirePostModelContactInformationAddress']:
                return NewHirePostModelContactInformationAddress
            __annotations__ = {
                "emailAddress": emailAddress,
                "name": name,
                "primaryPhone": primaryPhone,
                "secondaryPhone": secondaryPhone,
                "address": address,
            }
    
    emailAddress: MetaOapg.properties.emailAddress
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailAddress"]) -> MetaOapg.properties.emailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'NewHirePostModelContactInformationName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryPhone"]) -> MetaOapg.properties.primaryPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondaryPhone"]) -> MetaOapg.properties.secondaryPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'NewHirePostModelContactInformationAddress': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["emailAddress", "name", "primaryPhone", "secondaryPhone", "address", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailAddress"]) -> MetaOapg.properties.emailAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['NewHirePostModelContactInformationName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryPhone"]) -> typing.Union[MetaOapg.properties.primaryPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondaryPhone"]) -> typing.Union[MetaOapg.properties.secondaryPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['NewHirePostModelContactInformationAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["emailAddress", "name", "primaryPhone", "secondaryPhone", "address", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        emailAddress: typing.Union[MetaOapg.properties.emailAddress, str, ],
        name: typing.Union['NewHirePostModelContactInformationName', schemas.Unset] = schemas.unset,
        primaryPhone: typing.Union[MetaOapg.properties.primaryPhone, str, schemas.Unset] = schemas.unset,
        secondaryPhone: typing.Union[MetaOapg.properties.secondaryPhone, str, schemas.Unset] = schemas.unset,
        address: typing.Union['NewHirePostModelContactInformationAddress', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHirePostModelContactInformation':
        return super().__new__(
            cls,
            *args,
            emailAddress=emailAddress,
            name=name,
            primaryPhone=primaryPhone,
            secondaryPhone=secondaryPhone,
            address=address,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.new_hire_post_model_contact_information_address import NewHirePostModelContactInformationAddress
from ukg_python_sdk.model.new_hire_post_model_contact_information_name import NewHirePostModelContactInformationName
