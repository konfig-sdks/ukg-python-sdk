# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.course_delivery_met.post import CreateConfigurationUkgProRaw
from ukg_python_sdk.paths.course_delivery_met.get import GetConfigurationsRaw
from ukg_python_sdk.paths.course_delivery_met_code.put import UpdateConfigurationRaw


class CourseDeliveryMetApiRaw(
    CreateConfigurationUkgProRaw,
    GetConfigurationsRaw,
    UpdateConfigurationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
