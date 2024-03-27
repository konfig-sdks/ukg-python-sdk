import typing_extensions

from ukg_python_sdk.paths import PathValues
from ukg_python_sdk.apis.paths.personnel_v1_audit_details import PersonnelV1AuditDetails
from ukg_python_sdk.apis.paths.tenant_alias_api_candidates_candidate_id_background_checks import TenantAliasApiCandidatesCandidateIdBackgroundChecks
from ukg_python_sdk.apis.paths.tenant_alias_api_candidates_candidate_id_background_checks_background_check_id import TenantAliasApiCandidatesCandidateIdBackgroundChecksBackgroundCheckId
from ukg_python_sdk.apis.paths.tenant_alias_api_background_check_order_requests import TenantAliasApiBackgroundCheckOrderRequests
from ukg_python_sdk.apis.paths.configuration_v1_businessruleimport_tool_fileupload import ConfigurationV1BusinessruleimportToolFileupload
from ukg_python_sdk.apis.paths.configuration_v1_businessruleimport_tool_filestatus_file_id import ConfigurationV1BusinessruleimportToolFilestatusFileId
from ukg_python_sdk.apis.paths.configuration_v1_businessruleimport_tool_transactionstatus_staging_id import ConfigurationV1BusinessruleimportToolTransactionstatusStagingId
from ukg_python_sdk.apis.paths.configuration_v1_businessruleimport_tool_transaction import ConfigurationV1BusinessruleimportToolTransaction
from ukg_python_sdk.apis.paths.personnel_v1_integration_kronos_business_structure_status import PersonnelV1IntegrationKronosBusinessStructureStatus
from ukg_python_sdk.apis.paths.configuration_v1_code_tables import ConfigurationV1CodeTables
from ukg_python_sdk.apis.paths.configuration_v1_company_details import ConfigurationV1CompanyDetails
from ukg_python_sdk.apis.paths.personnel_v1_compensation_details import PersonnelV1CompensationDetails
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_compensation_details import PersonnelV1CompaniesCompanyIdCompensationDetails
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_employees_employee_id_compensation_details import PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdCompensationDetails
from ukg_python_sdk.apis.paths.personnel_v1_compensation_details_employee_id import PersonnelV1CompensationDetailsEmployeeId
from ukg_python_sdk.apis.paths.personnel_v1_emp_deductions import PersonnelV1EmpDeductions
from ukg_python_sdk.apis.paths.personnel_v1_dep_deductions import PersonnelV1DepDeductions
from ukg_python_sdk.apis.paths.payroll_v1_earnings_history_base_elements import PayrollV1EarningsHistoryBaseElements
from ukg_python_sdk.apis.paths.configuration_v1_earnings import ConfigurationV1Earnings
from ukg_python_sdk.apis.paths.configuration_v1_earnings_calculation_rule_tax_category_use_deduction_offset_country_code_include_in_shift_diffrential_include_in_manual_check import ConfigurationV1EarningsCalculationRuleTaxCategoryUseDeductionOffsetCountryCodeIncludeInShiftDiffrentialIncludeInManualCheck
from ukg_python_sdk.apis.paths.configuration_v1_earnings_earning_code import ConfigurationV1EarningsEarningCode
from ukg_python_sdk.apis.paths.personnel_v1_employee_changes import PersonnelV1EmployeeChanges
from ukg_python_sdk.apis.paths.personnel_v1_employee_changes_employee_id import PersonnelV1EmployeeChangesEmployeeId
from ukg_python_sdk.apis.paths.personnel_v1_employee_cobra_details import PersonnelV1EmployeeCobraDetails
from ukg_python_sdk.apis.paths.personnel_v1_contacts import PersonnelV1Contacts
from ukg_python_sdk.apis.paths.personnel_v1_contacts_contact_id import PersonnelV1ContactsContactId
from ukg_python_sdk.apis.paths.personnel_v1_employee_contract_details import PersonnelV1EmployeeContractDetails
from ukg_python_sdk.apis.paths.personnel_v1_emp_deductions_benefit_option_change_date import PersonnelV1EmpDeductionsBenefitOptionChangeDate
from ukg_python_sdk.apis.paths.personnel_v1_deduction_history_effective_change_dates import PersonnelV1DeductionHistoryEffectiveChangeDates
from ukg_python_sdk.apis.paths.personnel_v1_employee_demographic_details import PersonnelV1EmployeeDemographicDetails
from ukg_python_sdk.apis.paths.payroll_v1_direct_deposit import PayrollV1DirectDeposit
from ukg_python_sdk.apis.paths.payroll_v1_companies_company_id_direct_deposit import PayrollV1CompaniesCompanyIdDirectDeposit
from ukg_python_sdk.apis.paths.personnel_v1_employee_education import PersonnelV1EmployeeEducation
from ukg_python_sdk.apis.paths.personnel_v1_employee_employment_details import PersonnelV1EmployeeEmploymentDetails
from ukg_python_sdk.apis.paths.personnel_v1_employee_extended_elements import PersonnelV1EmployeeExtendedElements
from ukg_python_sdk.apis.paths.personnel_v1_employee_job_history_details import PersonnelV1EmployeeJobHistoryDetails
from ukg_python_sdk.apis.paths.personnel_v1_employee_job_history_details_system_id import PersonnelV1EmployeeJobHistoryDetailsSystemId
from ukg_python_sdk.apis.paths.personnel_v1_employee_ids import PersonnelV1EmployeeIds
from ukg_python_sdk.apis.paths.personnel_v1_empl_multiple_jobs import PersonnelV1EmplMultipleJobs
from ukg_python_sdk.apis.paths.personnel_v1_employee_multi_phone_numbers import PersonnelV1EmployeeMultiPhoneNumbers
from ukg_python_sdk.apis.paths.personnel_v1_empl_multiple_positions import PersonnelV1EmplMultiplePositions
from ukg_python_sdk.apis.paths.personnel_v1_national_documents import PersonnelV1NationalDocuments
from ukg_python_sdk.apis.paths.payroll_v1_companies_pay_statements_summary import PayrollV1CompaniesPayStatementsSummary
from ukg_python_sdk.apis.paths.payroll_v1_companies_pay_statements import PayrollV1CompaniesPayStatements
from ukg_python_sdk.apis.paths.payroll_v1_employees_pay_statements import PayrollV1EmployeesPayStatements
from ukg_python_sdk.apis.paths.payroll_v1_employees_pay_statement_last import PayrollV1EmployeesPayStatementLast
from ukg_python_sdk.apis.paths.payroll_v1_employees_pay_statement_pay_identifier import PayrollV1EmployeesPayStatementPayIdentifier
from ukg_python_sdk.apis.paths.personnel_v1_integration_kronos_employee_profiles import PersonnelV1IntegrationKronosEmployeeProfiles
from ukg_python_sdk.apis.paths.personnel_v1_employee_security_user_details import PersonnelV1EmployeeSecurityUserDetails
from ukg_python_sdk.apis.paths.personnel_v1_integration_kronos_employee_status import PersonnelV1IntegrationKronosEmployeeStatus
from ukg_python_sdk.apis.paths.personnel_v1_employee_supervisor_details import PersonnelV1EmployeeSupervisorDetails
from ukg_python_sdk.apis.paths.personnel_v1_employment_details import PersonnelV1EmploymentDetails
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_employment_details import PersonnelV1CompaniesCompanyIdEmploymentDetails
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_employees_employee_id_employment_details import PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdEmploymentDetails
from ukg_python_sdk.apis.paths.payroll_v2_general_ledger import PayrollV2GeneralLedger
from ukg_python_sdk.apis.paths.payroll_v2_general_ledger_run_id import PayrollV2GeneralLedgerRunId
from ukg_python_sdk.apis.paths.personnel_v1_employee_global_banks import PersonnelV1EmployeeGlobalBanks
from ukg_python_sdk.apis.paths.personnel_v1_employee_global_localization_elements import PersonnelV1EmployeeGlobalLocalizationElements
from ukg_python_sdk.apis.paths.personnel_v1_employee_pay_deduction_elements import PersonnelV1EmployeePayDeductionElements
from ukg_python_sdk.apis.paths.personnel_v1_import_tool import PersonnelV1ImportTool
from ukg_python_sdk.apis.paths.personnel_v1_import_tool_status_staging_id import PersonnelV1ImportToolStatusStagingId
from ukg_python_sdk.apis.paths.configuration_v1_insurance_rate import ConfigurationV1InsuranceRate
from ukg_python_sdk.apis.paths.personnel_v1_integration_audit_configuration import PersonnelV1IntegrationAuditConfiguration
from ukg_python_sdk.apis.paths.personnel_v1_international_employees import PersonnelV1InternationalEmployees
from ukg_python_sdk.apis.paths.personnel_v1_international_employees_employee_id import PersonnelV1InternationalEmployeesEmployeeId
from ukg_python_sdk.apis.paths.configuration_v1_jobgroup import ConfigurationV1Jobgroup
from ukg_python_sdk.apis.paths.jobs_code import JobsCode
from ukg_python_sdk.apis.paths.locations_code import LocationsCode
from ukg_python_sdk.apis.paths.hours_worked import HoursWorked
from ukg_python_sdk.apis.paths.tenants_tenant_identifier_new_hires_id import TenantsTenantIdentifierNewHiresId
from ukg_python_sdk.apis.paths.tenants_tenant_identifier_new_hires import TenantsTenantIdentifierNewHires
from ukg_python_sdk.apis.paths.signin_oauth2_t_tenant_name_access_token import SigninOauth2TTenantNameAccessToken
from ukg_python_sdk.apis.paths.personnel_v1_open_enrollment_dep_deductions import PersonnelV1OpenEnrollmentDepDeductions
from ukg_python_sdk.apis.paths.personnel_v1_open_enrollment_emp_deductions import PersonnelV1OpenEnrollmentEmpDeductions
from ukg_python_sdk.apis.paths.configuration_v1_option_rate import ConfigurationV1OptionRate
from ukg_python_sdk.apis.paths.configuration_v1_org_levels_level_code import ConfigurationV1OrgLevelsLevelCode
from ukg_python_sdk.apis.paths.configuration_v1_org_levels import ConfigurationV1OrgLevels
from ukg_python_sdk.apis.paths.configuration_v1_organization_reporting_category import ConfigurationV1OrganizationReportingCategory
from ukg_python_sdk.apis.paths.payroll_v1_pay_register import PayrollV1PayRegister
from ukg_python_sdk.apis.paths.payroll_v1_paygroup_payperiods import PayrollV1PaygroupPayperiods
from ukg_python_sdk.apis.paths.payroll_v1_payroll_deductions_history import PayrollV1PayrollDeductionsHistory
from ukg_python_sdk.apis.paths.services_payroll_v1_import_pay_items_earnings import ServicesPayrollV1ImportPayItemsEarnings
from ukg_python_sdk.apis.paths.services_payroll_v1_import_pay_items_earnings_ref_id import ServicesPayrollV1ImportPayItemsEarningsRefId
from ukg_python_sdk.apis.paths.personnel_v1_person_details import PersonnelV1PersonDetails
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_person_details import PersonnelV1CompaniesCompanyIdPersonDetails
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_employees_employee_id_person_details import PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPersonDetails
from ukg_python_sdk.apis.paths.personnel_v1_person_details_employee_id import PersonnelV1PersonDetailsEmployeeId
from ukg_python_sdk.apis.paths.personnel_v1_platform_configuration_fields_class_name_class_name import PersonnelV1PlatformConfigurationFieldsClassNameClassName
from ukg_python_sdk.apis.paths.personnel_v2_platform_configuration_fields_class_name_class_name import PersonnelV2PlatformConfigurationFieldsClassNameClassName
from ukg_python_sdk.apis.paths.configuration_v1_platform_configuration_custom_fields_schema import ConfigurationV1PlatformConfigurationCustomFieldsSchema
from ukg_python_sdk.apis.paths.personnel_v1_position_report import PersonnelV1PositionReport
from ukg_python_sdk.apis.paths.configuration_v1_positions import ConfigurationV1Positions
from ukg_python_sdk.apis.paths.personnel_v1_pto_plans import PersonnelV1PtoPlans
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_employees_employee_id_pto_plans_pto_plan import PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPtoPlansPtoPlan
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_employees_employee_id_pto_plans import PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPtoPlans
from ukg_python_sdk.apis.paths.configuration_v1_roles import ConfigurationV1Roles
from ukg_python_sdk.apis.paths.configuration_v1_shift_codes import ConfigurationV1ShiftCodes
from ukg_python_sdk.apis.paths.configuration_v1_tax_groups import ConfigurationV1TaxGroups
from ukg_python_sdk.apis.paths.talent_recruiting_v2_third_party_job_board_integrations_integration_id_postings import TalentRecruitingV2ThirdPartyJobBoardIntegrationsIntegrationIdPostings
from ukg_python_sdk.apis.paths.simpleschedule_activities import SimplescheduleActivities
from ukg_python_sdk.apis.paths.simpleschedule_assigned_holidays import SimplescheduleAssignedHolidays
from ukg_python_sdk.apis.paths.simpleschedule_employee_jobs import SimplescheduleEmployeeJobs
from ukg_python_sdk.apis.paths.simpleschedule_employees import SimplescheduleEmployees
from ukg_python_sdk.apis.paths.simpleschedule_hour_types import SimplescheduleHourTypes
from ukg_python_sdk.apis.paths.simpleschedule_schedule_details import SimplescheduleScheduleDetails
from ukg_python_sdk.apis.paths.simpleschedule_teams import SimplescheduleTeams
from ukg_python_sdk.apis.paths.simpleschedule_time_codes import SimplescheduleTimeCodes
from ukg_python_sdk.apis.paths.simpleschedule_timeoff_requests import SimplescheduleTimeoffRequests
from ukg_python_sdk.apis.paths.simpleschedule_coid_employees_eeid import SimplescheduleCoidEmployeesEeid
from ukg_python_sdk.apis.paths.time_clock_transactions import TimeClockTransactions
from ukg_python_sdk.apis.paths.time_pending_clock_transactions import TimePendingClockTransactions
from ukg_python_sdk.apis.paths.time_work_summaries import TimeWorkSummaries
from ukg_python_sdk.apis.paths.time_work_summary import TimeWorkSummary
from ukg_python_sdk.apis.paths.allergy_code import AllergyCode
from ukg_python_sdk.apis.paths.award_type_code import AwardTypeCode
from ukg_python_sdk.apis.paths.career_provider_code import CareerProviderCode
from ukg_python_sdk.apis.paths.child_support_type_code import ChildSupportTypeCode
from ukg_python_sdk.apis.paths.cobra_status_code import CobraStatusCode
from ukg_python_sdk.apis.paths.company_property_code import CompanyPropertyCode
from ukg_python_sdk.apis.paths.course_category_code import CourseCategoryCode
from ukg_python_sdk.apis.paths.course_delivery_met_code import CourseDeliveryMetCode
from ukg_python_sdk.apis.paths.course_sub_category_code import CourseSubCategoryCode
from ukg_python_sdk.apis.paths.disability_code import DisabilityCode
from ukg_python_sdk.apis.paths.employee_type_code import EmployeeTypeCode
from ukg_python_sdk.apis.paths.job_family_code import JobFamilyCode
from ukg_python_sdk.apis.paths.license_type_code import LicenseTypeCode
from ukg_python_sdk.apis.paths.loan_type_code import LoanTypeCode
from ukg_python_sdk.apis.paths.marital_status_code import MaritalStatusCode
from ukg_python_sdk.apis.paths.military_branches_code import MilitaryBranchesCode
from ukg_python_sdk.apis.paths.military_era_code import MilitaryEraCode
from ukg_python_sdk.apis.paths.name_prefix_code import NamePrefixCode
from ukg_python_sdk.apis.paths.other_phone_types_code import OtherPhoneTypesCode
from ukg_python_sdk.apis.paths.project_code import ProjectCode
from ukg_python_sdk.apis.paths.school_code import SchoolCode
from ukg_python_sdk.apis.paths.skill_proficiency_level_code import SkillProficiencyLevelCode
from ukg_python_sdk.apis.paths.skills_code import SkillsCode
from ukg_python_sdk.apis.paths.term_type_code import TermTypeCode
from ukg_python_sdk.apis.paths.waive_reason_code import WaiveReasonCode
from ukg_python_sdk.apis.paths.personnel_v1_user_defined_fields import PersonnelV1UserDefinedFields
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_user_defined_fields import PersonnelV1CompaniesCompanyIdUserDefinedFields
from ukg_python_sdk.apis.paths.personnel_v1_companies_company_id_employees_employee_id_user_defined_fields import PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdUserDefinedFields
from ukg_python_sdk.apis.paths.personnel_v1_user_details import PersonnelV1UserDetails
from ukg_python_sdk.apis.paths.personnel_v1_user_preferences import PersonnelV1UserPreferences
from ukg_python_sdk.apis.paths.personnel_v1_user_profile_details import PersonnelV1UserProfileDetails
from ukg_python_sdk.apis.paths.jobs import Jobs
from ukg_python_sdk.apis.paths.locations import Locations
from ukg_python_sdk.apis.paths.allergy import Allergy
from ukg_python_sdk.apis.paths.award_type import AwardType
from ukg_python_sdk.apis.paths.career_provider import CareerProvider
from ukg_python_sdk.apis.paths.child_support_type import ChildSupportType
from ukg_python_sdk.apis.paths.cobra_status import CobraStatus
from ukg_python_sdk.apis.paths.company_property import CompanyProperty
from ukg_python_sdk.apis.paths.course_category import CourseCategory
from ukg_python_sdk.apis.paths.course_delivery_met import CourseDeliveryMet
from ukg_python_sdk.apis.paths.course_sub_category import CourseSubCategory
from ukg_python_sdk.apis.paths.disability import Disability
from ukg_python_sdk.apis.paths.employee_type import EmployeeType
from ukg_python_sdk.apis.paths.job_family import JobFamily
from ukg_python_sdk.apis.paths.license_type import LicenseType
from ukg_python_sdk.apis.paths.loan_type import LoanType
from ukg_python_sdk.apis.paths.marital_status import MaritalStatus
from ukg_python_sdk.apis.paths.military_branches import MilitaryBranches
from ukg_python_sdk.apis.paths.military_era import MilitaryEra
from ukg_python_sdk.apis.paths.name_prefix import NamePrefix
from ukg_python_sdk.apis.paths.other_phone_types import OtherPhoneTypes
from ukg_python_sdk.apis.paths.project import Project
from ukg_python_sdk.apis.paths.school import School
from ukg_python_sdk.apis.paths.skill_proficiency_level import SkillProficiencyLevel
from ukg_python_sdk.apis.paths.skills import Skills
from ukg_python_sdk.apis.paths.term_type import TermType
from ukg_python_sdk.apis.paths.waive_reason import WaiveReason

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PERSONNEL_V1_AUDITDETAILS: PersonnelV1AuditDetails,
        PathValues.TENANTALIAS_API_CANDIDATES_CANDIDATEID_BACKGROUNDCHECKS: TenantAliasApiCandidatesCandidateIdBackgroundChecks,
        PathValues.TENANTALIAS_API_CANDIDATES_CANDIDATEID_BACKGROUNDCHECKS_BACKGROUNDCHECKID: TenantAliasApiCandidatesCandidateIdBackgroundChecksBackgroundCheckId,
        PathValues.TENANTALIAS_API_BACKGROUNDCHECKORDERREQUESTS: TenantAliasApiBackgroundCheckOrderRequests,
        PathValues.CONFIGURATION_V1_BUSINESSRULEIMPORTTOOL_FILEUPLOAD: ConfigurationV1BusinessruleimportToolFileupload,
        PathValues.CONFIGURATION_V1_BUSINESSRULEIMPORTTOOL_FILESTATUS_FILE_ID: ConfigurationV1BusinessruleimportToolFilestatusFileId,
        PathValues.CONFIGURATION_V1_BUSINESSRULEIMPORTTOOL_TRANSACTIONSTATUS_STAGING_ID: ConfigurationV1BusinessruleimportToolTransactionstatusStagingId,
        PathValues.CONFIGURATION_V1_BUSINESSRULEIMPORTTOOL_TRANSACTION: ConfigurationV1BusinessruleimportToolTransaction,
        PathValues.PERSONNEL_V1_INTEGRATION_KRONOS_BUSINESSSTRUCTURESTATUS: PersonnelV1IntegrationKronosBusinessStructureStatus,
        PathValues.CONFIGURATION_V1_CODETABLES: ConfigurationV1CodeTables,
        PathValues.CONFIGURATION_V1_COMPANYDETAILS: ConfigurationV1CompanyDetails,
        PathValues.PERSONNEL_V1_COMPENSATIONDETAILS: PersonnelV1CompensationDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_COMPENSATIONDETAILS: PersonnelV1CompaniesCompanyIdCompensationDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_COMPENSATIONDETAILS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdCompensationDetails,
        PathValues.PERSONNEL_V1_COMPENSATIONDETAILS_EMPLOYEE_ID: PersonnelV1CompensationDetailsEmployeeId,
        PathValues.PERSONNEL_V1_EMPDEDUCTIONS: PersonnelV1EmpDeductions,
        PathValues.PERSONNEL_V1_DEPDEDUCTIONS: PersonnelV1DepDeductions,
        PathValues.PAYROLL_V1_EARNINGSHISTORYBASEELEMENTS: PayrollV1EarningsHistoryBaseElements,
        PathValues.CONFIGURATION_V1_EARNINGS: ConfigurationV1Earnings,
        PathValues.CONFIGURATION_V1_EARNINGS_CALCULATION_RULE_TAX_CATEGORY_USE_DEDUCTION_OFFSET_COUNTRY_CODE_INCLUDE_IN_SHIFT_DIFFRENTIAL_INCLUDE_IN_MANUAL_CHECK: ConfigurationV1EarningsCalculationRuleTaxCategoryUseDeductionOffsetCountryCodeIncludeInShiftDiffrentialIncludeInManualCheck,
        PathValues.CONFIGURATION_V1_EARNINGS_EARNING_CODE: ConfigurationV1EarningsEarningCode,
        PathValues.PERSONNEL_V1_EMPLOYEECHANGES: PersonnelV1EmployeeChanges,
        PathValues.PERSONNEL_V1_EMPLOYEECHANGES_EMPLOYEE_ID: PersonnelV1EmployeeChangesEmployeeId,
        PathValues.PERSONNEL_V1_EMPLOYEECOBRADETAILS: PersonnelV1EmployeeCobraDetails,
        PathValues.PERSONNEL_V1_CONTACTS: PersonnelV1Contacts,
        PathValues.PERSONNEL_V1_CONTACTS_CONTACT_ID: PersonnelV1ContactsContactId,
        PathValues.PERSONNEL_V1_EMPLOYEECONTRACTDETAILS: PersonnelV1EmployeeContractDetails,
        PathValues.PERSONNEL_V1_EMPDEDUCTIONSBENEFITOPTIONCHANGEDATE: PersonnelV1EmpDeductionsBenefitOptionChangeDate,
        PathValues.PERSONNEL_V1_DEDUCTIONHISTORYEFFECTIVECHANGEDATES: PersonnelV1DeductionHistoryEffectiveChangeDates,
        PathValues.PERSONNEL_V1_EMPLOYEEDEMOGRAPHICDETAILS: PersonnelV1EmployeeDemographicDetails,
        PathValues.PAYROLL_V1_DIRECTDEPOSIT: PayrollV1DirectDeposit,
        PathValues.PAYROLL_V1_COMPANIES_COMPANY_ID_DIRECTDEPOSIT: PayrollV1CompaniesCompanyIdDirectDeposit,
        PathValues.PERSONNEL_V1_EMPLOYEEEDUCATION: PersonnelV1EmployeeEducation,
        PathValues.PERSONNEL_V1_EMPLOYEEEMPLOYMENTDETAILS: PersonnelV1EmployeeEmploymentDetails,
        PathValues.PERSONNEL_V1_EMPLOYEEEXTENDEDELEMENTS: PersonnelV1EmployeeExtendedElements,
        PathValues.PERSONNEL_V1_EMPLOYEEJOBHISTORYDETAILS: PersonnelV1EmployeeJobHistoryDetails,
        PathValues.PERSONNEL_V1_EMPLOYEEJOBHISTORYDETAILS_SYSTEM_ID: PersonnelV1EmployeeJobHistoryDetailsSystemId,
        PathValues.PERSONNEL_V1_EMPLOYEEIDS: PersonnelV1EmployeeIds,
        PathValues.PERSONNEL_V1_EMPLMULTIPLEJOBS: PersonnelV1EmplMultipleJobs,
        PathValues.PERSONNEL_V1_EMPLOYEEMULTIPHONENUMBERS: PersonnelV1EmployeeMultiPhoneNumbers,
        PathValues.PERSONNEL_V1_EMPLMULTIPLEPOSITIONS: PersonnelV1EmplMultiplePositions,
        PathValues.PERSONNEL_V1_NATIONALDOCUMENTS: PersonnelV1NationalDocuments,
        PathValues.PAYROLL_V1_COMPANIES_PAYSTATEMENTSSUMMARY: PayrollV1CompaniesPayStatementsSummary,
        PathValues.PAYROLL_V1_COMPANIES_PAYSTATEMENTS: PayrollV1CompaniesPayStatements,
        PathValues.PAYROLL_V1_EMPLOYEES_PAYSTATEMENTS: PayrollV1EmployeesPayStatements,
        PathValues.PAYROLL_V1_EMPLOYEES_PAYSTATEMENT_LAST: PayrollV1EmployeesPayStatementLast,
        PathValues.PAYROLL_V1_EMPLOYEES_PAYSTATEMENT_PAY_IDENTIFIER: PayrollV1EmployeesPayStatementPayIdentifier,
        PathValues.PERSONNEL_V1_INTEGRATION_KRONOS_EMPLOYEEPROFILES: PersonnelV1IntegrationKronosEmployeeProfiles,
        PathValues.PERSONNEL_V1_EMPLOYEESECURITYUSERDETAILS: PersonnelV1EmployeeSecurityUserDetails,
        PathValues.PERSONNEL_V1_INTEGRATION_KRONOS_EMPLOYEESTATUS: PersonnelV1IntegrationKronosEmployeeStatus,
        PathValues.PERSONNEL_V1_EMPLOYEESUPERVISORDETAILS: PersonnelV1EmployeeSupervisorDetails,
        PathValues.PERSONNEL_V1_EMPLOYMENTDETAILS: PersonnelV1EmploymentDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYMENTDETAILS: PersonnelV1CompaniesCompanyIdEmploymentDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_EMPLOYMENTDETAILS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdEmploymentDetails,
        PathValues.PAYROLL_V2_GENERALLEDGER: PayrollV2GeneralLedger,
        PathValues.PAYROLL_V2_GENERALLEDGER_RUN_ID: PayrollV2GeneralLedgerRunId,
        PathValues.PERSONNEL_V1_EMPLOYEEGLOBALBANKS: PersonnelV1EmployeeGlobalBanks,
        PathValues.PERSONNEL_V1_EMPLOYEEGLOBALLOCALIZATIONELEMENTS: PersonnelV1EmployeeGlobalLocalizationElements,
        PathValues.PERSONNEL_V1_EMPLOYEEPAYDEDUCTIONELEMENTS: PersonnelV1EmployeePayDeductionElements,
        PathValues.PERSONNEL_V1_IMPORTTOOL: PersonnelV1ImportTool,
        PathValues.PERSONNEL_V1_IMPORTTOOL_STATUS_STAGING_ID: PersonnelV1ImportToolStatusStagingId,
        PathValues.CONFIGURATION_V1_INSURANCERATE: ConfigurationV1InsuranceRate,
        PathValues.PERSONNEL_V1_INTEGRATIONAUDITCONFIGURATION: PersonnelV1IntegrationAuditConfiguration,
        PathValues.PERSONNEL_V1_INTERNATIONALEMPLOYEES: PersonnelV1InternationalEmployees,
        PathValues.PERSONNEL_V1_INTERNATIONALEMPLOYEES_EMPLOYEE_ID: PersonnelV1InternationalEmployeesEmployeeId,
        PathValues.CONFIGURATION_V1_JOBGROUP: ConfigurationV1Jobgroup,
        PathValues.JOBS_CODE: JobsCode,
        PathValues.LOCATIONS_CODE: LocationsCode,
        PathValues.HOURS_WORKED: HoursWorked,
        PathValues.TENANTS_TENANT_IDENTIFIER_NEWHIRES_ID: TenantsTenantIdentifierNewHiresId,
        PathValues.TENANTS_TENANT_IDENTIFIER_NEWHIRES: TenantsTenantIdentifierNewHires,
        PathValues.SIGNIN_OAUTH2_T_TENANTNAME_ACCESS_TOKEN: SigninOauth2TTenantNameAccessToken,
        PathValues.PERSONNEL_V1_OPENENROLLMENTDEPDEDUCTIONS: PersonnelV1OpenEnrollmentDepDeductions,
        PathValues.PERSONNEL_V1_OPENENROLLMENTEMPDEDUCTIONS: PersonnelV1OpenEnrollmentEmpDeductions,
        PathValues.CONFIGURATION_V1_OPTIONRATE: ConfigurationV1OptionRate,
        PathValues.CONFIGURATION_V1_ORGLEVELS_LEVEL_CODE: ConfigurationV1OrgLevelsLevelCode,
        PathValues.CONFIGURATION_V1_ORGLEVELS: ConfigurationV1OrgLevels,
        PathValues.CONFIGURATION_V1_ORGANIZATIONREPORTINGCATEGORY: ConfigurationV1OrganizationReportingCategory,
        PathValues.PAYROLL_V1_PAYREGISTER: PayrollV1PayRegister,
        PathValues.PAYROLL_V1_PAYGROUPPAYPERIODS: PayrollV1PaygroupPayperiods,
        PathValues.PAYROLL_V1_PAYROLLDEDUCTIONSHISTORY: PayrollV1PayrollDeductionsHistory,
        PathValues.SERVICES_PAYROLL_V1_IMPORTPAYITEMS_EARNINGS: ServicesPayrollV1ImportPayItemsEarnings,
        PathValues.SERVICES_PAYROLL_V1_IMPORTPAYITEMS_EARNINGS_REF_ID: ServicesPayrollV1ImportPayItemsEarningsRefId,
        PathValues.PERSONNEL_V1_PERSONDETAILS: PersonnelV1PersonDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_PERSONDETAILS: PersonnelV1CompaniesCompanyIdPersonDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PERSONDETAILS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPersonDetails,
        PathValues.PERSONNEL_V1_PERSONDETAILS_EMPLOYEE_ID: PersonnelV1PersonDetailsEmployeeId,
        PathValues.PERSONNEL_V1_PLATFORMCONFIGURATIONFIELDS_CLASSNAME_CLASS_NAME: PersonnelV1PlatformConfigurationFieldsClassNameClassName,
        PathValues.PERSONNEL_V2_PLATFORMCONFIGURATIONFIELDS_CLASSNAME_CLASS_NAME: PersonnelV2PlatformConfigurationFieldsClassNameClassName,
        PathValues.CONFIGURATION_V1_PLATFORMCONFIGURATION_CUSTOMFIELDSSCHEMA: ConfigurationV1PlatformConfigurationCustomFieldsSchema,
        PathValues.PERSONNEL_V1_POSITIONREPORT: PersonnelV1PositionReport,
        PathValues.CONFIGURATION_V1_POSITIONS: ConfigurationV1Positions,
        PathValues.PERSONNEL_V1_PTOPLANS: PersonnelV1PtoPlans,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PTOPLANS_PTO_PLAN: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPtoPlansPtoPlan,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PTOPLANS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPtoPlans,
        PathValues.CONFIGURATION_V1_ROLES: ConfigurationV1Roles,
        PathValues.CONFIGURATION_V1_SHIFTCODES: ConfigurationV1ShiftCodes,
        PathValues.CONFIGURATION_V1_TAXGROUPS: ConfigurationV1TaxGroups,
        PathValues.TALENT_RECRUITING_V2_THIRDPARTYJOBBOARDINTEGRATIONS_INTEGRATION_ID_POSTINGS: TalentRecruitingV2ThirdPartyJobBoardIntegrationsIntegrationIdPostings,
        PathValues.SIMPLESCHEDULE_ACTIVITIES: SimplescheduleActivities,
        PathValues.SIMPLESCHEDULE_ASSIGNED_HOLIDAYS: SimplescheduleAssignedHolidays,
        PathValues.SIMPLESCHEDULE_EMPLOYEE_JOBS: SimplescheduleEmployeeJobs,
        PathValues.SIMPLESCHEDULE_EMPLOYEES: SimplescheduleEmployees,
        PathValues.SIMPLESCHEDULE_HOUR_TYPES: SimplescheduleHourTypes,
        PathValues.SIMPLESCHEDULE_SCHEDULE_DETAILS: SimplescheduleScheduleDetails,
        PathValues.SIMPLESCHEDULE_TEAMS: SimplescheduleTeams,
        PathValues.SIMPLESCHEDULE_TIME_CODES: SimplescheduleTimeCodes,
        PathValues.SIMPLESCHEDULE_TIMEOFF_REQUESTS: SimplescheduleTimeoffRequests,
        PathValues.SIMPLESCHEDULE_COID_EMPLOYEES_EEID: SimplescheduleCoidEmployeesEeid,
        PathValues.TIME_CLOCK_TRANSACTIONS: TimeClockTransactions,
        PathValues.TIME_PENDING_CLOCK_TRANSACTIONS: TimePendingClockTransactions,
        PathValues.TIME_WORK_SUMMARIES: TimeWorkSummaries,
        PathValues.TIME_WORK_SUMMARY: TimeWorkSummary,
        PathValues.ALLERGY_CODE: AllergyCode,
        PathValues.AWARD_TYPE_CODE: AwardTypeCode,
        PathValues.CAREER_PROVIDER_CODE: CareerProviderCode,
        PathValues.CHILD_SUPPORT_TYPE_CODE: ChildSupportTypeCode,
        PathValues.COBRA_STATUS_CODE: CobraStatusCode,
        PathValues.COMPANY_PROPERTY_CODE: CompanyPropertyCode,
        PathValues.COURSE_CATEGORY_CODE: CourseCategoryCode,
        PathValues.COURSE_DELIVERY_MET_CODE: CourseDeliveryMetCode,
        PathValues.COURSE_SUB_CATEGORY_CODE: CourseSubCategoryCode,
        PathValues.DISABILITY_CODE: DisabilityCode,
        PathValues.EMPLOYEE_TYPE_CODE: EmployeeTypeCode,
        PathValues.JOB_FAMILY_CODE: JobFamilyCode,
        PathValues.LICENSE_TYPE_CODE: LicenseTypeCode,
        PathValues.LOAN_TYPE_CODE: LoanTypeCode,
        PathValues.MARITAL_STATUS_CODE: MaritalStatusCode,
        PathValues.MILITARY_BRANCHES_CODE: MilitaryBranchesCode,
        PathValues.MILITARY_ERA_CODE: MilitaryEraCode,
        PathValues.NAME_PREFIX_CODE: NamePrefixCode,
        PathValues.OTHER_PHONE_TYPES_CODE: OtherPhoneTypesCode,
        PathValues.PROJECT_CODE: ProjectCode,
        PathValues.SCHOOL_CODE: SchoolCode,
        PathValues.SKILL_PROFICIENCY_LEVEL_CODE: SkillProficiencyLevelCode,
        PathValues.SKILLS_CODE: SkillsCode,
        PathValues.TERM_TYPE_CODE: TermTypeCode,
        PathValues.WAIVE_REASON_CODE: WaiveReasonCode,
        PathValues.PERSONNEL_V1_USERDEFINEDFIELDS: PersonnelV1UserDefinedFields,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_USERDEFINEDFIELDS: PersonnelV1CompaniesCompanyIdUserDefinedFields,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_USERDEFINEDFIELDS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdUserDefinedFields,
        PathValues.PERSONNEL_V1_USERDETAILS: PersonnelV1UserDetails,
        PathValues.PERSONNEL_V1_USERPREFERENCES: PersonnelV1UserPreferences,
        PathValues.PERSONNEL_V1_USERPROFILEDETAILS: PersonnelV1UserProfileDetails,
        PathValues.JOBS: Jobs,
        PathValues.LOCATIONS: Locations,
        PathValues.ALLERGY: Allergy,
        PathValues.AWARD_TYPE: AwardType,
        PathValues.CAREER_PROVIDER: CareerProvider,
        PathValues.CHILD_SUPPORT_TYPE: ChildSupportType,
        PathValues.COBRA_STATUS: CobraStatus,
        PathValues.COMPANY_PROPERTY: CompanyProperty,
        PathValues.COURSE_CATEGORY: CourseCategory,
        PathValues.COURSE_DELIVERY_MET: CourseDeliveryMet,
        PathValues.COURSE_SUB_CATEGORY: CourseSubCategory,
        PathValues.DISABILITY: Disability,
        PathValues.EMPLOYEE_TYPE: EmployeeType,
        PathValues.JOB_FAMILY: JobFamily,
        PathValues.LICENSE_TYPE: LicenseType,
        PathValues.LOAN_TYPE: LoanType,
        PathValues.MARITAL_STATUS: MaritalStatus,
        PathValues.MILITARY_BRANCHES: MilitaryBranches,
        PathValues.MILITARY_ERA: MilitaryEra,
        PathValues.NAME_PREFIX: NamePrefix,
        PathValues.OTHER_PHONE_TYPES: OtherPhoneTypes,
        PathValues.PROJECT: Project,
        PathValues.SCHOOL: School,
        PathValues.SKILL_PROFICIENCY_LEVEL: SkillProficiencyLevel,
        PathValues.SKILLS: Skills,
        PathValues.TERM_TYPE: TermType,
        PathValues.WAIVE_REASON: WaiveReason,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PERSONNEL_V1_AUDITDETAILS: PersonnelV1AuditDetails,
        PathValues.TENANTALIAS_API_CANDIDATES_CANDIDATEID_BACKGROUNDCHECKS: TenantAliasApiCandidatesCandidateIdBackgroundChecks,
        PathValues.TENANTALIAS_API_CANDIDATES_CANDIDATEID_BACKGROUNDCHECKS_BACKGROUNDCHECKID: TenantAliasApiCandidatesCandidateIdBackgroundChecksBackgroundCheckId,
        PathValues.TENANTALIAS_API_BACKGROUNDCHECKORDERREQUESTS: TenantAliasApiBackgroundCheckOrderRequests,
        PathValues.CONFIGURATION_V1_BUSINESSRULEIMPORTTOOL_FILEUPLOAD: ConfigurationV1BusinessruleimportToolFileupload,
        PathValues.CONFIGURATION_V1_BUSINESSRULEIMPORTTOOL_FILESTATUS_FILE_ID: ConfigurationV1BusinessruleimportToolFilestatusFileId,
        PathValues.CONFIGURATION_V1_BUSINESSRULEIMPORTTOOL_TRANSACTIONSTATUS_STAGING_ID: ConfigurationV1BusinessruleimportToolTransactionstatusStagingId,
        PathValues.CONFIGURATION_V1_BUSINESSRULEIMPORTTOOL_TRANSACTION: ConfigurationV1BusinessruleimportToolTransaction,
        PathValues.PERSONNEL_V1_INTEGRATION_KRONOS_BUSINESSSTRUCTURESTATUS: PersonnelV1IntegrationKronosBusinessStructureStatus,
        PathValues.CONFIGURATION_V1_CODETABLES: ConfigurationV1CodeTables,
        PathValues.CONFIGURATION_V1_COMPANYDETAILS: ConfigurationV1CompanyDetails,
        PathValues.PERSONNEL_V1_COMPENSATIONDETAILS: PersonnelV1CompensationDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_COMPENSATIONDETAILS: PersonnelV1CompaniesCompanyIdCompensationDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_COMPENSATIONDETAILS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdCompensationDetails,
        PathValues.PERSONNEL_V1_COMPENSATIONDETAILS_EMPLOYEE_ID: PersonnelV1CompensationDetailsEmployeeId,
        PathValues.PERSONNEL_V1_EMPDEDUCTIONS: PersonnelV1EmpDeductions,
        PathValues.PERSONNEL_V1_DEPDEDUCTIONS: PersonnelV1DepDeductions,
        PathValues.PAYROLL_V1_EARNINGSHISTORYBASEELEMENTS: PayrollV1EarningsHistoryBaseElements,
        PathValues.CONFIGURATION_V1_EARNINGS: ConfigurationV1Earnings,
        PathValues.CONFIGURATION_V1_EARNINGS_CALCULATION_RULE_TAX_CATEGORY_USE_DEDUCTION_OFFSET_COUNTRY_CODE_INCLUDE_IN_SHIFT_DIFFRENTIAL_INCLUDE_IN_MANUAL_CHECK: ConfigurationV1EarningsCalculationRuleTaxCategoryUseDeductionOffsetCountryCodeIncludeInShiftDiffrentialIncludeInManualCheck,
        PathValues.CONFIGURATION_V1_EARNINGS_EARNING_CODE: ConfigurationV1EarningsEarningCode,
        PathValues.PERSONNEL_V1_EMPLOYEECHANGES: PersonnelV1EmployeeChanges,
        PathValues.PERSONNEL_V1_EMPLOYEECHANGES_EMPLOYEE_ID: PersonnelV1EmployeeChangesEmployeeId,
        PathValues.PERSONNEL_V1_EMPLOYEECOBRADETAILS: PersonnelV1EmployeeCobraDetails,
        PathValues.PERSONNEL_V1_CONTACTS: PersonnelV1Contacts,
        PathValues.PERSONNEL_V1_CONTACTS_CONTACT_ID: PersonnelV1ContactsContactId,
        PathValues.PERSONNEL_V1_EMPLOYEECONTRACTDETAILS: PersonnelV1EmployeeContractDetails,
        PathValues.PERSONNEL_V1_EMPDEDUCTIONSBENEFITOPTIONCHANGEDATE: PersonnelV1EmpDeductionsBenefitOptionChangeDate,
        PathValues.PERSONNEL_V1_DEDUCTIONHISTORYEFFECTIVECHANGEDATES: PersonnelV1DeductionHistoryEffectiveChangeDates,
        PathValues.PERSONNEL_V1_EMPLOYEEDEMOGRAPHICDETAILS: PersonnelV1EmployeeDemographicDetails,
        PathValues.PAYROLL_V1_DIRECTDEPOSIT: PayrollV1DirectDeposit,
        PathValues.PAYROLL_V1_COMPANIES_COMPANY_ID_DIRECTDEPOSIT: PayrollV1CompaniesCompanyIdDirectDeposit,
        PathValues.PERSONNEL_V1_EMPLOYEEEDUCATION: PersonnelV1EmployeeEducation,
        PathValues.PERSONNEL_V1_EMPLOYEEEMPLOYMENTDETAILS: PersonnelV1EmployeeEmploymentDetails,
        PathValues.PERSONNEL_V1_EMPLOYEEEXTENDEDELEMENTS: PersonnelV1EmployeeExtendedElements,
        PathValues.PERSONNEL_V1_EMPLOYEEJOBHISTORYDETAILS: PersonnelV1EmployeeJobHistoryDetails,
        PathValues.PERSONNEL_V1_EMPLOYEEJOBHISTORYDETAILS_SYSTEM_ID: PersonnelV1EmployeeJobHistoryDetailsSystemId,
        PathValues.PERSONNEL_V1_EMPLOYEEIDS: PersonnelV1EmployeeIds,
        PathValues.PERSONNEL_V1_EMPLMULTIPLEJOBS: PersonnelV1EmplMultipleJobs,
        PathValues.PERSONNEL_V1_EMPLOYEEMULTIPHONENUMBERS: PersonnelV1EmployeeMultiPhoneNumbers,
        PathValues.PERSONNEL_V1_EMPLMULTIPLEPOSITIONS: PersonnelV1EmplMultiplePositions,
        PathValues.PERSONNEL_V1_NATIONALDOCUMENTS: PersonnelV1NationalDocuments,
        PathValues.PAYROLL_V1_COMPANIES_PAYSTATEMENTSSUMMARY: PayrollV1CompaniesPayStatementsSummary,
        PathValues.PAYROLL_V1_COMPANIES_PAYSTATEMENTS: PayrollV1CompaniesPayStatements,
        PathValues.PAYROLL_V1_EMPLOYEES_PAYSTATEMENTS: PayrollV1EmployeesPayStatements,
        PathValues.PAYROLL_V1_EMPLOYEES_PAYSTATEMENT_LAST: PayrollV1EmployeesPayStatementLast,
        PathValues.PAYROLL_V1_EMPLOYEES_PAYSTATEMENT_PAY_IDENTIFIER: PayrollV1EmployeesPayStatementPayIdentifier,
        PathValues.PERSONNEL_V1_INTEGRATION_KRONOS_EMPLOYEEPROFILES: PersonnelV1IntegrationKronosEmployeeProfiles,
        PathValues.PERSONNEL_V1_EMPLOYEESECURITYUSERDETAILS: PersonnelV1EmployeeSecurityUserDetails,
        PathValues.PERSONNEL_V1_INTEGRATION_KRONOS_EMPLOYEESTATUS: PersonnelV1IntegrationKronosEmployeeStatus,
        PathValues.PERSONNEL_V1_EMPLOYEESUPERVISORDETAILS: PersonnelV1EmployeeSupervisorDetails,
        PathValues.PERSONNEL_V1_EMPLOYMENTDETAILS: PersonnelV1EmploymentDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYMENTDETAILS: PersonnelV1CompaniesCompanyIdEmploymentDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_EMPLOYMENTDETAILS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdEmploymentDetails,
        PathValues.PAYROLL_V2_GENERALLEDGER: PayrollV2GeneralLedger,
        PathValues.PAYROLL_V2_GENERALLEDGER_RUN_ID: PayrollV2GeneralLedgerRunId,
        PathValues.PERSONNEL_V1_EMPLOYEEGLOBALBANKS: PersonnelV1EmployeeGlobalBanks,
        PathValues.PERSONNEL_V1_EMPLOYEEGLOBALLOCALIZATIONELEMENTS: PersonnelV1EmployeeGlobalLocalizationElements,
        PathValues.PERSONNEL_V1_EMPLOYEEPAYDEDUCTIONELEMENTS: PersonnelV1EmployeePayDeductionElements,
        PathValues.PERSONNEL_V1_IMPORTTOOL: PersonnelV1ImportTool,
        PathValues.PERSONNEL_V1_IMPORTTOOL_STATUS_STAGING_ID: PersonnelV1ImportToolStatusStagingId,
        PathValues.CONFIGURATION_V1_INSURANCERATE: ConfigurationV1InsuranceRate,
        PathValues.PERSONNEL_V1_INTEGRATIONAUDITCONFIGURATION: PersonnelV1IntegrationAuditConfiguration,
        PathValues.PERSONNEL_V1_INTERNATIONALEMPLOYEES: PersonnelV1InternationalEmployees,
        PathValues.PERSONNEL_V1_INTERNATIONALEMPLOYEES_EMPLOYEE_ID: PersonnelV1InternationalEmployeesEmployeeId,
        PathValues.CONFIGURATION_V1_JOBGROUP: ConfigurationV1Jobgroup,
        PathValues.JOBS_CODE: JobsCode,
        PathValues.LOCATIONS_CODE: LocationsCode,
        PathValues.HOURS_WORKED: HoursWorked,
        PathValues.TENANTS_TENANT_IDENTIFIER_NEWHIRES_ID: TenantsTenantIdentifierNewHiresId,
        PathValues.TENANTS_TENANT_IDENTIFIER_NEWHIRES: TenantsTenantIdentifierNewHires,
        PathValues.SIGNIN_OAUTH2_T_TENANTNAME_ACCESS_TOKEN: SigninOauth2TTenantNameAccessToken,
        PathValues.PERSONNEL_V1_OPENENROLLMENTDEPDEDUCTIONS: PersonnelV1OpenEnrollmentDepDeductions,
        PathValues.PERSONNEL_V1_OPENENROLLMENTEMPDEDUCTIONS: PersonnelV1OpenEnrollmentEmpDeductions,
        PathValues.CONFIGURATION_V1_OPTIONRATE: ConfigurationV1OptionRate,
        PathValues.CONFIGURATION_V1_ORGLEVELS_LEVEL_CODE: ConfigurationV1OrgLevelsLevelCode,
        PathValues.CONFIGURATION_V1_ORGLEVELS: ConfigurationV1OrgLevels,
        PathValues.CONFIGURATION_V1_ORGANIZATIONREPORTINGCATEGORY: ConfigurationV1OrganizationReportingCategory,
        PathValues.PAYROLL_V1_PAYREGISTER: PayrollV1PayRegister,
        PathValues.PAYROLL_V1_PAYGROUPPAYPERIODS: PayrollV1PaygroupPayperiods,
        PathValues.PAYROLL_V1_PAYROLLDEDUCTIONSHISTORY: PayrollV1PayrollDeductionsHistory,
        PathValues.SERVICES_PAYROLL_V1_IMPORTPAYITEMS_EARNINGS: ServicesPayrollV1ImportPayItemsEarnings,
        PathValues.SERVICES_PAYROLL_V1_IMPORTPAYITEMS_EARNINGS_REF_ID: ServicesPayrollV1ImportPayItemsEarningsRefId,
        PathValues.PERSONNEL_V1_PERSONDETAILS: PersonnelV1PersonDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_PERSONDETAILS: PersonnelV1CompaniesCompanyIdPersonDetails,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PERSONDETAILS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPersonDetails,
        PathValues.PERSONNEL_V1_PERSONDETAILS_EMPLOYEE_ID: PersonnelV1PersonDetailsEmployeeId,
        PathValues.PERSONNEL_V1_PLATFORMCONFIGURATIONFIELDS_CLASSNAME_CLASS_NAME: PersonnelV1PlatformConfigurationFieldsClassNameClassName,
        PathValues.PERSONNEL_V2_PLATFORMCONFIGURATIONFIELDS_CLASSNAME_CLASS_NAME: PersonnelV2PlatformConfigurationFieldsClassNameClassName,
        PathValues.CONFIGURATION_V1_PLATFORMCONFIGURATION_CUSTOMFIELDSSCHEMA: ConfigurationV1PlatformConfigurationCustomFieldsSchema,
        PathValues.PERSONNEL_V1_POSITIONREPORT: PersonnelV1PositionReport,
        PathValues.CONFIGURATION_V1_POSITIONS: ConfigurationV1Positions,
        PathValues.PERSONNEL_V1_PTOPLANS: PersonnelV1PtoPlans,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PTOPLANS_PTO_PLAN: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPtoPlansPtoPlan,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_PTOPLANS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdPtoPlans,
        PathValues.CONFIGURATION_V1_ROLES: ConfigurationV1Roles,
        PathValues.CONFIGURATION_V1_SHIFTCODES: ConfigurationV1ShiftCodes,
        PathValues.CONFIGURATION_V1_TAXGROUPS: ConfigurationV1TaxGroups,
        PathValues.TALENT_RECRUITING_V2_THIRDPARTYJOBBOARDINTEGRATIONS_INTEGRATION_ID_POSTINGS: TalentRecruitingV2ThirdPartyJobBoardIntegrationsIntegrationIdPostings,
        PathValues.SIMPLESCHEDULE_ACTIVITIES: SimplescheduleActivities,
        PathValues.SIMPLESCHEDULE_ASSIGNED_HOLIDAYS: SimplescheduleAssignedHolidays,
        PathValues.SIMPLESCHEDULE_EMPLOYEE_JOBS: SimplescheduleEmployeeJobs,
        PathValues.SIMPLESCHEDULE_EMPLOYEES: SimplescheduleEmployees,
        PathValues.SIMPLESCHEDULE_HOUR_TYPES: SimplescheduleHourTypes,
        PathValues.SIMPLESCHEDULE_SCHEDULE_DETAILS: SimplescheduleScheduleDetails,
        PathValues.SIMPLESCHEDULE_TEAMS: SimplescheduleTeams,
        PathValues.SIMPLESCHEDULE_TIME_CODES: SimplescheduleTimeCodes,
        PathValues.SIMPLESCHEDULE_TIMEOFF_REQUESTS: SimplescheduleTimeoffRequests,
        PathValues.SIMPLESCHEDULE_COID_EMPLOYEES_EEID: SimplescheduleCoidEmployeesEeid,
        PathValues.TIME_CLOCK_TRANSACTIONS: TimeClockTransactions,
        PathValues.TIME_PENDING_CLOCK_TRANSACTIONS: TimePendingClockTransactions,
        PathValues.TIME_WORK_SUMMARIES: TimeWorkSummaries,
        PathValues.TIME_WORK_SUMMARY: TimeWorkSummary,
        PathValues.ALLERGY_CODE: AllergyCode,
        PathValues.AWARD_TYPE_CODE: AwardTypeCode,
        PathValues.CAREER_PROVIDER_CODE: CareerProviderCode,
        PathValues.CHILD_SUPPORT_TYPE_CODE: ChildSupportTypeCode,
        PathValues.COBRA_STATUS_CODE: CobraStatusCode,
        PathValues.COMPANY_PROPERTY_CODE: CompanyPropertyCode,
        PathValues.COURSE_CATEGORY_CODE: CourseCategoryCode,
        PathValues.COURSE_DELIVERY_MET_CODE: CourseDeliveryMetCode,
        PathValues.COURSE_SUB_CATEGORY_CODE: CourseSubCategoryCode,
        PathValues.DISABILITY_CODE: DisabilityCode,
        PathValues.EMPLOYEE_TYPE_CODE: EmployeeTypeCode,
        PathValues.JOB_FAMILY_CODE: JobFamilyCode,
        PathValues.LICENSE_TYPE_CODE: LicenseTypeCode,
        PathValues.LOAN_TYPE_CODE: LoanTypeCode,
        PathValues.MARITAL_STATUS_CODE: MaritalStatusCode,
        PathValues.MILITARY_BRANCHES_CODE: MilitaryBranchesCode,
        PathValues.MILITARY_ERA_CODE: MilitaryEraCode,
        PathValues.NAME_PREFIX_CODE: NamePrefixCode,
        PathValues.OTHER_PHONE_TYPES_CODE: OtherPhoneTypesCode,
        PathValues.PROJECT_CODE: ProjectCode,
        PathValues.SCHOOL_CODE: SchoolCode,
        PathValues.SKILL_PROFICIENCY_LEVEL_CODE: SkillProficiencyLevelCode,
        PathValues.SKILLS_CODE: SkillsCode,
        PathValues.TERM_TYPE_CODE: TermTypeCode,
        PathValues.WAIVE_REASON_CODE: WaiveReasonCode,
        PathValues.PERSONNEL_V1_USERDEFINEDFIELDS: PersonnelV1UserDefinedFields,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_USERDEFINEDFIELDS: PersonnelV1CompaniesCompanyIdUserDefinedFields,
        PathValues.PERSONNEL_V1_COMPANIES_COMPANY_ID_EMPLOYEES_EMPLOYEE_ID_USERDEFINEDFIELDS: PersonnelV1CompaniesCompanyIdEmployeesEmployeeIdUserDefinedFields,
        PathValues.PERSONNEL_V1_USERDETAILS: PersonnelV1UserDetails,
        PathValues.PERSONNEL_V1_USERPREFERENCES: PersonnelV1UserPreferences,
        PathValues.PERSONNEL_V1_USERPROFILEDETAILS: PersonnelV1UserProfileDetails,
        PathValues.JOBS: Jobs,
        PathValues.LOCATIONS: Locations,
        PathValues.ALLERGY: Allergy,
        PathValues.AWARD_TYPE: AwardType,
        PathValues.CAREER_PROVIDER: CareerProvider,
        PathValues.CHILD_SUPPORT_TYPE: ChildSupportType,
        PathValues.COBRA_STATUS: CobraStatus,
        PathValues.COMPANY_PROPERTY: CompanyProperty,
        PathValues.COURSE_CATEGORY: CourseCategory,
        PathValues.COURSE_DELIVERY_MET: CourseDeliveryMet,
        PathValues.COURSE_SUB_CATEGORY: CourseSubCategory,
        PathValues.DISABILITY: Disability,
        PathValues.EMPLOYEE_TYPE: EmployeeType,
        PathValues.JOB_FAMILY: JobFamily,
        PathValues.LICENSE_TYPE: LicenseType,
        PathValues.LOAN_TYPE: LoanType,
        PathValues.MARITAL_STATUS: MaritalStatus,
        PathValues.MILITARY_BRANCHES: MilitaryBranches,
        PathValues.MILITARY_ERA: MilitaryEra,
        PathValues.NAME_PREFIX: NamePrefix,
        PathValues.OTHER_PHONE_TYPES: OtherPhoneTypes,
        PathValues.PROJECT: Project,
        PathValues.SCHOOL: School,
        PathValues.SKILL_PROFICIENCY_LEVEL: SkillProficiencyLevel,
        PathValues.SKILLS: Skills,
        PathValues.TERM_TYPE: TermType,
        PathValues.WAIVE_REASON: WaiveReason,
    }
)
