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


class Positions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            alternateTitle = schemas.StrSchema
            companyId = schemas.StrSchema
            dateTimeChanged = schemas.DateTimeSchema
            dateTimeCreated = schemas.DateTimeSchema
            employeeType = schemas.StrSchema
            effectiveStartDate = schemas.DateTimeSchema
            effectiveStopDate = schemas.DateTimeSchema
            fundID = schemas.StrSchema
            glSegment = schemas.StrSchema
            isApproved = schemas.BoolSchema
            isEligibleForBenefits = schemas.BoolSchema
            isProrated = schemas.BoolSchema
            jobcode = schemas.StrSchema
            locationCode = schemas.StrSchema
            notes = schemas.StrSchema
            organizationLevelCode1 = schemas.StrSchema
            organizationLevelCode2 = schemas.StrSchema
            organizationLevelCode3 = schemas.StrSchema
            organizationLevelCode4 = schemas.StrSchema
            overstaffingAllowed = schemas.BoolSchema
            payGroupCode = schemas.StrSchema
            positionCode = schemas.StrSchema
            projectCode = schemas.StrSchema
            shiftGroupCode = schemas.StrSchema
            statusCode = schemas.StrSchema
            statusAsOfDate = schemas.DateTimeSchema
            userDefinedField01 = schemas.StrSchema
            userDefinedField02 = schemas.DateTimeSchema
            userDefinedField03 = schemas.NumberSchema
        
            @staticmethod
            def userDefinedField04() -> typing.Type['PositionsUserDefinedField04']:
                return PositionsUserDefinedField04
            integrationRecordId = schemas.StrSchema
            __annotations__ = {
                "alternateTitle": alternateTitle,
                "companyId": companyId,
                "dateTimeChanged": dateTimeChanged,
                "dateTimeCreated": dateTimeCreated,
                "employeeType": employeeType,
                "effectiveStartDate": effectiveStartDate,
                "effectiveStopDate": effectiveStopDate,
                "fundID": fundID,
                "glSegment": glSegment,
                "isApproved": isApproved,
                "isEligibleForBenefits": isEligibleForBenefits,
                "isProrated": isProrated,
                "jobcode": jobcode,
                "locationCode": locationCode,
                "notes": notes,
                "organizationLevelCode1": organizationLevelCode1,
                "organizationLevelCode2": organizationLevelCode2,
                "organizationLevelCode3": organizationLevelCode3,
                "organizationLevelCode4": organizationLevelCode4,
                "overstaffingAllowed": overstaffingAllowed,
                "payGroupCode": payGroupCode,
                "positionCode": positionCode,
                "projectCode": projectCode,
                "shiftGroupCode": shiftGroupCode,
                "statusCode": statusCode,
                "statusAsOfDate": statusAsOfDate,
                "userDefinedField01": userDefinedField01,
                "userDefinedField02": userDefinedField02,
                "userDefinedField03": userDefinedField03,
                "userDefinedField04": userDefinedField04,
                "integrationRecordId": integrationRecordId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alternateTitle"]) -> MetaOapg.properties.alternateTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTimeChanged"]) -> MetaOapg.properties.dateTimeChanged: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTimeCreated"]) -> MetaOapg.properties.dateTimeCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeType"]) -> MetaOapg.properties.employeeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveStartDate"]) -> MetaOapg.properties.effectiveStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveStopDate"]) -> MetaOapg.properties.effectiveStopDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fundID"]) -> MetaOapg.properties.fundID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["glSegment"]) -> MetaOapg.properties.glSegment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isApproved"]) -> MetaOapg.properties.isApproved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEligibleForBenefits"]) -> MetaOapg.properties.isEligibleForBenefits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isProrated"]) -> MetaOapg.properties.isProrated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobcode"]) -> MetaOapg.properties.jobcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationCode"]) -> MetaOapg.properties.locationCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevelCode1"]) -> MetaOapg.properties.organizationLevelCode1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevelCode2"]) -> MetaOapg.properties.organizationLevelCode2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevelCode3"]) -> MetaOapg.properties.organizationLevelCode3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevelCode4"]) -> MetaOapg.properties.organizationLevelCode4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overstaffingAllowed"]) -> MetaOapg.properties.overstaffingAllowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payGroupCode"]) -> MetaOapg.properties.payGroupCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionCode"]) -> MetaOapg.properties.positionCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectCode"]) -> MetaOapg.properties.projectCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftGroupCode"]) -> MetaOapg.properties.shiftGroupCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusCode"]) -> MetaOapg.properties.statusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusAsOfDate"]) -> MetaOapg.properties.statusAsOfDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userDefinedField01"]) -> MetaOapg.properties.userDefinedField01: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userDefinedField02"]) -> MetaOapg.properties.userDefinedField02: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userDefinedField03"]) -> MetaOapg.properties.userDefinedField03: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userDefinedField04"]) -> 'PositionsUserDefinedField04': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integrationRecordId"]) -> MetaOapg.properties.integrationRecordId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["alternateTitle", "companyId", "dateTimeChanged", "dateTimeCreated", "employeeType", "effectiveStartDate", "effectiveStopDate", "fundID", "glSegment", "isApproved", "isEligibleForBenefits", "isProrated", "jobcode", "locationCode", "notes", "organizationLevelCode1", "organizationLevelCode2", "organizationLevelCode3", "organizationLevelCode4", "overstaffingAllowed", "payGroupCode", "positionCode", "projectCode", "shiftGroupCode", "statusCode", "statusAsOfDate", "userDefinedField01", "userDefinedField02", "userDefinedField03", "userDefinedField04", "integrationRecordId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alternateTitle"]) -> typing.Union[MetaOapg.properties.alternateTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTimeChanged"]) -> typing.Union[MetaOapg.properties.dateTimeChanged, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTimeCreated"]) -> typing.Union[MetaOapg.properties.dateTimeCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeType"]) -> typing.Union[MetaOapg.properties.employeeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveStartDate"]) -> typing.Union[MetaOapg.properties.effectiveStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveStopDate"]) -> typing.Union[MetaOapg.properties.effectiveStopDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fundID"]) -> typing.Union[MetaOapg.properties.fundID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["glSegment"]) -> typing.Union[MetaOapg.properties.glSegment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isApproved"]) -> typing.Union[MetaOapg.properties.isApproved, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEligibleForBenefits"]) -> typing.Union[MetaOapg.properties.isEligibleForBenefits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isProrated"]) -> typing.Union[MetaOapg.properties.isProrated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobcode"]) -> typing.Union[MetaOapg.properties.jobcode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationCode"]) -> typing.Union[MetaOapg.properties.locationCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevelCode1"]) -> typing.Union[MetaOapg.properties.organizationLevelCode1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevelCode2"]) -> typing.Union[MetaOapg.properties.organizationLevelCode2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevelCode3"]) -> typing.Union[MetaOapg.properties.organizationLevelCode3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevelCode4"]) -> typing.Union[MetaOapg.properties.organizationLevelCode4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overstaffingAllowed"]) -> typing.Union[MetaOapg.properties.overstaffingAllowed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payGroupCode"]) -> typing.Union[MetaOapg.properties.payGroupCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionCode"]) -> typing.Union[MetaOapg.properties.positionCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectCode"]) -> typing.Union[MetaOapg.properties.projectCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftGroupCode"]) -> typing.Union[MetaOapg.properties.shiftGroupCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusCode"]) -> typing.Union[MetaOapg.properties.statusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusAsOfDate"]) -> typing.Union[MetaOapg.properties.statusAsOfDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userDefinedField01"]) -> typing.Union[MetaOapg.properties.userDefinedField01, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userDefinedField02"]) -> typing.Union[MetaOapg.properties.userDefinedField02, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userDefinedField03"]) -> typing.Union[MetaOapg.properties.userDefinedField03, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userDefinedField04"]) -> typing.Union['PositionsUserDefinedField04', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["integrationRecordId"]) -> typing.Union[MetaOapg.properties.integrationRecordId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["alternateTitle", "companyId", "dateTimeChanged", "dateTimeCreated", "employeeType", "effectiveStartDate", "effectiveStopDate", "fundID", "glSegment", "isApproved", "isEligibleForBenefits", "isProrated", "jobcode", "locationCode", "notes", "organizationLevelCode1", "organizationLevelCode2", "organizationLevelCode3", "organizationLevelCode4", "overstaffingAllowed", "payGroupCode", "positionCode", "projectCode", "shiftGroupCode", "statusCode", "statusAsOfDate", "userDefinedField01", "userDefinedField02", "userDefinedField03", "userDefinedField04", "integrationRecordId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        alternateTitle: typing.Union[MetaOapg.properties.alternateTitle, str, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, schemas.Unset] = schemas.unset,
        dateTimeChanged: typing.Union[MetaOapg.properties.dateTimeChanged, str, datetime, schemas.Unset] = schemas.unset,
        dateTimeCreated: typing.Union[MetaOapg.properties.dateTimeCreated, str, datetime, schemas.Unset] = schemas.unset,
        employeeType: typing.Union[MetaOapg.properties.employeeType, str, schemas.Unset] = schemas.unset,
        effectiveStartDate: typing.Union[MetaOapg.properties.effectiveStartDate, str, datetime, schemas.Unset] = schemas.unset,
        effectiveStopDate: typing.Union[MetaOapg.properties.effectiveStopDate, str, datetime, schemas.Unset] = schemas.unset,
        fundID: typing.Union[MetaOapg.properties.fundID, str, schemas.Unset] = schemas.unset,
        glSegment: typing.Union[MetaOapg.properties.glSegment, str, schemas.Unset] = schemas.unset,
        isApproved: typing.Union[MetaOapg.properties.isApproved, bool, schemas.Unset] = schemas.unset,
        isEligibleForBenefits: typing.Union[MetaOapg.properties.isEligibleForBenefits, bool, schemas.Unset] = schemas.unset,
        isProrated: typing.Union[MetaOapg.properties.isProrated, bool, schemas.Unset] = schemas.unset,
        jobcode: typing.Union[MetaOapg.properties.jobcode, str, schemas.Unset] = schemas.unset,
        locationCode: typing.Union[MetaOapg.properties.locationCode, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        organizationLevelCode1: typing.Union[MetaOapg.properties.organizationLevelCode1, str, schemas.Unset] = schemas.unset,
        organizationLevelCode2: typing.Union[MetaOapg.properties.organizationLevelCode2, str, schemas.Unset] = schemas.unset,
        organizationLevelCode3: typing.Union[MetaOapg.properties.organizationLevelCode3, str, schemas.Unset] = schemas.unset,
        organizationLevelCode4: typing.Union[MetaOapg.properties.organizationLevelCode4, str, schemas.Unset] = schemas.unset,
        overstaffingAllowed: typing.Union[MetaOapg.properties.overstaffingAllowed, bool, schemas.Unset] = schemas.unset,
        payGroupCode: typing.Union[MetaOapg.properties.payGroupCode, str, schemas.Unset] = schemas.unset,
        positionCode: typing.Union[MetaOapg.properties.positionCode, str, schemas.Unset] = schemas.unset,
        projectCode: typing.Union[MetaOapg.properties.projectCode, str, schemas.Unset] = schemas.unset,
        shiftGroupCode: typing.Union[MetaOapg.properties.shiftGroupCode, str, schemas.Unset] = schemas.unset,
        statusCode: typing.Union[MetaOapg.properties.statusCode, str, schemas.Unset] = schemas.unset,
        statusAsOfDate: typing.Union[MetaOapg.properties.statusAsOfDate, str, datetime, schemas.Unset] = schemas.unset,
        userDefinedField01: typing.Union[MetaOapg.properties.userDefinedField01, str, schemas.Unset] = schemas.unset,
        userDefinedField02: typing.Union[MetaOapg.properties.userDefinedField02, str, datetime, schemas.Unset] = schemas.unset,
        userDefinedField03: typing.Union[MetaOapg.properties.userDefinedField03, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        userDefinedField04: typing.Union['PositionsUserDefinedField04', schemas.Unset] = schemas.unset,
        integrationRecordId: typing.Union[MetaOapg.properties.integrationRecordId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Positions':
        return super().__new__(
            cls,
            *args,
            alternateTitle=alternateTitle,
            companyId=companyId,
            dateTimeChanged=dateTimeChanged,
            dateTimeCreated=dateTimeCreated,
            employeeType=employeeType,
            effectiveStartDate=effectiveStartDate,
            effectiveStopDate=effectiveStopDate,
            fundID=fundID,
            glSegment=glSegment,
            isApproved=isApproved,
            isEligibleForBenefits=isEligibleForBenefits,
            isProrated=isProrated,
            jobcode=jobcode,
            locationCode=locationCode,
            notes=notes,
            organizationLevelCode1=organizationLevelCode1,
            organizationLevelCode2=organizationLevelCode2,
            organizationLevelCode3=organizationLevelCode3,
            organizationLevelCode4=organizationLevelCode4,
            overstaffingAllowed=overstaffingAllowed,
            payGroupCode=payGroupCode,
            positionCode=positionCode,
            projectCode=projectCode,
            shiftGroupCode=shiftGroupCode,
            statusCode=statusCode,
            statusAsOfDate=statusAsOfDate,
            userDefinedField01=userDefinedField01,
            userDefinedField02=userDefinedField02,
            userDefinedField03=userDefinedField03,
            userDefinedField04=userDefinedField04,
            integrationRecordId=integrationRecordId,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.positions_user_defined_field04 import PositionsUserDefinedField04
