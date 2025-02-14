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


class PostingsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def title() -> typing.Type['Translations']:
                return Translations
        
            @staticmethod
            def description() -> typing.Type['PostingsItemDescription']:
                return PostingsItemDescription
            id = schemas.StrSchema
        
            @staticmethod
            def tenant() -> typing.Type['PostingsItemTenant']:
                return PostingsItemTenant
        
            @staticmethod
            def opportunity() -> typing.Type['PostingsItemOpportunity']:
                return PostingsItemOpportunity
            updated_at = schemas.StrSchema
            created_at = schemas.StrSchema
            requisition_number = schemas.StrSchema
        
            @staticmethod
            def default_locale() -> typing.Type['PostingsItemDefaultLocale']:
                return PostingsItemDefaultLocale
            compensation = schemas.StrSchema
        
            @staticmethod
            def job_family() -> typing.Type['PostingsItemJobFamily']:
                return PostingsItemJobFamily
        
            @staticmethod
            def locations() -> typing.Type['PostingsItemLocations']:
                return PostingsItemLocations
            locations_summary = schemas.StrSchema
        
            @staticmethod
            def company() -> typing.Type['PostingsItemCompany']:
                return PostingsItemCompany
            is_featured = schemas.BoolSchema
        
            @staticmethod
            def skill_criteria() -> typing.Type['PostingsItemSkillCriteria']:
                return PostingsItemSkillCriteria
        
            @staticmethod
            def work_experience_criteria() -> typing.Type['PostingsItemWorkExperienceCriteria']:
                return PostingsItemWorkExperienceCriteria
        
            @staticmethod
            def education_criteria() -> typing.Type['PostingsItemEducationCriteria']:
                return PostingsItemEducationCriteria
        
            @staticmethod
            def license_criteria() -> typing.Type['PostingsItemLicenseCriteria']:
                return PostingsItemLicenseCriteria
        
            @staticmethod
            def behavior_criteria() -> typing.Type['PostingsItemBehaviorCriteria']:
                return PostingsItemBehaviorCriteria
        
            @staticmethod
            def motivation_criteria() -> typing.Type['PostingsItemMotivationCriteria']:
                return PostingsItemMotivationCriteria
            publish_date = schemas.StrSchema
        
            @staticmethod
            def locales() -> typing.Type['PostingsItemLocales']:
                return PostingsItemLocales
            recruiting_apply_url = schemas.StrSchema
        
            @staticmethod
            def links() -> typing.Type['PostingsItemLinks']:
                return PostingsItemLinks
            __annotations__ = {
                "title": title,
                "description": description,
                "id": id,
                "tenant": tenant,
                "opportunity": opportunity,
                "updated_at": updated_at,
                "created_at": created_at,
                "requisition_number": requisition_number,
                "default_locale": default_locale,
                "compensation": compensation,
                "job_family": job_family,
                "locations": locations,
                "locations_summary": locations_summary,
                "company": company,
                "is_featured": is_featured,
                "skill_criteria": skill_criteria,
                "work_experience_criteria": work_experience_criteria,
                "education_criteria": education_criteria,
                "license_criteria": license_criteria,
                "behavior_criteria": behavior_criteria,
                "motivation_criteria": motivation_criteria,
                "publish_date": publish_date,
                "locales": locales,
                "recruiting_apply_url": recruiting_apply_url,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> 'Translations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'PostingsItemDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenant"]) -> 'PostingsItemTenant': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["opportunity"]) -> 'PostingsItemOpportunity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requisition_number"]) -> MetaOapg.properties.requisition_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_locale"]) -> 'PostingsItemDefaultLocale': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compensation"]) -> MetaOapg.properties.compensation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_family"]) -> 'PostingsItemJobFamily': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locations"]) -> 'PostingsItemLocations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locations_summary"]) -> MetaOapg.properties.locations_summary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'PostingsItemCompany': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_featured"]) -> MetaOapg.properties.is_featured: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skill_criteria"]) -> 'PostingsItemSkillCriteria': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_experience_criteria"]) -> 'PostingsItemWorkExperienceCriteria': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["education_criteria"]) -> 'PostingsItemEducationCriteria': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["license_criteria"]) -> 'PostingsItemLicenseCriteria': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["behavior_criteria"]) -> 'PostingsItemBehaviorCriteria': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["motivation_criteria"]) -> 'PostingsItemMotivationCriteria': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publish_date"]) -> MetaOapg.properties.publish_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locales"]) -> 'PostingsItemLocales': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruiting_apply_url"]) -> MetaOapg.properties.recruiting_apply_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'PostingsItemLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "id", "tenant", "opportunity", "updated_at", "created_at", "requisition_number", "default_locale", "compensation", "job_family", "locations", "locations_summary", "company", "is_featured", "skill_criteria", "work_experience_criteria", "education_criteria", "license_criteria", "behavior_criteria", "motivation_criteria", "publish_date", "locales", "recruiting_apply_url", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union['Translations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['PostingsItemDescription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenant"]) -> typing.Union['PostingsItemTenant', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["opportunity"]) -> typing.Union['PostingsItemOpportunity', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requisition_number"]) -> typing.Union[MetaOapg.properties.requisition_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_locale"]) -> typing.Union['PostingsItemDefaultLocale', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compensation"]) -> typing.Union[MetaOapg.properties.compensation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_family"]) -> typing.Union['PostingsItemJobFamily', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locations"]) -> typing.Union['PostingsItemLocations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locations_summary"]) -> typing.Union[MetaOapg.properties.locations_summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> typing.Union['PostingsItemCompany', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_featured"]) -> typing.Union[MetaOapg.properties.is_featured, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skill_criteria"]) -> typing.Union['PostingsItemSkillCriteria', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_experience_criteria"]) -> typing.Union['PostingsItemWorkExperienceCriteria', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["education_criteria"]) -> typing.Union['PostingsItemEducationCriteria', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["license_criteria"]) -> typing.Union['PostingsItemLicenseCriteria', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["behavior_criteria"]) -> typing.Union['PostingsItemBehaviorCriteria', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["motivation_criteria"]) -> typing.Union['PostingsItemMotivationCriteria', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publish_date"]) -> typing.Union[MetaOapg.properties.publish_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locales"]) -> typing.Union['PostingsItemLocales', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruiting_apply_url"]) -> typing.Union[MetaOapg.properties.recruiting_apply_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['PostingsItemLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "id", "tenant", "opportunity", "updated_at", "created_at", "requisition_number", "default_locale", "compensation", "job_family", "locations", "locations_summary", "company", "is_featured", "skill_criteria", "work_experience_criteria", "education_criteria", "license_criteria", "behavior_criteria", "motivation_criteria", "publish_date", "locales", "recruiting_apply_url", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union['Translations', schemas.Unset] = schemas.unset,
        description: typing.Union['PostingsItemDescription', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        tenant: typing.Union['PostingsItemTenant', schemas.Unset] = schemas.unset,
        opportunity: typing.Union['PostingsItemOpportunity', schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        requisition_number: typing.Union[MetaOapg.properties.requisition_number, str, schemas.Unset] = schemas.unset,
        default_locale: typing.Union['PostingsItemDefaultLocale', schemas.Unset] = schemas.unset,
        compensation: typing.Union[MetaOapg.properties.compensation, str, schemas.Unset] = schemas.unset,
        job_family: typing.Union['PostingsItemJobFamily', schemas.Unset] = schemas.unset,
        locations: typing.Union['PostingsItemLocations', schemas.Unset] = schemas.unset,
        locations_summary: typing.Union[MetaOapg.properties.locations_summary, str, schemas.Unset] = schemas.unset,
        company: typing.Union['PostingsItemCompany', schemas.Unset] = schemas.unset,
        is_featured: typing.Union[MetaOapg.properties.is_featured, bool, schemas.Unset] = schemas.unset,
        skill_criteria: typing.Union['PostingsItemSkillCriteria', schemas.Unset] = schemas.unset,
        work_experience_criteria: typing.Union['PostingsItemWorkExperienceCriteria', schemas.Unset] = schemas.unset,
        education_criteria: typing.Union['PostingsItemEducationCriteria', schemas.Unset] = schemas.unset,
        license_criteria: typing.Union['PostingsItemLicenseCriteria', schemas.Unset] = schemas.unset,
        behavior_criteria: typing.Union['PostingsItemBehaviorCriteria', schemas.Unset] = schemas.unset,
        motivation_criteria: typing.Union['PostingsItemMotivationCriteria', schemas.Unset] = schemas.unset,
        publish_date: typing.Union[MetaOapg.properties.publish_date, str, schemas.Unset] = schemas.unset,
        locales: typing.Union['PostingsItemLocales', schemas.Unset] = schemas.unset,
        recruiting_apply_url: typing.Union[MetaOapg.properties.recruiting_apply_url, str, schemas.Unset] = schemas.unset,
        links: typing.Union['PostingsItemLinks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostingsItem':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            id=id,
            tenant=tenant,
            opportunity=opportunity,
            updated_at=updated_at,
            created_at=created_at,
            requisition_number=requisition_number,
            default_locale=default_locale,
            compensation=compensation,
            job_family=job_family,
            locations=locations,
            locations_summary=locations_summary,
            company=company,
            is_featured=is_featured,
            skill_criteria=skill_criteria,
            work_experience_criteria=work_experience_criteria,
            education_criteria=education_criteria,
            license_criteria=license_criteria,
            behavior_criteria=behavior_criteria,
            motivation_criteria=motivation_criteria,
            publish_date=publish_date,
            locales=locales,
            recruiting_apply_url=recruiting_apply_url,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.postings_item_behavior_criteria import PostingsItemBehaviorCriteria
from ukg_python_sdk.model.postings_item_company import PostingsItemCompany
from ukg_python_sdk.model.postings_item_default_locale import PostingsItemDefaultLocale
from ukg_python_sdk.model.postings_item_description import PostingsItemDescription
from ukg_python_sdk.model.postings_item_education_criteria import PostingsItemEducationCriteria
from ukg_python_sdk.model.postings_item_job_family import PostingsItemJobFamily
from ukg_python_sdk.model.postings_item_license_criteria import PostingsItemLicenseCriteria
from ukg_python_sdk.model.postings_item_links import PostingsItemLinks
from ukg_python_sdk.model.postings_item_locales import PostingsItemLocales
from ukg_python_sdk.model.postings_item_locations import PostingsItemLocations
from ukg_python_sdk.model.postings_item_motivation_criteria import PostingsItemMotivationCriteria
from ukg_python_sdk.model.postings_item_opportunity import PostingsItemOpportunity
from ukg_python_sdk.model.postings_item_skill_criteria import PostingsItemSkillCriteria
from ukg_python_sdk.model.postings_item_tenant import PostingsItemTenant
from ukg_python_sdk.model.postings_item_work_experience_criteria import PostingsItemWorkExperienceCriteria
from ukg_python_sdk.model.translations import Translations
