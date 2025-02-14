# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class EarningsDto(BaseModel):
    earning_code: str = Field(alias='earningCode')

    long_description: str = Field(alias='longDescription')

    stub_description: str = Field(alias='stubDescription')

    time_clock_code: str = Field(alias='timeClockCode')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    block_federal_income_tax: typing.Optional[bool] = Field(None, alias='blockFederalIncomeTax')

    block_local_income_tax: typing.Optional[bool] = Field(None, alias='blockLocalIncomeTax')

    block_state_income_tax: typing.Optional[bool] = Field(None, alias='blockStateIncomeTax')

    calculation_rule: typing.Optional[str] = Field(None, alias='calculationRule')

    display_in_pay_data_entry: typing.Optional[bool] = Field(None, alias='displayInPayDataEntry')

    excel_in_total_hours: typing.Optional[bool] = Field(None, alias='excelInTotalHours')

    flat_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='flatHours')

    include_in_accruals: typing.Optional[str] = Field(None, alias='includeInAccruals')

    include_in_allocations: typing.Optional[bool] = Field(None, alias='includeInAllocations')

    include_flsa_average_pay_rate: typing.Optional[bool] = Field(None, alias='includeFlsaAveragePayRate')

    include_in_benefit_hours: typing.Optional[bool] = Field(None, alias='includeInBenefitHours')

    include_in_deferred_compensation: typing.Optional[bool] = Field(None, alias='includeInDeferredCompensation')

    include_in_deferred_compensation_hours: typing.Optional[bool] = Field(None, alias='includeInDeferredCompensationHours')

    include_in_earning_accumulation: typing.Optional[bool] = Field(None, alias='includeInEarningAccumulation')

    include_in_hours_accumulation: typing.Optional[bool] = Field(None, alias='includeInHoursAccumulation')

    include_in_manual_check: typing.Optional[bool] = Field(None, alias='includeInManualCheck')

    include_in_miscellaneous_earning1: typing.Optional[bool] = Field(None, alias='includeInMiscellaneousEarning1')

    include_in_miscellaneous_earning2: typing.Optional[bool] = Field(None, alias='includeInMiscellaneousEarning2')

    include_in_miscellaneous_earning3: typing.Optional[bool] = Field(None, alias='includeInMiscellaneousEarning3')

    include_in_miscellaneous_earning4: typing.Optional[bool] = Field(None, alias='includeInMiscellaneousEarning4')

    include_in_miscellaneous_earning5: typing.Optional[bool] = Field(None, alias='includeInMiscellaneousEarning5')

    include_in_miscellaneous_earning6: typing.Optional[bool] = Field(None, alias='includeInMiscellaneousEarning6')

    include_in_pension_accumulation: typing.Optional[bool] = Field(None, alias='includeInPensionAccumulation')

    include_in_retro_pay: typing.Optional[bool] = Field(None, alias='includeInRetroPay')

    include_in_shift_diffrential: typing.Optional[bool] = Field(None, alias='includeInShiftDiffrential')

    is_productive_time: typing.Optional[bool] = Field(None, alias='isProductiveTime')

    is_supplimental_wages: typing.Optional[bool] = Field(None, alias='isSupplimentalWages')

    monthly_pay_period1: typing.Optional[bool] = Field(None, alias='monthlyPayPeriod1')

    monthly_pay_period2: typing.Optional[bool] = Field(None, alias='monthlyPayPeriod2')

    monthly_pay_period3: typing.Optional[bool] = Field(None, alias='monthlyPayPeriod3')

    monthly_pay_period4: typing.Optional[bool] = Field(None, alias='monthlyPayPeriod4')

    monthly_pay_period5: typing.Optional[bool] = Field(None, alias='monthlyPayPeriod5')

    notes: typing.Optional[str] = Field(None, alias='notes')

    reduce_regular_dollars: typing.Optional[bool] = Field(None, alias='reduceRegularDollars')

    reduce_regular_hours: typing.Optional[bool] = Field(None, alias='reduceRegularHours')

    report_category: typing.Optional[str] = Field(None, alias='reportCategory')

    schedule_supplemental: typing.Optional[bool] = Field(None, alias='scheduleSupplemental')

    tax_category: typing.Optional[str] = Field(None, alias='taxCategory')

    country_code: typing.Optional[str] = Field(None, alias='countryCode')

    use_deduction_offset: typing.Optional[bool] = Field(None, alias='useDeductionOffset')

    include_in_registered_pension_plan: typing.Optional[bool] = Field(None, alias='includeInRegisteredPensionPlan')

    include_in_registered_retirement_savings_plan: typing.Optional[bool] = Field(None, alias='includeInRegisteredRetirementSavingsPlan')

    include_in_union_dues: typing.Optional[bool] = Field(None, alias='includeInUnionDues')

    include_in_union_dues_hours: typing.Optional[bool] = Field(None, alias='includeInUnionDuesHours')

    tax_calculation_rule: typing.Optional[str] = Field(None, alias='taxCalculationRule')

    exempt_from_earned_income_hours: typing.Optional[str] = Field(None, alias='exemptFromEarnedIncomeHours')

    include_in_health_care_hours: typing.Optional[bool] = Field(None, alias='includeInHealthCareHours')

    verification_type_code: typing.Optional[str] = Field(None, alias='verificationTypeCode')

    verification_type_description: typing.Optional[str] = Field(None, alias='verificationTypeDescription')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
