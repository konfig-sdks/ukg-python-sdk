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


class NewHiresGetById200ResponseJob(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Job of the new hire
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            
            
            class name(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            code = schemas.StrSchema
            requisitionId = schemas.StrSchema
            
            
            class selectedFLSAStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NOT_SPECIFIED__0(cls):
                    return cls("Not specified = 0")
                
                @schemas.classproperty
                def EXEMPT__1(cls):
                    return cls("Exempt = 1")
                
                @schemas.classproperty
                def NON_EXEMPT__2(cls):
                    return cls("NonExempt = 2")
        
            @staticmethod
            def componentCompany() -> typing.Type['NewHiresGetById200ResponseJobComponentCompany']:
                return NewHiresGetById200ResponseJobComponentCompany
        
            @staticmethod
            def workLocation() -> typing.Type['NewHiresGetById200ResponseJobWorkLocation']:
                return NewHiresGetById200ResponseJobWorkLocation
        
            @staticmethod
            def supervisor() -> typing.Type['NewHiresGetById200ResponseJobSupervisor']:
                return NewHiresGetById200ResponseJobSupervisor
        
            @staticmethod
            def employeeType() -> typing.Type['NewHiresGetById200ResponseJobEmployeeType']:
                return NewHiresGetById200ResponseJobEmployeeType
            __annotations__ = {
                "id": id,
                "name": name,
                "code": code,
                "requisitionId": requisitionId,
                "selectedFLSAStatus": selectedFLSAStatus,
                "componentCompany": componentCompany,
                "workLocation": workLocation,
                "supervisor": supervisor,
                "employeeType": employeeType,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requisitionId"]) -> MetaOapg.properties.requisitionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectedFLSAStatus"]) -> MetaOapg.properties.selectedFLSAStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentCompany"]) -> 'NewHiresGetById200ResponseJobComponentCompany': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workLocation"]) -> 'NewHiresGetById200ResponseJobWorkLocation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supervisor"]) -> 'NewHiresGetById200ResponseJobSupervisor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeType"]) -> 'NewHiresGetById200ResponseJobEmployeeType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "code", "requisitionId", "selectedFLSAStatus", "componentCompany", "workLocation", "supervisor", "employeeType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requisitionId"]) -> typing.Union[MetaOapg.properties.requisitionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectedFLSAStatus"]) -> typing.Union[MetaOapg.properties.selectedFLSAStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentCompany"]) -> typing.Union['NewHiresGetById200ResponseJobComponentCompany', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workLocation"]) -> typing.Union['NewHiresGetById200ResponseJobWorkLocation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supervisor"]) -> typing.Union['NewHiresGetById200ResponseJobSupervisor', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeType"]) -> typing.Union['NewHiresGetById200ResponseJobEmployeeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "code", "requisitionId", "selectedFLSAStatus", "componentCompany", "workLocation", "supervisor", "employeeType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        requisitionId: typing.Union[MetaOapg.properties.requisitionId, str, schemas.Unset] = schemas.unset,
        selectedFLSAStatus: typing.Union[MetaOapg.properties.selectedFLSAStatus, str, schemas.Unset] = schemas.unset,
        componentCompany: typing.Union['NewHiresGetById200ResponseJobComponentCompany', schemas.Unset] = schemas.unset,
        workLocation: typing.Union['NewHiresGetById200ResponseJobWorkLocation', schemas.Unset] = schemas.unset,
        supervisor: typing.Union['NewHiresGetById200ResponseJobSupervisor', schemas.Unset] = schemas.unset,
        employeeType: typing.Union['NewHiresGetById200ResponseJobEmployeeType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NewHiresGetById200ResponseJob':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            code=code,
            requisitionId=requisitionId,
            selectedFLSAStatus=selectedFLSAStatus,
            componentCompany=componentCompany,
            workLocation=workLocation,
            supervisor=supervisor,
            employeeType=employeeType,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.new_hires_get_by_id200_response_job_component_company import NewHiresGetById200ResponseJobComponentCompany
from ukg_python_sdk.model.new_hires_get_by_id200_response_job_employee_type import NewHiresGetById200ResponseJobEmployeeType
from ukg_python_sdk.model.new_hires_get_by_id200_response_job_supervisor import NewHiresGetById200ResponseJobSupervisor
from ukg_python_sdk.model.new_hires_get_by_id200_response_job_work_location import NewHiresGetById200ResponseJobWorkLocation
