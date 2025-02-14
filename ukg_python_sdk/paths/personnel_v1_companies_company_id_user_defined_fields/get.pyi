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

from ukg_python_sdk.model.user_defined_fields_get_single_company200_response import UserDefinedFieldsGetSingleCompany200Response as UserDefinedFieldsGetSingleCompany200ResponseSchema
from ukg_python_sdk.model.user_defined_fields_get_single_company400_response import UserDefinedFieldsGetSingleCompany400Response as UserDefinedFieldsGetSingleCompany400ResponseSchema
from ukg_python_sdk.model.user_defined_fields_get_single_company_response import UserDefinedFieldsGetSingleCompanyResponse as UserDefinedFieldsGetSingleCompanyResponseSchema
from ukg_python_sdk.model.user_defined_fields_get_single_company500_response import UserDefinedFieldsGetSingleCompany500Response as UserDefinedFieldsGetSingleCompany500ResponseSchema

from ukg_python_sdk.type.user_defined_fields_get_single_company_response import UserDefinedFieldsGetSingleCompanyResponse
from ukg_python_sdk.type.user_defined_fields_get_single_company200_response import UserDefinedFieldsGetSingleCompany200Response
from ukg_python_sdk.type.user_defined_fields_get_single_company500_response import UserDefinedFieldsGetSingleCompany500Response
from ukg_python_sdk.type.user_defined_fields_get_single_company400_response import UserDefinedFieldsGetSingleCompany400Response

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.user_defined_fields_get_single_company_response import UserDefinedFieldsGetSingleCompanyResponse as UserDefinedFieldsGetSingleCompanyResponsePydantic
from ukg_python_sdk.pydantic.user_defined_fields_get_single_company500_response import UserDefinedFieldsGetSingleCompany500Response as UserDefinedFieldsGetSingleCompany500ResponsePydantic
from ukg_python_sdk.pydantic.user_defined_fields_get_single_company400_response import UserDefinedFieldsGetSingleCompany400Response as UserDefinedFieldsGetSingleCompany400ResponsePydantic
from ukg_python_sdk.pydantic.user_defined_fields_get_single_company200_response import UserDefinedFieldsGetSingleCompany200Response as UserDefinedFieldsGetSingleCompany200ResponsePydantic

# Query params


class EmployeeIdSchema(
    schemas.StrSchema
):
    pass


class PageSchema(
    schemas.Int32Schema
):
    pass


class PerPageSchema(
    schemas.Int32Schema
):
    pass
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
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
SchemaFor200ResponseBodyApplicationJson = UserDefinedFieldsGetSingleCompanyResponseSchema
SchemaFor200ResponseBodyTextJson = UserDefinedFieldsGetSingleCompany200ResponseSchema
SchemaFor200ResponseBodyApplicationProblemjson = UserDefinedFieldsGetSingleCompany200ResponseSchema
SchemaFor200ResponseBodyApplicationXml = UserDefinedFieldsGetSingleCompany200ResponseSchema
SchemaFor200ResponseBodyTextXml = UserDefinedFieldsGetSingleCompany200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UserDefinedFieldsGetSingleCompanyResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UserDefinedFieldsGetSingleCompanyResponse


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
SchemaFor400ResponseBodyApplicationJson = UserDefinedFieldsGetSingleCompany400ResponseSchema
SchemaFor400ResponseBodyTextJson = UserDefinedFieldsGetSingleCompany400ResponseSchema
SchemaFor400ResponseBodyApplicationProblemjson = UserDefinedFieldsGetSingleCompany400ResponseSchema
SchemaFor400ResponseBodyApplicationXml = UserDefinedFieldsGetSingleCompany400ResponseSchema
SchemaFor400ResponseBodyTextXml = UserDefinedFieldsGetSingleCompany400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: UserDefinedFieldsGetSingleCompany400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: UserDefinedFieldsGetSingleCompany400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationProblemjson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextXml),
    },
)
SchemaFor500ResponseBodyApplicationJson = UserDefinedFieldsGetSingleCompany500ResponseSchema
SchemaFor500ResponseBodyTextJson = UserDefinedFieldsGetSingleCompany500ResponseSchema
SchemaFor500ResponseBodyApplicationProblemjson = UserDefinedFieldsGetSingleCompany500ResponseSchema
SchemaFor500ResponseBodyApplicationXml = UserDefinedFieldsGetSingleCompany500ResponseSchema
SchemaFor500ResponseBodyTextXml = UserDefinedFieldsGetSingleCompany500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: UserDefinedFieldsGetSingleCompany500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: UserDefinedFieldsGetSingleCompany500Response


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
_all_accept_content_types = (
    'application/json',
    'text/json',
    'application/problem+json',
    'application/xml',
    'text/xml',
)


class BaseApi(api_client.Api):

    def _get_single_company_mapped_args(
        self,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if employee_id is not None:
            _query_params["employeeId"] = employee_id
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_Page"] = per_page
        if company_id is not None:
            _path_params["companyId"] = company_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_single_company_oapg(
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
        Get User Defined Fields for single company
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
            request_query_employee_id,
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
            path_template='/personnel/v1/companies/{companyId}/user-defined-fields',
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


    def _get_single_company_oapg(
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
        Get User Defined Fields for single company
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
            request_query_employee_id,
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
            path_template='/personnel/v1/companies/{companyId}/user-defined-fields',
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


class GetSingleCompanyRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_single_company(
        self,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_single_company_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        return await self._aget_single_company_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_single_company(
        self,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_single_company_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        return self._get_single_company_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetSingleCompany(BaseApi):

    async def aget_single_company(
        self,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> UserDefinedFieldsGetSingleCompanyResponsePydantic:
        raw_response = await self.raw.aget_single_company(
            company_id=company_id,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
            **kwargs,
        )
        if validate:
            return RootModel[UserDefinedFieldsGetSingleCompanyResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UserDefinedFieldsGetSingleCompanyResponsePydantic, raw_response.body)
    
    
    def get_single_company(
        self,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> UserDefinedFieldsGetSingleCompanyResponsePydantic:
        raw_response = self.raw.get_single_company(
            company_id=company_id,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        if validate:
            return RootModel[UserDefinedFieldsGetSingleCompanyResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UserDefinedFieldsGetSingleCompanyResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_single_company_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        return await self._aget_single_company_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        company_id: str,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_single_company_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        return self._get_single_company_oapg(
            query_params=args.query,
            path_params=args.path,
        )

