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

from ukg_python_sdk.model.user_details_get_user_details404_response import UserDetailsGetUserDetails404Response as UserDetailsGetUserDetails404ResponseSchema
from ukg_python_sdk.model.user_details_get_user_details200_response import UserDetailsGetUserDetails200Response as UserDetailsGetUserDetails200ResponseSchema
from ukg_python_sdk.model.user_details_get_user_details_response import UserDetailsGetUserDetailsResponse as UserDetailsGetUserDetailsResponseSchema
from ukg_python_sdk.model.user_details_get_user_details500_response import UserDetailsGetUserDetails500Response as UserDetailsGetUserDetails500ResponseSchema

from ukg_python_sdk.type.user_details_get_user_details200_response import UserDetailsGetUserDetails200Response
from ukg_python_sdk.type.user_details_get_user_details_response import UserDetailsGetUserDetailsResponse
from ukg_python_sdk.type.user_details_get_user_details500_response import UserDetailsGetUserDetails500Response
from ukg_python_sdk.type.user_details_get_user_details404_response import UserDetailsGetUserDetails404Response

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.user_details_get_user_details_response import UserDetailsGetUserDetailsResponse as UserDetailsGetUserDetailsResponsePydantic
from ukg_python_sdk.pydantic.user_details_get_user_details404_response import UserDetailsGetUserDetails404Response as UserDetailsGetUserDetails404ResponsePydantic
from ukg_python_sdk.pydantic.user_details_get_user_details500_response import UserDetailsGetUserDetails500Response as UserDetailsGetUserDetails500ResponsePydantic
from ukg_python_sdk.pydantic.user_details_get_user_details200_response import UserDetailsGetUserDetails200Response as UserDetailsGetUserDetails200ResponsePydantic

# Query params
UserNameSchema = schemas.StrSchema
UserStatusSchema = schemas.StrSchema


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
        'userName': typing.Union[UserNameSchema, str, ],
        'userStatus': typing.Union[UserStatusSchema, str, ],
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'per_Page': typing.Union[PerPageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_user_name = api_client.QueryParameter(
    name="userName",
    style=api_client.ParameterStyle.FORM,
    schema=UserNameSchema,
    explode=True,
)
request_query_user_status = api_client.QueryParameter(
    name="userStatus",
    style=api_client.ParameterStyle.FORM,
    schema=UserStatusSchema,
    explode=True,
)
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
SchemaFor200ResponseBodyApplicationJson = UserDetailsGetUserDetailsResponseSchema
SchemaFor200ResponseBodyTextJson = UserDetailsGetUserDetails200ResponseSchema
SchemaFor200ResponseBodyApplicationProblemjson = UserDetailsGetUserDetails200ResponseSchema
SchemaFor200ResponseBodyApplicationXml = UserDetailsGetUserDetails200ResponseSchema
SchemaFor200ResponseBodyTextXml = UserDetailsGetUserDetails200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UserDetailsGetUserDetailsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UserDetailsGetUserDetailsResponse


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
SchemaFor404ResponseBodyApplicationJson = UserDetailsGetUserDetails404ResponseSchema
SchemaFor404ResponseBodyTextJson = UserDetailsGetUserDetails404ResponseSchema
SchemaFor404ResponseBodyApplicationProblemjson = UserDetailsGetUserDetails404ResponseSchema
SchemaFor404ResponseBodyApplicationXml = UserDetailsGetUserDetails404ResponseSchema
SchemaFor404ResponseBodyTextXml = UserDetailsGetUserDetails404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: UserDetailsGetUserDetails404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: UserDetailsGetUserDetails404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationProblemjson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextXml),
    },
)
SchemaFor500ResponseBodyApplicationJson = UserDetailsGetUserDetails500ResponseSchema
SchemaFor500ResponseBodyTextJson = UserDetailsGetUserDetails500ResponseSchema
SchemaFor500ResponseBodyApplicationProblemjson = UserDetailsGetUserDetails500ResponseSchema
SchemaFor500ResponseBodyApplicationXml = UserDetailsGetUserDetails500ResponseSchema
SchemaFor500ResponseBodyTextXml = UserDetailsGetUserDetails500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: UserDetailsGetUserDetails500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: UserDetailsGetUserDetails500Response


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

    def _get_user_details_mapped_args(
        self,
        user_name: typing.Optional[str] = None,
        user_status: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if user_name is not None:
            _query_params["userName"] = user_name
        if user_status is not None:
            _query_params["userStatus"] = user_status
        if employee_id is not None:
            _query_params["employeeId"] = employee_id
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_Page"] = per_page
        args.query = _query_params
        return args

    async def _aget_user_details_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Get User Details
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_user_name,
            request_query_user_status,
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
            path_template='/personnel/v1/user-details',
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


    def _get_user_details_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get User Details
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_user_name,
            request_query_user_status,
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
            path_template='/personnel/v1/user-details',
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


class GetUserDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_user_details(
        self,
        user_name: typing.Optional[str] = None,
        user_status: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_details_mapped_args(
            user_name=user_name,
            user_status=user_status,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        return await self._aget_user_details_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_user_details(
        self,
        user_name: typing.Optional[str] = None,
        user_status: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_details_mapped_args(
            user_name=user_name,
            user_status=user_status,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        return self._get_user_details_oapg(
            query_params=args.query,
        )

class GetUserDetails(BaseApi):

    async def aget_user_details(
        self,
        user_name: typing.Optional[str] = None,
        user_status: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> UserDetailsGetUserDetailsResponsePydantic:
        raw_response = await self.raw.aget_user_details(
            user_name=user_name,
            user_status=user_status,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
            **kwargs,
        )
        if validate:
            return RootModel[UserDetailsGetUserDetailsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UserDetailsGetUserDetailsResponsePydantic, raw_response.body)
    
    
    def get_user_details(
        self,
        user_name: typing.Optional[str] = None,
        user_status: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> UserDetailsGetUserDetailsResponsePydantic:
        raw_response = self.raw.get_user_details(
            user_name=user_name,
            user_status=user_status,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        if validate:
            return RootModel[UserDetailsGetUserDetailsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UserDetailsGetUserDetailsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        user_name: typing.Optional[str] = None,
        user_status: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_user_details_mapped_args(
            user_name=user_name,
            user_status=user_status,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        return await self._aget_user_details_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        user_name: typing.Optional[str] = None,
        user_status: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_user_details_mapped_args(
            user_name=user_name,
            user_status=user_status,
            employee_id=employee_id,
            page=page,
            per_page=per_page,
        )
        return self._get_user_details_oapg(
            query_params=args.query,
        )

