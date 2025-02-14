# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.project.post import CreateConfiguration
from ukg_python_sdk.paths.project.get import GetAllConfigurations
from ukg_python_sdk.paths.project_code.put import UpdateConfiguration
from ukg_python_sdk.apis.tags.project_api_raw import ProjectApiRaw


class ProjectApi(
    CreateConfiguration,
    GetAllConfigurations,
    UpdateConfiguration,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectApiRaw(api_client)
