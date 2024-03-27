# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ukg_python_sdk import schemas  # noqa: F401


class Skill(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An array containing candidate’s skills.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def skill() -> typing.Type['SkillSkill']:
                return SkillSkill
        
            @staticmethod
            def proficiency_level() -> typing.Type['SkillProficiencyLevel']:
                return SkillProficiencyLevel
            __annotations__ = {
                "id": id,
                "skill": skill,
                "proficiency_level": proficiency_level,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skill"]) -> 'SkillSkill': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proficiency_level"]) -> 'SkillProficiencyLevel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "skill", "proficiency_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skill"]) -> typing.Union['SkillSkill', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proficiency_level"]) -> typing.Union['SkillProficiencyLevel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "skill", "proficiency_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        skill: typing.Union['SkillSkill', schemas.Unset] = schemas.unset,
        proficiency_level: typing.Union['SkillProficiencyLevel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Skill':
        return super().__new__(
            cls,
            *args,
            id=id,
            skill=skill,
            proficiency_level=proficiency_level,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.skill_proficiency_level import SkillProficiencyLevel
from ukg_python_sdk.model.skill_skill import SkillSkill
