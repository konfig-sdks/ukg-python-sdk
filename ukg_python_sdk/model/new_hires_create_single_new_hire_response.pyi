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


class NewHiresCreateSingleNewHireResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def contactInformation() -> typing.Type['NewHiresCreateSingleNewHireResponseContactInformation']:
                return NewHiresCreateSingleNewHireResponseContactInformation
        
            @staticmethod
            def job() -> typing.Type['NewHiresCreateSingleNewHireResponseJob']:
                return NewHiresCreateSingleNewHireResponseJob
        
            @staticmethod
            def organizationLevels() -> typing.Type['NewHiresCreateSingleNewHireResponseOrganizationLevels']:
                return NewHiresCreateSingleNewHireResponseOrganizationLevels
        
            @staticmethod
            def compensation() -> typing.Type['NewHiresCreateSingleNewHireResponseCompensation']:
                return NewHiresCreateSingleNewHireResponseCompensation
        
            @staticmethod
            def onboardingOwner() -> typing.Type['NewHiresCreateSingleNewHireResponseOnboardingOwner']:
                return NewHiresCreateSingleNewHireResponseOnboardingOwner
            hireDate = schemas.DateTimeSchema
            orientationDate = schemas.DateTimeSchema
            startDate = schemas.DateTimeSchema
            pastStartDateReason = schemas.StrSchema
        
            @staticmethod
            def mentor() -> typing.Type['NewHiresCreateSingleNewHireResponseMentor']:
                return NewHiresCreateSingleNewHireResponseMentor
            personalMessage = schemas.StrSchema
        
            @staticmethod
            def provisioning() -> typing.Type['NewHiresCreateSingleNewHireResponseProvisioning']:
                return NewHiresCreateSingleNewHireResponseProvisioning
            onboardingStatus = schemas.StrSchema
            identityUserId = schemas.StrSchema
            externalUserId = schemas.StrSchema
            employeeNumber = schemas.StrSchema
            sentToProcessHireDate = schemas.DateTimeSchema
            launchedOn = schemas.DateTimeSchema
            createdAt = schemas.DateTimeSchema
            updatedAt = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "contactInformation": contactInformation,
                "job": job,
                "organizationLevels": organizationLevels,
                "compensation": compensation,
                "onboardingOwner": onboardingOwner,
                "hireDate": hireDate,
                "orientationDate": orientationDate,
                "startDate": startDate,
                "pastStartDateReason": pastStartDateReason,
                "mentor": mentor,
                "personalMessage": personalMessage,
                "provisioning": provisioning,
                "onboardingStatus": onboardingStatus,
                "identityUserId": identityUserId,
                "externalUserId": externalUserId,
                "employeeNumber": employeeNumber,
                "sentToProcessHireDate": sentToProcessHireDate,
                "launchedOn": launchedOn,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactInformation"]) -> 'NewHiresCreateSingleNewHireResponseContactInformation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job"]) -> 'NewHiresCreateSingleNewHireResponseJob': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationLevels"]) -> 'NewHiresCreateSingleNewHireResponseOrganizationLevels': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compensation"]) -> 'NewHiresCreateSingleNewHireResponseCompensation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboardingOwner"]) -> 'NewHiresCreateSingleNewHireResponseOnboardingOwner': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hireDate"]) -> MetaOapg.properties.hireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orientationDate"]) -> MetaOapg.properties.orientationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pastStartDateReason"]) -> MetaOapg.properties.pastStartDateReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mentor"]) -> 'NewHiresCreateSingleNewHireResponseMentor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalMessage"]) -> MetaOapg.properties.personalMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provisioning"]) -> 'NewHiresCreateSingleNewHireResponseProvisioning': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboardingStatus"]) -> MetaOapg.properties.onboardingStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identityUserId"]) -> MetaOapg.properties.identityUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalUserId"]) -> MetaOapg.properties.externalUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sentToProcessHireDate"]) -> MetaOapg.properties.sentToProcessHireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["launchedOn"]) -> MetaOapg.properties.launchedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "contactInformation", "job", "organizationLevels", "compensation", "onboardingOwner", "hireDate", "orientationDate", "startDate", "pastStartDateReason", "mentor", "personalMessage", "provisioning", "onboardingStatus", "identityUserId", "externalUserId", "employeeNumber", "sentToProcessHireDate", "launchedOn", "createdAt", "updatedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactInformation"]) -> typing.Union['NewHiresCreateSingleNewHireResponseContactInformation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job"]) -> typing.Union['NewHiresCreateSingleNewHireResponseJob', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationLevels"]) -> typing.Union['NewHiresCreateSingleNewHireResponseOrganizationLevels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compensation"]) -> typing.Union['NewHiresCreateSingleNewHireResponseCompensation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboardingOwner"]) -> typing.Union['NewHiresCreateSingleNewHireResponseOnboardingOwner', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hireDate"]) -> typing.Union[MetaOapg.properties.hireDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orientationDate"]) -> typing.Union[MetaOapg.properties.orientationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pastStartDateReason"]) -> typing.Union[MetaOapg.properties.pastStartDateReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mentor"]) -> typing.Union['NewHiresCreateSingleNewHireResponseMentor', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalMessage"]) -> typing.Union[MetaOapg.properties.personalMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provisioning"]) -> typing.Union['NewHiresCreateSingleNewHireResponseProvisioning', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboardingStatus"]) -> typing.Union[MetaOapg.properties.onboardingStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identityUserId"]) -> typing.Union[MetaOapg.properties.identityUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalUserId"]) -> typing.Union[MetaOapg.properties.externalUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> typing.Union[MetaOapg.properties.employeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sentToProcessHireDate"]) -> typing.Union[MetaOapg.properties.sentToProcessHireDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["launchedOn"]) -> typing.Union[MetaOapg.properties.launchedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "contactInformation", "job", "organizationLevels", "compensation", "onboardingOwner", "hireDate", "orientationDate", "startDate", "pastStartDateReason", "mentor", "personalMessage", "provisioning", "onboardingStatus", "identityUserId", "externalUserId", "employeeNumber", "sentToProcessHireDate", "launchedOn", "createdAt", "updatedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        contactInformation: typing.Union['NewHiresCreateSingleNewHireResponseContactInformation', schemas.Unset] = schemas.unset,
        job: typing.Union['NewHiresCreateSingleNewHireResponseJob', schemas.Unset] = schemas.unset,
        organizationLevels: typing.Union['NewHiresCreateSingleNewHireResponseOrganizationLevels', schemas.Unset] = schemas.unset,
        compensation: typing.Union['NewHiresCreateSingleNewHireResponseCompensation', schemas.Unset] = schemas.unset,
        onboardingOwner: typing.Union['NewHiresCreateSingleNewHireResponseOnboardingOwner', schemas.Unset] = schemas.unset,
        hireDate: typing.Union[MetaOapg.properties.hireDate, str, datetime, schemas.Unset] = schemas.unset,
        orientationDate: typing.Union[MetaOapg.properties.orientationDate, str, datetime, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, datetime, schemas.Unset] = schemas.unset,
        pastStartDateReason: typing.Union[MetaOapg.properties.pastStartDateReason, str, schemas.Unset] = schemas.unset,
        mentor: typing.Union['NewHiresCreateSingleNewHireResponseMentor', schemas.Unset] = schemas.unset,
        personalMessage: typing.Union[MetaOapg.properties.personalMessage, str, schemas.Unset] = schemas.unset,
        provisioning: typing.Union['NewHiresCreateSingleNewHireResponseProvisioning', schemas.Unset] = schemas.unset,
        onboardingStatus: typing.Union[MetaOapg.properties.onboardingStatus, str, schemas.Unset] = schemas.unset,
        identityUserId: typing.Union[MetaOapg.properties.identityUserId, str, schemas.Unset] = schemas.unset,
        externalUserId: typing.Union[MetaOapg.properties.externalUserId, str, schemas.Unset] = schemas.unset,
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, str, schemas.Unset] = schemas.unset,
        sentToProcessHireDate: typing.Union[MetaOapg.properties.sentToProcessHireDate, str, datetime, schemas.Unset] = schemas.unset,
        launchedOn: typing.Union[MetaOapg.properties.launchedOn, str, datetime, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHiresCreateSingleNewHireResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            contactInformation=contactInformation,
            job=job,
            organizationLevels=organizationLevels,
            compensation=compensation,
            onboardingOwner=onboardingOwner,
            hireDate=hireDate,
            orientationDate=orientationDate,
            startDate=startDate,
            pastStartDateReason=pastStartDateReason,
            mentor=mentor,
            personalMessage=personalMessage,
            provisioning=provisioning,
            onboardingStatus=onboardingStatus,
            identityUserId=identityUserId,
            externalUserId=externalUserId,
            employeeNumber=employeeNumber,
            sentToProcessHireDate=sentToProcessHireDate,
            launchedOn=launchedOn,
            createdAt=createdAt,
            updatedAt=updatedAt,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.new_hires_create_single_new_hire_response_compensation import NewHiresCreateSingleNewHireResponseCompensation
from ukg_python_sdk.model.new_hires_create_single_new_hire_response_contact_information import NewHiresCreateSingleNewHireResponseContactInformation
from ukg_python_sdk.model.new_hires_create_single_new_hire_response_job import NewHiresCreateSingleNewHireResponseJob
from ukg_python_sdk.model.new_hires_create_single_new_hire_response_mentor import NewHiresCreateSingleNewHireResponseMentor
from ukg_python_sdk.model.new_hires_create_single_new_hire_response_onboarding_owner import NewHiresCreateSingleNewHireResponseOnboardingOwner
from ukg_python_sdk.model.new_hires_create_single_new_hire_response_organization_levels import NewHiresCreateSingleNewHireResponseOrganizationLevels
from ukg_python_sdk.model.new_hires_create_single_new_hire_response_provisioning import NewHiresCreateSingleNewHireResponseProvisioning
