# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.course_category.post import CreateConfigurationUkgProRaw
from ukg_python_sdk.paths.course_category.get import GetAllConfigurationsRaw
from ukg_python_sdk.paths.course_category_code.put import UpdateConfigurationRaw


class CourseCategoryApiRaw(
    CreateConfigurationUkgProRaw,
    GetAllConfigurationsRaw,
    UpdateConfigurationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
