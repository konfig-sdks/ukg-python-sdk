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


class PostingsItemLicenseCriteriaItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            is_required = schemas.BoolSchema
        
            @staticmethod
            def license() -> typing.Type['PostingsItemLicenseCriteriaItemLicense']:
                return PostingsItemLicenseCriteriaItemLicense
            __annotations__ = {
                "is_required": is_required,
                "license": license,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_required"]) -> MetaOapg.properties.is_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license"]) -> 'PostingsItemLicenseCriteriaItemLicense': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_required", "license", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_required"]) -> typing.Union[MetaOapg.properties.is_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license"]) -> typing.Union['PostingsItemLicenseCriteriaItemLicense', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_required", "license", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_required: typing.Union[MetaOapg.properties.is_required, bool, schemas.Unset] = schemas.unset,
        license: typing.Union['PostingsItemLicenseCriteriaItemLicense', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostingsItemLicenseCriteriaItem':
        return super().__new__(
            cls,
            *args,
            is_required=is_required,
            license=license,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.postings_item_license_criteria_item_license import PostingsItemLicenseCriteriaItemLicense
