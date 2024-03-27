import typing_extensions

from ukg_python_sdk.apis.tags import TagValues
from ukg_python_sdk.apis.tags.time_api import TimeApi
from ukg_python_sdk.apis.tags.business_rule_import_tool_api import BusinessRuleImportToolApi
from ukg_python_sdk.apis.tags.compensation_details_api import CompensationDetailsApi
from ukg_python_sdk.apis.tags.person_details_api import PersonDetailsApi
from ukg_python_sdk.apis.tags.earnings_api import EarningsApi
from ukg_python_sdk.apis.tags.employee_pay_statement_api import EmployeePayStatementApi
from ukg_python_sdk.apis.tags.employment_details_api import EmploymentDetailsApi
from ukg_python_sdk.apis.tags.single_organization_level_api import SingleOrganizationLevelApi
from ukg_python_sdk.apis.tags.allergy_api import AllergyApi
from ukg_python_sdk.apis.tags.award_type_api import AwardTypeApi
from ukg_python_sdk.apis.tags.career_provider_api import CareerProviderApi
from ukg_python_sdk.apis.tags.child_support_type_api import ChildSupportTypeApi
from ukg_python_sdk.apis.tags.cobra_status_api import CobraStatusApi
from ukg_python_sdk.apis.tags.company_property_api import CompanyPropertyApi
from ukg_python_sdk.apis.tags.course_category_api import CourseCategoryApi
from ukg_python_sdk.apis.tags.course_delivery_met_api import CourseDeliveryMetApi
from ukg_python_sdk.apis.tags.course_sub_category_api import CourseSubCategoryApi
from ukg_python_sdk.apis.tags.disability_api import DisabilityApi
from ukg_python_sdk.apis.tags.employee_type_api import EmployeeTypeApi
from ukg_python_sdk.apis.tags.job_family_api import JobFamilyApi
from ukg_python_sdk.apis.tags.license_type_api import LicenseTypeApi
from ukg_python_sdk.apis.tags.loan_type_api import LoanTypeApi
from ukg_python_sdk.apis.tags.marital_status_api import MaritalStatusApi
from ukg_python_sdk.apis.tags.military_branches_api import MilitaryBranchesApi
from ukg_python_sdk.apis.tags.military_era_api import MilitaryEraApi
from ukg_python_sdk.apis.tags.name_prefix_api import NamePrefixApi
from ukg_python_sdk.apis.tags.other_phone_types_api import OtherPhoneTypesApi
from ukg_python_sdk.apis.tags.project_api import ProjectApi
from ukg_python_sdk.apis.tags.school_api import SchoolApi
from ukg_python_sdk.apis.tags.skill_proficiency_level_api import SkillProficiencyLevelApi
from ukg_python_sdk.apis.tags.skills_api import SkillsApi
from ukg_python_sdk.apis.tags.term_type_api import TermTypeApi
from ukg_python_sdk.apis.tags.waive_reason_api import WaiveReasonApi
from ukg_python_sdk.apis.tags.user_defined_fields_api import UserDefinedFieldsApi
from ukg_python_sdk.apis.tags.candidate_request_api import CandidateRequestApi
from ukg_python_sdk.apis.tags.code_tables_api import CodeTablesApi
from ukg_python_sdk.apis.tags.contact_api import ContactApi
from ukg_python_sdk.apis.tags.direct_deposit_api import DirectDepositApi
from ukg_python_sdk.apis.tags.employee_job_history_detail_api import EmployeeJobHistoryDetailApi
from ukg_python_sdk.apis.tags.company_pay_statement_api import CompanyPayStatementApi
from ukg_python_sdk.apis.tags.general_ledger_run_details_v2_api import GeneralLedgerRunDetailsV2Api
from ukg_python_sdk.apis.tags.import_tool_api import ImportToolApi
from ukg_python_sdk.apis.tags.international_employee_api import InternationalEmployeeApi
from ukg_python_sdk.apis.tags.jobs_api import JobsApi
from ukg_python_sdk.apis.tags.locations_api import LocationsApi
from ukg_python_sdk.apis.tags.new_hires_api import NewHiresApi
from ukg_python_sdk.apis.tags.view_or_create_organization_levels_api import ViewOrCreateOrganizationLevelsApi
from ukg_python_sdk.apis.tags.audit_details_api import AuditDetailsApi
from ukg_python_sdk.apis.tags.order_requests_api import OrderRequestsApi
from ukg_python_sdk.apis.tags.business_structure_status_api import BusinessStructureStatusApi
from ukg_python_sdk.apis.tags.company_details_api import CompanyDetailsApi
from ukg_python_sdk.apis.tags.emp_deductions_api import EmpDeductionsApi
from ukg_python_sdk.apis.tags.dependent_deductions_api import DependentDeductionsApi
from ukg_python_sdk.apis.tags.earnings_history_api import EarningsHistoryApi
from ukg_python_sdk.apis.tags.changes_by_date_api import ChangesByDateApi
from ukg_python_sdk.apis.tags.employee_changes_api import EmployeeChangesApi
from ukg_python_sdk.apis.tags.employee_cobra_details_api import EmployeeCobraDetailsApi
from ukg_python_sdk.apis.tags.employee_contract_api import EmployeeContractApi
from ukg_python_sdk.apis.tags.emp_ded_ben_option_date_api import EmpDedBenOptionDateApi
from ukg_python_sdk.apis.tags.employee_deduction_history_effective_date_api import EmployeeDeductionHistoryEffectiveDateApi
from ukg_python_sdk.apis.tags.employee_demographic_details_api import EmployeeDemographicDetailsApi
from ukg_python_sdk.apis.tags.employee_education_api import EmployeeEducationApi
from ukg_python_sdk.apis.tags.employee_employment_details_api import EmployeeEmploymentDetailsApi
from ukg_python_sdk.apis.tags.employee_extended_elements_api import EmployeeExtendedElementsApi
from ukg_python_sdk.apis.tags.employee_id_lookup_api import EmployeeIDLookupApi
from ukg_python_sdk.apis.tags.employee_multiple_jobs_opp_api import EmployeeMultipleJobsOPPApi
from ukg_python_sdk.apis.tags.employee_multi_phone_numbers_api import EmployeeMultiPhoneNumbersApi
from ukg_python_sdk.apis.tags.emp_multiple_positions_api import EmpMultiplePositionsApi
from ukg_python_sdk.apis.tags.national_document_api import NationalDocumentApi
from ukg_python_sdk.apis.tags.kronos_employee_profiles_api import KronosEmployeeProfilesApi
from ukg_python_sdk.apis.tags.employee_security_user_details_api import EmployeeSecurityUserDetailsApi
from ukg_python_sdk.apis.tags.kronos_employee_status_api import KronosEmployeeStatusApi
from ukg_python_sdk.apis.tags.employee_supervisor_details_api import EmployeeSupervisorDetailsApi
from ukg_python_sdk.apis.tags.employee_global_bank_api import EmployeeGlobalBankApi
from ukg_python_sdk.apis.tags.emp_global_localization_element_api import EmpGlobalLocalizationElementApi
from ukg_python_sdk.apis.tags.employee_pay_deduction_element_api import EmployeePayDeductionElementApi
from ukg_python_sdk.apis.tags.ins_rate_api import InsRateApi
from ukg_python_sdk.apis.tags.integration_audit_configuration_api import IntegrationAuditConfigurationApi
from ukg_python_sdk.apis.tags.job_group_api import JobGroupApi
from ukg_python_sdk.apis.tags.post_new_token_request_api import PostNewTokenRequestApi
from ukg_python_sdk.apis.tags.open_enrollment_dependent_deductions_api import OpenEnrollmentDependentDeductionsApi
from ukg_python_sdk.apis.tags.open_enrollment_employee_deductions_api import OpenEnrollmentEmployeeDeductionsApi
from ukg_python_sdk.apis.tags.option_rate_api import OptionRateApi
from ukg_python_sdk.apis.tags.organization_reporting_category_api import OrganizationReportingCategoryApi
from ukg_python_sdk.apis.tags.pay_register_api import PayRegisterApi
from ukg_python_sdk.apis.tags.pay_group_pay_period_api import PayGroupPayPeriodApi
from ukg_python_sdk.apis.tags.payroll_deductions_history_api import PayrollDeductionsHistoryApi
from ukg_python_sdk.apis.tags.v1_platform_configuration_custom_fields_data_api import V1PlatformConfigurationCustomFieldsDataApi
from ukg_python_sdk.apis.tags.v2_platform_configuration_custom_fields_data_api import V2PlatformConfigurationCustomFieldsDataApi
from ukg_python_sdk.apis.tags.platform_configuration_custom_fields_schema_api import PlatformConfigurationCustomFieldsSchemaApi
from ukg_python_sdk.apis.tags.position_report_api import PositionReportApi
from ukg_python_sdk.apis.tags.positions_api import PositionsApi
from ukg_python_sdk.apis.tags.get_all_pto_plans_api import GetAllPTOPlansApi
from ukg_python_sdk.apis.tags.pto_plan_post_api import PTOPlanPostApi
from ukg_python_sdk.apis.tags.get_specific_pto_plan_api import GetSpecificPTOPlanApi
from ukg_python_sdk.apis.tags.pto_plan_patch_api import PTOPlanPatchApi
from ukg_python_sdk.apis.tags.get_specific_employees_pto_plans_api import GetSpecificEmployeesPTOPlansApi
from ukg_python_sdk.apis.tags.roles_get_api import RolesGetApi
from ukg_python_sdk.apis.tags.shift_code_api import ShiftCodeApi
from ukg_python_sdk.apis.tags.tax_groups_api import TaxGroupsApi
from ukg_python_sdk.apis.tags.get_job_postings_api import GetJobPostingsApi
from ukg_python_sdk.apis.tags.activities_api import ActivitiesApi
from ukg_python_sdk.apis.tags.assigned_holidays_api import AssignedHolidaysApi
from ukg_python_sdk.apis.tags.employee_jobs_api import EmployeeJobsApi
from ukg_python_sdk.apis.tags.employees_api import EmployeesApi
from ukg_python_sdk.apis.tags.hour_types_api import HourTypesApi
from ukg_python_sdk.apis.tags.schedule_details_api import ScheduleDetailsApi
from ukg_python_sdk.apis.tags.teams_api import TeamsApi
from ukg_python_sdk.apis.tags.time_codes_api import TimeCodesApi
from ukg_python_sdk.apis.tags.time_off_requests_api import TimeOffRequestsApi
from ukg_python_sdk.apis.tags.uta_employee_api import UTAEmployeeApi
from ukg_python_sdk.apis.tags.user_details_api import UserDetailsApi
from ukg_python_sdk.apis.tags.user_preferences_api import UserPreferencesApi
from ukg_python_sdk.apis.tags.user_profile_details_api import UserProfileDetailsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TIME: TimeApi,
        TagValues.BUSINESS_RULE_IMPORT_TOOL: BusinessRuleImportToolApi,
        TagValues.COMPENSATION_DETAILS: CompensationDetailsApi,
        TagValues.PERSON_DETAILS: PersonDetailsApi,
        TagValues.EARNINGS: EarningsApi,
        TagValues.EMPLOYEE_PAY_STATEMENT: EmployeePayStatementApi,
        TagValues.EMPLOYMENT_DETAILS: EmploymentDetailsApi,
        TagValues.SINGLE_ORGANIZATION_LEVEL: SingleOrganizationLevelApi,
        TagValues.ALLERGY: AllergyApi,
        TagValues.AWARD_TYPE: AwardTypeApi,
        TagValues.CAREER_PROVIDER: CareerProviderApi,
        TagValues.CHILD_SUPPORT_TYPE: ChildSupportTypeApi,
        TagValues.COBRA_STATUS: CobraStatusApi,
        TagValues.COMPANY_PROPERTY: CompanyPropertyApi,
        TagValues.COURSE_CATEGORY: CourseCategoryApi,
        TagValues.COURSE_DELIVERY_MET: CourseDeliveryMetApi,
        TagValues.COURSE_SUB_CATEGORY: CourseSubCategoryApi,
        TagValues.DISABILITY: DisabilityApi,
        TagValues.EMPLOYEE_TYPE: EmployeeTypeApi,
        TagValues.JOB_FAMILY: JobFamilyApi,
        TagValues.LICENSE_TYPE: LicenseTypeApi,
        TagValues.LOAN_TYPE: LoanTypeApi,
        TagValues.MARITAL_STATUS: MaritalStatusApi,
        TagValues.MILITARY_BRANCHES: MilitaryBranchesApi,
        TagValues.MILITARY_ERA: MilitaryEraApi,
        TagValues.NAME_PREFIX: NamePrefixApi,
        TagValues.OTHER_PHONE_TYPES: OtherPhoneTypesApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.SCHOOL: SchoolApi,
        TagValues.SKILL_PROFICIENCY_LEVEL: SkillProficiencyLevelApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.TERM_TYPE: TermTypeApi,
        TagValues.WAIVE_REASON: WaiveReasonApi,
        TagValues.USER_DEFINED_FIELDS: UserDefinedFieldsApi,
        TagValues.CANDIDATE_REQUEST: CandidateRequestApi,
        TagValues.CODE_TABLES: CodeTablesApi,
        TagValues.CONTACT: ContactApi,
        TagValues.DIRECT_DEPOSIT: DirectDepositApi,
        TagValues.EMPLOYEE_JOB_HISTORY_DETAIL: EmployeeJobHistoryDetailApi,
        TagValues.COMPANY_PAY_STATEMENT: CompanyPayStatementApi,
        TagValues.GENERAL_LEDGER_RUN_DETAILS_V2: GeneralLedgerRunDetailsV2Api,
        TagValues.IMPORT_TOOL: ImportToolApi,
        TagValues.INTERNATIONAL_EMPLOYEE: InternationalEmployeeApi,
        TagValues.JOBS: JobsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.NEW_HIRES: NewHiresApi,
        TagValues.VIEW_OR_CREATE_ORGANIZATION_LEVELS: ViewOrCreateOrganizationLevelsApi,
        TagValues.AUDIT_DETAILS: AuditDetailsApi,
        TagValues.ORDER_REQUESTS: OrderRequestsApi,
        TagValues.BUSINESS_STRUCTURE_STATUS: BusinessStructureStatusApi,
        TagValues.COMPANY_DETAILS: CompanyDetailsApi,
        TagValues.EMP_DEDUCTIONS: EmpDeductionsApi,
        TagValues.DEPENDENT_DEDUCTIONS: DependentDeductionsApi,
        TagValues.EARNINGS_HISTORY: EarningsHistoryApi,
        TagValues.CHANGES_BY_DATE: ChangesByDateApi,
        TagValues.EMPLOYEE_CHANGES: EmployeeChangesApi,
        TagValues.EMPLOYEE_COBRA_DETAILS: EmployeeCobraDetailsApi,
        TagValues.EMPLOYEE_CONTRACT: EmployeeContractApi,
        TagValues.EMP_DED_BEN_OPTION_DATE: EmpDedBenOptionDateApi,
        TagValues.EMPLOYEE_DEDUCTION_HISTORY_EFFECTIVE_DATE: EmployeeDeductionHistoryEffectiveDateApi,
        TagValues.EMPLOYEE_DEMOGRAPHIC_DETAILS: EmployeeDemographicDetailsApi,
        TagValues.EMPLOYEE_EDUCATION: EmployeeEducationApi,
        TagValues.EMPLOYEE_EMPLOYMENT_DETAILS: EmployeeEmploymentDetailsApi,
        TagValues.EMPLOYEE_EXTENDED_ELEMENTS: EmployeeExtendedElementsApi,
        TagValues.EMPLOYEE_ID_LOOKUP: EmployeeIDLookupApi,
        TagValues.EMPLOYEE_MULTIPLE_JOBS_OPP: EmployeeMultipleJobsOPPApi,
        TagValues.EMPLOYEE_MULTI_PHONE_NUMBERS: EmployeeMultiPhoneNumbersApi,
        TagValues.EMP_MULTIPLE_POSITIONS: EmpMultiplePositionsApi,
        TagValues.NATIONAL_DOCUMENT: NationalDocumentApi,
        TagValues.KRONOS_EMPLOYEE_PROFILES: KronosEmployeeProfilesApi,
        TagValues.EMPLOYEE_SECURITY_USER_DETAILS: EmployeeSecurityUserDetailsApi,
        TagValues.KRONOS_EMPLOYEE_STATUS: KronosEmployeeStatusApi,
        TagValues.EMPLOYEE_SUPERVISOR_DETAILS: EmployeeSupervisorDetailsApi,
        TagValues.EMPLOYEE_GLOBAL_BANK: EmployeeGlobalBankApi,
        TagValues.EMP_GLOBAL_LOCALIZATION_ELEMENT: EmpGlobalLocalizationElementApi,
        TagValues.EMPLOYEE_PAY_DEDUCTION_ELEMENT: EmployeePayDeductionElementApi,
        TagValues.INS_RATE: InsRateApi,
        TagValues.INTEGRATION_AUDIT_CONFIGURATION: IntegrationAuditConfigurationApi,
        TagValues.JOB_GROUP: JobGroupApi,
        TagValues.POST_NEW_TOKEN_REQUEST: PostNewTokenRequestApi,
        TagValues.OPEN_ENROLLMENT_DEPENDENT_DEDUCTIONS: OpenEnrollmentDependentDeductionsApi,
        TagValues.OPEN_ENROLLMENT_EMPLOYEE_DEDUCTIONS: OpenEnrollmentEmployeeDeductionsApi,
        TagValues.OPTION_RATE: OptionRateApi,
        TagValues.ORGANIZATION_REPORTING_CATEGORY: OrganizationReportingCategoryApi,
        TagValues.PAY_REGISTER: PayRegisterApi,
        TagValues.PAY_GROUP_PAY_PERIOD: PayGroupPayPeriodApi,
        TagValues.PAYROLL_DEDUCTIONS_HISTORY: PayrollDeductionsHistoryApi,
        TagValues.V1_PLATFORM_CONFIGURATION_CUSTOM_FIELDS_DATA: V1PlatformConfigurationCustomFieldsDataApi,
        TagValues.V2_PLATFORM_CONFIGURATION_CUSTOM_FIELDS_DATA: V2PlatformConfigurationCustomFieldsDataApi,
        TagValues.PLATFORM_CONFIGURATION_CUSTOM_FIELDS_SCHEMA: PlatformConfigurationCustomFieldsSchemaApi,
        TagValues.POSITION_REPORT: PositionReportApi,
        TagValues.POSITIONS: PositionsApi,
        TagValues.GET_ALL_PTO_PLANS: GetAllPTOPlansApi,
        TagValues.PTO_PLAN_POST: PTOPlanPostApi,
        TagValues.GET_SPECIFIC_PTO_PLAN: GetSpecificPTOPlanApi,
        TagValues.PTO_PLAN_PATCH: PTOPlanPatchApi,
        TagValues.GET_SPECIFIC_EMPLOYEES_PTO_PLANS: GetSpecificEmployeesPTOPlansApi,
        TagValues.ROLES_GET: RolesGetApi,
        TagValues.SHIFT_CODE: ShiftCodeApi,
        TagValues.TAX_GROUPS: TaxGroupsApi,
        TagValues.GET_JOB_POSTINGS: GetJobPostingsApi,
        TagValues.ACTIVITIES: ActivitiesApi,
        TagValues.ASSIGNED_HOLIDAYS: AssignedHolidaysApi,
        TagValues.EMPLOYEE_JOBS: EmployeeJobsApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.HOUR_TYPES: HourTypesApi,
        TagValues.SCHEDULE_DETAILS: ScheduleDetailsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.TIME_CODES: TimeCodesApi,
        TagValues.TIME_OFF_REQUESTS: TimeOffRequestsApi,
        TagValues.UTA_EMPLOYEE: UTAEmployeeApi,
        TagValues.USER_DETAILS: UserDetailsApi,
        TagValues.USER_PREFERENCES: UserPreferencesApi,
        TagValues.USER_PROFILE_DETAILS: UserProfileDetailsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TIME: TimeApi,
        TagValues.BUSINESS_RULE_IMPORT_TOOL: BusinessRuleImportToolApi,
        TagValues.COMPENSATION_DETAILS: CompensationDetailsApi,
        TagValues.PERSON_DETAILS: PersonDetailsApi,
        TagValues.EARNINGS: EarningsApi,
        TagValues.EMPLOYEE_PAY_STATEMENT: EmployeePayStatementApi,
        TagValues.EMPLOYMENT_DETAILS: EmploymentDetailsApi,
        TagValues.SINGLE_ORGANIZATION_LEVEL: SingleOrganizationLevelApi,
        TagValues.ALLERGY: AllergyApi,
        TagValues.AWARD_TYPE: AwardTypeApi,
        TagValues.CAREER_PROVIDER: CareerProviderApi,
        TagValues.CHILD_SUPPORT_TYPE: ChildSupportTypeApi,
        TagValues.COBRA_STATUS: CobraStatusApi,
        TagValues.COMPANY_PROPERTY: CompanyPropertyApi,
        TagValues.COURSE_CATEGORY: CourseCategoryApi,
        TagValues.COURSE_DELIVERY_MET: CourseDeliveryMetApi,
        TagValues.COURSE_SUB_CATEGORY: CourseSubCategoryApi,
        TagValues.DISABILITY: DisabilityApi,
        TagValues.EMPLOYEE_TYPE: EmployeeTypeApi,
        TagValues.JOB_FAMILY: JobFamilyApi,
        TagValues.LICENSE_TYPE: LicenseTypeApi,
        TagValues.LOAN_TYPE: LoanTypeApi,
        TagValues.MARITAL_STATUS: MaritalStatusApi,
        TagValues.MILITARY_BRANCHES: MilitaryBranchesApi,
        TagValues.MILITARY_ERA: MilitaryEraApi,
        TagValues.NAME_PREFIX: NamePrefixApi,
        TagValues.OTHER_PHONE_TYPES: OtherPhoneTypesApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.SCHOOL: SchoolApi,
        TagValues.SKILL_PROFICIENCY_LEVEL: SkillProficiencyLevelApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.TERM_TYPE: TermTypeApi,
        TagValues.WAIVE_REASON: WaiveReasonApi,
        TagValues.USER_DEFINED_FIELDS: UserDefinedFieldsApi,
        TagValues.CANDIDATE_REQUEST: CandidateRequestApi,
        TagValues.CODE_TABLES: CodeTablesApi,
        TagValues.CONTACT: ContactApi,
        TagValues.DIRECT_DEPOSIT: DirectDepositApi,
        TagValues.EMPLOYEE_JOB_HISTORY_DETAIL: EmployeeJobHistoryDetailApi,
        TagValues.COMPANY_PAY_STATEMENT: CompanyPayStatementApi,
        TagValues.GENERAL_LEDGER_RUN_DETAILS_V2: GeneralLedgerRunDetailsV2Api,
        TagValues.IMPORT_TOOL: ImportToolApi,
        TagValues.INTERNATIONAL_EMPLOYEE: InternationalEmployeeApi,
        TagValues.JOBS: JobsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.NEW_HIRES: NewHiresApi,
        TagValues.VIEW_OR_CREATE_ORGANIZATION_LEVELS: ViewOrCreateOrganizationLevelsApi,
        TagValues.AUDIT_DETAILS: AuditDetailsApi,
        TagValues.ORDER_REQUESTS: OrderRequestsApi,
        TagValues.BUSINESS_STRUCTURE_STATUS: BusinessStructureStatusApi,
        TagValues.COMPANY_DETAILS: CompanyDetailsApi,
        TagValues.EMP_DEDUCTIONS: EmpDeductionsApi,
        TagValues.DEPENDENT_DEDUCTIONS: DependentDeductionsApi,
        TagValues.EARNINGS_HISTORY: EarningsHistoryApi,
        TagValues.CHANGES_BY_DATE: ChangesByDateApi,
        TagValues.EMPLOYEE_CHANGES: EmployeeChangesApi,
        TagValues.EMPLOYEE_COBRA_DETAILS: EmployeeCobraDetailsApi,
        TagValues.EMPLOYEE_CONTRACT: EmployeeContractApi,
        TagValues.EMP_DED_BEN_OPTION_DATE: EmpDedBenOptionDateApi,
        TagValues.EMPLOYEE_DEDUCTION_HISTORY_EFFECTIVE_DATE: EmployeeDeductionHistoryEffectiveDateApi,
        TagValues.EMPLOYEE_DEMOGRAPHIC_DETAILS: EmployeeDemographicDetailsApi,
        TagValues.EMPLOYEE_EDUCATION: EmployeeEducationApi,
        TagValues.EMPLOYEE_EMPLOYMENT_DETAILS: EmployeeEmploymentDetailsApi,
        TagValues.EMPLOYEE_EXTENDED_ELEMENTS: EmployeeExtendedElementsApi,
        TagValues.EMPLOYEE_ID_LOOKUP: EmployeeIDLookupApi,
        TagValues.EMPLOYEE_MULTIPLE_JOBS_OPP: EmployeeMultipleJobsOPPApi,
        TagValues.EMPLOYEE_MULTI_PHONE_NUMBERS: EmployeeMultiPhoneNumbersApi,
        TagValues.EMP_MULTIPLE_POSITIONS: EmpMultiplePositionsApi,
        TagValues.NATIONAL_DOCUMENT: NationalDocumentApi,
        TagValues.KRONOS_EMPLOYEE_PROFILES: KronosEmployeeProfilesApi,
        TagValues.EMPLOYEE_SECURITY_USER_DETAILS: EmployeeSecurityUserDetailsApi,
        TagValues.KRONOS_EMPLOYEE_STATUS: KronosEmployeeStatusApi,
        TagValues.EMPLOYEE_SUPERVISOR_DETAILS: EmployeeSupervisorDetailsApi,
        TagValues.EMPLOYEE_GLOBAL_BANK: EmployeeGlobalBankApi,
        TagValues.EMP_GLOBAL_LOCALIZATION_ELEMENT: EmpGlobalLocalizationElementApi,
        TagValues.EMPLOYEE_PAY_DEDUCTION_ELEMENT: EmployeePayDeductionElementApi,
        TagValues.INS_RATE: InsRateApi,
        TagValues.INTEGRATION_AUDIT_CONFIGURATION: IntegrationAuditConfigurationApi,
        TagValues.JOB_GROUP: JobGroupApi,
        TagValues.POST_NEW_TOKEN_REQUEST: PostNewTokenRequestApi,
        TagValues.OPEN_ENROLLMENT_DEPENDENT_DEDUCTIONS: OpenEnrollmentDependentDeductionsApi,
        TagValues.OPEN_ENROLLMENT_EMPLOYEE_DEDUCTIONS: OpenEnrollmentEmployeeDeductionsApi,
        TagValues.OPTION_RATE: OptionRateApi,
        TagValues.ORGANIZATION_REPORTING_CATEGORY: OrganizationReportingCategoryApi,
        TagValues.PAY_REGISTER: PayRegisterApi,
        TagValues.PAY_GROUP_PAY_PERIOD: PayGroupPayPeriodApi,
        TagValues.PAYROLL_DEDUCTIONS_HISTORY: PayrollDeductionsHistoryApi,
        TagValues.V1_PLATFORM_CONFIGURATION_CUSTOM_FIELDS_DATA: V1PlatformConfigurationCustomFieldsDataApi,
        TagValues.V2_PLATFORM_CONFIGURATION_CUSTOM_FIELDS_DATA: V2PlatformConfigurationCustomFieldsDataApi,
        TagValues.PLATFORM_CONFIGURATION_CUSTOM_FIELDS_SCHEMA: PlatformConfigurationCustomFieldsSchemaApi,
        TagValues.POSITION_REPORT: PositionReportApi,
        TagValues.POSITIONS: PositionsApi,
        TagValues.GET_ALL_PTO_PLANS: GetAllPTOPlansApi,
        TagValues.PTO_PLAN_POST: PTOPlanPostApi,
        TagValues.GET_SPECIFIC_PTO_PLAN: GetSpecificPTOPlanApi,
        TagValues.PTO_PLAN_PATCH: PTOPlanPatchApi,
        TagValues.GET_SPECIFIC_EMPLOYEES_PTO_PLANS: GetSpecificEmployeesPTOPlansApi,
        TagValues.ROLES_GET: RolesGetApi,
        TagValues.SHIFT_CODE: ShiftCodeApi,
        TagValues.TAX_GROUPS: TaxGroupsApi,
        TagValues.GET_JOB_POSTINGS: GetJobPostingsApi,
        TagValues.ACTIVITIES: ActivitiesApi,
        TagValues.ASSIGNED_HOLIDAYS: AssignedHolidaysApi,
        TagValues.EMPLOYEE_JOBS: EmployeeJobsApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.HOUR_TYPES: HourTypesApi,
        TagValues.SCHEDULE_DETAILS: ScheduleDetailsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.TIME_CODES: TimeCodesApi,
        TagValues.TIME_OFF_REQUESTS: TimeOffRequestsApi,
        TagValues.UTA_EMPLOYEE: UTAEmployeeApi,
        TagValues.USER_DETAILS: UserDetailsApi,
        TagValues.USER_PREFERENCES: UserPreferencesApi,
        TagValues.USER_PROFILE_DETAILS: UserProfileDetailsApi,
    }
)
