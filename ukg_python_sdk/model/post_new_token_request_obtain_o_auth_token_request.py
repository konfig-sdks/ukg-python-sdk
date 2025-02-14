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


class PostNewTokenRequestObtainOAuthTokenRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "grant_type",
            "scope",
            "client_secret",
            "client_id",
        }
        
        class properties:
            grant_type = schemas.StrSchema
            client_id = schemas.StrSchema
            client_secret = schemas.StrSchema
            scope = schemas.StrSchema
            __annotations__ = {
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
                "scope": scope,
            }
    
    grant_type: MetaOapg.properties.grant_type
    scope: MetaOapg.properties.scope
    client_secret: MetaOapg.properties.client_secret
    client_id: MetaOapg.properties.client_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["grant_type", "client_id", "client_secret", "scope", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["grant_type", "client_id", "client_secret", "scope", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        grant_type: typing.Union[MetaOapg.properties.grant_type, str, ],
        scope: typing.Union[MetaOapg.properties.scope, str, ],
        client_secret: typing.Union[MetaOapg.properties.client_secret, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostNewTokenRequestObtainOAuthTokenRequest':
        return super().__new__(
            cls,
            *args,
            grant_type=grant_type,
            scope=scope,
            client_secret=client_secret,
            client_id=client_id,
            _configuration=_configuration,
            **kwargs,
        )
