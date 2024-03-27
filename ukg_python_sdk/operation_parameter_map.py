operation_parameter_map = {
    '/simpleschedule/activities-GET': {
        'parameters': [
        ]
    },
    '/simpleschedule/assigned_holidays-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'emp_name'
            },
            {
                'name': 'emp_id'
            },
        ]
    },
    '/personnel/v1/audit-details-GET': {
        'parameters': [
            {
                'name': 'startDateTime'
            },
            {
                'name': 'endDateTime'
            },
            {
                'name': 'tableName'
            },
            {
                'name': 'fieldName'
            },
            {
                'name': 'action'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/configuration/v1/businessruleimport-tool/fileupload-POST': {
        'parameters': [
            {
                'name': 'transaction'
            },
            {
                'name': 'uniqueFileName'
            },
        ]
    },
    '/configuration/v1/businessruleimport-tool/filestatus/{fileId}-GET': {
        'parameters': [
            {
                'name': 'fileId'
            },
        ]
    },
    '/configuration/v1/businessruleimport-tool/transactionstatus/{stagingId}-GET': {
        'parameters': [
            {
                'name': 'stagingId'
            },
        ]
    },
    '/configuration/v1/businessruleimport-tool/transaction-POST': {
        'parameters': [
            {
                'name': 'transaction'
            },
            {
                'name': 'uniqueFileName'
            },
        ]
    },
    '/personnel/v1/integration/kronos/business-structure-status-GET': {
        'parameters': [
            {
                'name': 'modifiedAfterDateTime'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/{tenant-alias}/api/candidates/{candidate-id}/background-checks-POST': {
        'parameters': [
            {
                'name': 'author'
            },
            {
                'name': 'application'
            },
            {
                'name': 'status'
            },
            {
                'name': 'order_number'
            },
            {
                'name': 'packages'
            },
            {
                'name': 'candidate-id'
            },
            {
                'name': 'tenant-alias'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/{tenant-alias}/api/candidates/{candidate-id}/background-checks/{background-check-id}-PUT': {
        'parameters': [
            {
                'name': 'author'
            },
            {
                'name': 'application'
            },
            {
                'name': 'status'
            },
            {
                'name': 'order_number'
            },
            {
                'name': 'packages'
            },
            {
                'name': 'candidate-id'
            },
            {
                'name': 'background-check-id'
            },
            {
                'name': 'tenant-alias'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/personnel/v1/employee-changes-GET': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/configuration/v1/code-tables-POST': {
        'parameters': [
        ]
    },
    '/configuration/v1/code-tables-GET': {
        'parameters': [
        ]
    },
    '/configuration/v1/company-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'masterCompanyId'
            },
            {
                'name': 'companyCode'
            },
            {
                'name': 'isMasterCompany'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v1/companies/pay-statements-POST': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
            {
                'name': 'pagesCount'
            },
        ]
    },
    '/payroll/v1/companies/pay-statements-summary-POST': {
        'parameters': [
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
            {
                'name': 'pagesCount'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/compensation-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'primaryJobCode'
            },
            {
                'name': 'jobGroupCode'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'payGroupCode'
            },
            {
                'name': 'fullTimeOrPartTimeCode'
            },
            {
                'name': 'salaryOrHourlyCode'
            },
            {
                'name': 'primaryShiftCode'
            },
            {
                'name': 'primaryShiftGroupCode'
            },
            {
                'name': 'dateInJob'
            },
            {
                'name': 'dateLastPaid'
            },
            {
                'name': 'datePaidThru'
            },
            {
                'name': 'isAutoAllocated'
            },
            {
                'name': 'isAutoPaid'
            },
            {
                'name': 'isSeasonalWorker'
            },
            {
                'name': 'isHighlyCompensated'
            },
            {
                'name': 'isMultipleJob'
            },
            {
                'name': 'performanceReviewRating'
            },
            {
                'name': 'performanceReviewType'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/compensation-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'primaryJobCode'
            },
            {
                'name': 'jobGroupCode'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'payGroupCode'
            },
            {
                'name': 'fullTimeOrPartTimeCode'
            },
            {
                'name': 'salaryOrHourlyCode'
            },
            {
                'name': 'primaryShiftCode'
            },
            {
                'name': 'primaryShiftGroupCode'
            },
            {
                'name': 'dateInJob'
            },
            {
                'name': 'dateLastPaid'
            },
            {
                'name': 'datePaidThru'
            },
            {
                'name': 'isAutoAllocated'
            },
            {
                'name': 'isAutoPaid'
            },
            {
                'name': 'isSeasonalWorker'
            },
            {
                'name': 'isHighlyCompensated'
            },
            {
                'name': 'isMultipleJob'
            },
            {
                'name': 'performanceReviewRating'
            },
            {
                'name': 'performanceReviewType'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/employees/{employeeId}/compensation-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'primaryJobCode'
            },
            {
                'name': 'jobGroupCode'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'payGroupCode'
            },
            {
                'name': 'fullTimeOrPartTimeCode'
            },
            {
                'name': 'salaryOrHourlyCode'
            },
            {
                'name': 'primaryShiftCode'
            },
            {
                'name': 'primaryShiftGroupCode'
            },
            {
                'name': 'dateInJob'
            },
            {
                'name': 'dateLastPaid'
            },
            {
                'name': 'datePaidThru'
            },
            {
                'name': 'isAutoAllocated'
            },
            {
                'name': 'isAutoPaid'
            },
            {
                'name': 'isSeasonalWorker'
            },
            {
                'name': 'isHighlyCompensated'
            },
            {
                'name': 'isMultipleJob'
            },
            {
                'name': 'performanceReviewRating'
            },
            {
                'name': 'performanceReviewType'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/compensation-details/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
        ]
    },
    '/personnel/v1/contacts/{contactId}-GET': {
        'parameters': [
            {
                'name': 'contactId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'isActive'
            },
            {
                'name': 'relationshipCode'
            },
            {
                'name': 'contactId'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'cobraIsActive'
            },
            {
                'name': 'cobraStatus'
            },
            {
                'name': 'isBeneficiary'
            },
            {
                'name': 'isDependent'
            },
            {
                'name': 'dateOfCobraEvent'
            },
            {
                'name': 'statusAsOfDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/contacts-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'isActive'
            },
            {
                'name': 'relationshipCode'
            },
            {
                'name': 'contactId'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'cobraIsActive'
            },
            {
                'name': 'cobraStatus'
            },
            {
                'name': 'isBeneficiary'
            },
            {
                'name': 'isDependent'
            },
            {
                'name': 'dateOfCobraEvent'
            },
            {
                'name': 'statusAsOfDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/dep-deductions-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'contactId'
            },
            {
                'name': 'deductionCode'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'currentCOID'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v1/companies/{companyId}/direct-deposit-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'accountIsInactive'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeBankRoutingNumber'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v1/direct-deposit-GET': {
        'parameters': [
            {
                'name': 'accountIsInactive'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeBankRoutingNumber'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/services/payroll/v1/import-pay-items/earnings-POST': {
        'parameters': [
            {
                'name': 'X-Correlation-Id'
            },
            {
                'name': 'US-Client-Id'
            },
            {
                'name': 'earnings'
            },
            {
                'name': 'failAllOnRequest'
            },
        ]
    },
    '/services/payroll/v1/import-pay-items/earnings/{refId}-DELETE': {
        'parameters': [
            {
                'name': 'X-Correlation-Id'
            },
            {
                'name': 'US-Client-Id'
            },
            {
                'name': 'refId'
            },
        ]
    },
    '/configuration/v1/earnings/{calculationRule}/{taxCategory}/{useDeductionOffset}/{countryCode}/{includeInShiftDiffrential}/{includeInManualCheck}-GET': {
        'parameters': [
            {
                'name': 'calculationRule'
            },
            {
                'name': 'taxCategory'
            },
            {
                'name': 'useDeductionOffset'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'includeInShiftDiffrential'
            },
            {
                'name': 'includeInManualCheck'
            },
            {
                'name': 'earningCode'
            },
            {
                'name': 'includeInAccruals'
            },
            {
                'name': 'includeInDeferredCompensation'
            },
            {
                'name': 'includeInDeferredCompensationHours'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/services/payroll/v1/import-pay-items/earnings/{refId}-GET': {
        'parameters': [
            {
                'name': 'X-Correlation-Id'
            },
            {
                'name': 'US-Client-Id'
            },
            {
                'name': 'refId'
            },
        ]
    },
    '/configuration/v1/earnings-GET': {
        'parameters': [
            {
                'name': 'calculationRule'
            },
            {
                'name': 'taxCategory'
            },
            {
                'name': 'useDeductionOffset'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'includeInShiftDiffrential'
            },
            {
                'name': 'includeInManualCheck'
            },
            {
                'name': 'earningCode'
            },
            {
                'name': 'includeInAccruals'
            },
            {
                'name': 'includeInDeferredCompensation'
            },
            {
                'name': 'includeInDeferredCompensationHours'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/configuration/v1/earnings/{earningCode}-GET': {
        'parameters': [
            {
                'name': 'earningCode'
            },
            {
                'name': 'calculationRule'
            },
            {
                'name': 'taxCategory'
            },
            {
                'name': 'useDeductionOffset'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'includeInShiftDiffrential'
            },
            {
                'name': 'includeInManualCheck'
            },
            {
                'name': 'earningCode'
            },
            {
                'name': 'includeInAccruals'
            },
            {
                'name': 'includeInDeferredCompensation'
            },
            {
                'name': 'includeInDeferredCompensationHours'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v1/earnings-history-base-elements-GET': {
        'parameters': [
            {
                'name': 'companyID'
            },
            {
                'name': 'earningCode'
            },
            {
                'name': 'employeeID'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'payDate'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'periodControl'
            },
            {
                'name': 'startPerControl'
            },
            {
                'name': 'endPerControl'
            },
            {
                'name': 'includeInDeferredCompensation'
            },
            {
                'name': 'includeInDeferredCompensationHours'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/emp-deductions-benefit-option-change-date-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'deductionCode'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/emp-deductions-GET': {
        'parameters': [
            {
                'name': 'dedCode'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'benStatus'
            },
            {
                'name': 'benefitOption'
            },
            {
                'name': 'endDateTime'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-global-localization-elements-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'created'
            },
            {
                'name': 'effective'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/empl-multiple-positions-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'jobCode'
            },
            {
                'name': 'positionCode'
            },
            {
                'name': 'isPrimary'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-changes/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
        ]
    },
    '/personnel/v1/deduction-history-effective-change-dates-GET': {
        'parameters': [
            {
                'name': 'fieldName'
            },
            {
                'name': 'deductionCode'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'sessionDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-demographic-details-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'emailAddress'
            },
            {
                'name': 'addressState'
            },
            {
                'name': 'addressCountry'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-ids-POST': {
        'parameters': [
        ]
    },
    '/simpleschedule/employee_jobs-GET': {
        'parameters': [
            {
                'name': 'emp_name'
            },
            {
                'name': 'emp_id'
            },
        ]
    },
    '/personnel/v1/employee-security-user-details-GET': {
        'parameters': [
            {
                'name': 'userName'
            },
            {
                'name': 'employeeID'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-cobra-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'cobraIsActive'
            },
            {
                'name': 'cobraStatus'
            },
            {
                'name': 'dateOfCobraEvent'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-contract-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'contractNumber'
            },
            {
                'name': 'contractTypeCode'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'rowLastChanged'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-education-GET': {
        'parameters': [
            {
                'name': 'systemId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'country'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-employment-details-GET': {
        'parameters': [
            {
                'name': 'companyID'
            },
            {
                'name': 'employeeID'
            },
            {
                'name': 'primaryJobCode'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'fullTimeOrPartTimeCode'
            },
            {
                'name': 'primaryWorkLocationCode'
            },
            {
                'name': 'primaryProjectCode'
            },
            {
                'name': 'deductionGroupCode'
            },
            {
                'name': 'earningGroupCode'
            },
            {
                'name': 'employeeTypeCode'
            },
            {
                'name': 'employeeStatusCode'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'supervisorId'
            },
            {
                'name': 'originalHireDate'
            },
            {
                'name': 'lastHireDate'
            },
            {
                'name': 'dateOfTermination'
            },
            {
                'name': 'dateOfRetirement'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'dateLastPayDatePaid'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'isHomeCompany'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-extended-elements-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-global-banks-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'employeeCountry'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'dateModified'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-job-history-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'isOrgChange'
            },
            {
                'name': 'isJobChange'
            },
            {
                'name': 'isRateChange'
            },
            {
                'name': 'isPromotion'
            },
            {
                'name': 'systemId'
            },
            {
                'name': 'jobEffectiveDate'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-job-history-details/{systemId}-GET': {
        'parameters': [
            {
                'name': 'systemId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'isOrgChange'
            },
            {
                'name': 'isJobChange'
            },
            {
                'name': 'isRateChange'
            },
            {
                'name': 'isPromotion'
            },
            {
                'name': 'systemId'
            },
            {
                'name': 'jobEffectiveDate'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-multi-phone-numbers-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'systemId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/empl-multiple-jobs-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'jobCode'
            },
            {
                'name': 'isPrimaryJob'
            },
            {
                'name': 'jobIsInActive'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employee-pay-deduction-elements-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'country'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'payDeductionName'
            },
            {
                'name': 'periodStartName'
            },
            {
                'name': 'paymentOrDeductionIndicator'
            },
            {
                'name': 'modifiedDate'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v1/employees/pay-statements-POST': {
        'parameters': [
            {
                'name': 'employeeIdentifier'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
            {
                'name': 'pagesCount'
            },
        ]
    },
    '/payroll/v1/employees/pay-statement/{PayIdentifier}-GET': {
        'parameters': [
            {
                'name': 'PayIdentifier'
            },
        ]
    },
    '/payroll/v1/employees/pay-statement/last-POST': {
        'parameters': [
            {
                'name': 'employeeIdentifier'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
            {
                'name': 'pagesCount'
            },
        ]
    },
    '/personnel/v1/employee-supervisor-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'supervisorCompanyId'
            },
            {
                'name': 'supervisorEmployeeId'
            },
            {
                'name': 'supervisorCompanyCode'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/simpleschedule/employees-GET': {
        'parameters': [
            {
                'name': 'index'
            },
            {
                'name': 'max'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/employees/{employeeId}/employment-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'primaryJobCode'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'fullTimeOrPartTimeCode'
            },
            {
                'name': 'primaryWorkLocationCode'
            },
            {
                'name': 'primaryProjectCode'
            },
            {
                'name': 'deductionGroupCode'
            },
            {
                'name': 'earningGroupCode'
            },
            {
                'name': 'employeeTypeCode'
            },
            {
                'name': 'employeeStatusCode'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'supervisorID'
            },
            {
                'name': 'originalHireDate'
            },
            {
                'name': 'lastHireDate'
            },
            {
                'name': 'dateOfTermination'
            },
            {
                'name': 'dateOfRetirement'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'dateLastPayDatePaid'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'isHomeCompany'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/employment-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'primaryJobCode'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'fullTimeOrPartTimeCode'
            },
            {
                'name': 'primaryWorkLocationCode'
            },
            {
                'name': 'primaryProjectCode'
            },
            {
                'name': 'deductionGroupCode'
            },
            {
                'name': 'earningGroupCode'
            },
            {
                'name': 'employeeTypeCode'
            },
            {
                'name': 'employeeStatusCode'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'supervisorID'
            },
            {
                'name': 'originalHireDate'
            },
            {
                'name': 'lastHireDate'
            },
            {
                'name': 'dateOfTermination'
            },
            {
                'name': 'dateOfRetirement'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'dateLastPayDatePaid'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'isHomeCompany'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/employment-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'primaryJobCode'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'fullTimeOrPartTimeCode'
            },
            {
                'name': 'primaryWorkLocationCode'
            },
            {
                'name': 'primaryProjectCode'
            },
            {
                'name': 'deductionGroupCode'
            },
            {
                'name': 'earningGroupCode'
            },
            {
                'name': 'employeeTypeCode'
            },
            {
                'name': 'employeeStatusCode'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'supervisorID'
            },
            {
                'name': 'originalHireDate'
            },
            {
                'name': 'lastHireDate'
            },
            {
                'name': 'dateOfTermination'
            },
            {
                'name': 'dateOfRetirement'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'dateLastPayDatePaid'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'isHomeCompany'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v2/general-ledger-GET': {
        'parameters': [
            {
                'name': 'runId'
            },
            {
                'name': 'blockId'
            },
            {
                'name': 'mostRecent'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v2/general-ledger/{runId}-GET': {
        'parameters': [
            {
                'name': 'runId'
            },
            {
                'name': 'runId'
            },
            {
                'name': 'blockId'
            },
            {
                'name': 'mostRecent'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/pto-plans-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/talent/recruiting/v2/third-party-job-board-integrations/{integrationId}/postings-GET': {
        'parameters': [
            {
                'name': 'integrationId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/employees/{employeeId}/pto-plans-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_page'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/employees/{employeeId}/pto-plans/{ptoPlan}-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'ptoPlan'
            },
        ]
    },
    '/simpleschedule/hour_types-GET': {
        'parameters': [
        ]
    },
    '/personnel/v1/import-tool/status/{stagingId}-GET': {
        'parameters': [
            {
                'name': 'stagingId'
            },
        ]
    },
    '/personnel/v1/import-tool-POST': {
        'parameters': [
            {
                'name': 'transaction'
            },
            {
                'name': 'uniqueFileName'
            },
        ]
    },
    '/configuration/v1/insurance-rate-GET': {
        'parameters': [
            {
                'name': 'deductionCode'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'payFrequency'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/integration-audit-configuration-GET': {
        'parameters': [
            {
                'name': 'tableName'
            },
            {
                'name': 'fieldName'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/international-employees-GET': {
        'parameters': [
            {
                'name': 'countryCode'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/international-employees/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/configuration/v1/jobgroup-GET': {
        'parameters': [
            {
                'name': 'jobGroupCode'
            },
            {
                'name': 'jobGroupCountryCode'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/integration/kronos/employee-profiles-GET': {
        'parameters': [
            {
                'name': 'product'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'changeWindow'
            },
            {
                'name': 'includeHistoryIfChangeDetected'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/integration/kronos/employee-status-GET': {
        'parameters': [
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeIds'
            },
            {
                'name': 'inactiveTermWindow'
            },
            {
                'name': 'inactiveDisabledWindow'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/national-documents-GET': {
        'parameters': [
            {
                'name': 'contactId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'nationalDocumentIssuingCountryCode'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/tenants/{tenantIdentifier}/new-hires-POST': {
        'parameters': [
            {
                'name': 'tenantIdentifier'
            },
            {
                'name': 'contactInformation'
            },
            {
                'name': 'job'
            },
            {
                'name': 'organizationLevels'
            },
            {
                'name': 'compensation'
            },
            {
                'name': 'onboardingOwnerId'
            },
            {
                'name': 'hireDate'
            },
            {
                'name': 'orientationDate'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'pastStartDateReason'
            },
            {
                'name': 'mentor'
            },
            {
                'name': 'personalMessage'
            },
        ]
    },
    '/tenants/{tenantIdentifier}/new-hires/{id}-GET': {
        'parameters': [
            {
                'name': 'tenantIdentifier'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/personnel/v1/open-enrollment-dep-deductions-GET': {
        'parameters': [
            {
                'name': 'startDateTime'
            },
            {
                'name': 'endDateTime'
            },
            {
                'name': 'sessionType'
            },
            {
                'name': 'deductionCode'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/open-enrollment-emp-deductions-GET': {
        'parameters': [
            {
                'name': 'startDateTime'
            },
            {
                'name': 'endDateTime'
            },
            {
                'name': 'sessionType'
            },
            {
                'name': 'deductionCode'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/configuration/v1/option-rate-GET': {
        'parameters': [
            {
                'name': 'deductionCode'
            },
            {
                'name': 'benefitOption'
            },
            {
                'name': 'effectiveDate'
            },
            {
                'name': 'payFrequency'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/{tenant-alias}/api/background-check-order-requests-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'tenant-alias'
            },
        ]
    },
    '/configuration/v1/organization-reporting-category-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/employees/{employeeId}/pto-plans/{ptoPlan}-PATCH': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'ptoPlan'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'ptoPlan'
            },
            {
                'name': 'earned'
            },
            {
                'name': 'taken'
            },
            {
                'name': 'pendingBalance'
            },
            {
                'name': 'earnedThroughDate'
            },
            {
                'name': 'reset'
            },
            {
                'name': 'pendingMoveDate'
            },
        ]
    },
    '/personnel/v1/pto-plans-POST': {
        'parameters': [
        ]
    },
    '/payroll/v1/paygroup-payperiods-GET': {
        'parameters': [
            {
                'name': 'payDateSeq'
            },
            {
                'name': 'periodEndDate'
            },
            {
                'name': 'periodStartDate'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'payDate'
            },
            {
                'name': 'startPerControl'
            },
            {
                'name': 'endPerControl'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v1/pay-register-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'checkId'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'documentNumber'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'periodControl'
            },
            {
                'name': 'payDate'
            },
            {
                'name': 'periodEndDate'
            },
            {
                'name': 'periodStartDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/payroll/v1/payroll-deductions-history-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'checkId'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'deductionCode'
            },
            {
                'name': 'deductionType'
            },
            {
                'name': 'benefitOption'
            },
            {
                'name': 'benefitProvider'
            },
            {
                'name': 'payGroup'
            },
            {
                'name': 'periodControl'
            },
            {
                'name': 'payDate'
            },
            {
                'name': 'is401K'
            },
            {
                'name': 'is403B'
            },
            {
                'name': 'is408K'
            },
            {
                'name': 'is408P'
            },
            {
                'name': 'is457'
            },
            {
                'name': 'is457B'
            },
            {
                'name': 'is457F'
            },
            {
                'name': 'is501C'
            },
            {
                'name': 'isD125'
            },
            {
                'name': 'isDeductionOffSet'
            },
            {
                'name': 'isDeferredCompensation'
            },
            {
                'name': 'isDependentCare'
            },
            {
                'name': 'isHousing'
            },
            {
                'name': 'isNonQualifiedPlan'
            },
            {
                'name': 'startPerControl'
            },
            {
                'name': 'endPerControl'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/person-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'emailAddress'
            },
            {
                'name': 'addressState'
            },
            {
                'name': 'addressCountry'
            },
            {
                'name': 'cobraIsActive'
            },
            {
                'name': 'cobraStatus'
            },
            {
                'name': 'dateOfCobraEvent'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'nationalId'
            },
            {
                'name': 'nationalIdCountry'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/person-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'emailAddress'
            },
            {
                'name': 'addressState'
            },
            {
                'name': 'addressCountry'
            },
            {
                'name': 'cobraIsActive'
            },
            {
                'name': 'cobraStatus'
            },
            {
                'name': 'dateOfCobraEvent'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'nationalId'
            },
            {
                'name': 'nationalIdCountry'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/person-details/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/employees/{employeeId}/person-details-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'emailAddress'
            },
            {
                'name': 'addressState'
            },
            {
                'name': 'addressCountry'
            },
            {
                'name': 'cobraIsActive'
            },
            {
                'name': 'cobraStatus'
            },
            {
                'name': 'dateOfCobraEvent'
            },
            {
                'name': 'dateTimeCreated'
            },
            {
                'name': 'dateTimeChanged'
            },
            {
                'name': 'nationalId'
            },
            {
                'name': 'nationalIdCountry'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/configuration/v1/platform-configuration/custom-fields-schema-GET': {
        'parameters': [
            {
                'name': 'className'
            },
        ]
    },
    '/personnel/v1/position-report-GET': {
        'parameters': [
            {
                'name': 'positionCode'
            },
            {
                'name': 'reportsToPositionCode'
            },
            {
                'name': 'effectiveStartDate'
            },
            {
                'name': 'effectiveStopDate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/configuration/v1/positions-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeType'
            },
            {
                'name': 'statusCode'
            },
            {
                'name': 'payGroupCode'
            },
            {
                'name': 'positionCode'
            },
            {
                'name': 'projectCode'
            },
            {
                'name': 'shiftGroupCode'
            },
            {
                'name': 'isProrated'
            },
            {
                'name': 'isApproved'
            },
            {
                'name': 'isEligibleForBenefits'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/signin/oauth2/t/{tenant-name}/access_token-POST': {
        'parameters': [
            {
                'name': 'tenant-name'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'scope'
            },
        ]
    },
    '/configuration/v1/roles-GET': {
        'parameters': [
            {
                'name': 'rolName'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/simpleschedule/schedule_details-PUT': {
        'parameters': [
            {
                'name': 'scheduleDetails'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/configuration/v1/shift-codes-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/configuration/v1/org-levels/{level}/{code}-GET': {
        'parameters': [
            {
                'name': 'level'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/configuration/v1/org-levels/{level}/{code}-PUT': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
            {
                'name': 'level'
            },
            {
                'name': 'level'
            },
            {
                'name': 'code'
            },
            {
                'name': 'budgetGroup'
            },
            {
                'name': 'currentYearBudgetFTE'
            },
            {
                'name': 'currentYearBudgetSalary'
            },
            {
                'name': 'glSegment'
            },
            {
                'name': 'lastYearBudgetFTE'
            },
            {
                'name': 'lastYearBudgetSalary'
            },
            {
                'name': 'levelDescription'
            },
            {
                'name': 'reportingCategory'
            },
            {
                'name': 'isActive'
            },
        ]
    },
    '/configuration/v1/org-levels/{level}/{code}-PATCH': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
            {
                'name': 'level'
            },
            {
                'name': 'level'
            },
            {
                'name': 'code'
            },
            {
                'name': 'budgetGroup'
            },
            {
                'name': 'currentYearBudgetFTE'
            },
            {
                'name': 'currentYearBudgetSalary'
            },
            {
                'name': 'glSegment'
            },
            {
                'name': 'lastYearBudgetFTE'
            },
            {
                'name': 'lastYearBudgetSalary'
            },
            {
                'name': 'levelDescription'
            },
            {
                'name': 'reportingCategory'
            },
            {
                'name': 'isActive'
            },
        ]
    },
    '/configuration/v1/tax-groups-GET': {
        'parameters': [
            {
                'name': 'taxCalcGroupIdCode'
            },
            {
                'name': 'taxGroupIsInactive'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/simpleschedule/teams-GET': {
        'parameters': [
            {
                'name': 'index'
            },
            {
                'name': 'max'
            },
        ]
    },
    '/simpleschedule/time_codes-GET': {
        'parameters': [
        ]
    },
    '/simpleschedule/timeoff_requests-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'emp_name'
            },
            {
                'name': 'emp_id'
            },
        ]
    },
    '/simpleschedule/{coid}/employees/{eeid}-GET': {
        'parameters': [
            {
                'name': 'coid'
            },
            {
                'name': 'eeid'
            },
        ]
    },
    '/personnel/v1/user-preferences-GET': {
        'parameters': [
            {
                'name': 'userID'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/user-profile-details-GET': {
        'parameters': [
            {
                'name': 'masterCompany'
            },
            {
                'name': 'userStatus'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'roleId'
            },
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/user-defined-fields-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/user-defined-fields-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/companies/{companyId}/employees/{employeeId}/user-defined-fields-GET': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v1/user-details-GET': {
        'parameters': [
            {
                'name': 'userName'
            },
            {
                'name': 'userStatus'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/configuration/v1/org-levels-POST': {
        'parameters': [
        ]
    },
    '/configuration/v1/org-levels-GET': {
        'parameters': [
            {
                'name': 'levelDescription'
            },
            {
                'name': 'code'
            },
            {
                'name': 'budgetGroup'
            },
            {
                'name': 'reportingCategory'
            },
            {
                'name': 'isActive'
            },
        ]
    },
    '/allergy-GET': {
        'parameters': [
        ]
    },
    '/allergy-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/allergy/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/awardType-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/awardType-GET': {
        'parameters': [
        ]
    },
    '/awardType/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/careerProvider-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/careerProvider-GET': {
        'parameters': [
        ]
    },
    '/careerProvider/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/childSupportType-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/childSupportType-GET': {
        'parameters': [
        ]
    },
    '/childSupportType/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/cobraStatus-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/cobraStatus-GET': {
        'parameters': [
        ]
    },
    '/cobraStatus/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/companyProperty-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/companyProperty-GET': {
        'parameters': [
        ]
    },
    '/companyProperty/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/courseCategory-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/courseCategory-GET': {
        'parameters': [
        ]
    },
    '/courseCategory/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/courseDeliveryMet-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/courseDeliveryMet-GET': {
        'parameters': [
        ]
    },
    '/courseDeliveryMet/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/courseSubCategory-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/courseSubCategory-GET': {
        'parameters': [
        ]
    },
    '/courseSubCategory/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/disability-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/disability-GET': {
        'parameters': [
        ]
    },
    '/disability/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/employeeType-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/employeeType-GET': {
        'parameters': [
        ]
    },
    '/employeeType/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/jobFamily-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/jobFamily-GET': {
        'parameters': [
        ]
    },
    '/jobFamily/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/jobs-GET': {
        'parameters': [
            {
                'name': 'countryCode'
            },
            {
                'name': 'isActive'
            },
        ]
    },
    '/jobs/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/licenseType-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/licenseType-GET': {
        'parameters': [
        ]
    },
    '/licenseType/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/loanType-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/loanType-GET': {
        'parameters': [
        ]
    },
    '/loanType/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/locations/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/locations-GET': {
        'parameters': [
            {
                'name': 'countryCode'
            },
            {
                'name': 'isActive'
            },
        ]
    },
    '/maritalStatus-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/maritalStatus-GET': {
        'parameters': [
        ]
    },
    '/maritalStatus/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/militaryBranches-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/militaryBranches-GET': {
        'parameters': [
        ]
    },
    '/militaryBranches/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/militaryEra-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/militaryEra-GET': {
        'parameters': [
        ]
    },
    '/militaryEra/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/namePrefix-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/namePrefix-GET': {
        'parameters': [
        ]
    },
    '/namePrefix/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/otherPhoneTypes-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/otherPhoneTypes-GET': {
        'parameters': [
        ]
    },
    '/otherPhoneTypes/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/project-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/project-GET': {
        'parameters': [
        ]
    },
    '/project/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/school-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/school-GET': {
        'parameters': [
        ]
    },
    '/school/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/skillProficiencyLevel-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/skillProficiencyLevel-GET': {
        'parameters': [
        ]
    },
    '/skillProficiencyLevel/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/skills-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/skills-GET': {
        'parameters': [
        ]
    },
    '/skills/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/termType-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/termType-GET': {
        'parameters': [
        ]
    },
    '/termType/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
    '/hoursWorked-POST': {
        'parameters': [
            {
                'name': 'timeData'
            },
            {
                'name': 'X-Correlation-Id'
            },
            {
                'name': 'US-Tenant-Id'
            },
        ]
    },
    '/time/pending_clock_transactions-GET': {
        'parameters': [
            {
                'name': 'emp_name'
            },
            {
                'name': 'emp_id'
            },
        ]
    },
    '/time/clock_transactions-GET': {
        'parameters': [
            {
                'name': 'date'
            },
            {
                'name': 'emp_name'
            },
            {
                'name': 'emp_id'
            },
        ]
    },
    '/time/work_summaries-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'emp_name'
            },
            {
                'name': 'emp_id'
            },
            {
                'name': 'full'
            },
            {
                'name': 'authStatus'
            },
        ]
    },
    '/time/work_summary-GET': {
        'parameters': [
            {
                'name': 'workSummaryId'
            },
        ]
    },
    '/personnel/v1/platform-configuration-fields/class-name/{className}-GET': {
        'parameters': [
            {
                'name': 'className'
            },
            {
                'name': 'keyName'
            },
            {
                'name': 'keyValue'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'employmentStatus'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/personnel/v2/platform-configuration-fields/class-name/{className}-GET': {
        'parameters': [
            {
                'name': 'className'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'keyValue'
            },
            {
                'name': 'page'
            },
            {
                'name': 'per_Page'
            },
        ]
    },
    '/waiveReason-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'code'
            },
        ]
    },
    '/waiveReason-GET': {
        'parameters': [
        ]
    },
    '/waiveReason/{code}-PUT': {
        'parameters': [
            {
                'name': 'code'
            },
        ]
    },
};