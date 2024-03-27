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


class NewHiresGetById200ResponseProvisioning(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Provisioning for the new hire
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def provisioningItems() -> typing.Type['NewHiresGetById200ResponseProvisioningProvisioningItems']:
                return NewHiresGetById200ResponseProvisioningProvisioningItems
        
            @staticmethod
            def summaryEmailRecipients() -> typing.Type['NewHiresGetById200ResponseProvisioningSummaryEmailRecipients']:
                return NewHiresGetById200ResponseProvisioningSummaryEmailRecipients
            __annotations__ = {
                "provisioningItems": provisioningItems,
                "summaryEmailRecipients": summaryEmailRecipients,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provisioningItems"]) -> 'NewHiresGetById200ResponseProvisioningProvisioningItems': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summaryEmailRecipients"]) -> 'NewHiresGetById200ResponseProvisioningSummaryEmailRecipients': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["provisioningItems", "summaryEmailRecipients", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provisioningItems"]) -> typing.Union['NewHiresGetById200ResponseProvisioningProvisioningItems', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summaryEmailRecipients"]) -> typing.Union['NewHiresGetById200ResponseProvisioningSummaryEmailRecipients', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["provisioningItems", "summaryEmailRecipients", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        provisioningItems: typing.Union['NewHiresGetById200ResponseProvisioningProvisioningItems', schemas.Unset] = schemas.unset,
        summaryEmailRecipients: typing.Union['NewHiresGetById200ResponseProvisioningSummaryEmailRecipients', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHiresGetById200ResponseProvisioning':
        return super().__new__(
            cls,
            *args,
            provisioningItems=provisioningItems,
            summaryEmailRecipients=summaryEmailRecipients,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.new_hires_get_by_id200_response_provisioning_provisioning_items import NewHiresGetById200ResponseProvisioningProvisioningItems
from ukg_python_sdk.model.new_hires_get_by_id200_response_provisioning_summary_email_recipients import NewHiresGetById200ResponseProvisioningSummaryEmailRecipients
