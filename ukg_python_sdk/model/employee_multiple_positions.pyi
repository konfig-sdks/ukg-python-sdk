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


class EmployeeMultiplePositions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            employeeId = schemas.StrSchema
            companyId = schemas.StrSchema
            jobCode = schemas.StrSchema
            positionCode = schemas.StrSchema
            isPrimary = schemas.BoolSchema
            annualSalary = schemas.NumberSchema
            hourlyPayRate = schemas.NumberSchema
            fullTimeOrPartTimeCode = schemas.StrSchema
            fullTimeOrPartTime = schemas.StrSchema
            clockCode = schemas.StrSchema
            dateTimeCreated = schemas.DateTimeSchema
            employeeTypeCode = schemas.StrSchema
            employeeTypeDescription = schemas.StrSchema
            effectiveStartDate = schemas.DateTimeSchema
            effectiveStopDate = schemas.DateTimeSchema
            isEligibleForBenefits = schemas.BoolSchema
            locationCode = schemas.StrSchema
            notes = schemas.StrSchema
            organizationLevel1Code = schemas.StrSchema
            organizationLevel2Code = schemas.StrSchema
            organizationLevel3Code = schemas.StrSchema
            organizationLevel4Code = schemas.StrSchema
            otherRate1 = schemas.NumberSchema
            otherRate2 = schemas.NumberSchema
            otherRate3 = schemas.NumberSchema
            otherRate4 = schemas.NumberSchema
            overrideIncumbentData = schemas.StrSchema
            payGroupCode = schemas.StrSchema
            periodPayRate = schemas.NumberSchema
            piecePayRate = schemas.NumberSchema
            projectCode = schemas.StrSchema
            salaryOrHourlyCode = schemas.StrSchema
            salaryOrHourly = schemas.StrSchema
            scheduledAnnualHours = schemas.NumberSchema
            scheduledFullTimeEmployee = schemas.NumberSchema
            scheduledWorkHours = schemas.NumberSchema
            shiftCode = schemas.StrSchema
            shiftGroupCode = schemas.StrSchema
            shiftGroupDescription = schemas.StrSchema
            systemId = schemas.StrSchema
            weeklyPayRate = schemas.NumberSchema
            __annotations__ = {
                "employeeId": employeeId,
                "companyId": companyId,
                "jobCode": jobCode,
                "positionCode": positionCode,
                "isPrimary": isPrimary,
                "annualSalary": annualSalary,
                "hourlyPayRate": hourlyPayRate,
                "fullTimeOrPartTimeCode": fullTimeOrPartTimeCode,
                "fullTimeOrPartTime": fullTimeOrPartTime,
                "clockCode": clockCode,
                "dateTimeCreated": dateTimeCreated,
                "employeeTypeCode": employeeTypeCode,
                "employeeTypeDescription": employeeTypeDescription,
                "effectiveStartDate": effectiveStartDate,
                "effectiveStopDate": effectiveStopDate,
                "isEligibleForBenefits": isEligibleForBenefits,
                "locationCode": locationCode,
                "notes": notes,
                "organizationLevel1Code": organizationLevel1Code,
                "organizationLevel2Code": organizationLevel2Code,
                "organizationLevel3Code": organizationLevel3Code,
                "organizationLevel4Code": organizationLevel4Code,
                "otherRate1": otherRate1,
                "otherRate2": otherRate2,
                "otherRate3": otherRate3,
                "otherRate4": otherRate4,
                "overrideIncumbentData": overrideIncumbentData,
                "payGroupCode": payGroupCode,
                "periodPayRate": periodPayRate,
                "piecePayRate": piecePayRate,
                "projectCode": projectCode,
                "salaryOrHourlyCode": salaryOrHourlyCode,
                "salaryOrHourly": salaryOrHourly,
                "scheduledAnnualHours": scheduledAnnualHours,
                "scheduledFullTimeEmployee": scheduledFullTimeEmployee,
                "scheduledWorkHours": scheduledWorkHours,
                "shiftCode": shiftCode,
                "shiftGroupCode": shiftGroupCode,
                "shiftGroupDescription": shiftGroupDescription,
                "systemId": systemId,
                "weeklyPayRate": weeklyPayRate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobCode"]) -> MetaOapg.properties.jobCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionCode"]) -> MetaOapg.properties.positionCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPrimary"]) -> MetaOapg.properties.isPrimary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualSalary"]) -> MetaOapg.properties.annualSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourlyPayRate"]) -> MetaOapg.properties.hourlyPayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullTimeOrPartTimeCode"]) -> MetaOapg.properties.fullTimeOrPartTimeCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullTimeOrPartTime"]) -> MetaOapg.properties.fullTimeOrPartTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clockCode"]) -> MetaOapg.properties.clockCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTimeCreated"]) -> MetaOapg.properties.dateTimeCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeTypeCode"]) -> MetaOapg.properties.employeeTypeCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeTypeDescription"]) -> MetaOapg.properties.employeeTypeDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveStartDate"]) -> MetaOapg.properties.effectiveStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effectiveStopDate"]) -> MetaOapg.properties.effectiveStopDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEligibleForBenefits"]) -> MetaOapg.properties.isEligibleForBenefits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationCode"]) -> MetaOapg.properties.locationCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevel1Code"]) -> MetaOapg.properties.organizationLevel1Code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevel2Code"]) -> MetaOapg.properties.organizationLevel2Code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevel3Code"]) -> MetaOapg.properties.organizationLevel3Code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevel4Code"]) -> MetaOapg.properties.organizationLevel4Code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRate1"]) -> MetaOapg.properties.otherRate1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRate2"]) -> MetaOapg.properties.otherRate2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRate3"]) -> MetaOapg.properties.otherRate3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherRate4"]) -> MetaOapg.properties.otherRate4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overrideIncumbentData"]) -> MetaOapg.properties.overrideIncumbentData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payGroupCode"]) -> MetaOapg.properties.payGroupCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodPayRate"]) -> MetaOapg.properties.periodPayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["piecePayRate"]) -> MetaOapg.properties.piecePayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectCode"]) -> MetaOapg.properties.projectCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaryOrHourlyCode"]) -> MetaOapg.properties.salaryOrHourlyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salaryOrHourly"]) -> MetaOapg.properties.salaryOrHourly: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduledAnnualHours"]) -> MetaOapg.properties.scheduledAnnualHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduledFullTimeEmployee"]) -> MetaOapg.properties.scheduledFullTimeEmployee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduledWorkHours"]) -> MetaOapg.properties.scheduledWorkHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftCode"]) -> MetaOapg.properties.shiftCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftGroupCode"]) -> MetaOapg.properties.shiftGroupCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shiftGroupDescription"]) -> MetaOapg.properties.shiftGroupDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemId"]) -> MetaOapg.properties.systemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weeklyPayRate"]) -> MetaOapg.properties.weeklyPayRate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "companyId", "jobCode", "positionCode", "isPrimary", "annualSalary", "hourlyPayRate", "fullTimeOrPartTimeCode", "fullTimeOrPartTime", "clockCode", "dateTimeCreated", "employeeTypeCode", "employeeTypeDescription", "effectiveStartDate", "effectiveStopDate", "isEligibleForBenefits", "locationCode", "notes", "organizationLevel1Code", "organizationLevel2Code", "organizationLevel3Code", "organizationLevel4Code", "otherRate1", "otherRate2", "otherRate3", "otherRate4", "overrideIncumbentData", "payGroupCode", "periodPayRate", "piecePayRate", "projectCode", "salaryOrHourlyCode", "salaryOrHourly", "scheduledAnnualHours", "scheduledFullTimeEmployee", "scheduledWorkHours", "shiftCode", "shiftGroupCode", "shiftGroupDescription", "systemId", "weeklyPayRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobCode"]) -> typing.Union[MetaOapg.properties.jobCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionCode"]) -> typing.Union[MetaOapg.properties.positionCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPrimary"]) -> typing.Union[MetaOapg.properties.isPrimary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualSalary"]) -> typing.Union[MetaOapg.properties.annualSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourlyPayRate"]) -> typing.Union[MetaOapg.properties.hourlyPayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullTimeOrPartTimeCode"]) -> typing.Union[MetaOapg.properties.fullTimeOrPartTimeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullTimeOrPartTime"]) -> typing.Union[MetaOapg.properties.fullTimeOrPartTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clockCode"]) -> typing.Union[MetaOapg.properties.clockCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTimeCreated"]) -> typing.Union[MetaOapg.properties.dateTimeCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeTypeCode"]) -> typing.Union[MetaOapg.properties.employeeTypeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeTypeDescription"]) -> typing.Union[MetaOapg.properties.employeeTypeDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveStartDate"]) -> typing.Union[MetaOapg.properties.effectiveStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effectiveStopDate"]) -> typing.Union[MetaOapg.properties.effectiveStopDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEligibleForBenefits"]) -> typing.Union[MetaOapg.properties.isEligibleForBenefits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationCode"]) -> typing.Union[MetaOapg.properties.locationCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevel1Code"]) -> typing.Union[MetaOapg.properties.organizationLevel1Code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevel2Code"]) -> typing.Union[MetaOapg.properties.organizationLevel2Code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevel3Code"]) -> typing.Union[MetaOapg.properties.organizationLevel3Code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevel4Code"]) -> typing.Union[MetaOapg.properties.organizationLevel4Code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRate1"]) -> typing.Union[MetaOapg.properties.otherRate1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRate2"]) -> typing.Union[MetaOapg.properties.otherRate2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRate3"]) -> typing.Union[MetaOapg.properties.otherRate3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherRate4"]) -> typing.Union[MetaOapg.properties.otherRate4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overrideIncumbentData"]) -> typing.Union[MetaOapg.properties.overrideIncumbentData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payGroupCode"]) -> typing.Union[MetaOapg.properties.payGroupCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodPayRate"]) -> typing.Union[MetaOapg.properties.periodPayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["piecePayRate"]) -> typing.Union[MetaOapg.properties.piecePayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectCode"]) -> typing.Union[MetaOapg.properties.projectCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaryOrHourlyCode"]) -> typing.Union[MetaOapg.properties.salaryOrHourlyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salaryOrHourly"]) -> typing.Union[MetaOapg.properties.salaryOrHourly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduledAnnualHours"]) -> typing.Union[MetaOapg.properties.scheduledAnnualHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduledFullTimeEmployee"]) -> typing.Union[MetaOapg.properties.scheduledFullTimeEmployee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduledWorkHours"]) -> typing.Union[MetaOapg.properties.scheduledWorkHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftCode"]) -> typing.Union[MetaOapg.properties.shiftCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftGroupCode"]) -> typing.Union[MetaOapg.properties.shiftGroupCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shiftGroupDescription"]) -> typing.Union[MetaOapg.properties.shiftGroupDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemId"]) -> typing.Union[MetaOapg.properties.systemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weeklyPayRate"]) -> typing.Union[MetaOapg.properties.weeklyPayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "companyId", "jobCode", "positionCode", "isPrimary", "annualSalary", "hourlyPayRate", "fullTimeOrPartTimeCode", "fullTimeOrPartTime", "clockCode", "dateTimeCreated", "employeeTypeCode", "employeeTypeDescription", "effectiveStartDate", "effectiveStopDate", "isEligibleForBenefits", "locationCode", "notes", "organizationLevel1Code", "organizationLevel2Code", "organizationLevel3Code", "organizationLevel4Code", "otherRate1", "otherRate2", "otherRate3", "otherRate4", "overrideIncumbentData", "payGroupCode", "periodPayRate", "piecePayRate", "projectCode", "salaryOrHourlyCode", "salaryOrHourly", "scheduledAnnualHours", "scheduledFullTimeEmployee", "scheduledWorkHours", "shiftCode", "shiftGroupCode", "shiftGroupDescription", "systemId", "weeklyPayRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, schemas.Unset] = schemas.unset,
        jobCode: typing.Union[MetaOapg.properties.jobCode, str, schemas.Unset] = schemas.unset,
        positionCode: typing.Union[MetaOapg.properties.positionCode, str, schemas.Unset] = schemas.unset,
        isPrimary: typing.Union[MetaOapg.properties.isPrimary, bool, schemas.Unset] = schemas.unset,
        annualSalary: typing.Union[MetaOapg.properties.annualSalary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hourlyPayRate: typing.Union[MetaOapg.properties.hourlyPayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        fullTimeOrPartTimeCode: typing.Union[MetaOapg.properties.fullTimeOrPartTimeCode, str, schemas.Unset] = schemas.unset,
        fullTimeOrPartTime: typing.Union[MetaOapg.properties.fullTimeOrPartTime, str, schemas.Unset] = schemas.unset,
        clockCode: typing.Union[MetaOapg.properties.clockCode, str, schemas.Unset] = schemas.unset,
        dateTimeCreated: typing.Union[MetaOapg.properties.dateTimeCreated, str, datetime, schemas.Unset] = schemas.unset,
        employeeTypeCode: typing.Union[MetaOapg.properties.employeeTypeCode, str, schemas.Unset] = schemas.unset,
        employeeTypeDescription: typing.Union[MetaOapg.properties.employeeTypeDescription, str, schemas.Unset] = schemas.unset,
        effectiveStartDate: typing.Union[MetaOapg.properties.effectiveStartDate, str, datetime, schemas.Unset] = schemas.unset,
        effectiveStopDate: typing.Union[MetaOapg.properties.effectiveStopDate, str, datetime, schemas.Unset] = schemas.unset,
        isEligibleForBenefits: typing.Union[MetaOapg.properties.isEligibleForBenefits, bool, schemas.Unset] = schemas.unset,
        locationCode: typing.Union[MetaOapg.properties.locationCode, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        organizationLevel1Code: typing.Union[MetaOapg.properties.organizationLevel1Code, str, schemas.Unset] = schemas.unset,
        organizationLevel2Code: typing.Union[MetaOapg.properties.organizationLevel2Code, str, schemas.Unset] = schemas.unset,
        organizationLevel3Code: typing.Union[MetaOapg.properties.organizationLevel3Code, str, schemas.Unset] = schemas.unset,
        organizationLevel4Code: typing.Union[MetaOapg.properties.organizationLevel4Code, str, schemas.Unset] = schemas.unset,
        otherRate1: typing.Union[MetaOapg.properties.otherRate1, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        otherRate2: typing.Union[MetaOapg.properties.otherRate2, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        otherRate3: typing.Union[MetaOapg.properties.otherRate3, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        otherRate4: typing.Union[MetaOapg.properties.otherRate4, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        overrideIncumbentData: typing.Union[MetaOapg.properties.overrideIncumbentData, str, schemas.Unset] = schemas.unset,
        payGroupCode: typing.Union[MetaOapg.properties.payGroupCode, str, schemas.Unset] = schemas.unset,
        periodPayRate: typing.Union[MetaOapg.properties.periodPayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        piecePayRate: typing.Union[MetaOapg.properties.piecePayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        projectCode: typing.Union[MetaOapg.properties.projectCode, str, schemas.Unset] = schemas.unset,
        salaryOrHourlyCode: typing.Union[MetaOapg.properties.salaryOrHourlyCode, str, schemas.Unset] = schemas.unset,
        salaryOrHourly: typing.Union[MetaOapg.properties.salaryOrHourly, str, schemas.Unset] = schemas.unset,
        scheduledAnnualHours: typing.Union[MetaOapg.properties.scheduledAnnualHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        scheduledFullTimeEmployee: typing.Union[MetaOapg.properties.scheduledFullTimeEmployee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        scheduledWorkHours: typing.Union[MetaOapg.properties.scheduledWorkHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        shiftCode: typing.Union[MetaOapg.properties.shiftCode, str, schemas.Unset] = schemas.unset,
        shiftGroupCode: typing.Union[MetaOapg.properties.shiftGroupCode, str, schemas.Unset] = schemas.unset,
        shiftGroupDescription: typing.Union[MetaOapg.properties.shiftGroupDescription, str, schemas.Unset] = schemas.unset,
        systemId: typing.Union[MetaOapg.properties.systemId, str, schemas.Unset] = schemas.unset,
        weeklyPayRate: typing.Union[MetaOapg.properties.weeklyPayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeMultiplePositions':
        return super().__new__(
            cls,
            *args,
            employeeId=employeeId,
            companyId=companyId,
            jobCode=jobCode,
            positionCode=positionCode,
            isPrimary=isPrimary,
            annualSalary=annualSalary,
            hourlyPayRate=hourlyPayRate,
            fullTimeOrPartTimeCode=fullTimeOrPartTimeCode,
            fullTimeOrPartTime=fullTimeOrPartTime,
            clockCode=clockCode,
            dateTimeCreated=dateTimeCreated,
            employeeTypeCode=employeeTypeCode,
            employeeTypeDescription=employeeTypeDescription,
            effectiveStartDate=effectiveStartDate,
            effectiveStopDate=effectiveStopDate,
            isEligibleForBenefits=isEligibleForBenefits,
            locationCode=locationCode,
            notes=notes,
            organizationLevel1Code=organizationLevel1Code,
            organizationLevel2Code=organizationLevel2Code,
            organizationLevel3Code=organizationLevel3Code,
            organizationLevel4Code=organizationLevel4Code,
            otherRate1=otherRate1,
            otherRate2=otherRate2,
            otherRate3=otherRate3,
            otherRate4=otherRate4,
            overrideIncumbentData=overrideIncumbentData,
            payGroupCode=payGroupCode,
            periodPayRate=periodPayRate,
            piecePayRate=piecePayRate,
            projectCode=projectCode,
            salaryOrHourlyCode=salaryOrHourlyCode,
            salaryOrHourly=salaryOrHourly,
            scheduledAnnualHours=scheduledAnnualHours,
            scheduledFullTimeEmployee=scheduledFullTimeEmployee,
            scheduledWorkHours=scheduledWorkHours,
            shiftCode=shiftCode,
            shiftGroupCode=shiftGroupCode,
            shiftGroupDescription=shiftGroupDescription,
            systemId=systemId,
            weeklyPayRate=weeklyPayRate,
            _configuration=_configuration,
            **kwargs,
        )
