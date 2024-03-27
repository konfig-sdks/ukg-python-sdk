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


class EmpEmploymentDetails(BaseModel):
    company_i_d: typing.Optional[str] = Field(None, alias='companyID')

    company_code: typing.Optional[str] = Field(None, alias='companyCode')

    company_name: typing.Optional[str] = Field(None, alias='companyName')

    employee_i_d: typing.Optional[str] = Field(None, alias='employeeID')

    job_description: typing.Optional[str] = Field(None, alias='jobDescription')

    pay_group_description: typing.Optional[str] = Field(None, alias='payGroupDescription')

    primary_job_code: typing.Optional[str] = Field(None, alias='primaryJobCode')

    org_level1_code: typing.Optional[str] = Field(None, alias='orgLevel1Code')

    org_level2_code: typing.Optional[str] = Field(None, alias='orgLevel2Code')

    org_level3_code: typing.Optional[str] = Field(None, alias='orgLevel3Code')

    org_level4_code: typing.Optional[str] = Field(None, alias='orgLevel4Code')

    original_hire_date: typing.Optional[datetime] = Field(None, alias='originalHireDate')

    last_hire_date: typing.Optional[datetime] = Field(None, alias='lastHireDate')

    full_time_or_part_time_code: typing.Optional[str] = Field(None, alias='fullTimeOrPartTimeCode')

    primary_work_location_code: typing.Optional[str] = Field(None, alias='primaryWorkLocationCode')

    language_code: typing.Optional[str] = Field(None, alias='languageCode')

    primary_project_code: typing.Optional[str] = Field(None, alias='primaryProjectCode')

    work_phone_number: typing.Optional[str] = Field(None, alias='workPhoneNumber')

    work_phone_extension: typing.Optional[str] = Field(None, alias='workPhoneExtension')

    work_phone_country: typing.Optional[str] = Field(None, alias='workPhoneCountry')

    date_in_job: typing.Optional[datetime] = Field(None, alias='dateInJob')

    date_last_worked: typing.Optional[datetime] = Field(None, alias='dateLastWorked')

    date_of_benefit_seniority: typing.Optional[datetime] = Field(None, alias='dateOfBenefitSeniority')

    date_of_seniority: typing.Optional[datetime] = Field(None, alias='dateOfSeniority')

    deduction_group_code: typing.Optional[str] = Field(None, alias='deductionGroupCode')

    earning_group_code: typing.Optional[str] = Field(None, alias='earningGroupCode')

    employee_type_code: typing.Optional[str] = Field(None, alias='employeeTypeCode')

    employee_status_code: typing.Optional[str] = Field(None, alias='employeeStatusCode')

    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    job_change_reason_code: typing.Optional[str] = Field(None, alias='jobChangeReasonCode')

    job_title: typing.Optional[str] = Field(None, alias='jobTitle')

    leave_reason_code: typing.Optional[str] = Field(None, alias='leaveReasonCode')

    supervisor_i_d: typing.Optional[str] = Field(None, alias='supervisorID')

    supervisor_first_name: typing.Optional[str] = Field(None, alias='supervisorFirstName')

    supervisor_last_name: typing.Optional[str] = Field(None, alias='supervisorLastName')

    auto_allocate: typing.Optional[str] = Field(None, alias='autoAllocate')

    clock_code: typing.Optional[str] = Field(None, alias='clockCode')

    date_last_pay_date_paid: typing.Optional[datetime] = Field(None, alias='dateLastPayDatePaid')

    date_of_early_retirement: typing.Optional[datetime] = Field(None, alias='dateOfEarlyRetirement')

    date_of_local_union: typing.Optional[datetime] = Field(None, alias='dateOfLocalUnion')

    date_of_national_union: typing.Optional[datetime] = Field(None, alias='dateOfNationalUnion')

    date_of_retirement: typing.Optional[datetime] = Field(None, alias='dateOfRetirement')

    date_of_suspension: typing.Optional[datetime] = Field(None, alias='dateOfSuspension')

    date_of_termination: typing.Optional[datetime] = Field(None, alias='dateOfTermination')

    date_paid_thru: typing.Optional[datetime] = Field(None, alias='datePaidThru')

    status_start_date: typing.Optional[datetime] = Field(None, alias='statusStartDate')

    hire_source: typing.Optional[str] = Field(None, alias='hireSource')

    is_auto_allocated: typing.Optional[str] = Field(None, alias='isAutoAllocated')

    is_autopaid: typing.Optional[str] = Field(None, alias='isAutopaid')

    is_multiple_job: typing.Optional[str] = Field(None, alias='isMultipleJob')

    job_group_code: typing.Optional[str] = Field(None, alias='jobGroupCode')

    mailstop: typing.Optional[str] = Field(None, alias='mailstop')

    ok_to_rehire: typing.Optional[str] = Field(None, alias='okToRehire')

    pay_group: typing.Optional[str] = Field(None, alias='payGroup')

    pay_period: typing.Optional[str] = Field(None, alias='payPeriod')

    planned_leave_reason: typing.Optional[str] = Field(None, alias='plannedLeaveReason')

    position_code: typing.Optional[str] = Field(None, alias='positionCode')

    salary_or_hourly: typing.Optional[str] = Field(None, alias='salaryOrHourly')

    scheduled_annual_hrs: typing.Optional[typing.Union[int, float]] = Field(None, alias='scheduledAnnualHrs')

    scheduled_f_t_e: typing.Optional[typing.Union[int, float]] = Field(None, alias='scheduledFTE')

    scheduled_work_hrs: typing.Optional[typing.Union[int, float]] = Field(None, alias='scheduledWorkHrs')

    shift: typing.Optional[str] = Field(None, alias='shift')

    shift_group: typing.Optional[str] = Field(None, alias='shiftGroup')

    term_reason: typing.Optional[str] = Field(None, alias='termReason')

    termination_reason_description: typing.Optional[str] = Field(None, alias='terminationReasonDescription')

    term_type: typing.Optional[str] = Field(None, alias='termType')

    timeclock_i_d: typing.Optional[str] = Field(None, alias='timeclockID')

    union_local: typing.Optional[str] = Field(None, alias='unionLocal')

    union_national: typing.Optional[str] = Field(None, alias='unionNational')

    weekly_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='weeklyHours')

    date_time_created: typing.Optional[datetime] = Field(None, alias='dateTimeCreated')

    date_time_changed: typing.Optional[datetime] = Field(None, alias='dateTimeChanged')

    supervisor_employee_number: typing.Optional[str] = Field(None, alias='supervisorEmployeeNumber')

    supervisor_c_o_i_d: typing.Optional[str] = Field(None, alias='supervisorCOID')

    supervisor_company_code: typing.Optional[str] = Field(None, alias='supervisorCompanyCode')

    company_g_l_segment: typing.Optional[str] = Field(None, alias='companyGLSegment')

    location_g_l_segment: typing.Optional[str] = Field(None, alias='locationGLSegment')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
