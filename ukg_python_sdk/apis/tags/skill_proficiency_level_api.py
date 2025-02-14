# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from ukg_python_sdk.paths.skill_proficiency_level.post import CreateConfigurationUkgPro
from ukg_python_sdk.paths.skill_proficiency_level.get import GetAllConfigurations
from ukg_python_sdk.paths.skill_proficiency_level_code.put import UpdateConfiguration
from ukg_python_sdk.apis.tags.skill_proficiency_level_api_raw import SkillProficiencyLevelApiRaw


class SkillProficiencyLevelApi(
    CreateConfigurationUkgPro,
    GetAllConfigurations,
    UpdateConfiguration,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SkillProficiencyLevelApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SkillProficiencyLevelApiRaw(api_client)
