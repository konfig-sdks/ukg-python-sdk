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

from ukg_python_sdk.model.person_details_get_single_company_details500_response import PersonDetailsGetSingleCompanyDetails500Response as PersonDetailsGetSingleCompanyDetails500ResponseSchema
from ukg_python_sdk.model.person_details_get_single_company_details200_response import PersonDetailsGetSingleCompanyDetails200Response as PersonDetailsGetSingleCompanyDetails200ResponseSchema
from ukg_python_sdk.model.person_details_get_single_company_details_response import PersonDetailsGetSingleCompanyDetailsResponse as PersonDetailsGetSingleCompanyDetailsResponseSchema

from ukg_python_sdk.type.person_details_get_single_company_details200_response import PersonDetailsGetSingleCompanyDetails200Response
from ukg_python_sdk.type.person_details_get_single_company_details_response import PersonDetailsGetSingleCompanyDetailsResponse
from ukg_python_sdk.type.person_details_get_single_company_details500_response import PersonDetailsGetSingleCompanyDetails500Response

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.person_details_get_single_company_details_response import PersonDetailsGetSingleCompanyDetailsResponse as PersonDetailsGetSingleCompanyDetailsResponsePydantic
from ukg_python_sdk.pydantic.person_details_get_single_company_details500_response import PersonDetailsGetSingleCompanyDetails500Response as PersonDetailsGetSingleCompanyDetails500ResponsePydantic
from ukg_python_sdk.pydantic.person_details_get_single_company_details200_response import PersonDetailsGetSingleCompanyDetails200Response as PersonDetailsGetSingleCompanyDetails200ResponsePydantic

from . import path

# Query params
CompanyIdSchema = schemas.StrSchema
EmployeeIdSchema = schemas.StrSchema
LastNameSchema = schemas.StrSchema
EmailAddressSchema = schemas.StrSchema
AddressStateSchema = schemas.StrSchema
AddressCountrySchema = schemas.StrSchema
CobraIsActiveSchema = schemas.StrSchema
CobraStatusSchema = schemas.StrSchema
DateOfCobraEventSchema = schemas.StrSchema
DateTimeCreatedSchema = schemas.StrSchema
DateTimeChangedSchema = schemas.StrSchema
NationalIdSchema = schemas.StrSchema
NationalIdCountrySchema = schemas.StrSchema


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
        'companyId': typing.Union[CompanyIdSchema, str, ],
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
        'lastName': typing.Union[LastNameSchema, str, ],
        'emailAddress': typing.Union[EmailAddressSchema, str, ],
        'addressState': typing.Union[AddressStateSchema, str, ],
        'addressCountry': typing.Union[AddressCountrySchema, str, ],
        'cobraIsActive': typing.Union[CobraIsActiveSchema, str, ],
        'cobraStatus': typing.Union[CobraStatusSchema, str, ],
        'dateOfCobraEvent': typing.Union[DateOfCobraEventSchema, str, ],
        'dateTimeCreated': typing.Union[DateTimeCreatedSchema, str, ],
        'dateTimeChanged': typing.Union[DateTimeChangedSchema, str, ],
        'nationalId': typing.Union[NationalIdSchema, str, ],
        'nationalIdCountry': typing.Union[NationalIdCountrySchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'per_Page': typing.Union[PerPageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_company_id2 = api_client.QueryParameter(
    name="companyId",
    style=api_client.ParameterStyle.FORM,
    schema=CompanyIdSchema,
    explode=True,
)
request_query_employee_id = api_client.QueryParameter(
    name="employeeId",
    style=api_client.ParameterStyle.FORM,
    schema=EmployeeIdSchema,
    explode=True,
)
request_query_last_name = api_client.QueryParameter(
    name="lastName",
    style=api_client.ParameterStyle.FORM,
    schema=LastNameSchema,
    explode=True,
)
request_query_email_address = api_client.QueryParameter(
    name="emailAddress",
    style=api_client.ParameterStyle.FORM,
    schema=EmailAddressSchema,
    explode=True,
)
request_query_address_state = api_client.QueryParameter(
    name="addressState",
    style=api_client.ParameterStyle.FORM,
    schema=AddressStateSchema,
    explode=True,
)
request_query_address_country = api_client.QueryParameter(
    name="addressCountry",
    style=api_client.ParameterStyle.FORM,
    schema=AddressCountrySchema,
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
request_query_date_of_cobra_event = api_client.QueryParameter(
    name="dateOfCobraEvent",
    style=api_client.ParameterStyle.FORM,
    schema=DateOfCobraEventSchema,
    explode=True,
)
request_query_date_time_created = api_client.QueryParameter(
    name="dateTimeCreated",
    style=api_client.ParameterStyle.FORM,
    schema=DateTimeCreatedSchema,
    explode=True,
)
request_query_date_time_changed = api_client.QueryParameter(
    name="dateTimeChanged",
    style=api_client.ParameterStyle.FORM,
    schema=DateTimeChangedSchema,
    explode=True,
)
request_query_national_id = api_client.QueryParameter(
    name="nationalId",
    style=api_client.ParameterStyle.FORM,
    schema=NationalIdSchema,
    explode=True,
)
request_query_national_id_country = api_client.QueryParameter(
    name="nationalIdCountry",
    style=api_client.ParameterStyle.FORM,
    schema=NationalIdCountrySchema,
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
CompanyIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyId': typing.Union[CompanyIdSchema, str, ],
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


request_path_company_id = api_client.PathParameter(
    name="companyId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyIdSchema,
    required=True,
)
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = PersonDetailsGetSingleCompanyDetailsResponseSchema
SchemaFor200ResponseBodyTextJson = PersonDetailsGetSingleCompanyDetails200ResponseSchema
SchemaFor200ResponseBodyApplicationProblemjson = PersonDetailsGetSingleCompanyDetails200ResponseSchema
SchemaFor200ResponseBodyApplicationXml = PersonDetailsGetSingleCompanyDetails200ResponseSchema
SchemaFor200ResponseBodyTextXml = PersonDetailsGetSingleCompanyDetails200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PersonDetailsGetSingleCompanyDetailsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PersonDetailsGetSingleCompanyDetailsResponse


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
SchemaFor500ResponseBodyApplicationJson = PersonDetailsGetSingleCompanyDetails500ResponseSchema
SchemaFor500ResponseBodyTextJson = PersonDetailsGetSingleCompanyDetails500ResponseSchema
SchemaFor500ResponseBodyApplicationProblemjson = PersonDetailsGetSingleCompanyDetails500ResponseSchema
SchemaFor500ResponseBodyApplicationXml = PersonDetailsGetSingleCompanyDetails500ResponseSchema
SchemaFor500ResponseBodyTextXml = PersonDetailsGetSingleCompanyDetails500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: PersonDetailsGetSingleCompanyDetails500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: PersonDetailsGetSingleCompanyDetails500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyTextJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationProblemjson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaFor500ResponseBodyTextXml),
    },
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

    def _get_single_company_details_mapped_args(
        self,
        company_id: str,
        company_id2: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email_address: typing.Optional[str] = None,
        address_state: typing.Optional[str] = None,
        address_country: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        date_time_changed: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        national_id_country: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if company_id2 is not None:
            _query_params["companyId"] = company_id2
        if employee_id is not None:
            _query_params["employeeId"] = employee_id
        if last_name is not None:
            _query_params["lastName"] = last_name
        if email_address is not None:
            _query_params["emailAddress"] = email_address
        if address_state is not None:
            _query_params["addressState"] = address_state
        if address_country is not None:
            _query_params["addressCountry"] = address_country
        if cobra_is_active is not None:
            _query_params["cobraIsActive"] = cobra_is_active
        if cobra_status is not None:
            _query_params["cobraStatus"] = cobra_status
        if date_of_cobra_event is not None:
            _query_params["dateOfCobraEvent"] = date_of_cobra_event
        if date_time_created is not None:
            _query_params["dateTimeCreated"] = date_time_created
        if date_time_changed is not None:
            _query_params["dateTimeChanged"] = date_time_changed
        if national_id is not None:
            _query_params["nationalId"] = national_id
        if national_id_country is not None:
            _query_params["nationalIdCountry"] = national_id_country
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_Page"] = per_page
        if company_id is not None:
            _path_params["companyId"] = company_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_single_company_details_oapg(
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
        Get all person details for a single company
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
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
            request_query_company_id2,
            request_query_employee_id,
            request_query_last_name,
            request_query_email_address,
            request_query_address_state,
            request_query_address_country,
            request_query_cobra_is_active,
            request_query_cobra_status,
            request_query_date_of_cobra_event,
            request_query_date_time_created,
            request_query_date_time_changed,
            request_query_national_id,
            request_query_national_id_country,
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
            path_template='/personnel/v1/companies/{companyId}/person-details',
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


    def _get_single_company_details_oapg(
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
        Get all person details for a single company
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
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
            request_query_company_id2,
            request_query_employee_id,
            request_query_last_name,
            request_query_email_address,
            request_query_address_state,
            request_query_address_country,
            request_query_cobra_is_active,
            request_query_cobra_status,
            request_query_date_of_cobra_event,
            request_query_date_time_created,
            request_query_date_time_changed,
            request_query_national_id,
            request_query_national_id_country,
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
            path_template='/personnel/v1/companies/{companyId}/person-details',
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


class GetSingleCompanyDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_single_company_details(
        self,
        company_id: str,
        company_id2: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email_address: typing.Optional[str] = None,
        address_state: typing.Optional[str] = None,
        address_country: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        date_time_changed: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        national_id_country: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_single_company_details_mapped_args(
            company_id=company_id,
            company_id2=company_id2,
            employee_id=employee_id,
            last_name=last_name,
            email_address=email_address,
            address_state=address_state,
            address_country=address_country,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            date_of_cobra_event=date_of_cobra_event,
            date_time_created=date_time_created,
            date_time_changed=date_time_changed,
            national_id=national_id,
            national_id_country=national_id_country,
            page=page,
            per_page=per_page,
        )
        return await self._aget_single_company_details_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_single_company_details(
        self,
        company_id: str,
        company_id2: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email_address: typing.Optional[str] = None,
        address_state: typing.Optional[str] = None,
        address_country: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        date_time_changed: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        national_id_country: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_single_company_details_mapped_args(
            company_id=company_id,
            company_id2=company_id2,
            employee_id=employee_id,
            last_name=last_name,
            email_address=email_address,
            address_state=address_state,
            address_country=address_country,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            date_of_cobra_event=date_of_cobra_event,
            date_time_created=date_time_created,
            date_time_changed=date_time_changed,
            national_id=national_id,
            national_id_country=national_id_country,
            page=page,
            per_page=per_page,
        )
        return self._get_single_company_details_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetSingleCompanyDetails(BaseApi):

    async def aget_single_company_details(
        self,
        company_id: str,
        company_id2: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email_address: typing.Optional[str] = None,
        address_state: typing.Optional[str] = None,
        address_country: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        date_time_changed: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        national_id_country: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> PersonDetailsGetSingleCompanyDetailsResponsePydantic:
        raw_response = await self.raw.aget_single_company_details(
            company_id=company_id,
            company_id2=company_id2,
            employee_id=employee_id,
            last_name=last_name,
            email_address=email_address,
            address_state=address_state,
            address_country=address_country,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            date_of_cobra_event=date_of_cobra_event,
            date_time_created=date_time_created,
            date_time_changed=date_time_changed,
            national_id=national_id,
            national_id_country=national_id_country,
            page=page,
            per_page=per_page,
            **kwargs,
        )
        if validate:
            return RootModel[PersonDetailsGetSingleCompanyDetailsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PersonDetailsGetSingleCompanyDetailsResponsePydantic, raw_response.body)
    
    
    def get_single_company_details(
        self,
        company_id: str,
        company_id2: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email_address: typing.Optional[str] = None,
        address_state: typing.Optional[str] = None,
        address_country: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        date_time_changed: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        national_id_country: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> PersonDetailsGetSingleCompanyDetailsResponsePydantic:
        raw_response = self.raw.get_single_company_details(
            company_id=company_id,
            company_id2=company_id2,
            employee_id=employee_id,
            last_name=last_name,
            email_address=email_address,
            address_state=address_state,
            address_country=address_country,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            date_of_cobra_event=date_of_cobra_event,
            date_time_created=date_time_created,
            date_time_changed=date_time_changed,
            national_id=national_id,
            national_id_country=national_id_country,
            page=page,
            per_page=per_page,
        )
        if validate:
            return RootModel[PersonDetailsGetSingleCompanyDetailsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(PersonDetailsGetSingleCompanyDetailsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: str,
        company_id2: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email_address: typing.Optional[str] = None,
        address_state: typing.Optional[str] = None,
        address_country: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        date_time_changed: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        national_id_country: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_single_company_details_mapped_args(
            company_id=company_id,
            company_id2=company_id2,
            employee_id=employee_id,
            last_name=last_name,
            email_address=email_address,
            address_state=address_state,
            address_country=address_country,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            date_of_cobra_event=date_of_cobra_event,
            date_time_created=date_time_created,
            date_time_changed=date_time_changed,
            national_id=national_id,
            national_id_country=national_id_country,
            page=page,
            per_page=per_page,
        )
        return await self._aget_single_company_details_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        company_id: str,
        company_id2: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        email_address: typing.Optional[str] = None,
        address_state: typing.Optional[str] = None,
        address_country: typing.Optional[str] = None,
        cobra_is_active: typing.Optional[str] = None,
        cobra_status: typing.Optional[str] = None,
        date_of_cobra_event: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        date_time_changed: typing.Optional[str] = None,
        national_id: typing.Optional[str] = None,
        national_id_country: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_single_company_details_mapped_args(
            company_id=company_id,
            company_id2=company_id2,
            employee_id=employee_id,
            last_name=last_name,
            email_address=email_address,
            address_state=address_state,
            address_country=address_country,
            cobra_is_active=cobra_is_active,
            cobra_status=cobra_status,
            date_of_cobra_event=date_of_cobra_event,
            date_time_created=date_time_created,
            date_time_changed=date_time_changed,
            national_id=national_id,
            national_id_country=national_id_country,
            page=page,
            per_page=per_page,
        )
        return self._get_single_company_details_oapg(
            query_params=args.query,
            path_params=args.path,
        )

