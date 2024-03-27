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


class OpenEnrollmentEmployeeDeductions(BaseModel):
    benefit_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='benefitAmount')

    benefit_amount_rate_or_percent: typing.Optional[typing.Union[int, float]] = Field(None, alias='benefitAmountRateOrPercent')

    benefit_option: typing.Optional[str] = Field(None, alias='benefitOption')

    add_coverage: typing.Optional[bool] = Field(None, alias='addCoverage')

    change_reason: typing.Optional[str] = Field(None, alias='changeReason')

    benefit_start_date: typing.Optional[datetime] = Field(None, alias='benefitStartDate')

    benefit_status: typing.Optional[str] = Field(None, alias='benefitStatus')

    benefit_status_date: typing.Optional[datetime] = Field(None, alias='benefitStatusDate')

    benefit_stop_date: typing.Optional[datetime] = Field(None, alias='benefitStopDate')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    custom_amount1: typing.Optional[typing.Union[int, float]] = Field(None, alias='customAmount1')

    custom_amount2: typing.Optional[typing.Union[int, float]] = Field(None, alias='customAmount2')

    custom_date: typing.Optional[datetime] = Field(None, alias='customDate')

    change_datetime: typing.Optional[datetime] = Field(None, alias='changeDatetime')

    create_datetime: typing.Optional[datetime] = Field(None, alias='createDatetime')

    deduction_code: typing.Optional[str] = Field(None, alias='deductionCode')

    deduction_type: typing.Optional[str] = Field(None, alias='deductionType')

    employee_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='employeeAmount')

    employee_calculation_rate_or_percent: typing.Optional[typing.Union[int, float]] = Field(None, alias='employeeCalculationRateOrPercent')

    employee_eligibility_date: typing.Optional[datetime] = Field(None, alias='employeeEligibilityDate')

    employee_goal_amt: typing.Optional[typing.Union[int, float]] = Field(None, alias='employeeGoalAmt')

    employee_goal_to_date_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='employeeGoalToDateAmount')

    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    employee_member_or_case_no: typing.Optional[str] = Field(None, alias='employeeMemberOrCaseNo')

    employee_year_to_date_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='employeeYearToDateAmount')

    evidenceof_insurability_date: typing.Optional[datetime] = Field(None, alias='evidenceofInsurabilityDate')

    need_evidence_of_insurability: typing.Optional[bool] = Field(None, alias='needEvidenceOfInsurability')

    evidenceof_insurability_desired_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='evidenceofInsurabilityDesiredAmount')

    employee_eligibility_desired_calculation_rate_or_percent: typing.Optional[int] = Field(None, alias='employeeEligibilityDesiredCalculationRateOrPercent')

    employer_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='employerAmount')

    employer_calculation_rate_or_percent: typing.Optional[typing.Union[int, float]] = Field(None, alias='employerCalculationRateOrPercent')

    employer_calculation_rule: typing.Optional[str] = Field(None, alias='employerCalculationRule')

    employer_year_to_date_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='employerYearToDateAmount')

    is_deduction_offset: typing.Optional[bool] = Field(None, alias='isDeductionOffset')

    medical_indicator: typing.Optional[bool] = Field(None, alias='medicalIndicator')

    deduction_notes: typing.Optional[str] = Field(None, alias='deductionNotes')

    primary_care_physician: typing.Optional[str] = Field(None, alias='primaryCarePhysician')

    primary_care_physician_id: typing.Optional[str] = Field(None, alias='primaryCarePhysicianId')

    deduction_start_date: typing.Optional[datetime] = Field(None, alias='deductionStartDate')

    deduction_stop_date: typing.Optional[datetime] = Field(None, alias='deductionStopDate')

    benefit_waive_reason: typing.Optional[str] = Field(None, alias='benefitWaiveReason')

    is_benefit_waived: typing.Optional[bool] = Field(None, alias='isBenefitWaived')

    oe_drop: typing.Optional[bool] = Field(None, alias='oeDrop')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
