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


class TaxGroupsDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            taxCalcGroupIdCode = schemas.StrSchema
            taxCalcGroupDescription = schemas.StrSchema
            depositFrequencyCode = schemas.StrSchema
            depositFrequencyDescription = schemas.StrSchema
            taxCalcGroupTypeCode = schemas.StrSchema
            taxCalcGroupTypeDescription = schemas.StrSchema
            taxCalcGroupReportId = schemas.StrSchema
            taxGroupCountryCode = schemas.StrSchema
            dateFinalWagesPaid = schemas.DateTimeSchema
            dateMonthReset = schemas.DateTimeSchema
            dateQuarterReset = schemas.DateTimeSchema
            dateYearReset = schemas.DateTimeSchema
            taxGroupIsNotSubjectToSocMedTax = schemas.BoolSchema
            taxGroupIsNotPayingWages = schemas.BoolSchema
            taxGroupIsInactive = schemas.BoolSchema
            __annotations__ = {
                "taxCalcGroupIdCode": taxCalcGroupIdCode,
                "taxCalcGroupDescription": taxCalcGroupDescription,
                "depositFrequencyCode": depositFrequencyCode,
                "depositFrequencyDescription": depositFrequencyDescription,
                "taxCalcGroupTypeCode": taxCalcGroupTypeCode,
                "taxCalcGroupTypeDescription": taxCalcGroupTypeDescription,
                "taxCalcGroupReportId": taxCalcGroupReportId,
                "taxGroupCountryCode": taxGroupCountryCode,
                "dateFinalWagesPaid": dateFinalWagesPaid,
                "dateMonthReset": dateMonthReset,
                "dateQuarterReset": dateQuarterReset,
                "dateYearReset": dateYearReset,
                "taxGroupIsNotSubjectToSocMedTax": taxGroupIsNotSubjectToSocMedTax,
                "taxGroupIsNotPayingWages": taxGroupIsNotPayingWages,
                "taxGroupIsInactive": taxGroupIsInactive,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCalcGroupIdCode"]) -> MetaOapg.properties.taxCalcGroupIdCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCalcGroupDescription"]) -> MetaOapg.properties.taxCalcGroupDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depositFrequencyCode"]) -> MetaOapg.properties.depositFrequencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depositFrequencyDescription"]) -> MetaOapg.properties.depositFrequencyDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCalcGroupTypeCode"]) -> MetaOapg.properties.taxCalcGroupTypeCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCalcGroupTypeDescription"]) -> MetaOapg.properties.taxCalcGroupTypeDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCalcGroupReportId"]) -> MetaOapg.properties.taxCalcGroupReportId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxGroupCountryCode"]) -> MetaOapg.properties.taxGroupCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateFinalWagesPaid"]) -> MetaOapg.properties.dateFinalWagesPaid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateMonthReset"]) -> MetaOapg.properties.dateMonthReset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateQuarterReset"]) -> MetaOapg.properties.dateQuarterReset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateYearReset"]) -> MetaOapg.properties.dateYearReset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxGroupIsNotSubjectToSocMedTax"]) -> MetaOapg.properties.taxGroupIsNotSubjectToSocMedTax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxGroupIsNotPayingWages"]) -> MetaOapg.properties.taxGroupIsNotPayingWages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxGroupIsInactive"]) -> MetaOapg.properties.taxGroupIsInactive: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["taxCalcGroupIdCode", "taxCalcGroupDescription", "depositFrequencyCode", "depositFrequencyDescription", "taxCalcGroupTypeCode", "taxCalcGroupTypeDescription", "taxCalcGroupReportId", "taxGroupCountryCode", "dateFinalWagesPaid", "dateMonthReset", "dateQuarterReset", "dateYearReset", "taxGroupIsNotSubjectToSocMedTax", "taxGroupIsNotPayingWages", "taxGroupIsInactive", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCalcGroupIdCode"]) -> typing.Union[MetaOapg.properties.taxCalcGroupIdCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCalcGroupDescription"]) -> typing.Union[MetaOapg.properties.taxCalcGroupDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depositFrequencyCode"]) -> typing.Union[MetaOapg.properties.depositFrequencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depositFrequencyDescription"]) -> typing.Union[MetaOapg.properties.depositFrequencyDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCalcGroupTypeCode"]) -> typing.Union[MetaOapg.properties.taxCalcGroupTypeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCalcGroupTypeDescription"]) -> typing.Union[MetaOapg.properties.taxCalcGroupTypeDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCalcGroupReportId"]) -> typing.Union[MetaOapg.properties.taxCalcGroupReportId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxGroupCountryCode"]) -> typing.Union[MetaOapg.properties.taxGroupCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateFinalWagesPaid"]) -> typing.Union[MetaOapg.properties.dateFinalWagesPaid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateMonthReset"]) -> typing.Union[MetaOapg.properties.dateMonthReset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateQuarterReset"]) -> typing.Union[MetaOapg.properties.dateQuarterReset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateYearReset"]) -> typing.Union[MetaOapg.properties.dateYearReset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxGroupIsNotSubjectToSocMedTax"]) -> typing.Union[MetaOapg.properties.taxGroupIsNotSubjectToSocMedTax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxGroupIsNotPayingWages"]) -> typing.Union[MetaOapg.properties.taxGroupIsNotPayingWages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxGroupIsInactive"]) -> typing.Union[MetaOapg.properties.taxGroupIsInactive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["taxCalcGroupIdCode", "taxCalcGroupDescription", "depositFrequencyCode", "depositFrequencyDescription", "taxCalcGroupTypeCode", "taxCalcGroupTypeDescription", "taxCalcGroupReportId", "taxGroupCountryCode", "dateFinalWagesPaid", "dateMonthReset", "dateQuarterReset", "dateYearReset", "taxGroupIsNotSubjectToSocMedTax", "taxGroupIsNotPayingWages", "taxGroupIsInactive", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        taxCalcGroupIdCode: typing.Union[MetaOapg.properties.taxCalcGroupIdCode, str, schemas.Unset] = schemas.unset,
        taxCalcGroupDescription: typing.Union[MetaOapg.properties.taxCalcGroupDescription, str, schemas.Unset] = schemas.unset,
        depositFrequencyCode: typing.Union[MetaOapg.properties.depositFrequencyCode, str, schemas.Unset] = schemas.unset,
        depositFrequencyDescription: typing.Union[MetaOapg.properties.depositFrequencyDescription, str, schemas.Unset] = schemas.unset,
        taxCalcGroupTypeCode: typing.Union[MetaOapg.properties.taxCalcGroupTypeCode, str, schemas.Unset] = schemas.unset,
        taxCalcGroupTypeDescription: typing.Union[MetaOapg.properties.taxCalcGroupTypeDescription, str, schemas.Unset] = schemas.unset,
        taxCalcGroupReportId: typing.Union[MetaOapg.properties.taxCalcGroupReportId, str, schemas.Unset] = schemas.unset,
        taxGroupCountryCode: typing.Union[MetaOapg.properties.taxGroupCountryCode, str, schemas.Unset] = schemas.unset,
        dateFinalWagesPaid: typing.Union[MetaOapg.properties.dateFinalWagesPaid, str, datetime, schemas.Unset] = schemas.unset,
        dateMonthReset: typing.Union[MetaOapg.properties.dateMonthReset, str, datetime, schemas.Unset] = schemas.unset,
        dateQuarterReset: typing.Union[MetaOapg.properties.dateQuarterReset, str, datetime, schemas.Unset] = schemas.unset,
        dateYearReset: typing.Union[MetaOapg.properties.dateYearReset, str, datetime, schemas.Unset] = schemas.unset,
        taxGroupIsNotSubjectToSocMedTax: typing.Union[MetaOapg.properties.taxGroupIsNotSubjectToSocMedTax, bool, schemas.Unset] = schemas.unset,
        taxGroupIsNotPayingWages: typing.Union[MetaOapg.properties.taxGroupIsNotPayingWages, bool, schemas.Unset] = schemas.unset,
        taxGroupIsInactive: typing.Union[MetaOapg.properties.taxGroupIsInactive, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaxGroupsDetails':
        return super().__new__(
            cls,
            *args,
            taxCalcGroupIdCode=taxCalcGroupIdCode,
            taxCalcGroupDescription=taxCalcGroupDescription,
            depositFrequencyCode=depositFrequencyCode,
            depositFrequencyDescription=depositFrequencyDescription,
            taxCalcGroupTypeCode=taxCalcGroupTypeCode,
            taxCalcGroupTypeDescription=taxCalcGroupTypeDescription,
            taxCalcGroupReportId=taxCalcGroupReportId,
            taxGroupCountryCode=taxGroupCountryCode,
            dateFinalWagesPaid=dateFinalWagesPaid,
            dateMonthReset=dateMonthReset,
            dateQuarterReset=dateQuarterReset,
            dateYearReset=dateYearReset,
            taxGroupIsNotSubjectToSocMedTax=taxGroupIsNotSubjectToSocMedTax,
            taxGroupIsNotPayingWages=taxGroupIsNotPayingWages,
            taxGroupIsInactive=taxGroupIsInactive,
            _configuration=_configuration,
            **kwargs,
        )
