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


class EarningsDto(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "longDescription",
            "timeClockCode",
            "stubDescription",
            "earningCode",
        }
        
        class properties:
            earningCode = schemas.StrSchema
            longDescription = schemas.StrSchema
            stubDescription = schemas.StrSchema
            timeClockCode = schemas.StrSchema
            amount = schemas.Float64Schema
            blockFederalIncomeTax = schemas.BoolSchema
            blockLocalIncomeTax = schemas.BoolSchema
            blockStateIncomeTax = schemas.BoolSchema
            calculationRule = schemas.StrSchema
            displayInPayDataEntry = schemas.BoolSchema
            excelInTotalHours = schemas.BoolSchema
            flatHours = schemas.Float64Schema
            includeInAccruals = schemas.StrSchema
            includeInAllocations = schemas.BoolSchema
            includeFlsaAveragePayRate = schemas.BoolSchema
            includeInBenefitHours = schemas.BoolSchema
            includeInDeferredCompensation = schemas.BoolSchema
            includeInDeferredCompensationHours = schemas.BoolSchema
            includeInEarningAccumulation = schemas.BoolSchema
            includeInHoursAccumulation = schemas.BoolSchema
            includeInManualCheck = schemas.BoolSchema
            includeInMiscellaneousEarning1 = schemas.BoolSchema
            includeInMiscellaneousEarning2 = schemas.BoolSchema
            includeInMiscellaneousEarning3 = schemas.BoolSchema
            includeInMiscellaneousEarning4 = schemas.BoolSchema
            includeInMiscellaneousEarning5 = schemas.BoolSchema
            includeInMiscellaneousEarning6 = schemas.BoolSchema
            includeInPensionAccumulation = schemas.BoolSchema
            includeInRetroPay = schemas.BoolSchema
            includeInShiftDiffrential = schemas.BoolSchema
            isProductiveTime = schemas.BoolSchema
            isSupplimentalWages = schemas.BoolSchema
            monthlyPayPeriod1 = schemas.BoolSchema
            monthlyPayPeriod2 = schemas.BoolSchema
            monthlyPayPeriod3 = schemas.BoolSchema
            monthlyPayPeriod4 = schemas.BoolSchema
            monthlyPayPeriod5 = schemas.BoolSchema
            notes = schemas.StrSchema
            reduceRegularDollars = schemas.BoolSchema
            reduceRegularHours = schemas.BoolSchema
            reportCategory = schemas.StrSchema
            scheduleSupplemental = schemas.BoolSchema
            taxCategory = schemas.StrSchema
            countryCode = schemas.StrSchema
            useDeductionOffset = schemas.BoolSchema
            includeInRegisteredPensionPlan = schemas.BoolSchema
            includeInRegisteredRetirementSavingsPlan = schemas.BoolSchema
            includeInUnionDues = schemas.BoolSchema
            includeInUnionDuesHours = schemas.BoolSchema
            taxCalculationRule = schemas.StrSchema
            exemptFromEarnedIncomeHours = schemas.StrSchema
            includeInHealthCareHours = schemas.BoolSchema
            verificationTypeCode = schemas.StrSchema
            verificationTypeDescription = schemas.StrSchema
            __annotations__ = {
                "earningCode": earningCode,
                "longDescription": longDescription,
                "stubDescription": stubDescription,
                "timeClockCode": timeClockCode,
                "amount": amount,
                "blockFederalIncomeTax": blockFederalIncomeTax,
                "blockLocalIncomeTax": blockLocalIncomeTax,
                "blockStateIncomeTax": blockStateIncomeTax,
                "calculationRule": calculationRule,
                "displayInPayDataEntry": displayInPayDataEntry,
                "excelInTotalHours": excelInTotalHours,
                "flatHours": flatHours,
                "includeInAccruals": includeInAccruals,
                "includeInAllocations": includeInAllocations,
                "includeFlsaAveragePayRate": includeFlsaAveragePayRate,
                "includeInBenefitHours": includeInBenefitHours,
                "includeInDeferredCompensation": includeInDeferredCompensation,
                "includeInDeferredCompensationHours": includeInDeferredCompensationHours,
                "includeInEarningAccumulation": includeInEarningAccumulation,
                "includeInHoursAccumulation": includeInHoursAccumulation,
                "includeInManualCheck": includeInManualCheck,
                "includeInMiscellaneousEarning1": includeInMiscellaneousEarning1,
                "includeInMiscellaneousEarning2": includeInMiscellaneousEarning2,
                "includeInMiscellaneousEarning3": includeInMiscellaneousEarning3,
                "includeInMiscellaneousEarning4": includeInMiscellaneousEarning4,
                "includeInMiscellaneousEarning5": includeInMiscellaneousEarning5,
                "includeInMiscellaneousEarning6": includeInMiscellaneousEarning6,
                "includeInPensionAccumulation": includeInPensionAccumulation,
                "includeInRetroPay": includeInRetroPay,
                "includeInShiftDiffrential": includeInShiftDiffrential,
                "isProductiveTime": isProductiveTime,
                "isSupplimentalWages": isSupplimentalWages,
                "monthlyPayPeriod1": monthlyPayPeriod1,
                "monthlyPayPeriod2": monthlyPayPeriod2,
                "monthlyPayPeriod3": monthlyPayPeriod3,
                "monthlyPayPeriod4": monthlyPayPeriod4,
                "monthlyPayPeriod5": monthlyPayPeriod5,
                "notes": notes,
                "reduceRegularDollars": reduceRegularDollars,
                "reduceRegularHours": reduceRegularHours,
                "reportCategory": reportCategory,
                "scheduleSupplemental": scheduleSupplemental,
                "taxCategory": taxCategory,
                "countryCode": countryCode,
                "useDeductionOffset": useDeductionOffset,
                "includeInRegisteredPensionPlan": includeInRegisteredPensionPlan,
                "includeInRegisteredRetirementSavingsPlan": includeInRegisteredRetirementSavingsPlan,
                "includeInUnionDues": includeInUnionDues,
                "includeInUnionDuesHours": includeInUnionDuesHours,
                "taxCalculationRule": taxCalculationRule,
                "exemptFromEarnedIncomeHours": exemptFromEarnedIncomeHours,
                "includeInHealthCareHours": includeInHealthCareHours,
                "verificationTypeCode": verificationTypeCode,
                "verificationTypeDescription": verificationTypeDescription,
            }
    
    longDescription: MetaOapg.properties.longDescription
    timeClockCode: MetaOapg.properties.timeClockCode
    stubDescription: MetaOapg.properties.stubDescription
    earningCode: MetaOapg.properties.earningCode
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earningCode"]) -> MetaOapg.properties.earningCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longDescription"]) -> MetaOapg.properties.longDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stubDescription"]) -> MetaOapg.properties.stubDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeClockCode"]) -> MetaOapg.properties.timeClockCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockFederalIncomeTax"]) -> MetaOapg.properties.blockFederalIncomeTax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockLocalIncomeTax"]) -> MetaOapg.properties.blockLocalIncomeTax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockStateIncomeTax"]) -> MetaOapg.properties.blockStateIncomeTax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calculationRule"]) -> MetaOapg.properties.calculationRule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayInPayDataEntry"]) -> MetaOapg.properties.displayInPayDataEntry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excelInTotalHours"]) -> MetaOapg.properties.excelInTotalHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flatHours"]) -> MetaOapg.properties.flatHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInAccruals"]) -> MetaOapg.properties.includeInAccruals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInAllocations"]) -> MetaOapg.properties.includeInAllocations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeFlsaAveragePayRate"]) -> MetaOapg.properties.includeFlsaAveragePayRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInBenefitHours"]) -> MetaOapg.properties.includeInBenefitHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInDeferredCompensation"]) -> MetaOapg.properties.includeInDeferredCompensation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInDeferredCompensationHours"]) -> MetaOapg.properties.includeInDeferredCompensationHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInEarningAccumulation"]) -> MetaOapg.properties.includeInEarningAccumulation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInHoursAccumulation"]) -> MetaOapg.properties.includeInHoursAccumulation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInManualCheck"]) -> MetaOapg.properties.includeInManualCheck: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInMiscellaneousEarning1"]) -> MetaOapg.properties.includeInMiscellaneousEarning1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInMiscellaneousEarning2"]) -> MetaOapg.properties.includeInMiscellaneousEarning2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInMiscellaneousEarning3"]) -> MetaOapg.properties.includeInMiscellaneousEarning3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInMiscellaneousEarning4"]) -> MetaOapg.properties.includeInMiscellaneousEarning4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInMiscellaneousEarning5"]) -> MetaOapg.properties.includeInMiscellaneousEarning5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInMiscellaneousEarning6"]) -> MetaOapg.properties.includeInMiscellaneousEarning6: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInPensionAccumulation"]) -> MetaOapg.properties.includeInPensionAccumulation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInRetroPay"]) -> MetaOapg.properties.includeInRetroPay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInShiftDiffrential"]) -> MetaOapg.properties.includeInShiftDiffrential: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isProductiveTime"]) -> MetaOapg.properties.isProductiveTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSupplimentalWages"]) -> MetaOapg.properties.isSupplimentalWages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyPayPeriod1"]) -> MetaOapg.properties.monthlyPayPeriod1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyPayPeriod2"]) -> MetaOapg.properties.monthlyPayPeriod2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyPayPeriod3"]) -> MetaOapg.properties.monthlyPayPeriod3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyPayPeriod4"]) -> MetaOapg.properties.monthlyPayPeriod4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthlyPayPeriod5"]) -> MetaOapg.properties.monthlyPayPeriod5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reduceRegularDollars"]) -> MetaOapg.properties.reduceRegularDollars: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reduceRegularHours"]) -> MetaOapg.properties.reduceRegularHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reportCategory"]) -> MetaOapg.properties.reportCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduleSupplemental"]) -> MetaOapg.properties.scheduleSupplemental: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCategory"]) -> MetaOapg.properties.taxCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useDeductionOffset"]) -> MetaOapg.properties.useDeductionOffset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInRegisteredPensionPlan"]) -> MetaOapg.properties.includeInRegisteredPensionPlan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInRegisteredRetirementSavingsPlan"]) -> MetaOapg.properties.includeInRegisteredRetirementSavingsPlan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInUnionDues"]) -> MetaOapg.properties.includeInUnionDues: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInUnionDuesHours"]) -> MetaOapg.properties.includeInUnionDuesHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCalculationRule"]) -> MetaOapg.properties.taxCalculationRule: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exemptFromEarnedIncomeHours"]) -> MetaOapg.properties.exemptFromEarnedIncomeHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeInHealthCareHours"]) -> MetaOapg.properties.includeInHealthCareHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verificationTypeCode"]) -> MetaOapg.properties.verificationTypeCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verificationTypeDescription"]) -> MetaOapg.properties.verificationTypeDescription: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["earningCode", "longDescription", "stubDescription", "timeClockCode", "amount", "blockFederalIncomeTax", "blockLocalIncomeTax", "blockStateIncomeTax", "calculationRule", "displayInPayDataEntry", "excelInTotalHours", "flatHours", "includeInAccruals", "includeInAllocations", "includeFlsaAveragePayRate", "includeInBenefitHours", "includeInDeferredCompensation", "includeInDeferredCompensationHours", "includeInEarningAccumulation", "includeInHoursAccumulation", "includeInManualCheck", "includeInMiscellaneousEarning1", "includeInMiscellaneousEarning2", "includeInMiscellaneousEarning3", "includeInMiscellaneousEarning4", "includeInMiscellaneousEarning5", "includeInMiscellaneousEarning6", "includeInPensionAccumulation", "includeInRetroPay", "includeInShiftDiffrential", "isProductiveTime", "isSupplimentalWages", "monthlyPayPeriod1", "monthlyPayPeriod2", "monthlyPayPeriod3", "monthlyPayPeriod4", "monthlyPayPeriod5", "notes", "reduceRegularDollars", "reduceRegularHours", "reportCategory", "scheduleSupplemental", "taxCategory", "countryCode", "useDeductionOffset", "includeInRegisteredPensionPlan", "includeInRegisteredRetirementSavingsPlan", "includeInUnionDues", "includeInUnionDuesHours", "taxCalculationRule", "exemptFromEarnedIncomeHours", "includeInHealthCareHours", "verificationTypeCode", "verificationTypeDescription", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earningCode"]) -> MetaOapg.properties.earningCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longDescription"]) -> MetaOapg.properties.longDescription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stubDescription"]) -> MetaOapg.properties.stubDescription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeClockCode"]) -> MetaOapg.properties.timeClockCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockFederalIncomeTax"]) -> typing.Union[MetaOapg.properties.blockFederalIncomeTax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockLocalIncomeTax"]) -> typing.Union[MetaOapg.properties.blockLocalIncomeTax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockStateIncomeTax"]) -> typing.Union[MetaOapg.properties.blockStateIncomeTax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calculationRule"]) -> typing.Union[MetaOapg.properties.calculationRule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayInPayDataEntry"]) -> typing.Union[MetaOapg.properties.displayInPayDataEntry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excelInTotalHours"]) -> typing.Union[MetaOapg.properties.excelInTotalHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flatHours"]) -> typing.Union[MetaOapg.properties.flatHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInAccruals"]) -> typing.Union[MetaOapg.properties.includeInAccruals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInAllocations"]) -> typing.Union[MetaOapg.properties.includeInAllocations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeFlsaAveragePayRate"]) -> typing.Union[MetaOapg.properties.includeFlsaAveragePayRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInBenefitHours"]) -> typing.Union[MetaOapg.properties.includeInBenefitHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInDeferredCompensation"]) -> typing.Union[MetaOapg.properties.includeInDeferredCompensation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInDeferredCompensationHours"]) -> typing.Union[MetaOapg.properties.includeInDeferredCompensationHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInEarningAccumulation"]) -> typing.Union[MetaOapg.properties.includeInEarningAccumulation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInHoursAccumulation"]) -> typing.Union[MetaOapg.properties.includeInHoursAccumulation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInManualCheck"]) -> typing.Union[MetaOapg.properties.includeInManualCheck, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInMiscellaneousEarning1"]) -> typing.Union[MetaOapg.properties.includeInMiscellaneousEarning1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInMiscellaneousEarning2"]) -> typing.Union[MetaOapg.properties.includeInMiscellaneousEarning2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInMiscellaneousEarning3"]) -> typing.Union[MetaOapg.properties.includeInMiscellaneousEarning3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInMiscellaneousEarning4"]) -> typing.Union[MetaOapg.properties.includeInMiscellaneousEarning4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInMiscellaneousEarning5"]) -> typing.Union[MetaOapg.properties.includeInMiscellaneousEarning5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInMiscellaneousEarning6"]) -> typing.Union[MetaOapg.properties.includeInMiscellaneousEarning6, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInPensionAccumulation"]) -> typing.Union[MetaOapg.properties.includeInPensionAccumulation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInRetroPay"]) -> typing.Union[MetaOapg.properties.includeInRetroPay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInShiftDiffrential"]) -> typing.Union[MetaOapg.properties.includeInShiftDiffrential, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isProductiveTime"]) -> typing.Union[MetaOapg.properties.isProductiveTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSupplimentalWages"]) -> typing.Union[MetaOapg.properties.isSupplimentalWages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyPayPeriod1"]) -> typing.Union[MetaOapg.properties.monthlyPayPeriod1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyPayPeriod2"]) -> typing.Union[MetaOapg.properties.monthlyPayPeriod2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyPayPeriod3"]) -> typing.Union[MetaOapg.properties.monthlyPayPeriod3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyPayPeriod4"]) -> typing.Union[MetaOapg.properties.monthlyPayPeriod4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthlyPayPeriod5"]) -> typing.Union[MetaOapg.properties.monthlyPayPeriod5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reduceRegularDollars"]) -> typing.Union[MetaOapg.properties.reduceRegularDollars, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reduceRegularHours"]) -> typing.Union[MetaOapg.properties.reduceRegularHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reportCategory"]) -> typing.Union[MetaOapg.properties.reportCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduleSupplemental"]) -> typing.Union[MetaOapg.properties.scheduleSupplemental, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCategory"]) -> typing.Union[MetaOapg.properties.taxCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryCode"]) -> typing.Union[MetaOapg.properties.countryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useDeductionOffset"]) -> typing.Union[MetaOapg.properties.useDeductionOffset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInRegisteredPensionPlan"]) -> typing.Union[MetaOapg.properties.includeInRegisteredPensionPlan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInRegisteredRetirementSavingsPlan"]) -> typing.Union[MetaOapg.properties.includeInRegisteredRetirementSavingsPlan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInUnionDues"]) -> typing.Union[MetaOapg.properties.includeInUnionDues, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInUnionDuesHours"]) -> typing.Union[MetaOapg.properties.includeInUnionDuesHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCalculationRule"]) -> typing.Union[MetaOapg.properties.taxCalculationRule, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exemptFromEarnedIncomeHours"]) -> typing.Union[MetaOapg.properties.exemptFromEarnedIncomeHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeInHealthCareHours"]) -> typing.Union[MetaOapg.properties.includeInHealthCareHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verificationTypeCode"]) -> typing.Union[MetaOapg.properties.verificationTypeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verificationTypeDescription"]) -> typing.Union[MetaOapg.properties.verificationTypeDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["earningCode", "longDescription", "stubDescription", "timeClockCode", "amount", "blockFederalIncomeTax", "blockLocalIncomeTax", "blockStateIncomeTax", "calculationRule", "displayInPayDataEntry", "excelInTotalHours", "flatHours", "includeInAccruals", "includeInAllocations", "includeFlsaAveragePayRate", "includeInBenefitHours", "includeInDeferredCompensation", "includeInDeferredCompensationHours", "includeInEarningAccumulation", "includeInHoursAccumulation", "includeInManualCheck", "includeInMiscellaneousEarning1", "includeInMiscellaneousEarning2", "includeInMiscellaneousEarning3", "includeInMiscellaneousEarning4", "includeInMiscellaneousEarning5", "includeInMiscellaneousEarning6", "includeInPensionAccumulation", "includeInRetroPay", "includeInShiftDiffrential", "isProductiveTime", "isSupplimentalWages", "monthlyPayPeriod1", "monthlyPayPeriod2", "monthlyPayPeriod3", "monthlyPayPeriod4", "monthlyPayPeriod5", "notes", "reduceRegularDollars", "reduceRegularHours", "reportCategory", "scheduleSupplemental", "taxCategory", "countryCode", "useDeductionOffset", "includeInRegisteredPensionPlan", "includeInRegisteredRetirementSavingsPlan", "includeInUnionDues", "includeInUnionDuesHours", "taxCalculationRule", "exemptFromEarnedIncomeHours", "includeInHealthCareHours", "verificationTypeCode", "verificationTypeDescription", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        longDescription: typing.Union[MetaOapg.properties.longDescription, str, ],
        timeClockCode: typing.Union[MetaOapg.properties.timeClockCode, str, ],
        stubDescription: typing.Union[MetaOapg.properties.stubDescription, str, ],
        earningCode: typing.Union[MetaOapg.properties.earningCode, str, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        blockFederalIncomeTax: typing.Union[MetaOapg.properties.blockFederalIncomeTax, bool, schemas.Unset] = schemas.unset,
        blockLocalIncomeTax: typing.Union[MetaOapg.properties.blockLocalIncomeTax, bool, schemas.Unset] = schemas.unset,
        blockStateIncomeTax: typing.Union[MetaOapg.properties.blockStateIncomeTax, bool, schemas.Unset] = schemas.unset,
        calculationRule: typing.Union[MetaOapg.properties.calculationRule, str, schemas.Unset] = schemas.unset,
        displayInPayDataEntry: typing.Union[MetaOapg.properties.displayInPayDataEntry, bool, schemas.Unset] = schemas.unset,
        excelInTotalHours: typing.Union[MetaOapg.properties.excelInTotalHours, bool, schemas.Unset] = schemas.unset,
        flatHours: typing.Union[MetaOapg.properties.flatHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        includeInAccruals: typing.Union[MetaOapg.properties.includeInAccruals, str, schemas.Unset] = schemas.unset,
        includeInAllocations: typing.Union[MetaOapg.properties.includeInAllocations, bool, schemas.Unset] = schemas.unset,
        includeFlsaAveragePayRate: typing.Union[MetaOapg.properties.includeFlsaAveragePayRate, bool, schemas.Unset] = schemas.unset,
        includeInBenefitHours: typing.Union[MetaOapg.properties.includeInBenefitHours, bool, schemas.Unset] = schemas.unset,
        includeInDeferredCompensation: typing.Union[MetaOapg.properties.includeInDeferredCompensation, bool, schemas.Unset] = schemas.unset,
        includeInDeferredCompensationHours: typing.Union[MetaOapg.properties.includeInDeferredCompensationHours, bool, schemas.Unset] = schemas.unset,
        includeInEarningAccumulation: typing.Union[MetaOapg.properties.includeInEarningAccumulation, bool, schemas.Unset] = schemas.unset,
        includeInHoursAccumulation: typing.Union[MetaOapg.properties.includeInHoursAccumulation, bool, schemas.Unset] = schemas.unset,
        includeInManualCheck: typing.Union[MetaOapg.properties.includeInManualCheck, bool, schemas.Unset] = schemas.unset,
        includeInMiscellaneousEarning1: typing.Union[MetaOapg.properties.includeInMiscellaneousEarning1, bool, schemas.Unset] = schemas.unset,
        includeInMiscellaneousEarning2: typing.Union[MetaOapg.properties.includeInMiscellaneousEarning2, bool, schemas.Unset] = schemas.unset,
        includeInMiscellaneousEarning3: typing.Union[MetaOapg.properties.includeInMiscellaneousEarning3, bool, schemas.Unset] = schemas.unset,
        includeInMiscellaneousEarning4: typing.Union[MetaOapg.properties.includeInMiscellaneousEarning4, bool, schemas.Unset] = schemas.unset,
        includeInMiscellaneousEarning5: typing.Union[MetaOapg.properties.includeInMiscellaneousEarning5, bool, schemas.Unset] = schemas.unset,
        includeInMiscellaneousEarning6: typing.Union[MetaOapg.properties.includeInMiscellaneousEarning6, bool, schemas.Unset] = schemas.unset,
        includeInPensionAccumulation: typing.Union[MetaOapg.properties.includeInPensionAccumulation, bool, schemas.Unset] = schemas.unset,
        includeInRetroPay: typing.Union[MetaOapg.properties.includeInRetroPay, bool, schemas.Unset] = schemas.unset,
        includeInShiftDiffrential: typing.Union[MetaOapg.properties.includeInShiftDiffrential, bool, schemas.Unset] = schemas.unset,
        isProductiveTime: typing.Union[MetaOapg.properties.isProductiveTime, bool, schemas.Unset] = schemas.unset,
        isSupplimentalWages: typing.Union[MetaOapg.properties.isSupplimentalWages, bool, schemas.Unset] = schemas.unset,
        monthlyPayPeriod1: typing.Union[MetaOapg.properties.monthlyPayPeriod1, bool, schemas.Unset] = schemas.unset,
        monthlyPayPeriod2: typing.Union[MetaOapg.properties.monthlyPayPeriod2, bool, schemas.Unset] = schemas.unset,
        monthlyPayPeriod3: typing.Union[MetaOapg.properties.monthlyPayPeriod3, bool, schemas.Unset] = schemas.unset,
        monthlyPayPeriod4: typing.Union[MetaOapg.properties.monthlyPayPeriod4, bool, schemas.Unset] = schemas.unset,
        monthlyPayPeriod5: typing.Union[MetaOapg.properties.monthlyPayPeriod5, bool, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        reduceRegularDollars: typing.Union[MetaOapg.properties.reduceRegularDollars, bool, schemas.Unset] = schemas.unset,
        reduceRegularHours: typing.Union[MetaOapg.properties.reduceRegularHours, bool, schemas.Unset] = schemas.unset,
        reportCategory: typing.Union[MetaOapg.properties.reportCategory, str, schemas.Unset] = schemas.unset,
        scheduleSupplemental: typing.Union[MetaOapg.properties.scheduleSupplemental, bool, schemas.Unset] = schemas.unset,
        taxCategory: typing.Union[MetaOapg.properties.taxCategory, str, schemas.Unset] = schemas.unset,
        countryCode: typing.Union[MetaOapg.properties.countryCode, str, schemas.Unset] = schemas.unset,
        useDeductionOffset: typing.Union[MetaOapg.properties.useDeductionOffset, bool, schemas.Unset] = schemas.unset,
        includeInRegisteredPensionPlan: typing.Union[MetaOapg.properties.includeInRegisteredPensionPlan, bool, schemas.Unset] = schemas.unset,
        includeInRegisteredRetirementSavingsPlan: typing.Union[MetaOapg.properties.includeInRegisteredRetirementSavingsPlan, bool, schemas.Unset] = schemas.unset,
        includeInUnionDues: typing.Union[MetaOapg.properties.includeInUnionDues, bool, schemas.Unset] = schemas.unset,
        includeInUnionDuesHours: typing.Union[MetaOapg.properties.includeInUnionDuesHours, bool, schemas.Unset] = schemas.unset,
        taxCalculationRule: typing.Union[MetaOapg.properties.taxCalculationRule, str, schemas.Unset] = schemas.unset,
        exemptFromEarnedIncomeHours: typing.Union[MetaOapg.properties.exemptFromEarnedIncomeHours, str, schemas.Unset] = schemas.unset,
        includeInHealthCareHours: typing.Union[MetaOapg.properties.includeInHealthCareHours, bool, schemas.Unset] = schemas.unset,
        verificationTypeCode: typing.Union[MetaOapg.properties.verificationTypeCode, str, schemas.Unset] = schemas.unset,
        verificationTypeDescription: typing.Union[MetaOapg.properties.verificationTypeDescription, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EarningsDto':
        return super().__new__(
            cls,
            *args,
            longDescription=longDescription,
            timeClockCode=timeClockCode,
            stubDescription=stubDescription,
            earningCode=earningCode,
            amount=amount,
            blockFederalIncomeTax=blockFederalIncomeTax,
            blockLocalIncomeTax=blockLocalIncomeTax,
            blockStateIncomeTax=blockStateIncomeTax,
            calculationRule=calculationRule,
            displayInPayDataEntry=displayInPayDataEntry,
            excelInTotalHours=excelInTotalHours,
            flatHours=flatHours,
            includeInAccruals=includeInAccruals,
            includeInAllocations=includeInAllocations,
            includeFlsaAveragePayRate=includeFlsaAveragePayRate,
            includeInBenefitHours=includeInBenefitHours,
            includeInDeferredCompensation=includeInDeferredCompensation,
            includeInDeferredCompensationHours=includeInDeferredCompensationHours,
            includeInEarningAccumulation=includeInEarningAccumulation,
            includeInHoursAccumulation=includeInHoursAccumulation,
            includeInManualCheck=includeInManualCheck,
            includeInMiscellaneousEarning1=includeInMiscellaneousEarning1,
            includeInMiscellaneousEarning2=includeInMiscellaneousEarning2,
            includeInMiscellaneousEarning3=includeInMiscellaneousEarning3,
            includeInMiscellaneousEarning4=includeInMiscellaneousEarning4,
            includeInMiscellaneousEarning5=includeInMiscellaneousEarning5,
            includeInMiscellaneousEarning6=includeInMiscellaneousEarning6,
            includeInPensionAccumulation=includeInPensionAccumulation,
            includeInRetroPay=includeInRetroPay,
            includeInShiftDiffrential=includeInShiftDiffrential,
            isProductiveTime=isProductiveTime,
            isSupplimentalWages=isSupplimentalWages,
            monthlyPayPeriod1=monthlyPayPeriod1,
            monthlyPayPeriod2=monthlyPayPeriod2,
            monthlyPayPeriod3=monthlyPayPeriod3,
            monthlyPayPeriod4=monthlyPayPeriod4,
            monthlyPayPeriod5=monthlyPayPeriod5,
            notes=notes,
            reduceRegularDollars=reduceRegularDollars,
            reduceRegularHours=reduceRegularHours,
            reportCategory=reportCategory,
            scheduleSupplemental=scheduleSupplemental,
            taxCategory=taxCategory,
            countryCode=countryCode,
            useDeductionOffset=useDeductionOffset,
            includeInRegisteredPensionPlan=includeInRegisteredPensionPlan,
            includeInRegisteredRetirementSavingsPlan=includeInRegisteredRetirementSavingsPlan,
            includeInUnionDues=includeInUnionDues,
            includeInUnionDuesHours=includeInUnionDuesHours,
            taxCalculationRule=taxCalculationRule,
            exemptFromEarnedIncomeHours=exemptFromEarnedIncomeHours,
            includeInHealthCareHours=includeInHealthCareHours,
            verificationTypeCode=verificationTypeCode,
            verificationTypeDescription=verificationTypeDescription,
            _configuration=_configuration,
            **kwargs,
        )
