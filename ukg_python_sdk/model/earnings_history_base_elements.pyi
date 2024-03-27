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


class EarningsHistoryBaseElements(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            employeeId = schemas.StrSchema
            companyId = schemas.StrSchema
            earningCode = schemas.StrSchema
            employeeNumber = schemas.StrSchema
            genNumber = schemas.StrSchema
            periodControl = schemas.StrSchema
            payGroup = schemas.StrSchema
            accrualCode = schemas.StrSchema
            baseAmount = schemas.NumberSchema
            batchID = schemas.StrSchema
            calculationRule = schemas.StrSchema
            calculationSequence = schemas.StrSchema
            currentAmount = schemas.NumberSchema
            currentHours = schemas.NumberSchema
            glBaseSegmentId = schemas.StrSchema
            glFollowBaseAccountAllocation = schemas.StrSchema
            grossUp = schemas.StrSchema
            grossUpTarget = schemas.NumberSchema
            grossUpTaxCalculationMethod = schemas.IntSchema
            hourlyPayRate = schemas.NumberSchema
            includeInDeferredCompensation = schemas.BoolSchema
            includeInDeferredCompensationHours = schemas.BoolSchema
            isVoided = schemas.BoolSchema
            isVoidingRecord = schemas.BoolSchema
            jobCode = schemas.StrSchema
            jobPremiumAmount = schemas.NumberSchema
            jobPremiumRateOrPercent = schemas.NumberSchema
            location = schemas.StrSchema
            numberOfDays = schemas.IntSchema
            numberOfGames = schemas.IntSchema
            payDate = schemas.DateTimeSchema
            payoutRateType = schemas.StrSchema
            payRate = schemas.NumberSchema
            paySheetID = schemas.StrSchema
            periodPayRate = schemas.NumberSchema
            pieceCount = schemas.NumberSchema
            piecePayRate = schemas.NumberSchema
            planYear = schemas.StrSchema
            project = schemas.StrSchema
            reportCategory = schemas.StrSchema
            taxCalculationGroupId = schemas.StrSchema
            taxCategory = schemas.StrSchema
            timeClockCode = schemas.StrSchema
            tipCredit = schemas.NumberSchema
            tipGrossReceipts = schemas.NumberSchema
            tipType = schemas.StrSchema
            useDeductionOffSet = schemas.BoolSchema
            ytdAmount = schemas.NumberSchema
            ytdShiftAmount = schemas.NumberSchema
            __annotations__ = {
                "employeeId": employeeId,
                "companyId": companyId,
                "earningCode": earningCode,
                "employeeNumber": employeeNumber,
                "genNumber": genNumber,
                "periodControl": periodControl,
                "payGroup": payGroup,
                "accrualCode": accrualCode,
                "baseAmount": baseAmount,
                "batchID": batchID,
                "calculationRule": calculationRule,
                "calculationSequence": calculationSequence,
                "currentAmount": currentAmount,
                "currentHours": currentHours,
                "glBaseSegmentId": glBaseSegmentId,
                "glFollowBaseAccountAllocation": glFollowBaseAccountAllocation,
                "grossUp": grossUp,
                "grossUpTarget": grossUpTarget,
                "grossUpTaxCalculationMethod": grossUpTaxCalculationMethod,
                "hourlyPayRate": hourlyPayRate,
                "includeInDeferredCompensation": includeInDeferredCompensation,
                "includeInDeferredCompensationHours": includeInDeferredCompensationHours,
                "isVoided": isVoided,
                "isVoidingRecord": isVoidingRecord,
                "jobCode": jobCode,
                "jobPremiumAmount": jobPremiumAmount,
                "jobPremiumRateOrPercent": jobPremiumRateOrPercent,
                "location": location,
                "numberOfDays": numberOfDays,
                "numberOfGames": numberOfGames,
                "payDate": payDate,
                "payoutRateType": payoutRateType,
                "payRate": payRate,
                "paySheetID": paySheetID,
                "periodPayRate": periodPayRate,
                "pieceCount": pieceCount,
                "piecePayRate": piecePayRate,
                "planYear": planYear,
                "project": project,
                "reportCategory": reportCategory,
                "taxCalculationGroupId": taxCalculationGroupId,
                "taxCategory": taxCategory,
                "timeClockCode": timeClockCode,
                "tipCredit": tipCredit,
                "tipGrossReceipts": tipGrossReceipts,
                "tipType": tipType,
                "useDeductionOffSet": useDeductionOffSet,
                "ytdAmount": ytdAmount,
                "ytdShiftAmount": ytdShiftAmount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earningCode"]) -> MetaOapg.properties.earningCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["genNumber"]) -> MetaOapg.properties.genNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodControl"]) -> MetaOapg.properties.periodControl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payGroup"]) -> MetaOapg.properties.payGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accrualCode"]) -> MetaOapg.properties.accrualCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseAmount"]) -> MetaOapg.properties.baseAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batchID"]) -> MetaOapg.properties.batchID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calculationRule"]) -> MetaOapg.properties.calculationRule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calculationSequence"]) -> MetaOapg.properties.calculationSequence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentAmount"]) -> MetaOapg.properties.currentAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentHours"]) -> MetaOapg.properties.currentHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["glBaseSegmentId"]) -> MetaOapg.properties.glBaseSegmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["glFollowBaseAccountAllocation"]) -> MetaOapg.properties.glFollowBaseAccountAllocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grossUp"]) -> MetaOapg.properties.grossUp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grossUpTarget"]) -> MetaOapg.properties.grossUpTarget: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grossUpTaxCalculationMethod"]) -> MetaOapg.properties.grossUpTaxCalculationMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourlyPayRate"]) -> MetaOapg.properties.hourlyPayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInDeferredCompensation"]) -> MetaOapg.properties.includeInDeferredCompensation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInDeferredCompensationHours"]) -> MetaOapg.properties.includeInDeferredCompensationHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isVoided"]) -> MetaOapg.properties.isVoided: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isVoidingRecord"]) -> MetaOapg.properties.isVoidingRecord: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobCode"]) -> MetaOapg.properties.jobCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobPremiumAmount"]) -> MetaOapg.properties.jobPremiumAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobPremiumRateOrPercent"]) -> MetaOapg.properties.jobPremiumRateOrPercent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfDays"]) -> MetaOapg.properties.numberOfDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfGames"]) -> MetaOapg.properties.numberOfGames: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payDate"]) -> MetaOapg.properties.payDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payoutRateType"]) -> MetaOapg.properties.payoutRateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payRate"]) -> MetaOapg.properties.payRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paySheetID"]) -> MetaOapg.properties.paySheetID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodPayRate"]) -> MetaOapg.properties.periodPayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pieceCount"]) -> MetaOapg.properties.pieceCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["piecePayRate"]) -> MetaOapg.properties.piecePayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["planYear"]) -> MetaOapg.properties.planYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> MetaOapg.properties.project: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reportCategory"]) -> MetaOapg.properties.reportCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCalculationGroupId"]) -> MetaOapg.properties.taxCalculationGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCategory"]) -> MetaOapg.properties.taxCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeClockCode"]) -> MetaOapg.properties.timeClockCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tipCredit"]) -> MetaOapg.properties.tipCredit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tipGrossReceipts"]) -> MetaOapg.properties.tipGrossReceipts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tipType"]) -> MetaOapg.properties.tipType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useDeductionOffSet"]) -> MetaOapg.properties.useDeductionOffSet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ytdAmount"]) -> MetaOapg.properties.ytdAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ytdShiftAmount"]) -> MetaOapg.properties.ytdShiftAmount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "companyId", "earningCode", "employeeNumber", "genNumber", "periodControl", "payGroup", "accrualCode", "baseAmount", "batchID", "calculationRule", "calculationSequence", "currentAmount", "currentHours", "glBaseSegmentId", "glFollowBaseAccountAllocation", "grossUp", "grossUpTarget", "grossUpTaxCalculationMethod", "hourlyPayRate", "includeInDeferredCompensation", "includeInDeferredCompensationHours", "isVoided", "isVoidingRecord", "jobCode", "jobPremiumAmount", "jobPremiumRateOrPercent", "location", "numberOfDays", "numberOfGames", "payDate", "payoutRateType", "payRate", "paySheetID", "periodPayRate", "pieceCount", "piecePayRate", "planYear", "project", "reportCategory", "taxCalculationGroupId", "taxCategory", "timeClockCode", "tipCredit", "tipGrossReceipts", "tipType", "useDeductionOffSet", "ytdAmount", "ytdShiftAmount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earningCode"]) -> typing.Union[MetaOapg.properties.earningCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> typing.Union[MetaOapg.properties.employeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["genNumber"]) -> typing.Union[MetaOapg.properties.genNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodControl"]) -> typing.Union[MetaOapg.properties.periodControl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payGroup"]) -> typing.Union[MetaOapg.properties.payGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accrualCode"]) -> typing.Union[MetaOapg.properties.accrualCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseAmount"]) -> typing.Union[MetaOapg.properties.baseAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batchID"]) -> typing.Union[MetaOapg.properties.batchID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calculationRule"]) -> typing.Union[MetaOapg.properties.calculationRule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calculationSequence"]) -> typing.Union[MetaOapg.properties.calculationSequence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentAmount"]) -> typing.Union[MetaOapg.properties.currentAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentHours"]) -> typing.Union[MetaOapg.properties.currentHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["glBaseSegmentId"]) -> typing.Union[MetaOapg.properties.glBaseSegmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["glFollowBaseAccountAllocation"]) -> typing.Union[MetaOapg.properties.glFollowBaseAccountAllocation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grossUp"]) -> typing.Union[MetaOapg.properties.grossUp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grossUpTarget"]) -> typing.Union[MetaOapg.properties.grossUpTarget, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grossUpTaxCalculationMethod"]) -> typing.Union[MetaOapg.properties.grossUpTaxCalculationMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourlyPayRate"]) -> typing.Union[MetaOapg.properties.hourlyPayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInDeferredCompensation"]) -> typing.Union[MetaOapg.properties.includeInDeferredCompensation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInDeferredCompensationHours"]) -> typing.Union[MetaOapg.properties.includeInDeferredCompensationHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isVoided"]) -> typing.Union[MetaOapg.properties.isVoided, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isVoidingRecord"]) -> typing.Union[MetaOapg.properties.isVoidingRecord, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobCode"]) -> typing.Union[MetaOapg.properties.jobCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobPremiumAmount"]) -> typing.Union[MetaOapg.properties.jobPremiumAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobPremiumRateOrPercent"]) -> typing.Union[MetaOapg.properties.jobPremiumRateOrPercent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfDays"]) -> typing.Union[MetaOapg.properties.numberOfDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfGames"]) -> typing.Union[MetaOapg.properties.numberOfGames, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payDate"]) -> typing.Union[MetaOapg.properties.payDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payoutRateType"]) -> typing.Union[MetaOapg.properties.payoutRateType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payRate"]) -> typing.Union[MetaOapg.properties.payRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paySheetID"]) -> typing.Union[MetaOapg.properties.paySheetID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodPayRate"]) -> typing.Union[MetaOapg.properties.periodPayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pieceCount"]) -> typing.Union[MetaOapg.properties.pieceCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["piecePayRate"]) -> typing.Union[MetaOapg.properties.piecePayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["planYear"]) -> typing.Union[MetaOapg.properties.planYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union[MetaOapg.properties.project, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reportCategory"]) -> typing.Union[MetaOapg.properties.reportCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCalculationGroupId"]) -> typing.Union[MetaOapg.properties.taxCalculationGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCategory"]) -> typing.Union[MetaOapg.properties.taxCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeClockCode"]) -> typing.Union[MetaOapg.properties.timeClockCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tipCredit"]) -> typing.Union[MetaOapg.properties.tipCredit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tipGrossReceipts"]) -> typing.Union[MetaOapg.properties.tipGrossReceipts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tipType"]) -> typing.Union[MetaOapg.properties.tipType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useDeductionOffSet"]) -> typing.Union[MetaOapg.properties.useDeductionOffSet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ytdAmount"]) -> typing.Union[MetaOapg.properties.ytdAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ytdShiftAmount"]) -> typing.Union[MetaOapg.properties.ytdShiftAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "companyId", "earningCode", "employeeNumber", "genNumber", "periodControl", "payGroup", "accrualCode", "baseAmount", "batchID", "calculationRule", "calculationSequence", "currentAmount", "currentHours", "glBaseSegmentId", "glFollowBaseAccountAllocation", "grossUp", "grossUpTarget", "grossUpTaxCalculationMethod", "hourlyPayRate", "includeInDeferredCompensation", "includeInDeferredCompensationHours", "isVoided", "isVoidingRecord", "jobCode", "jobPremiumAmount", "jobPremiumRateOrPercent", "location", "numberOfDays", "numberOfGames", "payDate", "payoutRateType", "payRate", "paySheetID", "periodPayRate", "pieceCount", "piecePayRate", "planYear", "project", "reportCategory", "taxCalculationGroupId", "taxCategory", "timeClockCode", "tipCredit", "tipGrossReceipts", "tipType", "useDeductionOffSet", "ytdAmount", "ytdShiftAmount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, schemas.Unset] = schemas.unset,
        earningCode: typing.Union[MetaOapg.properties.earningCode, str, schemas.Unset] = schemas.unset,
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, str, schemas.Unset] = schemas.unset,
        genNumber: typing.Union[MetaOapg.properties.genNumber, str, schemas.Unset] = schemas.unset,
        periodControl: typing.Union[MetaOapg.properties.periodControl, str, schemas.Unset] = schemas.unset,
        payGroup: typing.Union[MetaOapg.properties.payGroup, str, schemas.Unset] = schemas.unset,
        accrualCode: typing.Union[MetaOapg.properties.accrualCode, str, schemas.Unset] = schemas.unset,
        baseAmount: typing.Union[MetaOapg.properties.baseAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        batchID: typing.Union[MetaOapg.properties.batchID, str, schemas.Unset] = schemas.unset,
        calculationRule: typing.Union[MetaOapg.properties.calculationRule, str, schemas.Unset] = schemas.unset,
        calculationSequence: typing.Union[MetaOapg.properties.calculationSequence, str, schemas.Unset] = schemas.unset,
        currentAmount: typing.Union[MetaOapg.properties.currentAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currentHours: typing.Union[MetaOapg.properties.currentHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        glBaseSegmentId: typing.Union[MetaOapg.properties.glBaseSegmentId, str, schemas.Unset] = schemas.unset,
        glFollowBaseAccountAllocation: typing.Union[MetaOapg.properties.glFollowBaseAccountAllocation, str, schemas.Unset] = schemas.unset,
        grossUp: typing.Union[MetaOapg.properties.grossUp, str, schemas.Unset] = schemas.unset,
        grossUpTarget: typing.Union[MetaOapg.properties.grossUpTarget, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        grossUpTaxCalculationMethod: typing.Union[MetaOapg.properties.grossUpTaxCalculationMethod, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hourlyPayRate: typing.Union[MetaOapg.properties.hourlyPayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        includeInDeferredCompensation: typing.Union[MetaOapg.properties.includeInDeferredCompensation, bool, schemas.Unset] = schemas.unset,
        includeInDeferredCompensationHours: typing.Union[MetaOapg.properties.includeInDeferredCompensationHours, bool, schemas.Unset] = schemas.unset,
        isVoided: typing.Union[MetaOapg.properties.isVoided, bool, schemas.Unset] = schemas.unset,
        isVoidingRecord: typing.Union[MetaOapg.properties.isVoidingRecord, bool, schemas.Unset] = schemas.unset,
        jobCode: typing.Union[MetaOapg.properties.jobCode, str, schemas.Unset] = schemas.unset,
        jobPremiumAmount: typing.Union[MetaOapg.properties.jobPremiumAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        jobPremiumRateOrPercent: typing.Union[MetaOapg.properties.jobPremiumRateOrPercent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, str, schemas.Unset] = schemas.unset,
        numberOfDays: typing.Union[MetaOapg.properties.numberOfDays, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        numberOfGames: typing.Union[MetaOapg.properties.numberOfGames, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payDate: typing.Union[MetaOapg.properties.payDate, str, datetime, schemas.Unset] = schemas.unset,
        payoutRateType: typing.Union[MetaOapg.properties.payoutRateType, str, schemas.Unset] = schemas.unset,
        payRate: typing.Union[MetaOapg.properties.payRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        paySheetID: typing.Union[MetaOapg.properties.paySheetID, str, schemas.Unset] = schemas.unset,
        periodPayRate: typing.Union[MetaOapg.properties.periodPayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pieceCount: typing.Union[MetaOapg.properties.pieceCount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        piecePayRate: typing.Union[MetaOapg.properties.piecePayRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        planYear: typing.Union[MetaOapg.properties.planYear, str, schemas.Unset] = schemas.unset,
        project: typing.Union[MetaOapg.properties.project, str, schemas.Unset] = schemas.unset,
        reportCategory: typing.Union[MetaOapg.properties.reportCategory, str, schemas.Unset] = schemas.unset,
        taxCalculationGroupId: typing.Union[MetaOapg.properties.taxCalculationGroupId, str, schemas.Unset] = schemas.unset,
        taxCategory: typing.Union[MetaOapg.properties.taxCategory, str, schemas.Unset] = schemas.unset,
        timeClockCode: typing.Union[MetaOapg.properties.timeClockCode, str, schemas.Unset] = schemas.unset,
        tipCredit: typing.Union[MetaOapg.properties.tipCredit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tipGrossReceipts: typing.Union[MetaOapg.properties.tipGrossReceipts, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tipType: typing.Union[MetaOapg.properties.tipType, str, schemas.Unset] = schemas.unset,
        useDeductionOffSet: typing.Union[MetaOapg.properties.useDeductionOffSet, bool, schemas.Unset] = schemas.unset,
        ytdAmount: typing.Union[MetaOapg.properties.ytdAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ytdShiftAmount: typing.Union[MetaOapg.properties.ytdShiftAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EarningsHistoryBaseElements':
        return super().__new__(
            cls,
            *args,
            employeeId=employeeId,
            companyId=companyId,
            earningCode=earningCode,
            employeeNumber=employeeNumber,
            genNumber=genNumber,
            periodControl=periodControl,
            payGroup=payGroup,
            accrualCode=accrualCode,
            baseAmount=baseAmount,
            batchID=batchID,
            calculationRule=calculationRule,
            calculationSequence=calculationSequence,
            currentAmount=currentAmount,
            currentHours=currentHours,
            glBaseSegmentId=glBaseSegmentId,
            glFollowBaseAccountAllocation=glFollowBaseAccountAllocation,
            grossUp=grossUp,
            grossUpTarget=grossUpTarget,
            grossUpTaxCalculationMethod=grossUpTaxCalculationMethod,
            hourlyPayRate=hourlyPayRate,
            includeInDeferredCompensation=includeInDeferredCompensation,
            includeInDeferredCompensationHours=includeInDeferredCompensationHours,
            isVoided=isVoided,
            isVoidingRecord=isVoidingRecord,
            jobCode=jobCode,
            jobPremiumAmount=jobPremiumAmount,
            jobPremiumRateOrPercent=jobPremiumRateOrPercent,
            location=location,
            numberOfDays=numberOfDays,
            numberOfGames=numberOfGames,
            payDate=payDate,
            payoutRateType=payoutRateType,
            payRate=payRate,
            paySheetID=paySheetID,
            periodPayRate=periodPayRate,
            pieceCount=pieceCount,
            piecePayRate=piecePayRate,
            planYear=planYear,
            project=project,
            reportCategory=reportCategory,
            taxCalculationGroupId=taxCalculationGroupId,
            taxCategory=taxCategory,
            timeClockCode=timeClockCode,
            tipCredit=tipCredit,
            tipGrossReceipts=tipGrossReceipts,
            tipType=tipType,
            useDeductionOffSet=useDeductionOffSet,
            ytdAmount=ytdAmount,
            ytdShiftAmount=ytdShiftAmount,
            _configuration=_configuration,
            **kwargs,
        )
