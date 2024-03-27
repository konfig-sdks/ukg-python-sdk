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
from ukg_python_sdk.paths.course_sub_category_code import put
from ukg_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCourseSubCategoryCode(ApiTestMixin, unittest.TestCase):
    """
    CourseSubCategoryCode unit test stubs
        Update a single courseSubCategory configuration
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
