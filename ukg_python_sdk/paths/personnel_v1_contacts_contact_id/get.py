# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from ukg_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from ukg_python_sdk.api_response import AsyncGeneratorResponse
from ukg_python_sdk import api_client, exceptions
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

from ukg_python_sdk.model.contact import Contact as ContactSchema

from ukg_python_sdk.type.contact import Contact

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.contact import Contact as ContactPydantic

from . import path

# Query params


class EmployeeIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z0-9]*$',
        }]


class IsActiveSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z]*$',
        }]


class RelationshipCodeSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z]*$',
        }]


class ContactIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z0-9]*$',
        }]


class CountryCodeSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z]*$',
        }]


class CobraIsActiveSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z]*$',
        }]


class CobraStatusSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z]*$',
        }]


class IsBeneficiarySchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z]*$',
        }]


class IsDependentSchema(
    schemas.StrSchema
):


    class MetaOapg:
        regex=[{
            'pattern': r'^[a-zA-Z]*$',
        }]
DateOfCobraEventSchema = schemas.StrSchema
StatusAsOfDateSchema = schemas.StrSchema


class PageSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 2147483647
        inclusive_minimum = 1


class PerPageSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 2147483647
        inclusive_minimum = 1
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
        'isActive': typing.Union[IsActiveSchema, str, ],
        'relationshipCode': typing.Union[RelationshipCodeSchema, str, ],
        'contactId': typing.Union[ContactIdSchema, str, ],
        'countryCode': typing.Union[CountryCodeSchema, str, ],
        'cobraIsActive': typing.Union[CobraIsActiveSchema, str, ],
        'cobraStatus': typing.Union[CobraStatusSchema, str, ],
        'isBeneficiary': typing.Union[IsBeneficiarySchema, str, ],
        'isDependent': typing.Union[IsDependentSchema, str, ],
        'dateOfCobraEvent': typing.Union[DateOfCobraEventSchema, str, ],
        'statusAsOfDate': typing.Union[StatusAsOfDateSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'per_Page': typing.Union[PerPageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_employee_id = api_client.QueryParameter(
    name="employeeId",
    style=api_client.ParameterStyle.FORM,
    schema=EmployeeIdSchema,
    explode=True,
)
request_query_is_active = api_client.QueryParameter(
    name="isActive",
    style=api_client.ParameterStyle.FORM,
    schema=IsActiveSchema,
    explode=True,
)
request_query_relationship_code = api_client.QueryParameter(
    name="relationshipCode",
    style=api_client.ParameterStyle.FORM,
    schema=RelationshipCodeSchema,
    explode=True,
)
request_query_contact_id2 = api_client.QueryParameter(
    name="contactId",
    style=api_client.ParameterStyle.FORM,
    schema=ContactIdSchema,
    explode=True,
)
request_query_country_code = api_client.QueryParameter(
    name="countryCode",
    style=api_client.ParameterStyle.FORM,
    schema=CountryCodeSchema,
    explode=True,
)
request_query_cobra_is_active = api_client.QueryParameter(
    name="cobraIsActive",
    style=api_client.ParameterStyle.FORM,
    schema=CobraIsActiveSchema,
    explode=True,
)
request_query_cobra_status = api_client.QueryParameter(
    name="cobraStatus",
    style=api_client.ParameterStyle.FORM,
    schema=CobraStatusSchema,
    explode=True,
)
request_query_is_beneficiary = api_client.QueryParameter(
    name="isBeneficiary",
    style=api_client.ParameterStyle.FORM,
    schema=IsBeneficiarySchema,
    explode=True,
)
request_query_is_dependent = api_client.QueryParameter(
    name="isDependent",
    style=api_client.ParameterStyle.FORM,
    schema=IsDependentSchema,
    explode=True,
)
request_query_date_of_cobra_event = api_client.QueryParameter(
    name="dateOfCobraEvent",
    style=api_client.ParameterStyle.FORM,
    schema=DateOfCobraEventSchema,
    explode=True,
)
request_query_status_as_of_date = api_client.QueryParameter(
    name="statusAsOfDate",
    style=api_client.ParameterStyle.FORM,
    schema=StatusAsOfDateSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_per_page = api_client.QueryParameter(
    name="per_Page",
    style=api_client.ParameterStyle.FORM,
    schema=PerPageSchema,
    explode=True,
)
# Path params
ContactIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'contactId': typing.Union[ContactIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_contact_id = api_client.PathParameter(
    name="contactId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContactIdSchema,
    required=True,
)
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = ContactSchema
SchemaFor200ResponseBodyTextJson = ContactSchema
SchemaFor200ResponseBodyApplicationProblemjson = ContactSchema
SchemaFor200ResponseBodyApplicationXml = ContactSchema
SchemaFor200ResponseBodyTextXml = ContactSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Contact


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Contact


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationProblemjson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextXml),
    },
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
    'application/problem+json',
    'application/xml',
    'text/xml',
)


class BaseApi(api_client.Api):

    def _get_personnel_contact_details_mapped_args(
        self,
        contact_id: str,
        employee_id: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        relationship_code: typing.Optional[str] = None,
        contact_id2: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        is_beneficiary: typing.Optional[str] = None,
        is_dependent: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        status_as_of_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if employee_id is not None:
            _query_params["employeeId"] = employee_id
        if is_active is not None:
            _query_params["isActive"] = is_active
        if relationship_code is not None:
            _query_params["relationshipCode"] = relationship_code
        if contact_id2 is not None:
            _query_params["contactId"] = contact_id2
        if country_code is not None:
            _query_params["countryCode"] = country_code
        if cobra_is_active is not None:
            _query_params["cobraIsActive"] = cobra_is_active
        if cobra_status is not None:
            _query_params["cobraStatus"] = cobra_status
        if is_beneficiary is not None:
            _query_params["isBeneficiary"] = is_beneficiary
        if is_dependent is not None:
            _query_params["isDependent"] = is_dependent
        if date_of_cobra_event is not None:
            _query_params["dateOfCobraEvent"] = date_of_cobra_event
        if status_as_of_date is not None:
            _query_params["statusAsOfDate"] = status_as_of_date
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_Page"] = per_page
        if contact_id is not None:
            _path_params["contactId"] = contact_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_personnel_contact_details_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get all details for a single person assigned to an employee as a contact
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_contact_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_employee_id,
            request_query_is_active,
            request_query_relationship_code,
            request_query_contact_id2,
            request_query_country_code,
            request_query_cobra_is_active,
            request_query_cobra_status,
            request_query_is_beneficiary,
            request_query_is_dependent,
            request_query_date_of_cobra_event,
            request_query_status_as_of_date,
            request_query_page,
            request_query_per_page,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/personnel/v1/contacts/{contactId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_personnel_contact_details_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get all details for a single person assigned to an employee as a contact
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_contact_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_employee_id,
            request_query_is_active,
            request_query_relationship_code,
            request_query_contact_id2,
            request_query_country_code,
            request_query_cobra_is_active,
            request_query_cobra_status,
            request_query_is_beneficiary,
            request_query_is_dependent,
            request_query_date_of_cobra_event,
            request_query_status_as_of_date,
            request_query_page,
            request_query_per_page,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/personnel/v1/contacts/{contactId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetPersonnelContactDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_personnel_contact_details(
        self,
        contact_id: str,
        employee_id: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        relationship_code: typing.Optional[str] = None,
        contact_id2: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        is_beneficiary: typing.Optional[str] = None,
        is_dependent: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        status_as_of_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_personnel_contact_details_mapped_args(
            contact_id=contact_id,
            employee_id=employee_id,
            is_active=is_active,
            relationship_code=relationship_code,
            contact_id2=contact_id2,
            country_code=country_code,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            is_beneficiary=is_beneficiary,
            is_dependent=is_dependent,
            date_of_cobra_event=date_of_cobra_event,
            status_as_of_date=status_as_of_date,
            page=page,
            per_page=per_page,
        )
        return await self._aget_personnel_contact_details_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_personnel_contact_details(
        self,
        contact_id: str,
        employee_id: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        relationship_code: typing.Optional[str] = None,
        contact_id2: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        is_beneficiary: typing.Optional[str] = None,
        is_dependent: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        status_as_of_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_personnel_contact_details_mapped_args(
            contact_id=contact_id,
            employee_id=employee_id,
            is_active=is_active,
            relationship_code=relationship_code,
            contact_id2=contact_id2,
            country_code=country_code,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            is_beneficiary=is_beneficiary,
            is_dependent=is_dependent,
            date_of_cobra_event=date_of_cobra_event,
            status_as_of_date=status_as_of_date,
            page=page,
            per_page=per_page,
        )
        return self._get_personnel_contact_details_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetPersonnelContactDetails(BaseApi):

    async def aget_personnel_contact_details(
        self,
        contact_id: str,
        employee_id: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        relationship_code: typing.Optional[str] = None,
        contact_id2: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        is_beneficiary: typing.Optional[str] = None,
        is_dependent: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        status_as_of_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ContactPydantic:
        raw_response = await self.raw.aget_personnel_contact_details(
            contact_id=contact_id,
            employee_id=employee_id,
            is_active=is_active,
            relationship_code=relationship_code,
            contact_id2=contact_id2,
            country_code=country_code,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            is_beneficiary=is_beneficiary,
            is_dependent=is_dependent,
            date_of_cobra_event=date_of_cobra_event,
            status_as_of_date=status_as_of_date,
            page=page,
            per_page=per_page,
            **kwargs,
        )
        if validate:
            return ContactPydantic(**raw_response.body)
        return api_client.construct_model_instance(ContactPydantic, raw_response.body)
    
    
    def get_personnel_contact_details(
        self,
        contact_id: str,
        employee_id: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        relationship_code: typing.Optional[str] = None,
        contact_id2: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        is_beneficiary: typing.Optional[str] = None,
        is_dependent: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        status_as_of_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ContactPydantic:
        raw_response = self.raw.get_personnel_contact_details(
            contact_id=contact_id,
            employee_id=employee_id,
            is_active=is_active,
            relationship_code=relationship_code,
            contact_id2=contact_id2,
            country_code=country_code,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            is_beneficiary=is_beneficiary,
            is_dependent=is_dependent,
            date_of_cobra_event=date_of_cobra_event,
            status_as_of_date=status_as_of_date,
            page=page,
            per_page=per_page,
        )
        if validate:
            return ContactPydantic(**raw_response.body)
        return api_client.construct_model_instance(ContactPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        contact_id: str,
        employee_id: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        relationship_code: typing.Optional[str] = None,
        contact_id2: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        is_beneficiary: typing.Optional[str] = None,
        is_dependent: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        status_as_of_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_personnel_contact_details_mapped_args(
            contact_id=contact_id,
            employee_id=employee_id,
            is_active=is_active,
            relationship_code=relationship_code,
            contact_id2=contact_id2,
            country_code=country_code,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            is_beneficiary=is_beneficiary,
            is_dependent=is_dependent,
            date_of_cobra_event=date_of_cobra_event,
            status_as_of_date=status_as_of_date,
            page=page,
            per_page=per_page,
        )
        return await self._aget_personnel_contact_details_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        contact_id: str,
        employee_id: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        relationship_code: typing.Optional[str] = None,
        contact_id2: typing.Optional[str] = None,
        country_code: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        is_beneficiary: typing.Optional[str] = None,
        is_dependent: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        status_as_of_date: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_personnel_contact_details_mapped_args(
            contact_id=contact_id,
            employee_id=employee_id,
            is_active=is_active,
            relationship_code=relationship_code,
            contact_id2=contact_id2,
            country_code=country_code,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            is_beneficiary=is_beneficiary,
            is_dependent=is_dependent,
            date_of_cobra_event=date_of_cobra_event,
            status_as_of_date=status_as_of_date,
            page=page,
            per_page=per_page,
        )
        return self._get_personnel_contact_details_oapg(
            query_params=args.query,
            path_params=args.path,
        )

