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


class OrgLevelsBodyItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "code",
            "level",
            "description",
        }
        
        class properties:
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            code = schemas.StrSchema
            level = schemas.NumberSchema
            budgetGroup = schemas.StrSchema
            currentYearBudgetFTE = schemas.Float64Schema
            currentYearBudgetSalary = schemas.Float64Schema
            
            
            class glSegment(
                schemas.StrSchema
            ):
                pass
            lastYearBudgetFTE = schemas.NumberSchema
            lastYearBudgetSalary = schemas.NumberSchema
            levelDescription = schemas.StrSchema
            reportingCategory = schemas.StrSchema
            isActive = schemas.BoolSchema
            __annotations__ = {
                "description": description,
                "code": code,
                "level": level,
                "budgetGroup": budgetGroup,
                "currentYearBudgetFTE": currentYearBudgetFTE,
                "currentYearBudgetSalary": currentYearBudgetSalary,
                "glSegment": glSegment,
                "lastYearBudgetFTE": lastYearBudgetFTE,
                "lastYearBudgetSalary": lastYearBudgetSalary,
                "levelDescription": levelDescription,
                "reportingCategory": reportingCategory,
                "isActive": isActive,
            }
    
    code: MetaOapg.properties.code
    level: MetaOapg.properties.level
    description: MetaOapg.properties.description
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budgetGroup"]) -> MetaOapg.properties.budgetGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentYearBudgetFTE"]) -> MetaOapg.properties.currentYearBudgetFTE: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentYearBudgetSalary"]) -> MetaOapg.properties.currentYearBudgetSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["glSegment"]) -> MetaOapg.properties.glSegment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastYearBudgetFTE"]) -> MetaOapg.properties.lastYearBudgetFTE: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastYearBudgetSalary"]) -> MetaOapg.properties.lastYearBudgetSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["levelDescription"]) -> MetaOapg.properties.levelDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reportingCategory"]) -> MetaOapg.properties.reportingCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "code", "level", "budgetGroup", "currentYearBudgetFTE", "currentYearBudgetSalary", "glSegment", "lastYearBudgetFTE", "lastYearBudgetSalary", "levelDescription", "reportingCategory", "isActive", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budgetGroup"]) -> typing.Union[MetaOapg.properties.budgetGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentYearBudgetFTE"]) -> typing.Union[MetaOapg.properties.currentYearBudgetFTE, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentYearBudgetSalary"]) -> typing.Union[MetaOapg.properties.currentYearBudgetSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["glSegment"]) -> typing.Union[MetaOapg.properties.glSegment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastYearBudgetFTE"]) -> typing.Union[MetaOapg.properties.lastYearBudgetFTE, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastYearBudgetSalary"]) -> typing.Union[MetaOapg.properties.lastYearBudgetSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["levelDescription"]) -> typing.Union[MetaOapg.properties.levelDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reportingCategory"]) -> typing.Union[MetaOapg.properties.reportingCategory, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "code", "level", "budgetGroup", "currentYearBudgetFTE", "currentYearBudgetSalary", "glSegment", "lastYearBudgetFTE", "lastYearBudgetSalary", "levelDescription", "reportingCategory", "isActive", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        level: typing.Union[MetaOapg.properties.level, decimal.Decimal, int, float, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        budgetGroup: typing.Union[MetaOapg.properties.budgetGroup, str, schemas.Unset] = schemas.unset,
        currentYearBudgetFTE: typing.Union[MetaOapg.properties.currentYearBudgetFTE, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currentYearBudgetSalary: typing.Union[MetaOapg.properties.currentYearBudgetSalary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        glSegment: typing.Union[MetaOapg.properties.glSegment, str, schemas.Unset] = schemas.unset,
        lastYearBudgetFTE: typing.Union[MetaOapg.properties.lastYearBudgetFTE, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        lastYearBudgetSalary: typing.Union[MetaOapg.properties.lastYearBudgetSalary, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        levelDescription: typing.Union[MetaOapg.properties.levelDescription, str, schemas.Unset] = schemas.unset,
        reportingCategory: typing.Union[MetaOapg.properties.reportingCategory, str, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrgLevelsBodyItem':
        return super().__new__(
            cls,
            *args,
            code=code,
            level=level,
            description=description,
            budgetGroup=budgetGroup,
            currentYearBudgetFTE=currentYearBudgetFTE,
            currentYearBudgetSalary=currentYearBudgetSalary,
            glSegment=glSegment,
            lastYearBudgetFTE=lastYearBudgetFTE,
            lastYearBudgetSalary=lastYearBudgetSalary,
            levelDescription=levelDescription,
            reportingCategory=reportingCategory,
            isActive=isActive,
            _configuration=_configuration,
            **kwargs,
        )
