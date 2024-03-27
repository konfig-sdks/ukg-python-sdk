<div align="center">

[![Visit Ukg](./header.png)](https://ukg.com)

# Ukg<a id="ukg"></a>

Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`ukg.activities.get_all`](#ukgactivitiesget_all)
  * [`ukg.assigned_holidays.get_all`](#ukgassigned_holidaysget_all)
  * [`ukg.audit_details.get_data`](#ukgaudit_detailsget_data)
  * [`ukg.business_rule_import_tool.business_rule_import_file_upload`](#ukgbusiness_rule_import_toolbusiness_rule_import_file_upload)
  * [`ukg.business_rule_import_tool.get_file_upload_status`](#ukgbusiness_rule_import_toolget_file_upload_status)
  * [`ukg.business_rule_import_tool.get_staging_status`](#ukgbusiness_rule_import_toolget_staging_status)
  * [`ukg.business_rule_import_tool.imports_business_rule_staging_data`](#ukgbusiness_rule_import_toolimports_business_rule_staging_data)
  * [`ukg.business_structure_status.list_employees_change_business_structure`](#ukgbusiness_structure_statuslist_employees_change_business_structure)
  * [`ukg.candidate_request.add_background_check`](#ukgcandidate_requestadd_background_check)
  * [`ukg.candidate_request.update_background_check`](#ukgcandidate_requestupdate_background_check)
  * [`ukg.changes_by_date.get_all_employee_changes_since_last_call`](#ukgchanges_by_dateget_all_employee_changes_since_last_call)
  * [`ukg.code_tables.create_code_tables`](#ukgcode_tablescreate_code_tables)
  * [`ukg.code_tables.get_info`](#ukgcode_tablesget_info)
  * [`ukg.company_details.get_company_details`](#ukgcompany_detailsget_company_details)
  * [`ukg.company_pay_statement.get_by_date_range`](#ukgcompany_pay_statementget_by_date_range)
  * [`ukg.company_pay_statement.get_pay_summaries`](#ukgcompany_pay_statementget_pay_summaries)
  * [`ukg.compensation_details.get_all_by_company`](#ukgcompensation_detailsget_all_by_company)
  * [`ukg.compensation_details.get_all_details`](#ukgcompensation_detailsget_all_details)
  * [`ukg.compensation_details.get_by_company_and_employee`](#ukgcompensation_detailsget_by_company_and_employee)
  * [`ukg.compensation_details.get_by_employee`](#ukgcompensation_detailsget_by_employee)
  * [`ukg.contact.get_personnel_contact_details`](#ukgcontactget_personnel_contact_details)
  * [`ukg.contact.get_personnel_details`](#ukgcontactget_personnel_details)
  * [`ukg.dependent_deductions.get`](#ukgdependent_deductionsget)
  * [`ukg.direct_deposit.list_direct_deposit_details_by_company`](#ukgdirect_depositlist_direct_deposit_details_by_company)
  * [`ukg.direct_deposit.list_employee_direct_deposit_details`](#ukgdirect_depositlist_employee_direct_deposit_details)
  * [`ukg.earnings.add_time_clock_data`](#ukgearningsadd_time_clock_data)
  * [`ukg.earnings.delete_earning`](#ukgearningsdelete_earning)
  * [`ukg.earnings.get_configurations_filtered_by_parameter`](#ukgearningsget_configurations_filtered_by_parameter)
  * [`ukg.earnings.get_status_details`](#ukgearningsget_status_details)
  * [`ukg.earnings.list_earnings_configurations`](#ukgearningslist_earnings_configurations)
  * [`ukg.earnings.specific_configuration_get`](#ukgearningsspecific_configuration_get)
  * [`ukg.earnings_history.get_ins_rate`](#ukgearnings_historyget_ins_rate)
  * [`ukg.emp_ded_ben_option_date.get`](#ukgemp_ded_ben_option_dateget)
  * [`ukg.emp_deductions.list`](#ukgemp_deductionslist)
  * [`ukg.emp_global_localization_element.get`](#ukgemp_global_localization_elementget)
  * [`ukg.emp_multiple_positions.get`](#ukgemp_multiple_positionsget)
  * [`ukg.employee_changes.get`](#ukgemployee_changesget)
  * [`ukg.employee_deduction_history_effective_date.get_by_deduction_code_and_field`](#ukgemployee_deduction_history_effective_dateget_by_deduction_code_and_field)
  * [`ukg.employee_demographic_details.get`](#ukgemployee_demographic_detailsget)
  * [`ukg.employee_id_lookup.by_company_ids`](#ukgemployee_id_lookupby_company_ids)
  * [`ukg.employee_jobs.get_all`](#ukgemployee_jobsget_all)
  * [`ukg.employee_security_user_details.get_details`](#ukgemployee_security_user_detailsget_details)
  * [`ukg.employee_cobra_details.get`](#ukgemployee_cobra_detailsget)
  * [`ukg.employee_contract.get`](#ukgemployee_contractget)
  * [`ukg.employee_education.get`](#ukgemployee_educationget)
  * [`ukg.employee_employment_details.get_details`](#ukgemployee_employment_detailsget_details)
  * [`ukg.employee_extended_elements.get`](#ukgemployee_extended_elementsget)
  * [`ukg.employee_global_bank.get`](#ukgemployee_global_bankget)
  * [`ukg.employee_job_history_detail.get`](#ukgemployee_job_history_detailget)
  * [`ukg.employee_job_history_detail.get_single_record`](#ukgemployee_job_history_detailget_single_record)
  * [`ukg.employee_multi_phone_numbers.get`](#ukgemployee_multi_phone_numbersget)
  * [`ukg.employee_multiple_jobs_opp.list_details`](#ukgemployee_multiple_jobs_opplist_details)
  * [`ukg.employee_pay_deduction_element.get`](#ukgemployee_pay_deduction_elementget)
  * [`ukg.employee_pay_statement.get_by_date_range`](#ukgemployee_pay_statementget_by_date_range)
  * [`ukg.employee_pay_statement.get_by_pay_identifier`](#ukgemployee_pay_statementget_by_pay_identifier)
  * [`ukg.employee_pay_statement.get_last_pay_statement`](#ukgemployee_pay_statementget_last_pay_statement)
  * [`ukg.employee_supervisor_details.get`](#ukgemployee_supervisor_detailsget)
  * [`ukg.employees.get_all`](#ukgemployeesget_all)
  * [`ukg.employment_details.get_by_company_id_and_employee_id`](#ukgemployment_detailsget_by_company_id_and_employee_id)
  * [`ukg.employment_details.get_details`](#ukgemployment_detailsget_details)
  * [`ukg.employment_details.list_by_company`](#ukgemployment_detailslist_by_company)
  * [`ukg.general_ledger_run_details_v2.get`](#ukggeneral_ledger_run_details_v2get)
  * [`ukg.general_ledger_run_details_v2.get_by_run_id`](#ukggeneral_ledger_run_details_v2get_by_run_id)
  * [`ukg.get_all_pto_plans.information`](#ukgget_all_pto_plansinformation)
  * [`ukg.get_job_postings.details`](#ukgget_job_postingsdetails)
  * [`ukg.get_specific_employees_pto_plans.info`](#ukgget_specific_employees_pto_plansinfo)
  * [`ukg.get_specific_pto_plan.info`](#ukgget_specific_pto_planinfo)
  * [`ukg.hour_types.obtain_all`](#ukghour_typesobtain_all)
  * [`ukg.import_tool.get_status`](#ukgimport_toolget_status)
  * [`ukg.import_tool.post`](#ukgimport_toolpost)
  * [`ukg.ins_rate.get_ins_rate`](#ukgins_rateget_ins_rate)
  * [`ukg.integration_audit_configuration.get_data`](#ukgintegration_audit_configurationget_data)
  * [`ukg.international_employee.get`](#ukginternational_employeeget)
  * [`ukg.international_employee.get_details`](#ukginternational_employeeget_details)
  * [`ukg.job_group.get`](#ukgjob_groupget)
  * [`ukg.kronos_employee_profiles.get_list`](#ukgkronos_employee_profilesget_list)
  * [`ukg.kronos_employee_status.get`](#ukgkronos_employee_statusget)
  * [`ukg.national_document.get`](#ukgnational_documentget)
  * [`ukg.new_hires.create_single_new_hire`](#ukgnew_hirescreate_single_new_hire)
  * [`ukg.new_hires.get_by_id`](#ukgnew_hiresget_by_id)
  * [`ukg.open_enrollment_dependent_deductions.get_data`](#ukgopen_enrollment_dependent_deductionsget_data)
  * [`ukg.open_enrollment_employee_deductions.get_audit_details`](#ukgopen_enrollment_employee_deductionsget_audit_details)
  * [`ukg.option_rate.get_data`](#ukgoption_rateget_data)
  * [`ukg.order_requests.background_check_details`](#ukgorder_requestsbackground_check_details)
  * [`ukg.organization_reporting_category.get`](#ukgorganization_reporting_categoryget)
  * [`ukg.pto_plan_patch.one_pto_plan`](#ukgpto_plan_patchone_pto_plan)
  * [`ukg.pto_plan_post.ultipro_record`](#ukgpto_plan_postultipro_record)
  * [`ukg.pay_group_pay_period.get_pay_group_pay_period`](#ukgpay_group_pay_periodget_pay_group_pay_period)
  * [`ukg.pay_register.get`](#ukgpay_registerget)
  * [`ukg.payroll_deductions_history.get`](#ukgpayroll_deductions_historyget)
  * [`ukg.person_details.get_all_details`](#ukgperson_detailsget_all_details)
  * [`ukg.person_details.get_single_company_details`](#ukgperson_detailsget_single_company_details)
  * [`ukg.person_details.get_single_detail_record`](#ukgperson_detailsget_single_detail_record)
  * [`ukg.person_details.get_single_record`](#ukgperson_detailsget_single_record)
  * [`ukg.platform_configuration_custom_fields_schema.get_fields_schema`](#ukgplatform_configuration_custom_fields_schemaget_fields_schema)
  * [`ukg.position_report.get`](#ukgposition_reportget)
  * [`ukg.positions.list_filtered`](#ukgpositionslist_filtered)
  * [`ukg.post_new_token_request.obtain_o_auth_token`](#ukgpost_new_token_requestobtain_o_auth_token)
  * [`ukg.roles_get.security_roles`](#ukgroles_getsecurity_roles)
  * [`ukg.schedule_details.publish_details`](#ukgschedule_detailspublish_details)
  * [`ukg.shift_code.get_data`](#ukgshift_codeget_data)
  * [`ukg.single_organization_level.get`](#ukgsingle_organization_levelget)
  * [`ukg.single_organization_level.update_org_level`](#ukgsingle_organization_levelupdate_org_level)
  * [`ukg.single_organization_level.update_properties`](#ukgsingle_organization_levelupdate_properties)
  * [`ukg.tax_groups.get_all_details`](#ukgtax_groupsget_all_details)
  * [`ukg.teams.get_all`](#ukgteamsget_all)
  * [`ukg.time_codes.get_all`](#ukgtime_codesget_all)
  * [`ukg.time_off_requests.get_all`](#ukgtime_off_requestsget_all)
  * [`ukg.uta_employee.get_by_co_id_and_ee_id`](#ukguta_employeeget_by_co_id_and_ee_id)
  * [`ukg.user_preferences.get_user_preferences_details`](#ukguser_preferencesget_user_preferences_details)
  * [`ukg.user_profile_details.get_all_details`](#ukguser_profile_detailsget_all_details)
  * [`ukg.user_defined_fields.get`](#ukguser_defined_fieldsget)
  * [`ukg.user_defined_fields.get_single_company`](#ukguser_defined_fieldsget_single_company)
  * [`ukg.user_defined_fields.get_single_employee`](#ukguser_defined_fieldsget_single_employee)
  * [`ukg.user_details.get_user_details`](#ukguser_detailsget_user_details)
  * [`ukg.view_or_create_organization_levels.create_org_level_config`](#ukgview_or_create_organization_levelscreate_org_level_config)
  * [`ukg.view_or_create_organization_levels.get_all_org_levels`](#ukgview_or_create_organization_levelsget_all_org_levels)
  * [`ukg.allergy.configurations_get`](#ukgallergyconfigurations_get)
  * [`ukg.allergy.create_configuration`](#ukgallergycreate_configuration)
  * [`ukg.allergy.update_single_configuration`](#ukgallergyupdate_single_configuration)
  * [`ukg.award_type.create_configuration`](#ukgaward_typecreate_configuration)
  * [`ukg.award_type.get_all_configurations`](#ukgaward_typeget_all_configurations)
  * [`ukg.award_type.update_configuration`](#ukgaward_typeupdate_configuration)
  * [`ukg.career_provider.create_configuration_ukg_pro`](#ukgcareer_providercreate_configuration_ukg_pro)
  * [`ukg.career_provider.get_configurations`](#ukgcareer_providerget_configurations)
  * [`ukg.career_provider.update_configuration`](#ukgcareer_providerupdate_configuration)
  * [`ukg.child_support_type.create_configuration_ukg_pro`](#ukgchild_support_typecreate_configuration_ukg_pro)
  * [`ukg.child_support_type.get_configurations`](#ukgchild_support_typeget_configurations)
  * [`ukg.child_support_type.update_configuration`](#ukgchild_support_typeupdate_configuration)
  * [`ukg.cobra_status.create_configuration`](#ukgcobra_statuscreate_configuration)
  * [`ukg.cobra_status.get_configurations`](#ukgcobra_statusget_configurations)
  * [`ukg.cobra_status.update_single_configuration`](#ukgcobra_statusupdate_single_configuration)
  * [`ukg.company_property.create_configuration_ukg_pro`](#ukgcompany_propertycreate_configuration_ukg_pro)
  * [`ukg.company_property.get_configurations`](#ukgcompany_propertyget_configurations)
  * [`ukg.company_property.update_configuration`](#ukgcompany_propertyupdate_configuration)
  * [`ukg.course_category.create_configuration_ukg_pro`](#ukgcourse_categorycreate_configuration_ukg_pro)
  * [`ukg.course_category.get_all_configurations`](#ukgcourse_categoryget_all_configurations)
  * [`ukg.course_category.update_configuration`](#ukgcourse_categoryupdate_configuration)
  * [`ukg.course_delivery_met.create_configuration_ukg_pro`](#ukgcourse_delivery_metcreate_configuration_ukg_pro)
  * [`ukg.course_delivery_met.get_configurations`](#ukgcourse_delivery_metget_configurations)
  * [`ukg.course_delivery_met.update_configuration`](#ukgcourse_delivery_metupdate_configuration)
  * [`ukg.course_sub_category.create_configuration_ukg_pro`](#ukgcourse_sub_categorycreate_configuration_ukg_pro)
  * [`ukg.course_sub_category.get_configurations`](#ukgcourse_sub_categoryget_configurations)
  * [`ukg.course_sub_category.update_configuration`](#ukgcourse_sub_categoryupdate_configuration)
  * [`ukg.disability.create_configuration_ukg_pro`](#ukgdisabilitycreate_configuration_ukg_pro)
  * [`ukg.disability.get_configurations`](#ukgdisabilityget_configurations)
  * [`ukg.disability.update_configuration`](#ukgdisabilityupdate_configuration)
  * [`ukg.employee_type.create_configuration_ukg_pro`](#ukgemployee_typecreate_configuration_ukg_pro)
  * [`ukg.employee_type.get_configurations`](#ukgemployee_typeget_configurations)
  * [`ukg.employee_type.update_configuration`](#ukgemployee_typeupdate_configuration)
  * [`ukg.job_family.create_configuration`](#ukgjob_familycreate_configuration)
  * [`ukg.job_family.get_all_configurations`](#ukgjob_familyget_all_configurations)
  * [`ukg.job_family.update_configuration`](#ukgjob_familyupdate_configuration)
  * [`ukg.jobs.get_all_configurations`](#ukgjobsget_all_configurations)
  * [`ukg.jobs.get_configuration`](#ukgjobsget_configuration)
  * [`ukg.license_type.create_configuration`](#ukglicense_typecreate_configuration)
  * [`ukg.license_type.get_configurations`](#ukglicense_typeget_configurations)
  * [`ukg.license_type.update_configuration`](#ukglicense_typeupdate_configuration)
  * [`ukg.loan_type.create_configuration`](#ukgloan_typecreate_configuration)
  * [`ukg.loan_type.get_configurations`](#ukgloan_typeget_configurations)
  * [`ukg.loan_type.update_configuration`](#ukgloan_typeupdate_configuration)
  * [`ukg.locations.get_configuration`](#ukglocationsget_configuration)
  * [`ukg.locations.get_configurations`](#ukglocationsget_configurations)
  * [`ukg.marital_status.create_configuration_ukg_pro`](#ukgmarital_statuscreate_configuration_ukg_pro)
  * [`ukg.marital_status.get_configurations`](#ukgmarital_statusget_configurations)
  * [`ukg.marital_status.update_configuration`](#ukgmarital_statusupdate_configuration)
  * [`ukg.military_branches.configure_ukg_pro`](#ukgmilitary_branchesconfigure_ukg_pro)
  * [`ukg.military_branches.get_all_configurations`](#ukgmilitary_branchesget_all_configurations)
  * [`ukg.military_branches.update_configuration`](#ukgmilitary_branchesupdate_configuration)
  * [`ukg.military_era.create_configuration_ukg_pro`](#ukgmilitary_eracreate_configuration_ukg_pro)
  * [`ukg.military_era.get_configurations`](#ukgmilitary_eraget_configurations)
  * [`ukg.military_era.update_configuration`](#ukgmilitary_eraupdate_configuration)
  * [`ukg.name_prefix.configure_name_prefix`](#ukgname_prefixconfigure_name_prefix)
  * [`ukg.name_prefix.get_configurations`](#ukgname_prefixget_configurations)
  * [`ukg.name_prefix.update_configuration`](#ukgname_prefixupdate_configuration)
  * [`ukg.other_phone_types.create_configuration_ukg_pro`](#ukgother_phone_typescreate_configuration_ukg_pro)
  * [`ukg.other_phone_types.get_configurations`](#ukgother_phone_typesget_configurations)
  * [`ukg.other_phone_types.update_configuration`](#ukgother_phone_typesupdate_configuration)
  * [`ukg.project.create_configuration`](#ukgprojectcreate_configuration)
  * [`ukg.project.get_all_configurations`](#ukgprojectget_all_configurations)
  * [`ukg.project.update_configuration`](#ukgprojectupdate_configuration)
  * [`ukg.school.create_configuration`](#ukgschoolcreate_configuration)
  * [`ukg.school.get_configurations`](#ukgschoolget_configurations)
  * [`ukg.school.update_configuration`](#ukgschoolupdate_configuration)
  * [`ukg.skill_proficiency_level.create_configuration_ukg_pro`](#ukgskill_proficiency_levelcreate_configuration_ukg_pro)
  * [`ukg.skill_proficiency_level.get_all_configurations`](#ukgskill_proficiency_levelget_all_configurations)
  * [`ukg.skill_proficiency_level.update_configuration`](#ukgskill_proficiency_levelupdate_configuration)
  * [`ukg.skills.create_configuration`](#ukgskillscreate_configuration)
  * [`ukg.skills.get_configurations`](#ukgskillsget_configurations)
  * [`ukg.skills.update_configuration`](#ukgskillsupdate_configuration)
  * [`ukg.term_type.create_configuration`](#ukgterm_typecreate_configuration)
  * [`ukg.term_type.get_configurations`](#ukgterm_typeget_configurations)
  * [`ukg.term_type.update_configuration`](#ukgterm_typeupdate_configuration)
  * [`ukg.time.add_time_entries`](#ukgtimeadd_time_entries)
  * [`ukg.time.get_pending_transactions`](#ukgtimeget_pending_transactions)
  * [`ukg.time.get_processed_transactions`](#ukgtimeget_processed_transactions)
  * [`ukg.time.get_work_summaries`](#ukgtimeget_work_summaries)
  * [`ukg.time.get_work_summary_by_id`](#ukgtimeget_work_summary_by_id)
  * [`ukg.v1_platform_configuration_custom_fields_data.get_fields_data`](#ukgv1_platform_configuration_custom_fields_dataget_fields_data)
  * [`ukg.v2_platform_configuration_custom_fields_data.get_fields_data`](#ukgv2_platform_configuration_custom_fields_dataget_fields_data)
  * [`ukg.waive_reason.create_configuration_ukg_pro`](#ukgwaive_reasoncreate_configuration_ukg_pro)
  * [`ukg.waive_reason.get_configurations`](#ukgwaive_reasonget_configurations)
  * [`ukg.waive_reason.update_single_configuration`](#ukgwaive_reasonupdate_single_configuration)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=UKG&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from ukg_python_sdk import Ukg, ApiException

ukg = Ukg(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Obtains all activities.
    get_all_response = ukg.activities.get_all()
    print(get_all_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi.get_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from ukg_python_sdk import Ukg, ApiException

ukg = Ukg(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Obtains all activities.
        get_all_response = await ukg.activities.aget_all()
        print(get_all_response)
    except ApiException as e:
        print("Exception when calling ActivitiesApi.get_all: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from ukg_python_sdk import Ukg, ApiException

ukg = Ukg(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Obtains all activities.
    get_all_response = ukg.activities.raw.get_all()
    pprint(get_all_response.body)
    pprint(get_all_response.body["entities"])
    pprint(get_all_response.body["index"])
    pprint(get_all_response.body["requested_count"])
    pprint(get_all_response.headers)
    pprint(get_all_response.status)
    pprint(get_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ActivitiesApi.get_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `ukg.activities.get_all`<a id="ukgactivitiesget_all"></a>

Obtains all activities.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = ukg.activities.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoActivityDto`](./ukg_python_sdk/pydantic/result_dto_activity_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/activities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.assigned_holidays.get_all`<a id="ukgassigned_holidaysget_all"></a>

Obtains all assigned holidays for a given employee.  Employee can be specified by their emp_name or emp_id.  At least one parameter must be specified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = ukg.assigned_holidays.get_all(
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    emp_name="string_example",
    emp_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `datetime`<a id="_from-datetime"></a>

Start range for holidays

##### to: `datetime`<a id="to-datetime"></a>

End range for holidays

##### emp_name: `str`<a id="emp_name-str"></a>

##### emp_id: `int`<a id="emp_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoHolidayDto`](./ukg_python_sdk/pydantic/result_dto_holiday_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/assigned_holidays` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.audit_details.get_data`<a id="ukgaudit_detailsget_data"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have \"View\" role for the \"Personnel Integration\" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}) .

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_response = ukg.audit_details.get_data(
    start_date_time="1970-01-01T00:00:00.00Z",
    end_date_time="1970-01-01T00:00:00.00Z",
    table_name="tableName_example",
    field_name="fieldName_example",
    action="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date_time: `datetime`<a id="start_date_time-datetime"></a>

##### end_date_time: `datetime`<a id="end_date_time-datetime"></a>

##### table_name: `str`<a id="table_name-str"></a>

##### field_name: `str`<a id="field_name-str"></a>

##### action: `str`<a id="action-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AuditDetailsGetDataResponse`](./ukg_python_sdk/pydantic/audit_details_get_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/audit-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.business_rule_import_tool.business_rule_import_file_upload`<a id="ukgbusiness_rule_import_toolbusiness_rule_import_file_upload"></a>

Takes an XML transaction and feeds it into the Business Rule Import Tool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
business_rule_import_file_upload_response = ukg.business_rule_import_tool.business_rule_import_file_upload(
    transaction="string_example",
    unique_file_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction: `str`<a id="transaction-str"></a>

The XML Serialized transaction

##### unique_file_name: `str`<a id="unique_file_name-str"></a>

An optionally provided unique file name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessRuleImportRequest`](./ukg_python_sdk/type/business_rule_import_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/businessruleimport-tool/fileupload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.business_rule_import_tool.get_file_upload_status`<a id="ukgbusiness_rule_import_toolget_file_upload_status"></a>

Retrieves the status of an Business Rule Import Tool transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_upload_status_response = ukg.business_rule_import_tool.get_file_upload_status(
    file_id="fileId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`FileStatusModel`](./ukg_python_sdk/pydantic/file_status_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/businessruleimport-tool/filestatus/{fileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.business_rule_import_tool.get_staging_status`<a id="ukgbusiness_rule_import_toolget_staging_status"></a>

Retrieves the status of an Business Rule Import Tool transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staging_status_response = ukg.business_rule_import_tool.get_staging_status(
    staging_id="stagingId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### staging_id: `str`<a id="staging_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessRuleImportFileStagingStatus`](./ukg_python_sdk/pydantic/business_rule_import_file_staging_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/businessruleimport-tool/transactionstatus/{stagingId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.business_rule_import_tool.imports_business_rule_staging_data`<a id="ukgbusiness_rule_import_toolimports_business_rule_staging_data"></a>

Takes an XML transaction and feeds it into the Business Rule Import Tool (Staging)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
imports_business_rule_staging_data_response = ukg.business_rule_import_tool.imports_business_rule_staging_data(
    transaction="string_example",
    unique_file_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction: `str`<a id="transaction-str"></a>

The XML Serialized transaction

##### unique_file_name: `str`<a id="unique_file_name-str"></a>

An optionally provided unique file name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessRuleImportRequest`](./ukg_python_sdk/type/business_rule_import_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessRuleImportFileStaging`](./ukg_python_sdk/pydantic/business_rule_import_file_staging.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/businessruleimport-tool/transaction` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.business_structure_status.list_employees_change_business_structure`<a id="ukgbusiness_structure_statuslist_employees_change_business_structure"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}) .


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employees_change_business_structure_response = ukg.business_structure_status.list_employees_change_business_structure(
    modified_after_date_time="1970-01-01T00:00:00.00Z",
    company_id="GqWzyBAw2ZuufUOHOEhA8I",
    effective_date="1970-01-01T00:00:00.00Z",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### modified_after_date_time: `datetime`<a id="modified_after_date_time-datetime"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessStructureStatusListEmployeesChangeBusinessStructureResponse`](./ukg_python_sdk/pydantic/business_structure_status_list_employees_change_business_structure_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/integration/kronos/business-structure-status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.candidate_request.add_background_check`<a id="ukgcandidate_requestadd_background_check"></a>

Add Background Check to Candidate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_background_check_response = ukg.candidate_request.add_background_check(
    author={
    },
    application={
    },
    status="string_example",
    order_number="string_example",
    packages={
        "id": "id_example",
        "name": "name_example",
    },
    candidate_id="candidate-id_example",
    tenant_alias="tenant-alias_example",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### author: [`BackgroundChecksAuthor`](./ukg_python_sdk/type/background_checks_author.py)<a id="author-backgroundchecksauthorukg_python_sdktypebackground_checks_authorpy"></a>


##### application: [`BackgroundChecksApplication`](./ukg_python_sdk/type/background_checks_application.py)<a id="application-backgroundchecksapplicationukg_python_sdktypebackground_checks_applicationpy"></a>


##### status: `str`<a id="status-str"></a>

The status of the background check order.

##### order_number: `str`<a id="order_number-str"></a>

Thebackground check order number. Maximum of 100 characters.

##### packages: [`BackgroundChecksPackages`](./ukg_python_sdk/type/background_checks_packages.py)<a id="packages-backgroundcheckspackagesukg_python_sdktypebackground_checks_packagespy"></a>


##### candidate_id: `str`<a id="candidate_id-str"></a>

##### tenant_alias: `str`<a id="tenant_alias-str"></a>

##### links: List[`Links`]<a id="links-listlinks"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BackgroundChecks`](./ukg_python_sdk/type/background_checks.py)
New background check to be added

#### 🔄 Return<a id="🔄-return"></a>

[`BackgroundChecks`](./ukg_python_sdk/pydantic/background_checks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{tenant-alias}/api/candidates/{candidate-id}/background-checks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.candidate_request.update_background_check`<a id="ukgcandidate_requestupdate_background_check"></a>

Update Candidate Background Check

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_background_check_response = ukg.candidate_request.update_background_check(
    author={
    },
    application={
    },
    status="string_example",
    order_number="string_example",
    packages={
        "id": "id_example",
        "name": "name_example",
    },
    candidate_id="candidate-id_example",
    background_check_id="background-check-id_example",
    tenant_alias="tenant-alias_example",
    links=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### author: [`BackgroundChecksAuthor`](./ukg_python_sdk/type/background_checks_author.py)<a id="author-backgroundchecksauthorukg_python_sdktypebackground_checks_authorpy"></a>


##### application: [`BackgroundChecksApplication`](./ukg_python_sdk/type/background_checks_application.py)<a id="application-backgroundchecksapplicationukg_python_sdktypebackground_checks_applicationpy"></a>


##### status: `str`<a id="status-str"></a>

The status of the background check order.

##### order_number: `str`<a id="order_number-str"></a>

Thebackground check order number. Maximum of 100 characters.

##### packages: [`BackgroundChecksPackages`](./ukg_python_sdk/type/background_checks_packages.py)<a id="packages-backgroundcheckspackagesukg_python_sdktypebackground_checks_packagespy"></a>


##### candidate_id: `str`<a id="candidate_id-str"></a>

##### background_check_id: `str`<a id="background_check_id-str"></a>

##### tenant_alias: `str`<a id="tenant_alias-str"></a>

##### links: List[`Links`]<a id="links-listlinks"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BackgroundChecks`](./ukg_python_sdk/type/background_checks.py)
Background check status to be updated

#### 🔄 Return<a id="🔄-return"></a>

[`BackgroundChecks`](./ukg_python_sdk/pydantic/background_checks.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{tenant-alias}/api/candidates/{candidate-id}/background-checks/{background-check-id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.changes_by_date.get_all_employee_changes_since_last_call`<a id="ukgchanges_by_dateget_all_employee_changes_since_last_call"></a>

Gets all of the employee information since the last API call (3 hour minimum). A time span can be defined by the query parameters, but to get near real time updates on when the employee has changed, you should call this service 8 times per day and no more frequent than three hours between calls. It should also be understood that you must compare the results for an employee with the results from a previous call to see what property or properties have changed. Permissions - Ultipro service account must have "View" role for the EmployeeExport Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_employee_changes_since_last_call_response = ukg.changes_by_date.get_all_employee_changes_since_last_call(
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    page=3.14,
    per_page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

Used to lookup employee changes within time span

##### end_date: `datetime`<a id="end_date-datetime"></a>

Used to lookup employee changes within time span

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

Pagination, which page you want to see

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

Pagination, how many records per page you want to see

#### 🔄 Return<a id="🔄-return"></a>

[`ChangesByDateGetAllEmployeeChangesSinceLastCallResponse`](./ukg_python_sdk/pydantic/changes_by_date_get_all_employee_changes_since_last_call_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-changes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.code_tables.create_code_tables`<a id="ukgcode_tablescreate_code_tables"></a>

Creates a new UKG Pro Code table configuration, Array of objects is permitted for multi-records support. Permissions - UKG Pro service account must have "Add" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}). There is a white list of code tables that we allow to be written, only these codes can be created: Allergy, Awardtype, Careerprovider, Childsupporttype, Cobrastatus, Coursecategory, Coursedeliverymet, Coursesubcategory, Disability, Educlevel, Educmajor, Emptype, Jobfamily, Licensetype, Loantype, Maritalstatus, Military, Militaryera, Otherphone, Prefix, Proficiency, Project, Property, School, Skills, Suffix, Termtype, Wellness.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_code_tables_response = ukg.code_tables.create_code_tables(
    body=[
        {
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeTablesCreateCodeTablesRequest`](./ukg_python_sdk/type/code_tables_create_code_tables_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CodeTablesCreateCodeTablesResponse`](./ukg_python_sdk/pydantic/code_tables_create_code_tables_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/code-tables` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.code_tables.get_info`<a id="ukgcode_tablesget_info"></a>

UKG Pro codes table lookup, will contain list of all tables with HATEOAS links to make a subsequent call to get all the codes for that table. If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = ukg.code_tables.get_info()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CodeTablesGetInfoResponse`](./ukg_python_sdk/pydantic/code_tables_get_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/code-tables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.company_details.get_company_details`<a id="ukgcompany_detailsget_company_details"></a>

Get all master company and component company details. If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_company_details_response = ukg.company_details.get_company_details(
    company_id="string_example",
    master_company_id="string_example",
    company_code="string_example",
    is_master_company="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

5 character value represents a UKG Pro CompanyID

##### master_company_id: `str`<a id="master_company_id-str"></a>

5 character value represents a UKG Pro Master CompanyID

##### company_code: `str`<a id="company_code-str"></a>

5 character value represents a UKG Pro Company Code

##### is_master_company: `str`<a id="is_master_company-str"></a>

true/false values represent if this company is a UKG Pro Master Company

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyDetailsGetCompanyDetailsResponse`](./ukg_python_sdk/pydantic/company_details_get_company_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/company-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.company_pay_statement.get_by_date_range`<a id="ukgcompany_pay_statementget_by_date_range"></a>

This method returns zero or more full pay statement documents for a given start date and end date. You may also pass in a PayGroup or CompanyIdentifer to further filter the list of pay summaries returned. <br />If no pagination parameters specified, the default is applied. Permissions - UKG Pro service account must have "View" role for the "Employee Pay Statements" Web Service. Headers - US-Customer-Api-Key, US-Client-id, Authorization ({username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_date_range_response = ukg.company_pay_statement.get_by_date_range(
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    company_id="string_example",
    pay_group="string_example",
    page=1,
    per_page=1,
    pages_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### pages_count: `int`<a id="pages_count-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyPayStatementFilter`](./ukg_python_sdk/type/company_pay_statement_filter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyPayStatementGetByDateRangeResponse`](./ukg_python_sdk/pydantic/company_pay_statement_get_by_date_range_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/companies/pay-statements` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.company_pay_statement.get_pay_summaries`<a id="ukgcompany_pay_statementget_pay_summaries"></a>

This method returns zero or more pay statement summaries for a given start date and end date. The pay summary information gives you a quick view of the total earnings, deductions and taxes. You may also pass in a PayGroup or CompanyIdentifer to further filter the list of pay summaries returned. <br />If no pagination parameters specified, the default is applied. Permissions - UKG Pro service account must have "View" role for the "Employee Pay Statements" Web Service. Headers - US-Customer-Api-Key, US-Client-id, Authorization ({username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_summaries_response = ukg.company_pay_statement.get_pay_summaries(
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    company_id="string_example",
    pay_group="string_example",
    page=1,
    per_page=1,
    pages_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### pages_count: `int`<a id="pages_count-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyPayStatementFilter`](./ukg_python_sdk/type/company_pay_statement_filter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CompanyPayStatementGetPaySummariesResponse`](./ukg_python_sdk/pydantic/company_pay_statement_get_pay_summaries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/companies/pay-statements-summary` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.compensation_details.get_all_by_company`<a id="ukgcompensation_detailsget_all_by_company"></a>

Get all compensation details by company. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Employee Compensation Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /companies/{companyId}/compensation-details?dateInJob=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /companies/{companyId}/compensation-details?dateInJob=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /companies/{companyId}/compensation-details?dateInJob=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /companies/{companyId}/compensation-details?dateInJob={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_by_company_response = ukg.compensation_details.get_all_by_company(
    company_id="companyId_example",
    company_id2="Cu2LC4aWwWL9Y864DZtaGR",
    employee_id="[q*RgcCecSDVGW8iZx9kSj",
    primary_job_code="Cu2LC4aWwWL9Y864DZtaGR",
    job_group_code="Cu2LC4aWwWL9Y864DZtaGR",
    job_title="Cu2LC4aWwWL9Y864DZtaGR",
    pay_group_code="Cu2LC4aWwWL9Y864DZtaGR",
    full_time_or_part_time_code="EiOTgswWMEJTcMoSLlNYUL",
    salary_or_hourly_code="EiOTgswWMEJTcMoSLlNYUL",
    primary_shift_code="EiOTgswWMEJTcMoSLlNYUL",
    primary_shift_group_code="EiOTgswWMEJTcMoSLlNYUL",
    date_in_job="string_example",
    date_last_paid="string_example",
    date_paid_thru="string_example",
    is_auto_allocated="EiOTgswWMEJTcMoSLlNYUL",
    is_auto_paid="EiOTgswWMEJTcMoSLlNYUL",
    is_seasonal_worker="EiOTgswWMEJTcMoSLlNYUL",
    is_highly_compensated="EiOTgswWMEJTcMoSLlNYUL",
    is_multiple_job="EiOTgswWMEJTcMoSLlNYUL",
    performance_review_rating="EiOTgswWMEJTcMoSLlNYUL",
    performance_review_type="EiOTgswWMEJTcMoSLlNYUL",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### company_id2: `str`<a id="company_id2-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### primary_job_code: `str`<a id="primary_job_code-str"></a>

##### job_group_code: `str`<a id="job_group_code-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### pay_group_code: `str`<a id="pay_group_code-str"></a>

##### full_time_or_part_time_code: `str`<a id="full_time_or_part_time_code-str"></a>

##### salary_or_hourly_code: `str`<a id="salary_or_hourly_code-str"></a>

##### primary_shift_code: `str`<a id="primary_shift_code-str"></a>

##### primary_shift_group_code: `str`<a id="primary_shift_group_code-str"></a>

##### date_in_job: `str`<a id="date_in_job-str"></a>

Used to find date in job less than, greater than, equal to, or between passed date(s)

##### date_last_paid: `str`<a id="date_last_paid-str"></a>

Used to find date last paid less than, greater than, equal to, or between passed date(s)

##### date_paid_thru: `str`<a id="date_paid_thru-str"></a>

Used to find date paid through less than, greater than, equal to, or between passed date(s)

##### is_auto_allocated: `str`<a id="is_auto_allocated-str"></a>

##### is_auto_paid: `str`<a id="is_auto_paid-str"></a>

##### is_seasonal_worker: `str`<a id="is_seasonal_worker-str"></a>

##### is_highly_compensated: `str`<a id="is_highly_compensated-str"></a>

##### is_multiple_job: `str`<a id="is_multiple_job-str"></a>

##### performance_review_rating: `str`<a id="performance_review_rating-str"></a>

##### performance_review_type: `str`<a id="performance_review_type-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationDetailsGetAllByCompanyResponse`](./ukg_python_sdk/pydantic/compensation_details_get_all_by_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/compensation-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.compensation_details.get_all_details`<a id="ukgcompensation_detailsget_all_details"></a>

Get all compensation details. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Employee Compensation Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /compensation-details?dateInJob=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /compensation-details?dateInJob=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /compensation-details?dateInJob=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /compensation-details?dateInJob={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_details_response = ukg.compensation_details.get_all_details(
    company_id="Cu2LC4aWwWL9Y864DZtaGR",
    employee_id="[q*RgcCecSDVGW8iZx9kSj",
    primary_job_code="Cu2LC4aWwWL9Y864DZtaGR",
    job_group_code="Cu2LC4aWwWL9Y864DZtaGR",
    job_title="Cu2LC4aWwWL9Y864DZtaGR",
    pay_group_code="Cu2LC4aWwWL9Y864DZtaGR",
    full_time_or_part_time_code="EiOTgswWMEJTcMoSLlNYUL",
    salary_or_hourly_code="EiOTgswWMEJTcMoSLlNYUL",
    primary_shift_code="EiOTgswWMEJTcMoSLlNYUL",
    primary_shift_group_code="EiOTgswWMEJTcMoSLlNYUL",
    date_in_job="string_example",
    date_last_paid="string_example",
    date_paid_thru="string_example",
    is_auto_allocated="EiOTgswWMEJTcMoSLlNYUL",
    is_auto_paid="EiOTgswWMEJTcMoSLlNYUL",
    is_seasonal_worker="EiOTgswWMEJTcMoSLlNYUL",
    is_highly_compensated="EiOTgswWMEJTcMoSLlNYUL",
    is_multiple_job="EiOTgswWMEJTcMoSLlNYUL",
    performance_review_rating="EiOTgswWMEJTcMoSLlNYUL",
    performance_review_type="EiOTgswWMEJTcMoSLlNYUL",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### primary_job_code: `str`<a id="primary_job_code-str"></a>

##### job_group_code: `str`<a id="job_group_code-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### pay_group_code: `str`<a id="pay_group_code-str"></a>

##### full_time_or_part_time_code: `str`<a id="full_time_or_part_time_code-str"></a>

##### salary_or_hourly_code: `str`<a id="salary_or_hourly_code-str"></a>

##### primary_shift_code: `str`<a id="primary_shift_code-str"></a>

##### primary_shift_group_code: `str`<a id="primary_shift_group_code-str"></a>

##### date_in_job: `str`<a id="date_in_job-str"></a>

Used to find date in job less than, greater than, equal to, or between passed date(s)

##### date_last_paid: `str`<a id="date_last_paid-str"></a>

Used to find date last paid less than, greater than, equal to, or between passed date(s)

##### date_paid_thru: `str`<a id="date_paid_thru-str"></a>

Used to find date paid through less than, greater than, equal to, or between passed date(s)

##### is_auto_allocated: `str`<a id="is_auto_allocated-str"></a>

##### is_auto_paid: `str`<a id="is_auto_paid-str"></a>

##### is_seasonal_worker: `str`<a id="is_seasonal_worker-str"></a>

##### is_highly_compensated: `str`<a id="is_highly_compensated-str"></a>

##### is_multiple_job: `str`<a id="is_multiple_job-str"></a>

##### performance_review_rating: `str`<a id="performance_review_rating-str"></a>

##### performance_review_type: `str`<a id="performance_review_type-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationDetailsGetAllDetailsResponse`](./ukg_python_sdk/pydantic/compensation_details_get_all_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/compensation-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.compensation_details.get_by_company_and_employee`<a id="ukgcompensation_detailsget_by_company_and_employee"></a>

Get all compensation details by company and employee. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Employee Compensation Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /companies/{companyId}/employees/{employeeId}/compensation-details?dateInJob=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /companies/{companyId}/employees/{employeeId}/compensation-details?dateInJob=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /companies/{companyId}/employees/{employeeId}/compensation-details?dateInJob=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /companies/{companyId}/employees/{employeeId}/compensation-details?dateInJob={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_company_and_employee_response = ukg.compensation_details.get_by_company_and_employee(
    company_id="companyId_example",
    employee_id="employeeId_example",
    company_id2="Cu2LC4aWwWL9Y864DZtaGR",
    employee_id2="[q*RgcCecSDVGW8iZx9kSj",
    primary_job_code="Cu2LC4aWwWL9Y864DZtaGR",
    job_group_code="Cu2LC4aWwWL9Y864DZtaGR",
    job_title="Cu2LC4aWwWL9Y864DZtaGR",
    pay_group_code="Cu2LC4aWwWL9Y864DZtaGR",
    full_time_or_part_time_code="EiOTgswWMEJTcMoSLlNYUL",
    salary_or_hourly_code="EiOTgswWMEJTcMoSLlNYUL",
    primary_shift_code="EiOTgswWMEJTcMoSLlNYUL",
    primary_shift_group_code="EiOTgswWMEJTcMoSLlNYUL",
    date_in_job="string_example",
    date_last_paid="string_example",
    date_paid_thru="string_example",
    is_auto_allocated="EiOTgswWMEJTcMoSLlNYUL",
    is_auto_paid="EiOTgswWMEJTcMoSLlNYUL",
    is_seasonal_worker="EiOTgswWMEJTcMoSLlNYUL",
    is_highly_compensated="EiOTgswWMEJTcMoSLlNYUL",
    is_multiple_job="EiOTgswWMEJTcMoSLlNYUL",
    performance_review_rating="EiOTgswWMEJTcMoSLlNYUL",
    performance_review_type="EiOTgswWMEJTcMoSLlNYUL",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id2: `str`<a id="company_id2-str"></a>

##### employee_id2: `str`<a id="employee_id2-str"></a>

##### primary_job_code: `str`<a id="primary_job_code-str"></a>

##### job_group_code: `str`<a id="job_group_code-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### pay_group_code: `str`<a id="pay_group_code-str"></a>

##### full_time_or_part_time_code: `str`<a id="full_time_or_part_time_code-str"></a>

##### salary_or_hourly_code: `str`<a id="salary_or_hourly_code-str"></a>

##### primary_shift_code: `str`<a id="primary_shift_code-str"></a>

##### primary_shift_group_code: `str`<a id="primary_shift_group_code-str"></a>

##### date_in_job: `str`<a id="date_in_job-str"></a>

Used to find date in job less than, greater than, equal to, or between passed date(s)

##### date_last_paid: `str`<a id="date_last_paid-str"></a>

Used to find date last paid less than, greater than, equal to, or between passed date(s)

##### date_paid_thru: `str`<a id="date_paid_thru-str"></a>

Used to find date paid through less than, greater than, equal to, or between passed date(s)

##### is_auto_allocated: `str`<a id="is_auto_allocated-str"></a>

##### is_auto_paid: `str`<a id="is_auto_paid-str"></a>

##### is_seasonal_worker: `str`<a id="is_seasonal_worker-str"></a>

##### is_highly_compensated: `str`<a id="is_highly_compensated-str"></a>

##### is_multiple_job: `str`<a id="is_multiple_job-str"></a>

##### performance_review_rating: `str`<a id="performance_review_rating-str"></a>

##### performance_review_type: `str`<a id="performance_review_type-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CompensationDetailsGetByCompanyAndEmployeeResponse`](./ukg_python_sdk/pydantic/compensation_details_get_by_company_and_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/employees/{employeeId}/compensation-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.compensation_details.get_by_employee`<a id="ukgcompensation_detailsget_by_employee"></a>

Get all compensation details by employee. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Employee Compensation Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /compensation-details/{employeeId}?dateInJob=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /compensation-details/{employeeId}?dateInJob=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /compensation-details/{employeeId}?dateInJob=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /compensation-details/{employeeId}?dateInJob={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_response = ukg.compensation_details.get_by_employee(
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmpCompensationDetails`](./ukg_python_sdk/pydantic/emp_compensation_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/compensation-details/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.contact.get_personnel_contact_details`<a id="ukgcontactget_personnel_contact_details"></a>

Get all details for a single person assigned to an employee as a contact. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /contacts/{contactId}?statusAsOfDate=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /contacts/{contactId}?statusAsOfDate=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /contacts/{contactId}?statusAsOfDate=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /contacts/{contactId}?statusAsOfDate={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_personnel_contact_details_response = ukg.contact.get_personnel_contact_details(
    contact_id="contactId_example",
    employee_id="Cu2LC4aWwWL9Y864DZtaGR",
    is_active="EiOTgswWMEJTcMoSLlNYUL",
    relationship_code="EiOTgswWMEJTcMoSLlNYUL",
    contact_id2="Cu2LC4aWwWL9Y864DZtaGR",
    country_code="EiOTgswWMEJTcMoSLlNYUL",
    cobra_is_active="EiOTgswWMEJTcMoSLlNYUL",
    cobra_status="EiOTgswWMEJTcMoSLlNYUL",
    is_beneficiary="EiOTgswWMEJTcMoSLlNYUL",
    is_dependent="EiOTgswWMEJTcMoSLlNYUL",
    date_of_cobra_event="string_example",
    status_as_of_date="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### is_active: `str`<a id="is_active-str"></a>

##### relationship_code: `str`<a id="relationship_code-str"></a>

##### contact_id2: `str`<a id="contact_id2-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### cobra_is_active: `str`<a id="cobra_is_active-str"></a>

##### cobra_status: `str`<a id="cobra_status-str"></a>

##### is_beneficiary: `str`<a id="is_beneficiary-str"></a>

##### is_dependent: `str`<a id="is_dependent-str"></a>

##### date_of_cobra_event: `str`<a id="date_of_cobra_event-str"></a>

Used to find date of COBRA event less than, greater than, equal to, or between passed date(s)

##### status_as_of_date: `str`<a id="status_as_of_date-str"></a>

Used to find contact status as of date less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Contact`](./ukg_python_sdk/pydantic/contact.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/contacts/{contactId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.contact.get_personnel_details`<a id="ukgcontactget_personnel_details"></a>

Get all details for a person assigned to an employee as a contact. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /contacts?statusAsOfDate=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /contacts?statusAsOfDate=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /contacts?statusAsOfDate=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /contacts?statusAsOfDate={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_personnel_details_response = ukg.contact.get_personnel_details(
    employee_id="Cu2LC4aWwWL9Y864DZtaGR",
    is_active="EiOTgswWMEJTcMoSLlNYUL",
    relationship_code="EiOTgswWMEJTcMoSLlNYUL",
    contact_id="Cu2LC4aWwWL9Y864DZtaGR",
    country_code="EiOTgswWMEJTcMoSLlNYUL",
    cobra_is_active="EiOTgswWMEJTcMoSLlNYUL",
    cobra_status="EiOTgswWMEJTcMoSLlNYUL",
    is_beneficiary="EiOTgswWMEJTcMoSLlNYUL",
    is_dependent="EiOTgswWMEJTcMoSLlNYUL",
    date_of_cobra_event="string_example",
    status_as_of_date="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### is_active: `str`<a id="is_active-str"></a>

##### relationship_code: `str`<a id="relationship_code-str"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### cobra_is_active: `str`<a id="cobra_is_active-str"></a>

##### cobra_status: `str`<a id="cobra_status-str"></a>

##### is_beneficiary: `str`<a id="is_beneficiary-str"></a>

##### is_dependent: `str`<a id="is_dependent-str"></a>

##### date_of_cobra_event: `str`<a id="date_of_cobra_event-str"></a>

Used to find date of COBRA event less than, greater than, equal to, or between passed date(s)

##### status_as_of_date: `str`<a id="status_as_of_date-str"></a>

Used to find contact status as of date less than, greater than,equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Contact`](./ukg_python_sdk/pydantic/contact.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/contacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.dependent_deductions.get`<a id="ukgdependent_deductionsget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.dependent_deductions.get(
    company_id="string_example",
    contact_id="string_example",
    deduction_code="string_example",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    effective_date="1970-01-01T00:00:00.00Z",
    current_coid="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

##### current_coid: `str`<a id="current_coid-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DependentDeductionsGetResponse`](./ukg_python_sdk/pydantic/dependent_deductions_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/dep-deductions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.direct_deposit.list_direct_deposit_details_by_company`<a id="ukgdirect_depositlist_direct_deposit_details_by_company"></a>

Get list of direct deposit details for US and Canadian employees by company.  
If no pagination parameters specified, the default/max is applied. Permissions - UltiPro service account must have "View" role for the "Employee Direct Deposit" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /companies/{companyId}/direct-deposit?dateTimeChanged=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /companies/{companyId}/direct-deposit?dateTimeChanged=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /companies/{companyId}/direct-deposit?dateTimeChanged=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /companies/{companyId}/direct-deposit?dateTimeChanged={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_direct_deposit_details_by_company_response = ukg.direct_deposit.list_direct_deposit_details_by_company(
    company_id="companyId_example",
    account_is_inactive="string_example",
    employee_id="string_example",
    company_id2="string_example",
    employee_bank_routing_number="string_example",
    country_code="string_example",
    date_time_changed="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### account_is_inactive: `str`<a id="account_is_inactive-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id2: `str`<a id="company_id2-str"></a>

##### employee_bank_routing_number: `str`<a id="employee_bank_routing_number-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### date_time_changed: `str`<a id="date_time_changed-str"></a>

Used to find direct deposit record changed date less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DirectDepositListDirectDepositDetailsByCompanyResponse`](./ukg_python_sdk/pydantic/direct_deposit_list_direct_deposit_details_by_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/companies/{companyId}/direct-deposit` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.direct_deposit.list_employee_direct_deposit_details`<a id="ukgdirect_depositlist_employee_direct_deposit_details"></a>

Get list of direct deposit details for US and Canadian employees.  
If no pagination parameters specified, the default/max is applied. Permissions - UltiPro service account must have "View" role for the "Employee Direct Deposit" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /direct-deposit?dateTimeChanged=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /direct-deposit?dateTimeChanged=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /direct-deposit?dateTimeChanged=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /direct-deposit?dateTimeChanged={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employee_direct_deposit_details_response = ukg.direct_deposit.list_employee_direct_deposit_details(
    account_is_inactive="string_example",
    employee_id="string_example",
    company_id="string_example",
    employee_bank_routing_number="string_example",
    country_code="string_example",
    date_time_changed="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_is_inactive: `str`<a id="account_is_inactive-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_bank_routing_number: `str`<a id="employee_bank_routing_number-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### date_time_changed: `str`<a id="date_time_changed-str"></a>

Used to find direct deposit record changed date less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DirectDepositListEmployeeDirectDepositDetailsResponse`](./ukg_python_sdk/pydantic/direct_deposit_list_employee_direct_deposit_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/direct-deposit` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.earnings.add_time_clock_data`<a id="ukgearningsadd_time_clock_data"></a>

Add UKG Pro time clock data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_time_clock_data_response = ukg.earnings.add_time_clock_data(
    x_correlation_id="X-Correlation-Id_example",
    us_client_id="US-Client-Id_example",
    earnings=[
        {
            "ref_id": "00000000-0000-0000-0000-000000000000",
            "company_code": "company_code_example",
            "emp_no": "emp_no_example",
            "code": "code_example",
            "source": "source_example",
        }
    ],
    fail_all_on_request=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_correlation_id: `str`<a id="x_correlation_id-str"></a>

##### us_client_id: `str`<a id="us_client_id-str"></a>

##### earnings: List[`Earning`]<a id="earnings-listearning"></a>

##### fail_all_on_request: `bool`<a id="fail_all_on_request-bool"></a>

failAllOnRequest, evaluating this to true will cause the entire request to fail given any errors, otherwise valid earnings will be staged for import.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EarningsAddTimeClockDataRequest`](./ukg_python_sdk/type/earnings_add_time_clock_data_request.py)
Add earnings from WFM for the purpose of processing payroll.

#### 🔄 Return<a id="🔄-return"></a>

[`EarningsAddTimeClockDataResponse`](./ukg_python_sdk/pydantic/earnings_add_time_clock_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/services/payroll/v1/import-pay-items/earnings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.earnings.delete_earning`<a id="ukgearningsdelete_earning"></a>

Delete a earning

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.earnings.delete_earning(
    x_correlation_id="X-Correlation-Id_example",
    us_client_id="US-Client-Id_example",
    ref_id="refId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_correlation_id: `str`<a id="x_correlation_id-str"></a>

##### us_client_id: `str`<a id="us_client_id-str"></a>

##### ref_id: `str`<a id="ref_id-str"></a>

Earning unique Identifier for earning

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/services/payroll/v1/import-pay-items/earnings/{refId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.earnings.get_configurations_filtered_by_parameter`<a id="ukgearningsget_configurations_filtered_by_parameter"></a>

Get all the earning configuration filtered by the parameter(s) passed. </br>If no pagination parameters specified, the default/max is applied. It is a public API that user can access once they have a valid username and password. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_filtered_by_parameter_response = ukg.earnings.get_configurations_filtered_by_parameter(
    calculation_rule="calculationRule_example",
    tax_category="taxCategory_example",
    use_deduction_offset="useDeductionOffset_example",
    country_code="countryCode_example",
    include_in_shift_diffrential="includeInShiftDiffrential_example",
    include_in_manual_check="includeInManualCheck_example",
    earning_code="string_example",
    include_in_accruals="string_example",
    include_in_deferred_compensation=True,
    include_in_deferred_compensation_hours=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### calculation_rule: `str`<a id="calculation_rule-str"></a>

##### tax_category: `str`<a id="tax_category-str"></a>

##### use_deduction_offset: `str`<a id="use_deduction_offset-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### include_in_shift_diffrential: `str`<a id="include_in_shift_diffrential-str"></a>

##### include_in_manual_check: `str`<a id="include_in_manual_check-str"></a>

##### earning_code: `str`<a id="earning_code-str"></a>

##### include_in_accruals: `str`<a id="include_in_accruals-str"></a>

##### include_in_deferred_compensation: `bool`<a id="include_in_deferred_compensation-bool"></a>

##### include_in_deferred_compensation_hours: `bool`<a id="include_in_deferred_compensation_hours-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EarningsGetConfigurationsFilteredByParameterResponse`](./ukg_python_sdk/pydantic/earnings_get_configurations_filtered_by_parameter_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/earnings/{calculationRule}/{taxCategory}/{useDeductionOffset}/{countryCode}/{includeInShiftDiffrential}/{includeInManualCheck}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.earnings.get_status_details`<a id="ukgearningsget_status_details"></a>

Get status details for specified earning

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_details_response = ukg.earnings.get_status_details(
    x_correlation_id="X-Correlation-Id_example",
    us_client_id="US-Client-Id_example",
    ref_id="refId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_correlation_id: `str`<a id="x_correlation_id-str"></a>

##### us_client_id: `str`<a id="us_client_id-str"></a>

##### ref_id: `str`<a id="ref_id-str"></a>

Earning unique Identifier for earning

#### 🔄 Return<a id="🔄-return"></a>

[`EarningStatusResponse`](./ukg_python_sdk/pydantic/earning_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/services/payroll/v1/import-pay-items/earnings/{refId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.earnings.list_earnings_configurations`<a id="ukgearningslist_earnings_configurations"></a>

Get details of all earnings configuration setup at company level. </br>If no pagination parameters specified, the default/max is applied. It is a public API that user can access once they have a valid username and password. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_earnings_configurations_response = ukg.earnings.list_earnings_configurations(
    calculation_rule="string_example",
    tax_category="string_example",
    use_deduction_offset="string_example",
    country_code="string_example",
    include_in_shift_diffrential="string_example",
    include_in_manual_check="string_example",
    earning_code="string_example",
    include_in_accruals="string_example",
    include_in_deferred_compensation=True,
    include_in_deferred_compensation_hours=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### calculation_rule: `str`<a id="calculation_rule-str"></a>

##### tax_category: `str`<a id="tax_category-str"></a>

##### use_deduction_offset: `str`<a id="use_deduction_offset-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### include_in_shift_diffrential: `str`<a id="include_in_shift_diffrential-str"></a>

##### include_in_manual_check: `str`<a id="include_in_manual_check-str"></a>

##### earning_code: `str`<a id="earning_code-str"></a>

##### include_in_accruals: `str`<a id="include_in_accruals-str"></a>

##### include_in_deferred_compensation: `bool`<a id="include_in_deferred_compensation-bool"></a>

##### include_in_deferred_compensation_hours: `bool`<a id="include_in_deferred_compensation_hours-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EarningsListEarningsConfigurationsResponse`](./ukg_python_sdk/pydantic/earnings_list_earnings_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/earnings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.earnings.specific_configuration_get`<a id="ukgearningsspecific_configuration_get"></a>

Get details of the earning configuration requested. </br>If no pagination parameters specified, the default/max is applied. It is a public API that user can access once they have a valid username and password. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
specific_configuration_get_response = ukg.earnings.specific_configuration_get(
    earning_code="earningCode_example",
    calculation_rule="string_example",
    tax_category="string_example",
    use_deduction_offset="string_example",
    country_code="string_example",
    include_in_shift_diffrential="string_example",
    include_in_manual_check="string_example",
    earning_code2="string_example",
    include_in_accruals="string_example",
    include_in_deferred_compensation=True,
    include_in_deferred_compensation_hours=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### earning_code: `str`<a id="earning_code-str"></a>

##### calculation_rule: `str`<a id="calculation_rule-str"></a>

##### tax_category: `str`<a id="tax_category-str"></a>

##### use_deduction_offset: `str`<a id="use_deduction_offset-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### include_in_shift_diffrential: `str`<a id="include_in_shift_diffrential-str"></a>

##### include_in_manual_check: `str`<a id="include_in_manual_check-str"></a>

##### earning_code2: `str`<a id="earning_code2-str"></a>

##### include_in_accruals: `str`<a id="include_in_accruals-str"></a>

##### include_in_deferred_compensation: `bool`<a id="include_in_deferred_compensation-bool"></a>

##### include_in_deferred_compensation_hours: `bool`<a id="include_in_deferred_compensation_hours-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EarningsSpecificConfigurationGetResponse`](./ukg_python_sdk/pydantic/earnings_specific_configuration_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/earnings/{earningCode}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.earnings_history.get_ins_rate`<a id="ukgearnings_historyget_ins_rate"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Payroll Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ins_rate_response = ukg.earnings_history.get_ins_rate(
    company_id="string_example",
    earning_code="string_example",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    employee_number="4807288800152802179809",
    pay_date="1970-01-01T00:00:00.00Z",
    pay_group="string_example",
    period_control="4807288800152802179809",
    start_per_control="4807288800152802179809",
    end_per_control="4807288800152802179809",
    include_in_deferred_compensation=True,
    include_in_deferred_compensation_hours=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### earning_code: `str`<a id="earning_code-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### pay_date: `datetime`<a id="pay_date-datetime"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### period_control: `str`<a id="period_control-str"></a>

##### start_per_control: `str`<a id="start_per_control-str"></a>

##### end_per_control: `str`<a id="end_per_control-str"></a>

##### include_in_deferred_compensation: `bool`<a id="include_in_deferred_compensation-bool"></a>

##### include_in_deferred_compensation_hours: `bool`<a id="include_in_deferred_compensation_hours-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EarningsHistoryGetInsRateResponse`](./ukg_python_sdk/pydantic/earnings_history_get_ins_rate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/earnings-history-base-elements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.emp_ded_ben_option_date.get`<a id="ukgemp_ded_ben_option_dateget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.emp_ded_ben_option_date.get(
    company_id="string_example",
    deduction_code="string_example",
    effective_date="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmpDedBenOptionDateGetResponse`](./ukg_python_sdk/pydantic/emp_ded_ben_option_date_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/emp-deductions-benefit-option-change-date` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.emp_deductions.list`<a id="ukgemp_deductionslist"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Api endpoints. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})

Correct syntax when using parameters are as follows: 
<ul> 
<li>Get Employee deductions for companyid
  <ul> 
  <li>Example: /personnel/v1/companies/{companyId}/emp-deductions?DedCode={DedCode}</li> 
  </ul> 
  </li>
<li>Get Employee deductions for companyid and employeeid 
  <ul> 
  <li>Example: /personnel/v1/companies/{companyId}/employees/{employeeId}/emp-deductions?DedCode={DedCode}}</li>
  </ul> 
  </li>
<li>Get Employee deductions per page
  <ul>
  <li>Example: personnel/v1/emp-deductions?DedCode={DedCode}&page=1&per_page=100</li> 
  </ul>
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = ukg.emp_deductions.list(
    ded_code="dedCode_example",
    employee_id="Cu2LC4aWwWL9Y864DZtaGR",
    company_id="string_example",
    ben_status="string_example",
    benefit_option="string_example",
    end_date_time="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ded_code: `str`<a id="ded_code-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### ben_status: `str`<a id="ben_status-str"></a>

##### benefit_option: `str`<a id="benefit_option-str"></a>

##### end_date_time: `datetime`<a id="end_date_time-datetime"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmpDeductionsListResponse`](./ukg_python_sdk/pydantic/emp_deductions_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/emp-deductions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.emp_global_localization_element.get`<a id="ukgemp_global_localization_elementget"></a>

Get all global employee localization fields added to UKG Pro through platform configuration with the prefix of 'GBLPay'.  
If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /employee-global-localization-elements?created=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /employee-global-localization-elements?created=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /employee-global-localization-elements?created=01-01-1900</li> 
  </ul>
  </li>
<li>between ({minimum date,maximum date}) 
  <ul>
  <li>Example: /employee-global-localization-elements?created={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.emp_global_localization_element.get(
    employee_id="string_example",
    company_id="string_example",
    created="1970-01-01T00:00:00.00Z",
    effective="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### created: `datetime`<a id="created-datetime"></a>

Used to find employee localization fields created less than, greater than, equal to, or between passed date(s)

##### effective: `datetime`<a id="effective-datetime"></a>

Used to find employee localization fields effective less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmpGlobalLocalizationElementModel`](./ukg_python_sdk/pydantic/emp_global_localization_element_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-global-localization-elements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.emp_multiple_positions.get`<a id="ukgemp_multiple_positionsget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.emp_multiple_positions.get(
    employee_id="string_example",
    company_id="string_example",
    job_code="string_example",
    position_code="string_example",
    is_primary="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### job_code: `str`<a id="job_code-str"></a>

##### position_code: `str`<a id="position_code-str"></a>

##### is_primary: `str`<a id="is_primary-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmpMultiplePositionsGetResponse`](./ukg_python_sdk/pydantic/emp_multiple_positions_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/empl-multiple-positions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_changes.get`<a id="ukgemployee_changesget"></a>

Gets all of the employee information since the last API call (minimum 3 hours), for a specific employeeId. The data is windowed in 3 hour increments. To get near real time updates on when the employee has changed, you should call this service 8 times per day and no more frequent than three hours between calls. It should also be understood that you must compare the results for an employee with the results from a previous call to see what property or properties have changed. The Permissions - Ultipro service account must have "View" role for the EmployeeExport Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_changes.get(
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeChangesGetResponse`](./ukg_python_sdk/pydantic/employee_changes_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-changes/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_deduction_history_effective_date.get_by_deduction_code_and_field`<a id="ukgemployee_deduction_history_effective_dateget_by_deduction_code_and_field"></a>

If no pagination parameters specified, the default/max is applied. 
 Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Api endpoints. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).</br>
  fieldName is a required parameter that takes one of the following:
   <ul>
   <li>changeReason</li>
   <li>benefitStartDate</li>
   <li>benefitStopDate</li>
   <li>benefitOption</li>
   <li>employeeAmount</li>
   <li>employeeBenefitAmount</li>
   <li>employeeGoalAmount</li>
   <li>eoiDesiredAmount</li>
   <li>eoiDesiredCalcRateOrPercent</li>
   <li>declinedByCarrier</li>
   <li>declinedByCarrierReason</li>
   <li>waiveReason</li>
   <li>deductionStartDate</li>
   <li>deductionStopDate</li>
   </ul>
   sessionDate is an optional parameter that defaults to today's date if null.</br>
  deductionCode is a required parameter that takes a list of codes [ded1,ded2].</br>
  CompanyId is an optional parameter that takes a list of IDs [coid1,coid2].</br>
   

 Correct syntax when using parameters are as follows: 
 <ul> 
   <li>Get deductions history change date by single deduction code 
   <ul> 
   <li>Example: /personnel/v1/deduction-history-effective-change-dates?fieldName={fieldName}&deductionCode={dedCode}</li> 
   </ul> 
   </li>
 <li>Get deductions history change date by multiple deduction code 
   <ul> 
   <li>Example: /personnel/v1/deduction-history-effective-change-dates?fieldName={fieldName}&deductionCode={dedCode1,dedCode2}</li>
   </ul> 
   </li>
   <li>Get deductions history change date multiple deduction code with multiple company 
   <ul> 
   <li>Example: /personnel/v1/deduction-history-effective-change-dates?fieldName={fieldName}&deductionCode={dedCode1,dedCode2}&companyId={companyId1,companyId1}</li>
   </ul> 
   </li>
   <li>Get deductions history change date by sessionDate,deduction code and company 
   <ul> 
   <li>Example: /personnel/v1/deduction-history-effective-change-dates?fieldName={fieldName}&sessionDate={sessionDate}deductionCode={deductionCode}&companyId={companyId}</li>
   </ul> 
   </li>
 <li>Get deductions history change date per page
   <ul>
   <li>Example: /personnel/v1/deduction-history-effective-change-dates?fieldName={fieldName}&page=1&per_page=100</li> 
   </ul>
   </li>
 </ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_deduction_code_and_field_response = ukg.employee_deduction_history_effective_date.get_by_deduction_code_and_field(
    field_name="fieldName_example",
    deduction_code="deductionCode_example",
    company_id="string_example",
    session_date="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_name: `str`<a id="field_name-str"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### session_date: `datetime`<a id="session_date-datetime"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeDeductionHistoryEffectiveDateGetByDeductionCodeAndFieldResponse`](./ukg_python_sdk/pydantic/employee_deduction_history_effective_date_get_by_deduction_code_and_field_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/deduction-history-effective-change-dates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_demographic_details.get`<a id="ukgemployee_demographic_detailsget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_demographic_details.get(
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    company_id="GqWzyBAw2ZuufUOHOEhA8I",
    last_name="ZziDDpmUvrJlSttzFEqBDF",
    email_address="string_example",
    address_state="ZziDDpmUvrJlSttzFEqBDF",
    address_country="ZziDDpmUvrJlSttzFEqBDF",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email_address: `str`<a id="email_address-str"></a>

##### address_state: `str`<a id="address_state-str"></a>

##### address_country: `str`<a id="address_country-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeDemographicDetailsGetResponse`](./ukg_python_sdk/pydantic/employee_demographic_details_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-demographic-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_id_lookup.by_company_ids`<a id="ukgemployee_id_lookupby_company_ids"></a>

Look up Employee ID/Company ID. This operation is a POST due the sensitive nature of the lookup properties not appropriate for URI. This service also supports multiple records to be looked up in the body of the request (array of Identifier objects). Permissions - Ultipro service account must have the "View" and "Add" roles for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
by_company_ids_response = ukg.employee_id_lookup.by_company_ids(
    body=[
        {
            "employee_identifier_type": "EmailAddress",
            "employee_identifier_value": "employee_identifier_value_example",
            "company_identifier_type": "Company ID",
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeIdLookupByCompanyIdsRequest`](./ukg_python_sdk/type/employee_id_lookup_by_company_ids_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeIdLookupByCompanyIdsResponse`](./ukg_python_sdk/pydantic/employee_id_lookup_by_company_ids_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-ids` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_jobs.get_all`<a id="ukgemployee_jobsget_all"></a>

Obtains all jobs for an employee.  Employee can be specified by their emp_name or emp_id.  At least one parameter must be specified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = ukg.employee_jobs.get_all(
    emp_name="string_example",
    emp_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### emp_name: `str`<a id="emp_name-str"></a>

##### emp_id: `int`<a id="emp_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoEmployeeJobDto`](./ukg_python_sdk/pydantic/result_dto_employee_job_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/employee_jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_security_user_details.get_details`<a id="ukgemployee_security_user_detailsget_details"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = ukg.employee_security_user_details.get_details(
    user_name="string_example",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_name: `str`<a id="user_name-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeSecurityUserDetailsGetDetailsResponse`](./ukg_python_sdk/pydantic/employee_security_user_details_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-security-user-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_cobra_details.get`<a id="ukgemployee_cobra_detailsget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_cobra_details.get(
    company_id="string_example",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    cobra_is_active=True,
    cobra_status="string_example",
    date_of_cobra_event="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### cobra_is_active: `bool`<a id="cobra_is_active-bool"></a>

##### cobra_status: `str`<a id="cobra_status-str"></a>

##### date_of_cobra_event: `datetime`<a id="date_of_cobra_event-datetime"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeCobraDetailsGetResponse`](./ukg_python_sdk/pydantic/employee_cobra_details_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-cobra-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_contract.get`<a id="ukgemployee_contractget"></a>

Get all employment contract details. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /employee-contract-details?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /employee-contract-details?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /employee-contract-details?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /employee-contract-details?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_contract.get(
    company_id="string_example",
    employee_id="string_example",
    contract_number="string_example",
    contract_type_code="string_example",
    effective_date="string_example",
    date_time_created="string_example",
    row_last_changed="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### contract_number: `str`<a id="contract_number-str"></a>

##### contract_type_code: `str`<a id="contract_type_code-str"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

Used to find contracts effective date less than, greater than, equal to, or between passed date(s)

##### date_time_created: `str`<a id="date_time_created-str"></a>

Used to find contract record created date less than, greater than, equal to, or between passed date(s)

##### row_last_changed: `str`<a id="row_last_changed-str"></a>

Used to find contract record changed date less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeContract`](./ukg_python_sdk/pydantic/employee_contract.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-contract-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_education.get`<a id="ukgemployee_educationget"></a>

Get all education details. If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_education.get(
    system_id="string_example",
    employee_id="string_example",
    country="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### system_id: `str`<a id="system_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### country: `str`<a id="country-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeEducationModel`](./ukg_python_sdk/pydantic/employee_education_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-education` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_employment_details.get_details`<a id="ukgemployee_employment_detailsget_details"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})
<ul> <li>Company ID parameter can take in multiple deduction codes
separated by coma. ex: [ABC, DEF]</li> <li>Primary Job Code parameter
can take in multiple pay frequencies separated by coma. ex: [ABC,
DEF]</li> <li>Primary Work Location Code parameter can take in multiple
pay frequencies separated by coma. ex: [ABC, DEF]</li> <li>Primary
Project Code parameter can take in multiple pay frequencies separated by
coma. ex: [ABC, DEF]</li> <li>Deduction Group Code parameter can take in
multiple pay frequencies separated by coma. ex: [ABC, DEF]</li>
<li>Earning Group Code parameter can take in multiple pay frequencies
separated by coma. ex: [ABC, DEF]</li> <li>Employee Type Code parameter
can take in multiple pay frequencies separated by coma. ex: [ABC,
DEF]</li> <li>Employee Status Code parameter can take in multiple pay
frequencies separated by coma. ex: [ABC, DEF]</li> <li>Pay Group
parameter can take in multiple pay frequencies separated by coma. ex:
[ABC, DEF]</li> </ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = ukg.employee_employment_details.get_details(
    company_id="string_example",
    employee_id="Cu2LC4aWwWL9Y864DZtaGR",
    primary_job_code="string_example",
    job_title="Cu2LC4aWwWL9Y864DZtaGR",
    full_time_or_part_time_code="EiOTgswWMEJTcMoSLlNYUL",
    primary_work_location_code="string_example",
    primary_project_code="string_example",
    deduction_group_code="string_example",
    earning_group_code="string_example",
    employee_type_code="string_example",
    employee_status_code="string_example",
    employee_number="4807288800152802179809",
    supervisor_id="string_example",
    original_hire_date="1970-01-01T00:00:00.00Z",
    last_hire_date="1970-01-01T00:00:00.00Z",
    date_of_termination="1970-01-01T00:00:00.00Z",
    date_of_retirement="1970-01-01T00:00:00.00Z",
    date_time_created="1970-01-01T00:00:00.00Z",
    date_time_changed="1970-01-01T00:00:00.00Z",
    date_last_pay_date_paid="1970-01-01T00:00:00.00Z",
    pay_group="string_example",
    is_home_company="y",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### primary_job_code: `str`<a id="primary_job_code-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### full_time_or_part_time_code: `str`<a id="full_time_or_part_time_code-str"></a>

##### primary_work_location_code: `str`<a id="primary_work_location_code-str"></a>

##### primary_project_code: `str`<a id="primary_project_code-str"></a>

##### deduction_group_code: `str`<a id="deduction_group_code-str"></a>

##### earning_group_code: `str`<a id="earning_group_code-str"></a>

##### employee_type_code: `str`<a id="employee_type_code-str"></a>

##### employee_status_code: `str`<a id="employee_status_code-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### supervisor_id: `str`<a id="supervisor_id-str"></a>

##### original_hire_date: `datetime`<a id="original_hire_date-datetime"></a>

##### last_hire_date: `datetime`<a id="last_hire_date-datetime"></a>

##### date_of_termination: `datetime`<a id="date_of_termination-datetime"></a>

##### date_of_retirement: `datetime`<a id="date_of_retirement-datetime"></a>

##### date_time_created: `datetime`<a id="date_time_created-datetime"></a>

##### date_time_changed: `datetime`<a id="date_time_changed-datetime"></a>

##### date_last_pay_date_paid: `datetime`<a id="date_last_pay_date_paid-datetime"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### is_home_company: `str`<a id="is_home_company-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeEmploymentDetailsGetDetailsResponse`](./ukg_python_sdk/pydantic/employee_employment_details_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-employment-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_extended_elements.get`<a id="ukgemployee_extended_elementsget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_extended_elements.get(
    company_id="string_example",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    date_time_created="1970-01-01T00:00:00.00Z",
    date_time_changed="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### date_time_created: `datetime`<a id="date_time_created-datetime"></a>

##### date_time_changed: `datetime`<a id="date_time_changed-datetime"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeExtendedElementsGetResponse`](./ukg_python_sdk/pydantic/employee_extended_elements_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-extended-elements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_global_bank.get`<a id="ukgemployee_global_bankget"></a>

Get all direct deposit details for global employees.  
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Global Employee Direct Deposit" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /employee-global-banks?dateModified=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /employee-global-banks?dateModified=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /employee-global-banks?dateModified=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /employee-global-banks?dateModified={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_global_bank.get(
    company_id="string_example",
    employee_id="string_example",
    employee_country="string_example",
    pay_group="string_example",
    date_modified="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### employee_country: `str`<a id="employee_country-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### date_modified: `str`<a id="date_modified-str"></a>

Used to find global employee's direct deposit modified date less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeGlobalBanksModel`](./ukg_python_sdk/pydantic/employee_global_banks_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-global-banks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_job_history_detail.get`<a id="ukgemployee_job_history_detailget"></a>

Get all employee job history details. If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Employee Job History Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /employee-job-history-details?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /employee-job-history-details?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /employee-job-history-details?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /employee-job-history-details?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_job_history_detail.get(
    company_id="string_example",
    employee_id="string_example",
    is_org_change="string_example",
    is_job_change="string_example",
    is_rate_change="string_example",
    is_promotion="string_example",
    system_id="string_example",
    job_effective_date="string_example",
    date_time_created="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### is_org_change: `str`<a id="is_org_change-str"></a>

##### is_job_change: `str`<a id="is_job_change-str"></a>

##### is_rate_change: `str`<a id="is_rate_change-str"></a>

##### is_promotion: `str`<a id="is_promotion-str"></a>

##### system_id: `str`<a id="system_id-str"></a>

##### job_effective_date: `str`<a id="job_effective_date-str"></a>

Used to find job history effective date less than, greater than, equal to, or between passed date(s)

##### date_time_created: `str`<a id="date_time_created-str"></a>

Used to find job history created less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeJobHistoryDetail`](./ukg_python_sdk/pydantic/employee_job_history_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-job-history-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_job_history_detail.get_single_record`<a id="ukgemployee_job_history_detailget_single_record"></a>

Get a single job history detail record. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Employee Job History Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /employee-job-history-details/systemID/[systemID]?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /employee-job-history-details/systemID/[systemID]?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /employee-job-history-details/systemID/[systemID]?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /employee-job-history-details/systemID/[systemID]?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_record_response = ukg.employee_job_history_detail.get_single_record(
    system_id="systemId_example",
    company_id="string_example",
    employee_id="string_example",
    is_org_change="string_example",
    is_job_change="string_example",
    is_rate_change="string_example",
    is_promotion="string_example",
    system_id2="string_example",
    job_effective_date="string_example",
    date_time_created="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### system_id: `str`<a id="system_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### is_org_change: `str`<a id="is_org_change-str"></a>

##### is_job_change: `str`<a id="is_job_change-str"></a>

##### is_rate_change: `str`<a id="is_rate_change-str"></a>

##### is_promotion: `str`<a id="is_promotion-str"></a>

##### system_id2: `str`<a id="system_id2-str"></a>

##### job_effective_date: `str`<a id="job_effective_date-str"></a>

Used to find job history effective date less than, greater than, equal to, or between passed date(s)

##### date_time_created: `str`<a id="date_time_created-str"></a>

Used to find job history created less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeJobHistoryDetail`](./ukg_python_sdk/pydantic/employee_job_history_detail.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-job-history-details/{systemId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_multi_phone_numbers.get`<a id="ukgemployee_multi_phone_numbersget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_multi_phone_numbers.get(
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    system_id="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### system_id: `str`<a id="system_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeMultiPhoneNumbersGetResponse`](./ukg_python_sdk/pydantic/employee_multi_phone_numbers_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-multi-phone-numbers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_multiple_jobs_opp.list_details`<a id="ukgemployee_multiple_jobs_opplist_details"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})

 Correct syntax when using parameters are as follows: 
<ul>
<li>Get Multiple jobs for employee ID
<ul>
<li>Example: /personnel/v1/empl-multiple-jobs?employeeId={employeeId}</li>
</ul>
</li>
<li>Get Multiple jobs for company ID
<ul>
<li>Example: /personnel/v1/empl-multiple-jobs?companyId={companyId}</li>
</ul>
</li>
<li>Get Multiple jobs for employee ID and company Id
<ul>
<li>Example: /personnel/v1/empl-multiple-jobs?employeeId={employeeId}&companyId={companyId}</li>
</ul>
</li>
<li>Get Multiple jobs per page
<ul>
<li>Example: /personnel/v1/empl-multiple-jobs?page=1&per_page=10000</li>
</ul>
</li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_details_response = ukg.employee_multiple_jobs_opp.list_details(
    employee_id="Cu2LC4aWwWL9Y864DZtaGR",
    company_id="string_example",
    job_code="string_example",
    is_primary_job="string_example",
    job_is_in_active="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### job_code: `str`<a id="job_code-str"></a>

##### is_primary_job: `str`<a id="is_primary_job-str"></a>

##### job_is_in_active: `str`<a id="job_is_in_active-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeMultipleJobsOppListDetailsResponse`](./ukg_python_sdk/pydantic/employee_multiple_jobs_opp_list_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/empl-multiple-jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_pay_deduction_element.get`<a id="ukgemployee_pay_deduction_elementget"></a>

Get all global employee payments and deductions.  
If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /employee-pay-deduction-elements?modifiedDate=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /employee-pay-deduction-elements?modifiedDate=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /employee-pay-deduction-elements?modifiedDate=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /employee-pay-deduction-elements?modifiedDate={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_pay_deduction_element.get(
    company_id="string_example",
    employee_id="string_example",
    country="string_example",
    pay_group="string_example",
    pay_deduction_name="string_example",
    period_start_name="string_example",
    payment_or_deduction_indicator="string_example",
    modified_date="string_example",
    start_date="string_example",
    end_date="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### country: `str`<a id="country-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### pay_deduction_name: `str`<a id="pay_deduction_name-str"></a>

##### period_start_name: `str`<a id="period_start_name-str"></a>

##### payment_or_deduction_indicator: `str`<a id="payment_or_deduction_indicator-str"></a>

##### modified_date: `str`<a id="modified_date-str"></a>

Used to find a payment or deduction modified less than, greater than, equal to, or between passed date(s)

##### start_date: `str`<a id="start_date-str"></a>

Used to find a payment or deduction where the pay period start is less than, greater than, equal to, or between passed date(s)

##### end_date: `str`<a id="end_date-str"></a>

Used to find a payment or deduction where the pay period end is less than, greater than, equal to, or between passed date(s)

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePayDeductionElementsModel`](./ukg_python_sdk/pydantic/employee_pay_deduction_elements_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-pay-deduction-elements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_pay_statement.get_by_date_range`<a id="ukgemployee_pay_statementget_by_date_range"></a>

This method returns zero or more pay statements for a specific employee identified by the passed-in employee identifier. The pay statement returned is based on the start date and the end date passed in. <br />If no pagination parameters specified, the default is applied. Permissions - UKG Pro service account must have "View" role for the "Employee Pay Statements" Web Service. Headers - US-Customer-Api-Key, US-Client-id, Authorization ({username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_date_range_response = ukg.employee_pay_statement.get_by_date_range(
    employee_identifier={
    },
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
    pages_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_identifier: [`EmployeeIdentifier`](./ukg_python_sdk/type/employee_identifier.py)<a id="employee_identifier-employeeidentifierukg_python_sdktypeemployee_identifierpy"></a>


##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### pages_count: `int`<a id="pages_count-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePayStatementRangeFilter`](./ukg_python_sdk/type/employee_pay_statement_range_filter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePayStatementGetByDateRangeResponse`](./ukg_python_sdk/pydantic/employee_pay_statement_get_by_date_range_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/employees/pay-statements` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_pay_statement.get_by_pay_identifier`<a id="ukgemployee_pay_statementget_by_pay_identifier"></a>

This method returns zero or one pay statements based on the given pay identifier. The pay identifier is a string value that represents a unique pay statement.<br /> If no pagination parameters specified, the default is applied. Permissions - UKG Pro service account must have "View" role for the "Employee Pay Statements" Web Service. Headers - US-Customer-Api-Key, US-Client-id, Authorization ({username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_pay_identifier_response = ukg.employee_pay_statement.get_by_pay_identifier(
    pay_identifier="PayIdentifier_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_identifier: `str`<a id="pay_identifier-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePayStatementModel`](./ukg_python_sdk/pydantic/employee_pay_statement_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/employees/pay-statement/{PayIdentifier}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_pay_statement.get_last_pay_statement`<a id="ukgemployee_pay_statementget_last_pay_statement"></a>

This method allows you to retrieve an individual pay statement by providing an employee identifier. This is helpful if you are designing an application that is aware of the employees to retrieve. <br />If no pagination parameters specified, the default is applied. Permissions - UKG Pro service account must have "View" role for the "Employee Pay Statements" Web Service. Headers - US-Customer-Api-Key, US-Client-id, Authorization ({username}:{password})

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_last_pay_statement_response = ukg.employee_pay_statement.get_last_pay_statement(
    employee_identifier={
    },
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
    pages_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_identifier: [`EmployeeIdentifier`](./ukg_python_sdk/type/employee_identifier.py)<a id="employee_identifier-employeeidentifierukg_python_sdktypeemployee_identifierpy"></a>


##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### pages_count: `int`<a id="pages_count-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePayStatementRangeFilter`](./ukg_python_sdk/type/employee_pay_statement_range_filter.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePayStatementModel`](./ukg_python_sdk/pydantic/employee_pay_statement_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/employees/pay-statement/last` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_supervisor_details.get`<a id="ukgemployee_supervisor_detailsget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.employee_supervisor_details.get(
    company_id="string_example",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    supervisor_company_id="string_example",
    supervisor_employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    supervisor_company_code="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### supervisor_company_id: `str`<a id="supervisor_company_id-str"></a>

##### supervisor_employee_id: `str`<a id="supervisor_employee_id-str"></a>

##### supervisor_company_code: `str`<a id="supervisor_company_code-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeSupervisorDetailsGetResponse`](./ukg_python_sdk/pydantic/employee_supervisor_details_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employee-supervisor-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employees.get_all`<a id="ukgemployeesget_all"></a>

Obtains all employees which have been setup for scheduling.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = ukg.employees.get_all(
    index=1,
    max=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### index: `int`<a id="index-int"></a>

Index when paging is to be used.

##### max: `int`<a id="max-int"></a>

Max elements per page

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoEmployeeDto`](./ukg_python_sdk/pydantic/result_dto_employee_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employment_details.get_by_company_id_and_employee_id`<a id="ukgemployment_detailsget_by_company_id_and_employee_id"></a>

Get a single employment detail by company. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /companies/{companyId}/employees/{employeeId}/employment-details?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /companies/{companyId}/employees/{employeeId}/employment-details?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /companies/{companyId}/employees/{employeeId}/employment-details?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /companies/{companyId}/employees/{employeeId}/employment-details?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_company_id_and_employee_id_response = ukg.employment_details.get_by_company_id_and_employee_id(
    company_id="companyId_example",
    employee_id="employeeId_example",
    company_id2="string_example",
    employee_id2="string_example",
    primary_job_code="string_example",
    job_title="string_example",
    full_time_or_part_time_code="string_example",
    primary_work_location_code="string_example",
    primary_project_code="string_example",
    deduction_group_code="string_example",
    earning_group_code="string_example",
    employee_type_code="string_example",
    employee_status_code="string_example",
    employee_number="string_example",
    supervisor_id="string_example",
    original_hire_date="string_example",
    last_hire_date="string_example",
    date_of_termination="string_example",
    date_of_retirement="string_example",
    date_time_created="string_example",
    date_time_changed="string_example",
    date_last_pay_date_paid="string_example",
    pay_group="string_example",
    is_home_company=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id2: `str`<a id="company_id2-str"></a>

##### employee_id2: `str`<a id="employee_id2-str"></a>

##### primary_job_code: `str`<a id="primary_job_code-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### full_time_or_part_time_code: `str`<a id="full_time_or_part_time_code-str"></a>

##### primary_work_location_code: `str`<a id="primary_work_location_code-str"></a>

##### primary_project_code: `str`<a id="primary_project_code-str"></a>

##### deduction_group_code: `str`<a id="deduction_group_code-str"></a>

##### earning_group_code: `str`<a id="earning_group_code-str"></a>

##### employee_type_code: `str`<a id="employee_type_code-str"></a>

##### employee_status_code: `str`<a id="employee_status_code-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### supervisor_id: `str`<a id="supervisor_id-str"></a>

##### original_hire_date: `str`<a id="original_hire_date-str"></a>

##### last_hire_date: `str`<a id="last_hire_date-str"></a>

##### date_of_termination: `str`<a id="date_of_termination-str"></a>

##### date_of_retirement: `str`<a id="date_of_retirement-str"></a>

##### date_time_created: `str`<a id="date_time_created-str"></a>

##### date_time_changed: `str`<a id="date_time_changed-str"></a>

##### date_last_pay_date_paid: `str`<a id="date_last_pay_date_paid-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### is_home_company: `bool`<a id="is_home_company-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentDetailsGetByCompanyIdAndEmployeeIdResponse`](./ukg_python_sdk/pydantic/employment_details_get_by_company_id_and_employee_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/employees/{employeeId}/employment-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employment_details.get_details`<a id="ukgemployment_detailsget_details"></a>

Get all employment record details. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /employment-details?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /employment-details?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /employment-details?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /employment-details?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = ukg.employment_details.get_details(
    company_id="string_example",
    employee_id="string_example",
    primary_job_code="string_example",
    job_title="string_example",
    full_time_or_part_time_code="string_example",
    primary_work_location_code="string_example",
    primary_project_code="string_example",
    deduction_group_code="string_example",
    earning_group_code="string_example",
    employee_type_code="string_example",
    employee_status_code="string_example",
    employee_number="string_example",
    supervisor_id="string_example",
    original_hire_date="string_example",
    last_hire_date="string_example",
    date_of_termination="string_example",
    date_of_retirement="string_example",
    date_time_created="string_example",
    date_time_changed="string_example",
    date_last_pay_date_paid="string_example",
    pay_group="string_example",
    is_home_company=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### primary_job_code: `str`<a id="primary_job_code-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### full_time_or_part_time_code: `str`<a id="full_time_or_part_time_code-str"></a>

##### primary_work_location_code: `str`<a id="primary_work_location_code-str"></a>

##### primary_project_code: `str`<a id="primary_project_code-str"></a>

##### deduction_group_code: `str`<a id="deduction_group_code-str"></a>

##### earning_group_code: `str`<a id="earning_group_code-str"></a>

##### employee_type_code: `str`<a id="employee_type_code-str"></a>

##### employee_status_code: `str`<a id="employee_status_code-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### supervisor_id: `str`<a id="supervisor_id-str"></a>

##### original_hire_date: `str`<a id="original_hire_date-str"></a>

##### last_hire_date: `str`<a id="last_hire_date-str"></a>

##### date_of_termination: `str`<a id="date_of_termination-str"></a>

##### date_of_retirement: `str`<a id="date_of_retirement-str"></a>

##### date_time_created: `str`<a id="date_time_created-str"></a>

##### date_time_changed: `str`<a id="date_time_changed-str"></a>

##### date_last_pay_date_paid: `str`<a id="date_last_pay_date_paid-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### is_home_company: `bool`<a id="is_home_company-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentDetailsGetDetailsResponse`](./ukg_python_sdk/pydantic/employment_details_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/employment-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employment_details.list_by_company`<a id="ukgemployment_detailslist_by_company"></a>

Get all employment record details by company. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /companies/{companyId}/employment-details?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /companies/{companyId}/employment-details?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /companies/{companyId}/employment-details?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /companies/{companyId}/employment-details?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_company_response = ukg.employment_details.list_by_company(
    company_id="companyId_example",
    company_id2="string_example",
    employee_id="string_example",
    primary_job_code="string_example",
    job_title="string_example",
    full_time_or_part_time_code="string_example",
    primary_work_location_code="string_example",
    primary_project_code="string_example",
    deduction_group_code="string_example",
    earning_group_code="string_example",
    employee_type_code="string_example",
    employee_status_code="string_example",
    employee_number="string_example",
    supervisor_id="string_example",
    original_hire_date="string_example",
    last_hire_date="string_example",
    date_of_termination="string_example",
    date_of_retirement="string_example",
    date_time_created="string_example",
    date_time_changed="string_example",
    date_last_pay_date_paid="string_example",
    pay_group="string_example",
    is_home_company=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### company_id2: `str`<a id="company_id2-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### primary_job_code: `str`<a id="primary_job_code-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### full_time_or_part_time_code: `str`<a id="full_time_or_part_time_code-str"></a>

##### primary_work_location_code: `str`<a id="primary_work_location_code-str"></a>

##### primary_project_code: `str`<a id="primary_project_code-str"></a>

##### deduction_group_code: `str`<a id="deduction_group_code-str"></a>

##### earning_group_code: `str`<a id="earning_group_code-str"></a>

##### employee_type_code: `str`<a id="employee_type_code-str"></a>

##### employee_status_code: `str`<a id="employee_status_code-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### supervisor_id: `str`<a id="supervisor_id-str"></a>

##### original_hire_date: `str`<a id="original_hire_date-str"></a>

##### last_hire_date: `str`<a id="last_hire_date-str"></a>

##### date_of_termination: `str`<a id="date_of_termination-str"></a>

##### date_of_retirement: `str`<a id="date_of_retirement-str"></a>

##### date_time_created: `str`<a id="date_time_created-str"></a>

##### date_time_changed: `str`<a id="date_time_changed-str"></a>

##### date_last_pay_date_paid: `str`<a id="date_last_pay_date_paid-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### is_home_company: `bool`<a id="is_home_company-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentDetailsListByCompanyResponse`](./ukg_python_sdk/pydantic/employment_details_list_by_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/employment-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.general_ledger_run_details_v2.get`<a id="ukggeneral_ledger_run_details_v2get"></a>

Returns a list of details for a general ledger run, filterable by runId and blockId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.general_ledger_run_details_v2.get(
    run_id="string_example",
    block_id="string_example",
    most_recent="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_id: `str`<a id="run_id-str"></a>

##### block_id: `str`<a id="block_id-str"></a>

##### most_recent: `str`<a id="most_recent-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GeneralLedgerRunDetailsV2GetResponse`](./ukg_python_sdk/pydantic/general_ledger_run_details_v2_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v2/general-ledger` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.general_ledger_run_details_v2.get_by_run_id`<a id="ukggeneral_ledger_run_details_v2get_by_run_id"></a>

Returns a list of details for a general ledger run, filterable by runId and blockId

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_run_id_response = ukg.general_ledger_run_details_v2.get_by_run_id(
    run_id="runId_example",
    run_id2="string_example",
    block_id="string_example",
    most_recent="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_id: `str`<a id="run_id-str"></a>

##### run_id2: `str`<a id="run_id2-str"></a>

##### block_id: `str`<a id="block_id-str"></a>

##### most_recent: `str`<a id="most_recent-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GeneralLedgerRunDetailsV2GetByRunIdResponse`](./ukg_python_sdk/pydantic/general_ledger_run_details_v2_get_by_run_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v2/general-ledger/{runId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.get_all_pto_plans.information`<a id="ukgget_all_pto_plansinformation"></a>

Returns information about an UltiPro employees PTO Plans. Permissions - Ultipro service account must have "View" role for the "PTO Plan Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
information_response = ukg.get_all_pto_plans.information(
    page=3.14,
    per_page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

Pagination, which page you want to see

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

Pagination, how many records per page you want to see

#### 🔄 Return<a id="🔄-return"></a>

[`GetAllPtoPlansInformationResponse`](./ukg_python_sdk/pydantic/get_all_pto_plans_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/pto-plans` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.get_job_postings.details`<a id="ukgget_job_postingsdetails"></a>

The Job Postings API returns detailed information about jobs in UltiPro Recruiting such as title, description, compensation, available locations, company, talent factors like skills, work experience, education, licenses, behaviors and motivations, the published date, and the url to the job on UltiPro's Recruiting. Consumers should iterate through the pages until no more records are returned. 

The "company" property contains "name" and "doing_business_as", if the company name needs to be publicly exposed, the "doing_business_as" name should be used. Some properties may have several translations available, the possible language codes are: en_us, en_gb, es_es, fr_ca, de_de, and pr_br.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
details_response = ukg.get_job_postings.details(
    integration_id="integrationId_example",
    page=3.14,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### integration_id: `str`<a id="integration_id-str"></a>

A unique integration id provided by Ultimate Software to the Partner during the integration registration process. 

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

Pagination page number

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

Pagination amount of records per page to display

#### 🔄 Return<a id="🔄-return"></a>

[`Postings`](./ukg_python_sdk/pydantic/postings.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/talent/recruiting/v2/third-party-job-board-integrations/{integrationId}/postings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.get_specific_employees_pto_plans.info`<a id="ukgget_specific_employees_pto_plansinfo"></a>

Returns information about an UltiPro employees PTO Plans. Permissions - Ultipro service account must have "View" role for the "PTO Plan Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
info_response = ukg.get_specific_employees_pto_plans.info(
    company_id="companyId_example",
    employee_id="employeeId_example",
    page=3.14,
    per_page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

Company Identifier

##### employee_id: `str`<a id="employee_id-str"></a>

Employee Identifier

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

Pagination, which page you want to see

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

Pagination, how many records per page you want to see

#### 🔄 Return<a id="🔄-return"></a>

[`GetSpecificEmployeesPtoPlansInfoResponse`](./ukg_python_sdk/pydantic/get_specific_employees_pto_plans_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/employees/{employeeId}/pto-plans` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.get_specific_pto_plan.info`<a id="ukgget_specific_pto_planinfo"></a>

Returns information about an UltiPro employees PTO Plans. Work flow or Approvers is not supported. Permissions - Ultipro service account must have "View" role for the "PTO Plan Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
info_response = ukg.get_specific_pto_plan.info(
    company_id="companyId_example",
    employee_id="employeeId_example",
    pto_plan="ptoPlan_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

Company Identifier

##### employee_id: `str`<a id="employee_id-str"></a>

Employee Identifier

##### pto_plan: `str`<a id="pto_plan-str"></a>

PTO Plan Identifier

#### 🔄 Return<a id="🔄-return"></a>

[`GetSpecificPtoPlanInfoResponse`](./ukg_python_sdk/pydantic/get_specific_pto_plan_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/employees/{employeeId}/pto-plans/{ptoPlan}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.hour_types.obtain_all`<a id="ukghour_typesobtain_all"></a>

Obtains all hour types.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
obtain_all_response = ukg.hour_types.obtain_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoHourTypeDto`](./ukg_python_sdk/pydantic/result_dto_hour_type_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/hour_types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.import_tool.get_status`<a id="ukgimport_toolget_status"></a>

Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}). UltiPro service account must have View role for the Personnel Integration Web Service. This GET call has a requirement of PersonnelResourceAuthorize(ApiOperation.Read)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_response = ukg.import_tool.get_status(
    staging_id="stagingId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### staging_id: `str`<a id="staging_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UltimateSoftwareFoundationServicesApiUltiProPersonnelImportToolModelsFileStagingStatus`](./ukg_python_sdk/pydantic/ultimate_software_foundation_services_api_ulti_pro_personnel_import_tool_models_file_staging_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/import-tool/status/{stagingId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.import_tool.post`<a id="ukgimport_toolpost"></a>

Submits an encoded XML transaction to the Import Tool. Transaction results can be viewed on the Administration > Integration Studio > Import Tool > Results page. Reference the Import Tool XML and Configuration Settings Guide for transaction details. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}). UltiPro service account must have the View and Add roles for the Personnel Integration Web Service. This POST call has a requirement of PersonnelResourceAuthorize(ApiOperation.Create)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
post_response = ukg.import_tool.post(
    transaction="string_example",
    unique_file_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction: `str`<a id="transaction-str"></a>

The XML Serialized transaction

##### unique_file_name: `str`<a id="unique_file_name-str"></a>

An optionally provided unique file name

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UltimateSoftwareFoundationServicesApiUltiProPersonnelImportToolModelsImportRequest`](./ukg_python_sdk/type/ultimate_software_foundation_services_api_ulti_pro_personnel_import_tool_models_import_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ImportToolPostResponse`](./ukg_python_sdk/pydantic/import_tool_post_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/import-tool` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.ins_rate.get_ins_rate`<a id="ukgins_rateget_ins_rate"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ins_rate_response = ukg.ins_rate.get_ins_rate(
    deduction_code="string_example",
    effective_date="1970-01-01T00:00:00.00Z",
    pay_frequency="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

##### pay_frequency: `str`<a id="pay_frequency-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InsRateGetInsRateResponse`](./ukg_python_sdk/pydantic/ins_rate_get_ins_rate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/insurance-rate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.integration_audit_configuration.get_data`<a id="ukgintegration_audit_configurationget_data"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_response = ukg.integration_audit_configuration.get_data(
    table_name="string_example",
    field_name="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### table_name: `str`<a id="table_name-str"></a>

##### field_name: `str`<a id="field_name-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`IntegrationAuditConfigurationGetDataResponse`](./ukg_python_sdk/pydantic/integration_audit_configuration_get_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/integration-audit-configuration` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.international_employee.get`<a id="ukginternational_employeeget"></a>

Get all international employee details. If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.international_employee.get(
    country_code="string_example",
    effective_date="string_example",
    employee_id="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InternationalEmployeeGetResponse`](./ukg_python_sdk/pydantic/international_employee_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/international-employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.international_employee.get_details`<a id="ukginternational_employeeget_details"></a>

Get a single employees international details. If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = ukg.international_employee.get_details(
    employee_id="employeeId_example",
    country_code="string_example",
    effective_date="string_example",
    employee_id2="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### effective_date: `str`<a id="effective_date-str"></a>

##### employee_id2: `str`<a id="employee_id2-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`InternationalEmployeeGetDetailsResponse`](./ukg_python_sdk/pydantic/international_employee_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/international-employees/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.job_group.get`<a id="ukgjob_groupget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.job_group.get(
    job_group_code="string_example",
    job_group_country_code="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_group_code: `str`<a id="job_group_code-str"></a>

##### job_group_country_code: `str`<a id="job_group_country_code-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JobGroupGetResponse`](./ukg_python_sdk/pydantic/job_group_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/jobgroup` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.kronos_employee_profiles.get_list`<a id="ukgkronos_employee_profilesget_list"></a>

If no pagination parameters specified, the default/max is applied.
  
  Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Api endpoints. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}). <br><br>/personnel/v1/integration/kronos/employee-profiles can take following optional parameter:<br><ul><li>Product: Required parameter </li> <li>companyId: Can take in multiple IDs separated by comma. ex: {id1}, {id2}</li><li>employeeId: Can take in multiple IDs separated by comma. ex: {id1}, {id2}</li><li>includeHistoryIfChangeDetected</li><li>effectiveDate</li><li>changeWindow</li><li>per_Page</li><li>page</li><br>Correct syntax when using parameters are as follows:<ul><li>Get kronos employee profiles with required product parameter<ul>   <li>Example: personnel/v1/integration/kronos/employee-profiles?product={productCode}</ul></li><li>Get kronos employee profiles by companyId and employeeId<ul><li>Example: personnel/v1/integration/kronos/employee-profiles?product={productCode}&companyId={COID1}&employeeId={EEID1}, {EEID2}&effectiveDate={date}</li></ul></li><li>Get employee profiles by includeHistoryIfChangeDetected<ul><li>Example: personnel/v1/integration/kronos/employee-profiles?product={productCode}&companyId={COID1}&employeeId={EEID1}&effectiveDate={date}&includeHistoryIfChangeDetected=true</li></ul></li><li>Get kronos employee profiles by perPage and page<ul><li>Example: personnel/v1/integration/kronos/employee-profiles?product={productCode}&page=1&per_Page={pageSize}</li></ul></ul>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = ukg.kronos_employee_profiles.get_list(
    product="product_example",
    company_id="string_example",
    employee_id="string_example",
    effective_date="1970-01-01T00:00:00.00Z",
    change_window=1,
    include_history_if_change_detected=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product: `str`<a id="product-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

##### change_window: `int`<a id="change_window-int"></a>

##### include_history_if_change_detected: `bool`<a id="include_history_if_change_detected-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`KronosEmployeeProfilesGetListResponse`](./ukg_python_sdk/pydantic/kronos_employee_profiles_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/integration/kronos/employee-profiles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.kronos_employee_status.get`<a id="ukgkronos_employee_statusget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.kronos_employee_status.get(
    effective_date="1970-01-01T00:00:00.00Z",
    company_id="string_example",
    employee_ids="string_example",
    inactive_term_window=1,
    inactive_disabled_window=1,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_ids: `str`<a id="employee_ids-str"></a>

##### inactive_term_window: `int`<a id="inactive_term_window-int"></a>

##### inactive_disabled_window: `int`<a id="inactive_disabled_window-int"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`KronosEmployeeStatusGetResponse`](./ukg_python_sdk/pydantic/kronos_employee_status_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/integration/kronos/employee-status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.national_document.get`<a id="ukgnational_documentget"></a>

All employee national document details. If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.national_document.get(
    contact_id="string_example",
    employee_id="string_example",
    national_document_issuing_country_code="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact_id: `str`<a id="contact_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### national_document_issuing_country_code: `str`<a id="national_document_issuing_country_code-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`NationalDocumentModel`](./ukg_python_sdk/pydantic/national_document_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/national-documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.new_hires.create_single_new_hire`<a id="ukgnew_hirescreate_single_new_hire"></a>

Creates a single New Hire

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_single_new_hire_response = ukg.new_hires.create_single_new_hire(
    tenant_identifier="tenantIdentifier_example",
    contact_information={
        "email_address": "hugo2296@gmail.com",
        "primary_phone": "3056985433",
        "secondary_phone": "3056986533",
    },
    job={
        "code": "DJOB",
        "requisition_id": "DEV30335",
        "selected_flsa_status": "2",
    },
    organization_levels=[
        {
            "id": "89e9f572-4c63-4630-8008-dd09c97ab64cX",
            "level": "1",
            "code": "ORG1",
        }
    ],
    compensation={
        "is_full_time": True,
        "is_salaried": False,
        "work_hours": 40,
        "weekly_hours": 0,
        "currency_code": "CAD",
        "pay_rate": 50000,
        "rate_per": "Y",
    },
    onboarding_owner_id="74A3D0C8-FF2A-4EC9-9263-F515B000A0C5",
    hire_date="1970-01-01T00:00:00.00Z",
    orientation_date="1970-01-01T00:00:00.00Z",
    start_date="1970-01-01T00:00:00.00Z",
    past_start_date_reason="An internal audit revealed that the new hire was not initiated",
    mentor={
        "description": "Oden will be your mentor and is THE person to get you up to speed on the product. She loves helping new team members.",
        "id": "2c9e2b00-f229-4930-9d82-e86e11d6440bX",
    },
    personal_message="Hugo, I was very impressed with your passion. I am looking forward to working with you and I know your expertise in this space will help our team get to the next level.",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_identifier: `str`<a id="tenant_identifier-str"></a>

Unique identifier of the tenant to interact with. Can be either the tenant alias or tenant ID.

##### contact_information: [`NewHiresCreateSingleNewHireRequestContactInformation`](./ukg_python_sdk/type/new_hires_create_single_new_hire_request_contact_information.py)<a id="contact_information-newhirescreatesinglenewhirerequestcontactinformationukg_python_sdktypenew_hires_create_single_new_hire_request_contact_informationpy"></a>


##### job: [`NewHiresCreateSingleNewHireRequestJob`](./ukg_python_sdk/type/new_hires_create_single_new_hire_request_job.py)<a id="job-newhirescreatesinglenewhirerequestjobukg_python_sdktypenew_hires_create_single_new_hire_request_jobpy"></a>


##### organization_levels: [`NewHiresCreateSingleNewHireRequestOrganizationLevels`](./ukg_python_sdk/type/new_hires_create_single_new_hire_request_organization_levels.py)<a id="organization_levels-newhirescreatesinglenewhirerequestorganizationlevelsukg_python_sdktypenew_hires_create_single_new_hire_request_organization_levelspy"></a>

##### compensation: [`NewHiresCreateSingleNewHireRequestCompensation`](./ukg_python_sdk/type/new_hires_create_single_new_hire_request_compensation.py)<a id="compensation-newhirescreatesinglenewhirerequestcompensationukg_python_sdktypenew_hires_create_single_new_hire_request_compensationpy"></a>


##### onboarding_owner_id: `str`<a id="onboarding_owner_id-str"></a>

External user identifier of the onboarding owner

##### hire_date: `datetime`<a id="hire_date-datetime"></a>

Hire date of the new hire

##### orientation_date: `datetime`<a id="orientation_date-datetime"></a>

Orientation date of the new hire

##### start_date: `datetime`<a id="start_date-datetime"></a>

Start date of the new hire

##### past_start_date_reason: `str`<a id="past_start_date_reason-str"></a>

Reason why the new hire start date is 4 or more business days in the past

##### mentor: [`NewHiresCreateSingleNewHireRequestMentor`](./ukg_python_sdk/type/new_hires_create_single_new_hire_request_mentor.py)<a id="mentor-newhirescreatesinglenewhirerequestmentorukg_python_sdktypenew_hires_create_single_new_hire_request_mentorpy"></a>


##### personal_message: `str`<a id="personal_message-str"></a>

Personal message for the new hire

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NewHiresCreateSingleNewHireRequest`](./ukg_python_sdk/type/new_hires_create_single_new_hire_request.py)
New Hire object to be added

#### 🔄 Return<a id="🔄-return"></a>

[`NewHiresCreateSingleNewHireResponse`](./ukg_python_sdk/pydantic/new_hires_create_single_new_hire_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tenants/{tenantIdentifier}/new-hires` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.new_hires.get_by_id`<a id="ukgnew_hiresget_by_id"></a>

Gets a single New Hire by Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = ukg.new_hires.get_by_id(
    tenant_identifier="tenantIdentifier_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_identifier: `str`<a id="tenant_identifier-str"></a>

Unique identifier of the tenant to interact with. Can be either the tenant alias or tenant ID.

##### id: `str`<a id="id-str"></a>

Unique identifier for the New Hire

#### 🔄 Return<a id="🔄-return"></a>

[`NewHiresGetByIdResponse`](./ukg_python_sdk/pydantic/new_hires_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tenants/{tenantIdentifier}/new-hires/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.open_enrollment_dependent_deductions.get_data`<a id="ukgopen_enrollment_dependent_deductionsget_data"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})
 <ul><li>StartDateTime is a required parameter. </li><li>EndDateTime is a required parameter.</li>  <li>SessionType is a required parameter. </li><li>DeductionCode is a required parameter that takes a list of deduction codes [ded1, ded2].</li></ul>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_response = ukg.open_enrollment_dependent_deductions.get_data(
    start_date_time="1970-01-01T00:00:00.00Z",
    end_date_time="1970-01-01T00:00:00.00Z",
    session_type="sessionType_example",
    deduction_code="deductionCode_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date_time: `datetime`<a id="start_date_time-datetime"></a>

##### end_date_time: `datetime`<a id="end_date_time-datetime"></a>

##### session_type: `str`<a id="session_type-str"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OpenEnrollmentDependentDeductionsGetDataResponse`](./ukg_python_sdk/pydantic/open_enrollment_dependent_deductions_get_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/open-enrollment-dep-deductions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.open_enrollment_employee_deductions.get_audit_details`<a id="ukgopen_enrollment_employee_deductionsget_audit_details"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_audit_details_response = ukg.open_enrollment_employee_deductions.get_audit_details(
    start_date_time="1970-01-01T00:00:00.00Z",
    end_date_time="1970-01-01T00:00:00.00Z",
    session_type="sessionType_example",
    deduction_code="deductionCode_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_date_time: `datetime`<a id="start_date_time-datetime"></a>

##### end_date_time: `datetime`<a id="end_date_time-datetime"></a>

##### session_type: `str`<a id="session_type-str"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OpenEnrollmentEmployeeDeductionsGetAuditDetailsResponse`](./ukg_python_sdk/pydantic/open_enrollment_employee_deductions_get_audit_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/open-enrollment-emp-deductions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.option_rate.get_data`<a id="ukgoption_rateget_data"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have \"View\" role for the \"Company Configuration Integration\" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

Effective date parameter gets effective record as of the given date. If it's not passed, effected date is defaulted to current date.

Deduction code parameter can take in multiple deduction codes separated by coma. ex: [DEN, MED, VIS] .

Pay frequency parameter can take in multiple pay frequencies separated by coma. ex: [B, M] .


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_response = ukg.option_rate.get_data(
    deduction_code="string_example",
    benefit_option="string_example",
    effective_date="1970-01-01T00:00:00.00Z",
    pay_frequency="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

##### benefit_option: `str`<a id="benefit_option-str"></a>

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

##### pay_frequency: `str`<a id="pay_frequency-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OptionRateGetDataResponse`](./ukg_python_sdk/pydantic/option_rate_get_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/option-rate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.order_requests.background_check_details`<a id="ukgorder_requestsbackground_check_details"></a>

Background Check Order Request with Candidate, Application, and Opportunity info

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
background_check_details_response = ukg.order_requests.background_check_details(
    token="token_example",
    tenant_alias="tenant-alias_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### token: `str`<a id="token-str"></a>

A temporary Background Check Request tokena ssociated with the background check request that has been previously provided in the Background Check Request Redirect URL

##### tenant_alias: `str`<a id="tenant_alias-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Output`](./ukg_python_sdk/pydantic/output.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{tenant-alias}/api/background-check-order-requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.organization_reporting_category.get`<a id="ukgorganization_reporting_categoryget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.organization_reporting_category.get(
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationReportingCategoryGetResponse`](./ukg_python_sdk/pydantic/organization_reporting_category_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/organization-reporting-category` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.pto_plan_patch.one_pto_plan`<a id="ukgpto_plan_patchone_pto_plan"></a>

Allows the ability to update one PTO Plan for an employee. Work Flow or Approvers is not supported. Permissions - Ultipro service account must have "Edit" role for the "PTO Plan Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
one_pto_plan_response = ukg.pto_plan_patch.one_pto_plan(
    employee_id="string_example",
    company_id="string_example",
    pto_plan="string_example",
    company_id="companyId_example",
    employee_id="employeeId_example",
    pto_plan="ptoPlan_example",
    earned=3.14,
    taken=3.14,
    pending_balance=3.14,
    earned_through_date="string_example",
    reset="string_example",
    pending_move_date="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

Company Identifier

##### employee_id: `str`<a id="employee_id-str"></a>

Employee Identifier

##### pto_plan: `str`<a id="pto_plan-str"></a>

PTO Plan Identifier

##### requestBody: [`PtoPlans`](./ukg_python_sdk/type/pto_plans.py)<a id="requestbody-ptoplansukg_python_sdktypepto_planspy"></a>

The pto-plan to be written

#### 🔄 Return<a id="🔄-return"></a>

[`PtoPlans`](./ukg_python_sdk/pydantic/pto_plans.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/employees/{employeeId}/pto-plans/{ptoPlan}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.pto_plan_post.ultipro_record`<a id="ukgpto_plan_postultipro_record"></a>

Creates a new UltiPro PTO plan record. Array of objects is permitted for multi-records support. Work Flow or Approvers is not supported. Permissions - Ultipro service account must have "Add" role for the "PTO Plan Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ultipro_record_response = ukg.pto_plan_post.ultipro_record(
    body=[
        {
            "employee_id": "employee_id_example",
            "company_id": "company_id_example",
            "pto_plan": "pto_plan_example",
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PtoPlansBody`](./ukg_python_sdk/type/pto_plans_body.py)
The pto-plan to be written

#### 🔄 Return<a id="🔄-return"></a>

[`MultiStatusResponse`](./ukg_python_sdk/pydantic/multi_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/pto-plans` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.pay_group_pay_period.get_pay_group_pay_period`<a id="ukgpay_group_pay_periodget_pay_group_pay_period"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Payroll Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_group_pay_period_response = ukg.pay_group_pay_period.get_pay_group_pay_period(
    pay_date_seq=1,
    period_end_date="1970-01-01T00:00:00.00Z",
    period_start_date="1970-01-01T00:00:00.00Z",
    pay_group="string_example",
    pay_date="1970-01-01T00:00:00.00Z",
    start_per_control="string_example",
    end_per_control="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_date_seq: `int`<a id="pay_date_seq-int"></a>

##### period_end_date: `datetime`<a id="period_end_date-datetime"></a>

##### period_start_date: `datetime`<a id="period_start_date-datetime"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### pay_date: `datetime`<a id="pay_date-datetime"></a>

##### start_per_control: `str`<a id="start_per_control-str"></a>

##### end_per_control: `str`<a id="end_per_control-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PayGroupPayPeriodGetPayGroupPayPeriodResponse`](./ukg_python_sdk/pydantic/pay_group_pay_period_get_pay_group_pay_period_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/paygroup-payperiods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.pay_register.get`<a id="ukgpay_registerget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Payroll Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.pay_register.get(
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    company_id="string_example",
    check_id="string_example",
    employee_number="string_example",
    document_number="string_example",
    pay_group="string_example",
    period_control="string_example",
    pay_date="1970-01-01T00:00:00.00Z",
    period_end_date="string_example",
    period_start_date="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### check_id: `str`<a id="check_id-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### document_number: `str`<a id="document_number-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### period_control: `str`<a id="period_control-str"></a>

##### pay_date: `datetime`<a id="pay_date-datetime"></a>

##### period_end_date: `str`<a id="period_end_date-str"></a>

##### period_start_date: `str`<a id="period_start_date-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PayRegisterGetResponse`](./ukg_python_sdk/pydantic/pay_register_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/pay-register` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.payroll_deductions_history.get`<a id="ukgpayroll_deductions_historyget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Payroll Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.payroll_deductions_history.get(
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    company_id="string_example",
    check_id="string_example",
    employee_number="string_example",
    deduction_code="string_example",
    deduction_type="string_example",
    benefit_option="string_example",
    benefit_provider="string_example",
    pay_group="string_example",
    period_control="string_example",
    pay_date="1970-01-01T00:00:00.00Z",
    is401_k="string_example",
    is403_b="string_example",
    is408_k="string_example",
    is408_p="string_example",
    is457="string_example",
    is457_b="string_example",
    is457_f="string_example",
    is501_c="string_example",
    is_d125="string_example",
    is_deduction_off_set="string_example",
    is_deferred_compensation="string_example",
    is_dependent_care="string_example",
    is_housing="string_example",
    is_non_qualified_plan="string_example",
    start_per_control="string_example",
    end_per_control="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### check_id: `str`<a id="check_id-str"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

##### deduction_type: `str`<a id="deduction_type-str"></a>

##### benefit_option: `str`<a id="benefit_option-str"></a>

##### benefit_provider: `str`<a id="benefit_provider-str"></a>

##### pay_group: `str`<a id="pay_group-str"></a>

##### period_control: `str`<a id="period_control-str"></a>

##### pay_date: `datetime`<a id="pay_date-datetime"></a>

##### is401_k: `str`<a id="is401_k-str"></a>

##### is403_b: `str`<a id="is403_b-str"></a>

##### is408_k: `str`<a id="is408_k-str"></a>

##### is408_p: `str`<a id="is408_p-str"></a>

##### is457: `str`<a id="is457-str"></a>

##### is457_b: `str`<a id="is457_b-str"></a>

##### is457_f: `str`<a id="is457_f-str"></a>

##### is501_c: `str`<a id="is501_c-str"></a>

##### is_d125: `str`<a id="is_d125-str"></a>

##### is_deduction_off_set: `str`<a id="is_deduction_off_set-str"></a>

##### is_deferred_compensation: `str`<a id="is_deferred_compensation-str"></a>

##### is_dependent_care: `str`<a id="is_dependent_care-str"></a>

##### is_housing: `str`<a id="is_housing-str"></a>

##### is_non_qualified_plan: `str`<a id="is_non_qualified_plan-str"></a>

##### start_per_control: `str`<a id="start_per_control-str"></a>

##### end_per_control: `str`<a id="end_per_control-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollDeductionsHistoryGetResponse`](./ukg_python_sdk/pydantic/payroll_deductions_history_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/v1/payroll-deductions-history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.person_details.get_all_details`<a id="ukgperson_detailsget_all_details"></a>

Get all person details. 
If no pagination parameters specified, the default/max is applied.  
Permissions - UKG Pro service account must have "View" role for the "Employee Person Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /person-details?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /person-details?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /person-details?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /person-details?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_details_response = ukg.person_details.get_all_details(
    company_id="string_example",
    employee_id="string_example",
    last_name="string_example",
    email_address="string_example",
    address_state="string_example",
    address_country="string_example",
    cobra_is_active="string_example",
    cobra_status="string_example",
    date_of_cobra_event="string_example",
    date_time_created="string_example",
    date_time_changed="string_example",
    national_id="string_example",
    national_id_country="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email_address: `str`<a id="email_address-str"></a>

##### address_state: `str`<a id="address_state-str"></a>

##### address_country: `str`<a id="address_country-str"></a>

##### cobra_is_active: `str`<a id="cobra_is_active-str"></a>

##### cobra_status: `str`<a id="cobra_status-str"></a>

##### date_of_cobra_event: `str`<a id="date_of_cobra_event-str"></a>

Used to find date of COBRA event less than, greater than, equal to, or between passed date(s)

##### date_time_created: `str`<a id="date_time_created-str"></a>

Used to find person record created less than, greater than, equal to, or between passed date(s)

##### date_time_changed: `str`<a id="date_time_changed-str"></a>

Used to find person record changed less than, greater than, equal to, or between passed date(s)

##### national_id: `str`<a id="national_id-str"></a>

##### national_id_country: `str`<a id="national_id_country-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonDetailsGetAllDetailsResponse`](./ukg_python_sdk/pydantic/person_details_get_all_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/person-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.person_details.get_single_company_details`<a id="ukgperson_detailsget_single_company_details"></a>

Get all person details for a single company. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Employee Person Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /companies/{companyId}/person-details?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /companies/{companyId}/person-details?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /companies/{companyId}/person-details?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /companies/{companyId}/person-details?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_company_details_response = ukg.person_details.get_single_company_details(
    company_id="companyId_example",
    company_id2="string_example",
    employee_id="string_example",
    last_name="string_example",
    email_address="string_example",
    address_state="string_example",
    address_country="string_example",
    cobra_is_active="string_example",
    cobra_status="string_example",
    date_of_cobra_event="string_example",
    date_time_created="string_example",
    date_time_changed="string_example",
    national_id="string_example",
    national_id_country="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### company_id2: `str`<a id="company_id2-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email_address: `str`<a id="email_address-str"></a>

##### address_state: `str`<a id="address_state-str"></a>

##### address_country: `str`<a id="address_country-str"></a>

##### cobra_is_active: `str`<a id="cobra_is_active-str"></a>

##### cobra_status: `str`<a id="cobra_status-str"></a>

##### date_of_cobra_event: `str`<a id="date_of_cobra_event-str"></a>

Used to find date of COBRA event less than, greater than, equal to, or between passed date(s)

##### date_time_created: `str`<a id="date_time_created-str"></a>

Used to find person record created less than, greater than, equal to, or between passed date(s)

##### date_time_changed: `str`<a id="date_time_changed-str"></a>

Used to find person record changed less than, greater than, equal to, or between passed date(s)

##### national_id: `str`<a id="national_id-str"></a>

##### national_id_country: `str`<a id="national_id_country-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonDetailsGetSingleCompanyDetailsResponse`](./ukg_python_sdk/pydantic/person_details_get_single_company_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/person-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.person_details.get_single_detail_record`<a id="ukgperson_detailsget_single_detail_record"></a>

Get a single person detail record. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Employee Person Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /person-details/{employeeId}?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /person-details/{employeeId}?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /person-details/{employeeId}?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /person-details/{employeeId}?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_detail_record_response = ukg.person_details.get_single_detail_record(
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EmpPersonDetails`](./ukg_python_sdk/pydantic/emp_person_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/person-details/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.person_details.get_single_record`<a id="ukgperson_detailsget_single_record"></a>

Get a single person detail record for a single company. 
If no pagination parameters specified, the default/max is applied. 
Permissions - UKG Pro service account must have "View" role for the "Employee Person Details" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).
Correct syntax when using date-time parameters are as follows: 
<ul> 
<li>less than (=<) 
  <ul> 
  <li>Example: /companies/{companyId}/employees/{employeeId}/person-details?dateTimeCreated=<01-01-1900</li> 
  </ul> 
  </li>
<li>greater than (=>) 
  <ul> 
  <li>Example: /companies/{companyId}/employees/{employeeId}/person-details?dateTimeCreated=>01-01-1900</li>
  </ul> 
  </li>
<li>equal to (=) 
  <ul>
  <li>Example: /companies/{companyId}/employees/{employeeId}/person-details?dateTimeCreated=01-01-1900</li> 
  </ul>
  </li>
<li>between (={minimum date,maximum date}) 
  <ul>
  <li>Example: /companies/{companyId}/employees/{employeeId}/person-details?dateTimeCreated={01-01-1900,01-01-1901}</li> 
  </ul> 
  </li>
</ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_record_response = ukg.person_details.get_single_record(
    company_id="companyId_example",
    employee_id="employeeId_example",
    company_id2="string_example",
    employee_id2="string_example",
    last_name="string_example",
    email_address="string_example",
    address_state="string_example",
    address_country="string_example",
    cobra_is_active="string_example",
    cobra_status="string_example",
    date_of_cobra_event="string_example",
    date_time_created="string_example",
    date_time_changed="string_example",
    national_id="string_example",
    national_id_country="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### company_id2: `str`<a id="company_id2-str"></a>

##### employee_id2: `str`<a id="employee_id2-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email_address: `str`<a id="email_address-str"></a>

##### address_state: `str`<a id="address_state-str"></a>

##### address_country: `str`<a id="address_country-str"></a>

##### cobra_is_active: `str`<a id="cobra_is_active-str"></a>

##### cobra_status: `str`<a id="cobra_status-str"></a>

##### date_of_cobra_event: `str`<a id="date_of_cobra_event-str"></a>

Used to find date of COBRA event less than, greater than, equal to, or between passed date(s)

##### date_time_created: `str`<a id="date_time_created-str"></a>

Used to find person record created less than, greater than, equal to, or between passed date(s)

##### date_time_changed: `str`<a id="date_time_changed-str"></a>

Used to find person record changed less than, greater than, equal to, or between passed date(s)

##### national_id: `str`<a id="national_id-str"></a>

##### national_id_country: `str`<a id="national_id_country-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PersonDetailsGetSingleRecordResponse`](./ukg_python_sdk/pydantic/person_details_get_single_record_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/employees/{employeeId}/person-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.platform_configuration_custom_fields_schema.get_fields_schema`<a id="ukgplatform_configuration_custom_fields_schemaget_fields_schema"></a>

Gets Platform Configuration standard classes custom fields schema info from the MetaDocument table. <br /> UKG Pro service account must have "View" role for the "Company Configuration Integration" Web Service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fields_schema_response = ukg.platform_configuration_custom_fields_schema.get_fields_schema(
    class_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### class_name: `str`<a id="class_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchema`](./ukg_python_sdk/pydantic/ultimate_software_foundation_services_api_ulti_pro_configuration_platform_configuration_models_pc_field_schema.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/platform-configuration/custom-fields-schema` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.position_report.get`<a id="ukgposition_reportget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).  


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.position_report.get(
    position_code="string_example",
    reports_to_position_code="string_example",
    effective_start_date="1970-01-01T00:00:00.00Z",
    effective_stop_date="1970-01-01T00:00:00.00Z",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### position_code: `str`<a id="position_code-str"></a>

##### reports_to_position_code: `str`<a id="reports_to_position_code-str"></a>

##### effective_start_date: `datetime`<a id="effective_start_date-datetime"></a>

##### effective_stop_date: `datetime`<a id="effective_stop_date-datetime"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PositionReportGetResponse`](./ukg_python_sdk/pydantic/position_report_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/position-report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.positions.list_filtered`<a id="ukgpositionslist_filtered"></a>

If no pagination parameters specified, the default/max is applied.
  Permissions - UKG Pro service account must have "View" role for the "Company Configuration Integration" Api endpoints. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).</br></br>
  
   
   /configuration/v1/position endpoint can take following optional parameter:
  <ul>
    <li>
    companyId :- Can take in multiple IDs separated by comma. ex: [id1, id2]
    </li>
    <li>
    employeeType :- Can take in multiple IDs separated by comma. ex: [id1, id2]
    </li>
    <li>
    payGroupCode :- Can take in multiple IDs separated by comma. ex: [id1, id2]
    </li>
    <li>
    statusCode :- Can take in multiple IDs separated by comma. ex: [id1, id2]
    </li>
    <li>
    positionCode :- Can take in multiple IDs separated by comma. ex: [id1, id2]
    </li>
     <li>
    projectCode :- Can take in multiple IDs separated by comma. ex: [id1, id2]
    </li>
      <li>
    shiftGroupCode :- Can take in multiple IDs separated by comma. ex: [id1, id2]
    </li>
    <li>
    isProrated 
    </li>
    <li>
    isApproved 
    </li>
     <li>
    isEligibleForBenefits
  </li>
 <ul><br/>
 
 Correct syntax when using parameters are as follows: 
  <ul> 
    <li>Get positions without parameter
    <ul> 
    <li>Example: /configuration/v1/positions 
    </ul> 
    </li>
    <li>Get positions by single companyid 
    <ul> 
    <li>Example: /configuration/v1/positions?companyid={companyid}</li>
    </ul> 
    </li>
  <li>Get positions by multiple companyid 
    <ul> 
    <li>Example: /configuration/v1/positions?companyid=[companyid1,companyid2]</li>
    </ul> 
    </li>
    <li>Get positions by positionsCode
    <ul> 
    <li>Example: configuration/v1/positions?positionCode={positionCode}</li>
    </ul> 
    </li>
    <li>Get positions by isEligibleForBenefits 
    <ul> 
    <li>Example: configuration/v1/positions?isEligibleForBenefits={isEligibleForBenefit}</li>
    </ul> 
    </li>
    <li>Get positions by employeeType 
    <ul> 
    <li>Example: configuration/v1/positions?employeeType={employeeType}</li>
    </ul> 
    </li>
    <li>Get positions by statusCode 
    <ul> 
    <li>Example: configuration/v1/positions?statusCode={statusCode}</li>
    </ul> 
    </li>
    <li>Get positions by shiftGroupCode 
    <ul> 
    <li>Example: configuration/v1/positions?shiftGrouptCode={shiftGrouptCode}</li>
    </ul> 
    </li>
     <li>Get positions by using all parameter 
    <ul> 
    <li>Example: configuration/v1/positions?isApproved={isApproved}&employeeType={employeeType}&shiftGroupCode={shiftGroupCode}&isEligibleForBenefits={isEligibleForBenefits}&isProrated={isProrated}&statusCode={statusCode}&payGroupCode={payGroup}&positionCode={positionCode}&projectCode={projectCode}&companyId={companyId}&page={page}&per_Page={per_Page}</li>
    </ul> 
    </li>
  
  </ul>
 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_filtered_response = ukg.positions.list_filtered(
    company_id="string_example",
    employee_type="string_example",
    status_code="string_example",
    pay_group_code="string_example",
    position_code="string_example",
    project_code="string_example",
    shift_group_code="string_example",
    is_prorated=True,
    is_approved=True,
    is_eligible_for_benefits=True,
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_type: `str`<a id="employee_type-str"></a>

##### status_code: `str`<a id="status_code-str"></a>

##### pay_group_code: `str`<a id="pay_group_code-str"></a>

##### position_code: `str`<a id="position_code-str"></a>

##### project_code: `str`<a id="project_code-str"></a>

##### shift_group_code: `str`<a id="shift_group_code-str"></a>

##### is_prorated: `bool`<a id="is_prorated-bool"></a>

##### is_approved: `bool`<a id="is_approved-bool"></a>

##### is_eligible_for_benefits: `bool`<a id="is_eligible_for_benefits-bool"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PositionsListFilteredResponse`](./ukg_python_sdk/pydantic/positions_list_filtered_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/positions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.post_new_token_request.obtain_o_auth_token`<a id="ukgpost_new_token_requestobtain_o_auth_token"></a>

Obtain new token to use in subsequent service requests <b>ONLY</b> for services that use oAuth.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
obtain_o_auth_token_response = ukg.post_new_token_request.obtain_o_auth_token(
    tenant_name="tenant-name_example",
    grant_type="string_example",
    client_id="string_example",
    client_secret="string_example",
    scope="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_name: `str`<a id="tenant_name-str"></a>

Tenant Name provided to you from UltiPro

##### grant_type: `str`<a id="grant_type-str"></a>

You should enter \\\"client_credentials\\\" for this value

##### client_id: `str`<a id="client_id-str"></a>

This is from UltiPro Identity and provided to you

##### client_secret: `str`<a id="client_secret-str"></a>

This is from UltiPro Identity and provided to you

##### scope: `str`<a id="scope-str"></a>

you should enter \\\"profile\\\" for this

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostNewTokenRequestObtainOAuthTokenRequest`](./ukg_python_sdk/type/post_new_token_request_obtain_o_auth_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TokenResponse`](./ukg_python_sdk/pydantic/token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/signin/oauth2/t/{tenant-name}/access_token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.roles_get.security_roles`<a id="ukgroles_getsecurity_roles"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have \"View\" role for the \"Company Configuration Integration\" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
security_roles_response = ukg.roles_get.security_roles(
    rol_name="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rol_name: `str`<a id="rol_name-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Roles`](./ukg_python_sdk/pydantic/roles.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/roles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.schedule_details.publish_details`<a id="ukgschedule_detailspublish_details"></a>

Publish schedule details. Returns a multi-status messages based on detail validation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
publish_details_response = ukg.schedule_details.publish_details(
    schedule_details=[
        {
        }
    ],
    comment="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### schedule_details: List[`ScheduleDetailDto`]<a id="schedule_details-listscheduledetaildto"></a>

##### comment: `str`<a id="comment-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PublishScheduleDetailDto`](./ukg_python_sdk/type/publish_schedule_detail_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ScheduleDetailsPublishDetailsResponse`](./ukg_python_sdk/pydantic/schedule_details_publish_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/schedule_details` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.shift_code.get_data`<a id="ukgshift_codeget_data"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have \"View\" role for the \"Company Configuration Integration\" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_response = ukg.shift_code.get_data(
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ShiftCodeGetDataResponse`](./ukg_python_sdk/pydantic/shift_code_get_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/shift-codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.single_organization_level.get`<a id="ukgsingle_organization_levelget"></a>

The org-levels endpoint returns information about the UltiPro organizational level configurations. The unique identifier for an org-levels configuration, is level and code properties concatenated, therefore both values are needed. Permissions - Ultipro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.single_organization_level.get(
    level="level_example",
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### level: `str`<a id="level-str"></a>

Description of the org-level.

##### code: `str`<a id="code-str"></a>

Organization code.

#### 🔄 Return<a id="🔄-return"></a>

[`OrgLevels`](./ukg_python_sdk/pydantic/org_levels.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/org-levels/{level}/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.single_organization_level.update_org_level`<a id="ukgsingle_organization_levelupdate_org_level"></a>

Allows the ability update a single organizational level configuration. Permissions - Ultipro service account must have "Edit" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_org_level_response = ukg.single_organization_level.update_org_level(
    description="string_example",
    code="string_example",
    level=3.14,
    level="level_example",
    code="code_example",
    budget_group="string_example",
    current_year_budget_fte=3.14,
    current_year_budget_salary=3.14,
    gl_segment="a",
    last_year_budget_fte=3.14,
    last_year_budget_salary=3.14,
    level_description="string_example",
    reporting_category="string_example",
    is_active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### level: `str`<a id="level-str"></a>

Description of the org-level.

##### code: `str`<a id="code-str"></a>

Organization code.

##### requestBody: [`OrgLevels`](./ukg_python_sdk/type/org_levels.py)<a id="requestbody-orglevelsukg_python_sdktypeorg_levelspy"></a>

The org-level to be written.

#### 🔄 Return<a id="🔄-return"></a>

[`OrgLevels`](./ukg_python_sdk/pydantic/org_levels.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/org-levels/{level}/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.single_organization_level.update_properties`<a id="ukgsingle_organization_levelupdate_properties"></a>

Allows the ability update one or more properties of a single org-level configuration. Permissions - Ultipro service account must have "Edit" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_properties_response = ukg.single_organization_level.update_properties(
    description="string_example",
    code="string_example",
    level=3.14,
    level="level_example",
    code="code_example",
    budget_group="string_example",
    current_year_budget_fte=3.14,
    current_year_budget_salary=3.14,
    gl_segment="a",
    last_year_budget_fte=3.14,
    last_year_budget_salary=3.14,
    level_description="string_example",
    reporting_category="string_example",
    is_active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### level: `str`<a id="level-str"></a>

Description of the org-level.

##### code: `str`<a id="code-str"></a>

Organization code.

##### requestBody: [`OrgLevels`](./ukg_python_sdk/type/org_levels.py)<a id="requestbody-orglevelsukg_python_sdktypeorg_levelspy"></a>

The org-level to be written.

#### 🔄 Return<a id="🔄-return"></a>

[`OrgLevels`](./ukg_python_sdk/pydantic/org_levels.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/org-levels/{level}/{code}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.tax_groups.get_all_details`<a id="ukgtax_groupsget_all_details"></a>

taxCalcGroupIdCode optional parameter can take in multiple IDs separated by comma. ex: [id1, id2] and taxGroupIsInactive is also optional. Permissions - UKG Pro service account must have 'View' role for the 'Company Configuration Integration' Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_details_response = ukg.tax_groups.get_all_details(
    tax_calc_group_id_code="string_example",
    tax_group_is_inactive="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tax_calc_group_id_code: `str`<a id="tax_calc_group_id_code-str"></a>

##### tax_group_is_inactive: `str`<a id="tax_group_is_inactive-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TaxGroupsGetAllDetailsResponse`](./ukg_python_sdk/pydantic/tax_groups_get_all_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/tax-groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.teams.get_all`<a id="ukgteamsget_all"></a>

Obtains all teams.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = ukg.teams.get_all(
    index=1,
    max=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### index: `int`<a id="index-int"></a>

Index when paging is to be used.

##### max: `int`<a id="max-int"></a>

Max elements per page

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoWorkbrainTeamDto`](./ukg_python_sdk/pydantic/result_dto_workbrain_team_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.time_codes.get_all`<a id="ukgtime_codesget_all"></a>

Obtains all time codes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = ukg.time_codes.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoTimeCodeDto`](./ukg_python_sdk/pydantic/result_dto_time_code_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/time_codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.time_off_requests.get_all`<a id="ukgtime_off_requestsget_all"></a>

Obtains all time off requests between the specified range.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = ukg.time_off_requests.get_all(
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    emp_name="string_example",
    emp_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `datetime`<a id="_from-datetime"></a>

Start range for requests

##### to: `datetime`<a id="to-datetime"></a>

End range for requests

##### emp_name: `str`<a id="emp_name-str"></a>

##### emp_id: `int`<a id="emp_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoTimeOffRequestDto`](./ukg_python_sdk/pydantic/result_dto_time_off_request_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/timeoff_requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.uta_employee.get_by_co_id_and_ee_id`<a id="ukguta_employeeget_by_co_id_and_ee_id"></a>

Obtains a UTA Employee by coId and eeId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_co_id_and_ee_id_response = ukg.uta_employee.get_by_co_id_and_ee_id(
    coid="coid_example",
    eeid="eeid_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### coid: `str`<a id="coid-str"></a>

coid of employee.

##### eeid: `str`<a id="eeid-str"></a>

eeid of employee.

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoEmployeeDto`](./ukg_python_sdk/pydantic/result_dto_employee_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/simpleschedule/{coid}/employees/{eeid}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.user_preferences.get_user_preferences_details`<a id="ukguser_preferencesget_user_preferences_details"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have \"View\" role for the \"Personnel Integration\" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_preferences_details_response = ukg.user_preferences.get_user_preferences_details(
    user_id="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserPreferencesGetUserPreferencesDetailsResponse`](./ukg_python_sdk/pydantic/user_preferences_get_user_preferences_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/user-preferences` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.user_profile_details.get_all_details`<a id="ukguser_profile_detailsget_all_details"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have \"View\" role for the \"Personnel Integration\" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_details_response = ukg.user_profile_details.get_all_details(
    master_company="string_example",
    user_status="string_example",
    user_id="string_example",
    role_id="string_example",
    company_id="string_example",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### master_company: `str`<a id="master_company-str"></a>

##### user_status: `str`<a id="user_status-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### role_id: `str`<a id="role_id-str"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserProfileDetailsGetAllDetailsResponse`](./ukg_python_sdk/pydantic/user_profile_details_get_all_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/user-profile-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.user_defined_fields.get`<a id="ukguser_defined_fieldsget"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})
<ul> <li>CompanyId parameter can take in multiple company Ids
separated by comma. ex: [ABC, DEF]</li> <li>EmployeeId parameter
can take in multiple employee Ids separated by comma. ex: [ABC,
DEF]</li> </ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = ukg.user_defined_fields.get(
    company_id="string_example",
    employee_id="Cu2LC4aWwWL9Y864DZtaGR",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserDefinedFieldsGetResponse`](./ukg_python_sdk/pydantic/user_defined_fields_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/user-defined-fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.user_defined_fields.get_single_company`<a id="ukguser_defined_fieldsget_single_company"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})
<ul> <li>CompanyId parameter can take in multiple company Ids
separated by comma. ex: [ABC, DEF]</li> <li>EmployeeId parameter
can take in multiple employee Ids separated by comma. ex: [ABC,
DEF]</li> </ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_company_response = ukg.user_defined_fields.get_single_company(
    company_id="companyId_example",
    employee_id="Cu2LC4aWwWL9Y864DZtaGR",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserDefinedFieldsGetSingleCompanyResponse`](./ukg_python_sdk/pydantic/user_defined_fields_get_single_company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/user-defined-fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.user_defined_fields.get_single_employee`<a id="ukguser_defined_fieldsget_single_employee"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})
<ul> <li>CompanyId parameter can take in multiple company Ids
separated by comma. ex: [ABC, DEF]</li> <li>EmployeeId parameter
can take in multiple employee Ids separated by comma. ex: [ABC,
DEF]</li> </ul>


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_employee_response = ukg.user_defined_fields.get_single_employee(
    company_id="companyId_example",
    employee_id="Cu2LC4aWwWL9Y864DZtaGR",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserDefinedFieldsGetSingleEmployeeResponse`](./ukg_python_sdk/pydantic/user_defined_fields_get_single_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/companies/{companyId}/employees/{employeeId}/user-defined-fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.user_details.get_user_details`<a id="ukguser_detailsget_user_details"></a>

If no pagination parameters specified, the default/max is applied. Permissions - UKG Pro service account must have "View" role for the "Personnel Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password})  


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_details_response = ukg.user_details.get_user_details(
    user_name="string_example",
    user_status="string_example",
    employee_id="GqWzyBAw2ZuufUOHOEhA8I",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_name: `str`<a id="user_name-str"></a>

##### user_status: `str`<a id="user_status-str"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### page: `int`<a id="page-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserDetailsGetUserDetailsResponse`](./ukg_python_sdk/pydantic/user_details_get_user_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/user-details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.view_or_create_organization_levels.create_org_level_config`<a id="ukgview_or_create_organization_levelscreate_org_level_config"></a>

Creates a new UltiPro org-level configuration, Array of objects is permitted for multi-records support. Permissions - Ultipro service account must have "Add" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_org_level_config_response = ukg.view_or_create_organization_levels.create_org_level_config(
    body=[
        {
            "description": "description_example",
            "code": "code_example",
            "level": 3.14,
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrgLevelsBody`](./ukg_python_sdk/type/org_levels_body.py)
The org-level to be written.

#### 🔄 Return<a id="🔄-return"></a>

[`MultiStatusResponse`](./ukg_python_sdk/pydantic/multi_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/org-levels` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.view_or_create_organization_levels.get_all_org_levels`<a id="ukgview_or_create_organization_levelsget_all_org_levels"></a>

Returns information about the UltiPro org-level configurations. Permissions - Ultipro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_org_levels_response = ukg.view_or_create_organization_levels.get_all_org_levels(
    level_description="string_example",
    code="string_example",
    budget_group="string_example",
    reporting_category="string_example",
    is_active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### level_description: `str`<a id="level_description-str"></a>

Description of the org-level.

##### code: `str`<a id="code-str"></a>

Organization code.

##### budget_group: `str`<a id="budget_group-str"></a>

Organizational budget group.

##### reporting_category: `str`<a id="reporting_category-str"></a>

Reporting category.

##### is_active: `bool`<a id="is_active-bool"></a>

Active status.

#### 🔄 Return<a id="🔄-return"></a>

[`ViewOrCreateOrganizationLevelsGetAllOrgLevelsResponse`](./ukg_python_sdk/pydantic/view_or_create_organization_levels_get_all_org_levels_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/configuration/v1/org-levels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.allergy.configurations_get`<a id="ukgallergyconfigurations_get"></a>

'The allergy endpoint returns information about the UKG Pro allergy configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
configurations_get_response = ukg.allergy.configurations_get()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AllergyConfigurationsGetResponse`](./ukg_python_sdk/pydantic/allergy_configurations_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/allergy` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.allergy.create_configuration`<a id="ukgallergycreate_configuration"></a>

'Creates a new UKG Pro allergy configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.allergy.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The allergy code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/allergy` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.allergy.update_single_configuration`<a id="ukgallergyupdate_single_configuration"></a>

'Allows the ability update a single allergy configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.allergy.update_single_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/allergy/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.award_type.create_configuration`<a id="ukgaward_typecreate_configuration"></a>

'Creates a new UKG Pro awardType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.award_type.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The awardType code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/awardType` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.award_type.get_all_configurations`<a id="ukgaward_typeget_all_configurations"></a>

'The awardType endpoint returns information about the UKG Pro awardType configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_configurations_response = ukg.award_type.get_all_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AwardTypeGetAllConfigurationsResponse`](./ukg_python_sdk/pydantic/award_type_get_all_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/awardType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.award_type.update_configuration`<a id="ukgaward_typeupdate_configuration"></a>

'Allows the ability update a single awardType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.award_type.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/awardType/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.career_provider.create_configuration_ukg_pro`<a id="ukgcareer_providercreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro careerProvider configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.career_provider.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The careerProvider code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/careerProvider` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.career_provider.get_configurations`<a id="ukgcareer_providerget_configurations"></a>

'The careerProvider endpoint returns information about the UKG Pro careerProvider configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.career_provider.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CareerProviderGetConfigurationsResponse`](./ukg_python_sdk/pydantic/career_provider_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/careerProvider` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.career_provider.update_configuration`<a id="ukgcareer_providerupdate_configuration"></a>

'Allows the ability update a single careerProvider configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.career_provider.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/careerProvider/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.child_support_type.create_configuration_ukg_pro`<a id="ukgchild_support_typecreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro childSupportType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.child_support_type.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The childSupportType code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/childSupportType` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.child_support_type.get_configurations`<a id="ukgchild_support_typeget_configurations"></a>

'The childSupportType endpoint returns information about the UKG Pro childSupportType configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.child_support_type.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ChildSupportTypeGetConfigurationsResponse`](./ukg_python_sdk/pydantic/child_support_type_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/childSupportType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.child_support_type.update_configuration`<a id="ukgchild_support_typeupdate_configuration"></a>

'Allows the ability update a single childSupportType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.child_support_type.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/childSupportType/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.cobra_status.create_configuration`<a id="ukgcobra_statuscreate_configuration"></a>

'Creates a new UKG Pro cobraStatus configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.cobra_status.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The cobraStatus code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cobraStatus` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.cobra_status.get_configurations`<a id="ukgcobra_statusget_configurations"></a>

'The cobraStatus endpoint returns information about the UKG Pro cobraStatus configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.cobra_status.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CobraStatusGetConfigurationsResponse`](./ukg_python_sdk/pydantic/cobra_status_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cobraStatus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.cobra_status.update_single_configuration`<a id="ukgcobra_statusupdate_single_configuration"></a>

'Allows the ability update a single cobraStatus configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.cobra_status.update_single_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cobraStatus/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.company_property.create_configuration_ukg_pro`<a id="ukgcompany_propertycreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro companyProperty configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.company_property.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The companyProperty code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companyProperty` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.company_property.get_configurations`<a id="ukgcompany_propertyget_configurations"></a>

'The companyProperty endpoint returns information about the UKG Pro companyProperty configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.company_property.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyPropertyGetConfigurationsResponse`](./ukg_python_sdk/pydantic/company_property_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companyProperty` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.company_property.update_configuration`<a id="ukgcompany_propertyupdate_configuration"></a>

'Allows the ability update a single companyProperty configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.company_property.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/companyProperty/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_category.create_configuration_ukg_pro`<a id="ukgcourse_categorycreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro courseCategory configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.course_category.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The courseCategory code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseCategory` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_category.get_all_configurations`<a id="ukgcourse_categoryget_all_configurations"></a>

'The courseCategory endpoint returns information about the UKG Pro courseCategory configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_configurations_response = ukg.course_category.get_all_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CourseCategoryGetAllConfigurationsResponse`](./ukg_python_sdk/pydantic/course_category_get_all_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseCategory` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_category.update_configuration`<a id="ukgcourse_categoryupdate_configuration"></a>

'Allows the ability update a single courseCategory configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.course_category.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseCategory/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_delivery_met.create_configuration_ukg_pro`<a id="ukgcourse_delivery_metcreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro courseDeliveryMet configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.course_delivery_met.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The courseDeliveryMet code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseDeliveryMet` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_delivery_met.get_configurations`<a id="ukgcourse_delivery_metget_configurations"></a>

'The courseDeliveryMet endpoint returns information about the UKG Pro courseDeliveryMet configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.course_delivery_met.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CourseDeliveryMetGetConfigurationsResponse`](./ukg_python_sdk/pydantic/course_delivery_met_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseDeliveryMet` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_delivery_met.update_configuration`<a id="ukgcourse_delivery_metupdate_configuration"></a>

'Allows the ability update a single courseDeliveryMet configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.course_delivery_met.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseDeliveryMet/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_sub_category.create_configuration_ukg_pro`<a id="ukgcourse_sub_categorycreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro courseSubCategory configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.course_sub_category.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The courseSubCategory code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseSubCategory` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_sub_category.get_configurations`<a id="ukgcourse_sub_categoryget_configurations"></a>

'The courseSubCategory endpoint returns information about the UKG Pro courseSubCategory configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.course_sub_category.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CourseSubCategoryGetConfigurationsResponse`](./ukg_python_sdk/pydantic/course_sub_category_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseSubCategory` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.course_sub_category.update_configuration`<a id="ukgcourse_sub_categoryupdate_configuration"></a>

'Allows the ability update a single courseSubCategory configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.course_sub_category.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courseSubCategory/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.disability.create_configuration_ukg_pro`<a id="ukgdisabilitycreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro disability configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.disability.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The disability code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/disability` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.disability.get_configurations`<a id="ukgdisabilityget_configurations"></a>

'The disability endpoint returns information about the UKG Pro disability configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.disability.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`DisabilityGetConfigurationsResponse`](./ukg_python_sdk/pydantic/disability_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/disability` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.disability.update_configuration`<a id="ukgdisabilityupdate_configuration"></a>

'Allows the ability update a single disability configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.disability.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/disability/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_type.create_configuration_ukg_pro`<a id="ukgemployee_typecreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro employeeType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.employee_type.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The employeeType code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employeeType` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_type.get_configurations`<a id="ukgemployee_typeget_configurations"></a>

'The employeeType endpoint returns information about the UKG Pro employeeType configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.employee_type.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTypeGetConfigurationsResponse`](./ukg_python_sdk/pydantic/employee_type_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employeeType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.employee_type.update_configuration`<a id="ukgemployee_typeupdate_configuration"></a>

'Allows the ability update a single employeeType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.employee_type.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employeeType/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.job_family.create_configuration`<a id="ukgjob_familycreate_configuration"></a>

'Creates a new UKG Pro jobFamily configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.job_family.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The jobFamily code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobFamily` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.job_family.get_all_configurations`<a id="ukgjob_familyget_all_configurations"></a>

'The jobFamily endpoint returns information about the UKG Pro jobFamily configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_configurations_response = ukg.job_family.get_all_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`JobFamilyGetAllConfigurationsResponse`](./ukg_python_sdk/pydantic/job_family_get_all_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobFamily` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.job_family.update_configuration`<a id="ukgjob_familyupdate_configuration"></a>

'Allows the ability update a single jobFamily configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.job_family.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobFamily/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.jobs.get_all_configurations`<a id="ukgjobsget_all_configurations"></a>

The jobs endpoint returns information about the UltiPro jobs configurations. Permissions - Ultipro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_configurations_response = ukg.jobs.get_all_configurations(
    country_code="string_example",
    is_active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

Job country code.

##### is_active: `bool`<a id="is_active-bool"></a>

Active status.

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetAllConfigurationsResponse`](./ukg_python_sdk/pydantic/jobs_get_all_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.jobs.get_configuration`<a id="ukgjobsget_configuration"></a>

The jobs endpoint returns information about the UltiPro jobs configuration. The unique identifier for a jobs configuration is the code property. Permissions - Ultipro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configuration_response = ukg.jobs.get_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Job code.

#### 🔄 Return<a id="🔄-return"></a>

[`Jobs`](./ukg_python_sdk/pydantic/jobs.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.license_type.create_configuration`<a id="ukglicense_typecreate_configuration"></a>

'Creates a new UKG Pro licenseType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.license_type.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The licenseType code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/licenseType` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.license_type.get_configurations`<a id="ukglicense_typeget_configurations"></a>

'The licenseType endpoint returns information about the UKG Pro licenseType configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.license_type.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LicenseTypeGetConfigurationsResponse`](./ukg_python_sdk/pydantic/license_type_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/licenseType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.license_type.update_configuration`<a id="ukglicense_typeupdate_configuration"></a>

'Allows the ability update a single licenseType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.license_type.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/licenseType/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.loan_type.create_configuration`<a id="ukgloan_typecreate_configuration"></a>

'Creates a new UKG Pro loanType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.loan_type.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The loanType code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/loanType` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.loan_type.get_configurations`<a id="ukgloan_typeget_configurations"></a>

'The loanType endpoint returns information about the UKG Pro loanType configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.loan_type.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LoanTypeGetConfigurationsResponse`](./ukg_python_sdk/pydantic/loan_type_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/loanType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.loan_type.update_configuration`<a id="ukgloan_typeupdate_configuration"></a>

'Allows the ability update a single loanType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.loan_type.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/loanType/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.locations.get_configuration`<a id="ukglocationsget_configuration"></a>

The locations endpoint returns information about the UltiPro locations configuration. The unique identifier for a locations configuration is the code property. Permissions - Ultipro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configuration_response = ukg.locations.get_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

location code.

#### 🔄 Return<a id="🔄-return"></a>

[`Locations`](./ukg_python_sdk/pydantic/locations.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations/{code}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.locations.get_configurations`<a id="ukglocationsget_configurations"></a>

The locations endpoint returns information about the UltiPro locations configurations. Permissions - Ultipro service account must have "View" role for the "Company Configuration Integration" Web Service. Headers - US-Customer-Api-Key, Authorization (base64 encoded {username}:{password}).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.locations.get_configurations(
    country_code="string_example",
    is_active=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

location country code.

##### is_active: `bool`<a id="is_active-bool"></a>

Active status.

#### 🔄 Return<a id="🔄-return"></a>

[`LocationsGetConfigurationsResponse`](./ukg_python_sdk/pydantic/locations_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.marital_status.create_configuration_ukg_pro`<a id="ukgmarital_statuscreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro maritalStatus configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.marital_status.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The maritalStatus code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/maritalStatus` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.marital_status.get_configurations`<a id="ukgmarital_statusget_configurations"></a>

'The maritalStatus endpoint returns information about the UKG Pro maritalStatus configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.marital_status.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MaritalStatusGetConfigurationsResponse`](./ukg_python_sdk/pydantic/marital_status_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/maritalStatus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.marital_status.update_configuration`<a id="ukgmarital_statusupdate_configuration"></a>

'Allows the ability update a single maritalStatus configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.marital_status.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/maritalStatus/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.military_branches.configure_ukg_pro`<a id="ukgmilitary_branchesconfigure_ukg_pro"></a>

'Creates a new UKG Pro militaryBranches configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.military_branches.configure_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The militaryBranches code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/militaryBranches` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.military_branches.get_all_configurations`<a id="ukgmilitary_branchesget_all_configurations"></a>

'The militaryBranches endpoint returns information about the UKG Pro militaryBranches configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_configurations_response = ukg.military_branches.get_all_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MilitaryBranchesGetAllConfigurationsResponse`](./ukg_python_sdk/pydantic/military_branches_get_all_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/militaryBranches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.military_branches.update_configuration`<a id="ukgmilitary_branchesupdate_configuration"></a>

'Allows the ability update a single militaryBranches configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.military_branches.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/militaryBranches/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.military_era.create_configuration_ukg_pro`<a id="ukgmilitary_eracreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro militaryEra configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.military_era.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The militaryEra code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/militaryEra` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.military_era.get_configurations`<a id="ukgmilitary_eraget_configurations"></a>

'The militaryEra endpoint returns information about the UKG Pro militaryEra configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.military_era.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`MilitaryEraGetConfigurationsResponse`](./ukg_python_sdk/pydantic/military_era_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/militaryEra` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.military_era.update_configuration`<a id="ukgmilitary_eraupdate_configuration"></a>

'Allows the ability update a single militaryEra configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.military_era.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/militaryEra/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.name_prefix.configure_name_prefix`<a id="ukgname_prefixconfigure_name_prefix"></a>

'Creates a new UKG Pro namePrefix configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.name_prefix.configure_name_prefix(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The namePrefix code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/namePrefix` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.name_prefix.get_configurations`<a id="ukgname_prefixget_configurations"></a>

'The namePrefix endpoint returns information about the UKG Pro namePrefix configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.name_prefix.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`NamePrefixGetConfigurationsResponse`](./ukg_python_sdk/pydantic/name_prefix_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/namePrefix` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.name_prefix.update_configuration`<a id="ukgname_prefixupdate_configuration"></a>

'Allows the ability update a single namePrefix configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.name_prefix.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/namePrefix/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.other_phone_types.create_configuration_ukg_pro`<a id="ukgother_phone_typescreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro otherPhoneTypes configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.other_phone_types.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The otherPhoneTypes code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/otherPhoneTypes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.other_phone_types.get_configurations`<a id="ukgother_phone_typesget_configurations"></a>

'The otherPhoneTypes endpoint returns information about the UKG Pro otherPhoneTypes configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.other_phone_types.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OtherPhoneTypesGetConfigurationsResponse`](./ukg_python_sdk/pydantic/other_phone_types_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/otherPhoneTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.other_phone_types.update_configuration`<a id="ukgother_phone_typesupdate_configuration"></a>

'Allows the ability update a single otherPhoneTypes configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.other_phone_types.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/otherPhoneTypes/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.project.create_configuration`<a id="ukgprojectcreate_configuration"></a>

'Creates a new UKG Pro project configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.project.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The project code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.project.get_all_configurations`<a id="ukgprojectget_all_configurations"></a>

'The Project endpoint returns information about the UKG Pro Project configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_configurations_response = ukg.project.get_all_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectGetAllConfigurationsResponse`](./ukg_python_sdk/pydantic/project_get_all_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.project.update_configuration`<a id="ukgprojectupdate_configuration"></a>

'Allows the ability update a single project configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.project.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/project/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.school.create_configuration`<a id="ukgschoolcreate_configuration"></a>

'Creates a new UKG Pro school configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.school.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The school code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/school` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.school.get_configurations`<a id="ukgschoolget_configurations"></a>

'The school endpoint returns information about the UKG Pro school configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.school.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SchoolGetConfigurationsResponse`](./ukg_python_sdk/pydantic/school_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/school` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.school.update_configuration`<a id="ukgschoolupdate_configuration"></a>

'Allows the ability update a single school configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.school.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/school/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.skill_proficiency_level.create_configuration_ukg_pro`<a id="ukgskill_proficiency_levelcreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro skillProficiencyLevel configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.skill_proficiency_level.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The skillProficiencyLevel code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skillProficiencyLevel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.skill_proficiency_level.get_all_configurations`<a id="ukgskill_proficiency_levelget_all_configurations"></a>

'The skillProficiencyLevel endpoint returns information about the UKG Pro skillProficiencyLevel configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_configurations_response = ukg.skill_proficiency_level.get_all_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SkillProficiencyLevelGetAllConfigurationsResponse`](./ukg_python_sdk/pydantic/skill_proficiency_level_get_all_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skillProficiencyLevel` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.skill_proficiency_level.update_configuration`<a id="ukgskill_proficiency_levelupdate_configuration"></a>

'Allows the ability update a single skillProficiencyLevel configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.skill_proficiency_level.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skillProficiencyLevel/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.skills.create_configuration`<a id="ukgskillscreate_configuration"></a>

'Creates a new UKG Pro skills configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.skills.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The skills code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skills` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.skills.get_configurations`<a id="ukgskillsget_configurations"></a>

'The skills endpoint returns information about the UKG Pro skills configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.skills.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SkillsGetConfigurationsResponse`](./ukg_python_sdk/pydantic/skills_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skills` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.skills.update_configuration`<a id="ukgskillsupdate_configuration"></a>

'Allows the ability update a single skills configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.skills.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/skills/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.term_type.create_configuration`<a id="ukgterm_typecreate_configuration"></a>

'Creates a new UKG Pro termType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.term_type.create_configuration(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The termType code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/termType` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.term_type.get_configurations`<a id="ukgterm_typeget_configurations"></a>

'The termType endpoint returns information about the UKG Pro termType configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.term_type.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TermTypeGetConfigurationsResponse`](./ukg_python_sdk/pydantic/term_type_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/termType` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.term_type.update_configuration`<a id="ukgterm_typeupdate_configuration"></a>

'Allows the ability update a single termType configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.term_type.update_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/termType/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.time.add_time_entries`<a id="ukgtimeadd_time_entries"></a>

Add multiple Time entries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_time_entries_response = ukg.time.add_time_entries(
    time_data=[
        {
            "date_worked": "1970-01-01T00:00:00.00Z",
            "hours_worked": 3.14,
        }
    ],
    x_correlation_id="X-Correlation-Id_example",
    us_tenant_id="US-Tenant-Id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_data: List[`TimeItem`]<a id="time_data-listtimeitem"></a>

##### x_correlation_id: `str`<a id="x_correlation_id-str"></a>

This value MUST be supplied by the originator, used for tracing

##### us_tenant_id: `str`<a id="us_tenant_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeItemList`](./ukg_python_sdk/type/time_item_list.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeItemList`](./ukg_python_sdk/pydantic/time_item_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hoursWorked` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.time.get_pending_transactions`<a id="ukgtimeget_pending_transactions"></a>

Obtain all pending clock transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pending_transactions_response = ukg.time.get_pending_transactions(
    emp_name="string_example",
    emp_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### emp_name: `str`<a id="emp_name-str"></a>

Employee can be specified by their emp_name or emp_id.  At least one parameter must be specified.

##### emp_id: `int`<a id="emp_id-int"></a>

Employee can be specified by their emp_name or emp_id.  At least one parameter must be specified.

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoClockTransactionDto`](./ukg_python_sdk/pydantic/result_dto_clock_transaction_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/pending_clock_transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.time.get_processed_transactions`<a id="ukgtimeget_processed_transactions"></a>

Obtain all processed clock transactions for a given date.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_processed_transactions_response = ukg.time.get_processed_transactions(
    date="1970-01-01T00:00:00.00Z",
    emp_name="string_example",
    emp_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date: `datetime`<a id="date-datetime"></a>

Date of clock transaction

##### emp_name: `str`<a id="emp_name-str"></a>

Employee can be specified by their emp_name or emp_id.  At least one parameter must be specified.

##### emp_id: `int`<a id="emp_id-int"></a>

Employee can be specified by their emp_name or emp_id.  At least one parameter must be specified.

#### 🔄 Return<a id="🔄-return"></a>

[`ResultDtoClockTransactionDto`](./ukg_python_sdk/pydantic/result_dto_clock_transaction_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/clock_transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.time.get_work_summaries`<a id="ukgtimeget_work_summaries"></a>

Obtain work summaries between the provided date range.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_summaries_response = ukg.time.get_work_summaries(
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    emp_name="string_example",
    emp_id=1,
    full=False,
    auth_status=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `datetime`<a id="_from-datetime"></a>

Start range for work summaries

##### to: `datetime`<a id="to-datetime"></a>

End range for work summaries

##### emp_name: `str`<a id="emp_name-str"></a>

Employee can be specified by their emp_name or emp_id.  At least one parameter must be specified.

##### emp_id: `int`<a id="emp_id-int"></a>

Employee can be specified by their emp_name or emp_id.  At least one parameter must be specified.

##### full: `bool`<a id="full-bool"></a>

Specifies if both clock and work detail data should be loaded

##### auth_status: `bool`<a id="auth_status-bool"></a>

If specified will load only work summaries with Authorized status equal to true or false

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetDtoWorkSummaryDto`](./ukg_python_sdk/pydantic/timesheet_dto_work_summary_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/work_summaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.time.get_work_summary_by_id`<a id="ukgtimeget_work_summary_by_id"></a>

Obtain a work summary by the specified id.  Will load a full work summary (includes clock and work detail information).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_summary_by_id_response = ukg.time.get_work_summary_by_id(
    work_summary_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### work_summary_id: `int`<a id="work_summary_id-int"></a>

Work Summary id

#### 🔄 Return<a id="🔄-return"></a>

[`WorkSummaryDto`](./ukg_python_sdk/pydantic/work_summary_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/work_summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.v1_platform_configuration_custom_fields_data.get_fields_data`<a id="ukgv1_platform_configuration_custom_fields_dataget_fields_data"></a>

Returns information about the UKG Pro Platform Configuration Custom Fields Data. Specifically, each of a classes' custom fields and their respective values. The keyNames, keyValues, employment status, and fields vary and are dependent on the class in question. Classes marked '(not emp specific)' in the list below will not work with the employmentStatus parameter.<br />UKG Pro service account must have "View" role for the "Personnel Integration" Web Service.<br /><b>Supported classes</b>:<br />
1. Address<br />
2. Person<br />
3. PersonName<br />
4. Employee<br />
5. PhoneNumber<br />
6. Employment<br />
7. InternationalEmployee<br />
8. ComponentCompany - (not emp specific)<br />
9. Location - (not emp specific)<br />
10. Job -(not emp specific)<br />
11. OrgLevel1 - (not emp specific)<br />
12. OrgLevel2 - (not emp specific)<br />
13. OrgLevel3 - (not emp specific)<br />
14. OrgLevel4 - (not emp specific).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fields_data_response = ukg.v1_platform_configuration_custom_fields_data.get_fields_data(
    class_name="className_example",
    key_name="string_example",
    key_value="string_example",
    fields="string_example",
    employment_status="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### class_name: `str`<a id="class_name-str"></a>

The name of a supported class, as listed above, to pull custom fields from.

##### key_name: `str`<a id="key_name-str"></a>

Optional keyName to allow filtering results by the corresponding keyValue. keyNames are specific IDs that apply to the class in question.

##### key_value: `str`<a id="key_value-str"></a>

Optional keyValue. Allows filtering results to only include a specific keyValue(s). keyValues correspond to a supplied keyName.

##### fields: `str`<a id="fields-str"></a>

The exact name of a custom field or fields in a comma seperated list. Filters results to only fields with those names.

##### employment_status: `str`<a id="employment_status-str"></a>

Use in junction with employment specific queries to filter custom field results by an internal employment status.

##### page: `int`<a id="page-int"></a>

Offsets results. Used with page number to allow filtering results to a specific range of custom fields.

##### per_page: `int`<a id="per_page-int"></a>

Offsets results. Used with page to allow filtering results to a specific range of custom fields.

#### 🔄 Return<a id="🔄-return"></a>

[`PcFieldsDataGetFieldsDataResponse`](./ukg_python_sdk/pydantic/pc_fields_data_get_fields_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v1/platform-configuration-fields/class-name/{className}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.v2_platform_configuration_custom_fields_data.get_fields_data`<a id="ukgv2_platform_configuration_custom_fields_dataget_fields_data"></a>

This API is similar to the v1 Platform Configuration Fields className API with added support of filtering data by KeyValue. The fields and keyValues are dependent on the class in question - expected key values are listed along with the supported classes below.<br /> 
This API uses pre-defined Views in the UKG Pro database to retrieve the data whereas the v1 version of this API uses functions to retrieve the data.<br />UKG Pro service account must have "View" role for the "Personnel Integration" Web Service.<br /><b>Supported classes</b>:<br />
1. Address (takes value of an employee Id as keyValue)<br />
2. Person (takes value of an employee Id as keyValue)<br />
3. Employee (takes value of an employee Id as keyValue)<br />
4. PhoneNumber (takes value of an employee Id as keyValue)<br />
5. Employment (takes value of an employee Id and a company code as keyValue. Accepted format for keyValue <b>employeeId:companyCode</b>)<br />
6. Location (takes value of a location code as keyValue)<br />
7. Job (takes value of a job code as keyValue)<br />
8. OrgLevel1 (takes value of an org code as keyValue)<br />
9. OrgLevel2 (takes value of an org code as keyValue)<br />
10. OrgLevel3 (takes value of an org code as keyValue)<br />
11. OrgLevel4 (takes value of an org code as keyValue)<br />
12. InternationalEmployee (takes value of an employee Id and a country code as keyValue. Accepted format for keyValue <b>employeeId:countryCode</b>)<br />
13. Contacts (takes value of a SystemId as keyValue)<br /><br /><b>Classes NOT supported</b>:<br />
1. ComponentCompany<br />
2. PersonNames (fields of this class are available in class Person)<br />

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_fields_data_response = ukg.v2_platform_configuration_custom_fields_data.get_fields_data(
    class_name="className_example",
    fields="string_example",
    key_value="string_example",
    page=1,
    per_page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### class_name: `str`<a id="class_name-str"></a>

The name of a supported class, as listed above, to pull custom fields from.

##### fields: `str`<a id="fields-str"></a>

The exact name of a custom field or fields in a comma seperated list. Filters results to only fields with those names.

##### key_value: `str`<a id="key_value-str"></a>

keyValue to filter results by, allowing filtering by specific Ids. This value is dependent on the className, as listed in the implementation notes.

##### page: `int`<a id="page-int"></a>

Offsets results. Used with page number to allow filtering results to a certain range of custom fields.

##### per_page: `int`<a id="per_page-int"></a>

Offsets results. Used with page to allow filtering results to a certain range of custom fields.

#### 🔄 Return<a id="🔄-return"></a>

[`PcFieldsDataV2GetFieldsDataResponse`](./ukg_python_sdk/pydantic/pc_fields_data_v2_get_fields_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/personnel/v2/platform-configuration-fields/class-name/{className}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.waive_reason.create_configuration_ukg_pro`<a id="ukgwaive_reasoncreate_configuration_ukg_pro"></a>

'Creates a new UKG Pro waiveReason configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.waive_reason.create_configuration_ukg_pro(
    description="string_example",
    code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Description.

##### code: `str`<a id="code-str"></a>

Code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CodeObject`](./ukg_python_sdk/type/code_object.py)
The waiveReason code to be written.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/waiveReason` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.waive_reason.get_configurations`<a id="ukgwaive_reasonget_configurations"></a>

'The waiveReason endpoint returns information about the UKG Pro waiveReason configurations.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_configurations_response = ukg.waive_reason.get_configurations()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WaiveReasonGetConfigurationsResponse`](./ukg_python_sdk/pydantic/waive_reason_get_configurations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/waiveReason` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ukg.waive_reason.update_single_configuration`<a id="ukgwaive_reasonupdate_single_configuration"></a>

'Allows the ability update a single waiveReason configuration.'


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ukg.waive_reason.update_single_configuration(
    code="code_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Project code.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/waiveReason/{code}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
