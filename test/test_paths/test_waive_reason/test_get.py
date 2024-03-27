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
from ukg_python_sdk.paths.waive_reason import get
from ukg_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestWaiveReason(ApiTestMixin, unittest.TestCase):
    """
    WaiveReason unit test stubs
        Retrieve all waiveReason configurations
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
