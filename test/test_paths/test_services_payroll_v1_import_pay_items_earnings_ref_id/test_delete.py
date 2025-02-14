# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import ukg_python_sdk
from ukg_python_sdk.paths.services_payroll_v1_import_pay_items_earnings_ref_id import delete
from ukg_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestServicesPayrollV1ImportPayItemsEarningsRefId(ApiTestMixin, unittest.TestCase):
    """
    ServicesPayrollV1ImportPayItemsEarningsRefId unit test stubs
        Delete a earning
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
