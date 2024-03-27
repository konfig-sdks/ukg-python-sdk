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


class NewHiresGetById200ResponseProvisioningProvisioningItems(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The list of provisioning items selected for this New Hire
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['NewHiresGetById200ResponseProvisioningProvisioningItemsItem']:
            return NewHiresGetById200ResponseProvisioningProvisioningItemsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['NewHiresGetById200ResponseProvisioningProvisioningItemsItem'], typing.List['NewHiresGetById200ResponseProvisioningProvisioningItemsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'NewHiresGetById200ResponseProvisioningProvisioningItems':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'NewHiresGetById200ResponseProvisioningProvisioningItemsItem':
        return super().__getitem__(i)

from ukg_python_sdk.model.new_hires_get_by_id200_response_provisioning_provisioning_items_item import NewHiresGetById200ResponseProvisioningProvisioningItemsItem
