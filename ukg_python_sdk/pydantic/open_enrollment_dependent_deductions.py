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


class OpenEnrollmentDependentDeductions(BaseModel):
    benefit_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='benefitAmount')

    change_reason: typing.Optional[str] = Field(None, alias='changeReason')

    relationship: typing.Optional[str] = Field(None, alias='relationship')

    benefit_start_date: typing.Optional[datetime] = Field(None, alias='benefitStartDate')

    benefit_status: typing.Optional[str] = Field(None, alias='benefitStatus')

    benefit_status_date: typing.Optional[datetime] = Field(None, alias='benefitStatusDate')

    benefit_stop_date: typing.Optional[datetime] = Field(None, alias='benefitStopDate')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    change_datetime: typing.Optional[datetime] = Field(None, alias='changeDatetime')

    contact_id: typing.Optional[str] = Field(None, alias='contactId')

    create_datetime: typing.Optional[datetime] = Field(None, alias='createDatetime')

    certificate_no: typing.Optional[str] = Field(None, alias='certificateNo')

    current_co_id: typing.Optional[str] = Field(None, alias='currentCoId')

    declined_by_carrier: typing.Optional[str] = Field(None, alias='declinedByCarrier')

    declined_by_carrier_date: typing.Optional[datetime] = Field(None, alias='declinedByCarrierDate')

    declined_by_carrier_reason: typing.Optional[str] = Field(None, alias='declinedByCarrierReason')

    deduction_code: typing.Optional[str] = Field(None, alias='deductionCode')

    deduction_type: typing.Optional[str] = Field(None, alias='deductionType')

    dep_b_plan_t_v_i_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='depBPlanTVID')

    employee_id: typing.Optional[str] = Field(None, alias='employeeId')

    evidenceof_insurability_date: typing.Optional[datetime] = Field(None, alias='evidenceofInsurabilityDate')

    need_evidence_of_insurability: typing.Optional[bool] = Field(None, alias='needEvidenceOfInsurability')

    employer_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='employerAmount')

    deduction_notes: typing.Optional[str] = Field(None, alias='deductionNotes')

    primary_care_physician: typing.Optional[str] = Field(None, alias='primaryCarePhysician')

    primary_care_physician_id: typing.Optional[str] = Field(None, alias='primaryCarePhysicianId')

    system_id: typing.Optional[str] = Field(None, alias='systemId')

    is_benefit_waived: typing.Optional[bool] = Field(None, alias='isBenefitWaived')

    oe_drop: typing.Optional[bool] = Field(None, alias='oeDrop')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
