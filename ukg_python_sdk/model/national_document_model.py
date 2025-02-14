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


class NationalDocumentModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            employeeId = schemas.StrSchema
            nationalDocumentId = schemas.StrSchema
            contactId = schemas.StrSchema
            nationalDocumentNumber = schemas.StrSchema
            nationalDocumentDescription = schemas.StrSchema
            nationalDocumentTypeCode = schemas.StrSchema
            nationalDocumentIssuingCountryCode = schemas.StrSchema
            nationalDocumentIssuingPlace = schemas.StrSchema
            nationalDocumentIssueDate = schemas.DateTimeSchema
            employeeNumber = schemas.StrSchema
            __annotations__ = {
                "employeeId": employeeId,
                "nationalDocumentId": nationalDocumentId,
                "contactId": contactId,
                "nationalDocumentNumber": nationalDocumentNumber,
                "nationalDocumentDescription": nationalDocumentDescription,
                "nationalDocumentTypeCode": nationalDocumentTypeCode,
                "nationalDocumentIssuingCountryCode": nationalDocumentIssuingCountryCode,
                "nationalDocumentIssuingPlace": nationalDocumentIssuingPlace,
                "nationalDocumentIssueDate": nationalDocumentIssueDate,
                "employeeNumber": employeeNumber,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationalDocumentId"]) -> MetaOapg.properties.nationalDocumentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactId"]) -> MetaOapg.properties.contactId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationalDocumentNumber"]) -> MetaOapg.properties.nationalDocumentNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationalDocumentDescription"]) -> MetaOapg.properties.nationalDocumentDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationalDocumentTypeCode"]) -> MetaOapg.properties.nationalDocumentTypeCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationalDocumentIssuingCountryCode"]) -> MetaOapg.properties.nationalDocumentIssuingCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationalDocumentIssuingPlace"]) -> MetaOapg.properties.nationalDocumentIssuingPlace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationalDocumentIssueDate"]) -> MetaOapg.properties.nationalDocumentIssueDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "nationalDocumentId", "contactId", "nationalDocumentNumber", "nationalDocumentDescription", "nationalDocumentTypeCode", "nationalDocumentIssuingCountryCode", "nationalDocumentIssuingPlace", "nationalDocumentIssueDate", "employeeNumber", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationalDocumentId"]) -> typing.Union[MetaOapg.properties.nationalDocumentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactId"]) -> typing.Union[MetaOapg.properties.contactId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationalDocumentNumber"]) -> typing.Union[MetaOapg.properties.nationalDocumentNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationalDocumentDescription"]) -> typing.Union[MetaOapg.properties.nationalDocumentDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationalDocumentTypeCode"]) -> typing.Union[MetaOapg.properties.nationalDocumentTypeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationalDocumentIssuingCountryCode"]) -> typing.Union[MetaOapg.properties.nationalDocumentIssuingCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationalDocumentIssuingPlace"]) -> typing.Union[MetaOapg.properties.nationalDocumentIssuingPlace, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationalDocumentIssueDate"]) -> typing.Union[MetaOapg.properties.nationalDocumentIssueDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> typing.Union[MetaOapg.properties.employeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "nationalDocumentId", "contactId", "nationalDocumentNumber", "nationalDocumentDescription", "nationalDocumentTypeCode", "nationalDocumentIssuingCountryCode", "nationalDocumentIssuingPlace", "nationalDocumentIssueDate", "employeeNumber", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, schemas.Unset] = schemas.unset,
        nationalDocumentId: typing.Union[MetaOapg.properties.nationalDocumentId, str, schemas.Unset] = schemas.unset,
        contactId: typing.Union[MetaOapg.properties.contactId, str, schemas.Unset] = schemas.unset,
        nationalDocumentNumber: typing.Union[MetaOapg.properties.nationalDocumentNumber, str, schemas.Unset] = schemas.unset,
        nationalDocumentDescription: typing.Union[MetaOapg.properties.nationalDocumentDescription, str, schemas.Unset] = schemas.unset,
        nationalDocumentTypeCode: typing.Union[MetaOapg.properties.nationalDocumentTypeCode, str, schemas.Unset] = schemas.unset,
        nationalDocumentIssuingCountryCode: typing.Union[MetaOapg.properties.nationalDocumentIssuingCountryCode, str, schemas.Unset] = schemas.unset,
        nationalDocumentIssuingPlace: typing.Union[MetaOapg.properties.nationalDocumentIssuingPlace, str, schemas.Unset] = schemas.unset,
        nationalDocumentIssueDate: typing.Union[MetaOapg.properties.nationalDocumentIssueDate, str, datetime, schemas.Unset] = schemas.unset,
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NationalDocumentModel':
        return super().__new__(
            cls,
            *args,
            employeeId=employeeId,
            nationalDocumentId=nationalDocumentId,
            contactId=contactId,
            nationalDocumentNumber=nationalDocumentNumber,
            nationalDocumentDescription=nationalDocumentDescription,
            nationalDocumentTypeCode=nationalDocumentTypeCode,
            nationalDocumentIssuingCountryCode=nationalDocumentIssuingCountryCode,
            nationalDocumentIssuingPlace=nationalDocumentIssuingPlace,
            nationalDocumentIssueDate=nationalDocumentIssueDate,
            employeeNumber=employeeNumber,
            _configuration=_configuration,
            **kwargs,
        )
