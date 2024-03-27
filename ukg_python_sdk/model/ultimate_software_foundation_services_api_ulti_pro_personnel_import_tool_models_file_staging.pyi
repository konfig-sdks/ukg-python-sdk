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


class UltimateSoftwareFoundationServicesApiUltiProPersonnelImportToolModelsFileStaging(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            stagingId = schemas.UUIDSchema
            dateTimeCreated = schemas.DateTimeSchema
            fileName = schemas.StrSchema
            __annotations__ = {
                "stagingId": stagingId,
                "dateTimeCreated": dateTimeCreated,
                "fileName": fileName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stagingId"]) -> MetaOapg.properties.stagingId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTimeCreated"]) -> MetaOapg.properties.dateTimeCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stagingId", "dateTimeCreated", "fileName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stagingId"]) -> typing.Union[MetaOapg.properties.stagingId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTimeCreated"]) -> typing.Union[MetaOapg.properties.dateTimeCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stagingId", "dateTimeCreated", "fileName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        stagingId: typing.Union[MetaOapg.properties.stagingId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        dateTimeCreated: typing.Union[MetaOapg.properties.dateTimeCreated, str, datetime, schemas.Unset] = schemas.unset,
        fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UltimateSoftwareFoundationServicesApiUltiProPersonnelImportToolModelsFileStaging':
        return super().__new__(
            cls,
            *args,
            stagingId=stagingId,
            dateTimeCreated=dateTimeCreated,
            fileName=fileName,
            _configuration=_configuration,
            **kwargs,
        )
