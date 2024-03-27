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

from ukg_python_sdk.model.bad_request import BadRequest as BadRequestSchema
from ukg_python_sdk.model.background_checks_application import BackgroundChecksApplication as BackgroundChecksApplicationSchema
from ukg_python_sdk.model.background_checks import BackgroundChecks as BackgroundChecksSchema
from ukg_python_sdk.model.links import Links as LinksSchema
from ukg_python_sdk.model.background_checks_author import BackgroundChecksAuthor as BackgroundChecksAuthorSchema
from ukg_python_sdk.model.background_checks_packages import BackgroundChecksPackages as BackgroundChecksPackagesSchema

from ukg_python_sdk.type.background_checks_author import BackgroundChecksAuthor
from ukg_python_sdk.type.background_checks import BackgroundChecks
from ukg_python_sdk.type.bad_request import BadRequest
from ukg_python_sdk.type.background_checks_packages import BackgroundChecksPackages
from ukg_python_sdk.type.links import Links
from ukg_python_sdk.type.background_checks_application import BackgroundChecksApplication

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.background_checks_application import BackgroundChecksApplication as BackgroundChecksApplicationPydantic
from ukg_python_sdk.pydantic.links import Links as LinksPydantic
from ukg_python_sdk.pydantic.background_checks import BackgroundChecks as BackgroundChecksPydantic
from ukg_python_sdk.pydantic.bad_request import BadRequest as BadRequestPydantic
from ukg_python_sdk.pydantic.background_checks_author import BackgroundChecksAuthor as BackgroundChecksAuthorPydantic
from ukg_python_sdk.pydantic.background_checks_packages import BackgroundChecksPackages as BackgroundChecksPackagesPydantic

# Path params
CandidateIdSchema = schemas.StrSchema
TenantAliasSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'candidate-id': typing.Union[CandidateIdSchema, str, ],
        'tenant-alias': typing.Union[TenantAliasSchema, str, ],
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


request_path_candidate_id = api_client.PathParameter(
    name="candidate-id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CandidateIdSchema,
    required=True,
)
request_path_tenant_alias = api_client.PathParameter(
    name="tenant-alias",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TenantAliasSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = BackgroundChecksSchema


request_body_background_checks = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = BackgroundChecksSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: BackgroundChecks


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: BackgroundChecks


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = BadRequestSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: BadRequest


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: BadRequest


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_background_check_mapped_args(
        self,
        author: BackgroundChecksAuthor,
        application: BackgroundChecksApplication,
        status: str,
        order_number: str,
        packages: BackgroundChecksPackages,
        candidate_id: str,
        tenant_alias: str,
        links: typing.Optional[typing.List[Links]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if author is not None:
            _body["author"] = author
        if application is not None:
            _body["application"] = application
        if status is not None:
            _body["status"] = status
        if order_number is not None:
            _body["order_number"] = order_number
        if packages is not None:
            _body["packages"] = packages
        if links is not None:
            _body["links"] = links
        args.body = _body
        if candidate_id is not None:
            _path_params["candidate-id"] = candidate_id
        if tenant_alias is not None:
            _path_params["tenant-alias"] = tenant_alias
        args.path = _path_params
        return args

    async def _aadd_background_check_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Background Check Request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_candidate_id,
            request_path_tenant_alias,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{tenant-alias}/api/candidates/{candidate-id}/background-checks',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_background_checks.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _add_background_check_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Background Check Request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_candidate_id,
            request_path_tenant_alias,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{tenant-alias}/api/candidates/{candidate-id}/background-checks',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_background_checks.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class AddBackgroundCheckRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_background_check(
        self,
        author: BackgroundChecksAuthor,
        application: BackgroundChecksApplication,
        status: str,
        order_number: str,
        packages: BackgroundChecksPackages,
        candidate_id: str,
        tenant_alias: str,
        links: typing.Optional[typing.List[Links]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_background_check_mapped_args(
            author=author,
            application=application,
            status=status,
            order_number=order_number,
            packages=packages,
            candidate_id=candidate_id,
            tenant_alias=tenant_alias,
            links=links,
        )
        return await self._aadd_background_check_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def add_background_check(
        self,
        author: BackgroundChecksAuthor,
        application: BackgroundChecksApplication,
        status: str,
        order_number: str,
        packages: BackgroundChecksPackages,
        candidate_id: str,
        tenant_alias: str,
        links: typing.Optional[typing.List[Links]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_background_check_mapped_args(
            author=author,
            application=application,
            status=status,
            order_number=order_number,
            packages=packages,
            candidate_id=candidate_id,
            tenant_alias=tenant_alias,
            links=links,
        )
        return self._add_background_check_oapg(
            body=args.body,
            path_params=args.path,
        )

class AddBackgroundCheck(BaseApi):

    async def aadd_background_check(
        self,
        author: BackgroundChecksAuthor,
        application: BackgroundChecksApplication,
        status: str,
        order_number: str,
        packages: BackgroundChecksPackages,
        candidate_id: str,
        tenant_alias: str,
        links: typing.Optional[typing.List[Links]] = None,
        validate: bool = False,
        **kwargs,
    ) -> BackgroundChecksPydantic:
        raw_response = await self.raw.aadd_background_check(
            author=author,
            application=application,
            status=status,
            order_number=order_number,
            packages=packages,
            candidate_id=candidate_id,
            tenant_alias=tenant_alias,
            links=links,
            **kwargs,
        )
        if validate:
            return BackgroundChecksPydantic(**raw_response.body)
        return api_client.construct_model_instance(BackgroundChecksPydantic, raw_response.body)
    
    
    def add_background_check(
        self,
        author: BackgroundChecksAuthor,
        application: BackgroundChecksApplication,
        status: str,
        order_number: str,
        packages: BackgroundChecksPackages,
        candidate_id: str,
        tenant_alias: str,
        links: typing.Optional[typing.List[Links]] = None,
        validate: bool = False,
    ) -> BackgroundChecksPydantic:
        raw_response = self.raw.add_background_check(
            author=author,
            application=application,
            status=status,
            order_number=order_number,
            packages=packages,
            candidate_id=candidate_id,
            tenant_alias=tenant_alias,
            links=links,
        )
        if validate:
            return BackgroundChecksPydantic(**raw_response.body)
        return api_client.construct_model_instance(BackgroundChecksPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        author: BackgroundChecksAuthor,
        application: BackgroundChecksApplication,
        status: str,
        order_number: str,
        packages: BackgroundChecksPackages,
        candidate_id: str,
        tenant_alias: str,
        links: typing.Optional[typing.List[Links]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_background_check_mapped_args(
            author=author,
            application=application,
            status=status,
            order_number=order_number,
            packages=packages,
            candidate_id=candidate_id,
            tenant_alias=tenant_alias,
            links=links,
        )
        return await self._aadd_background_check_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        author: BackgroundChecksAuthor,
        application: BackgroundChecksApplication,
        status: str,
        order_number: str,
        packages: BackgroundChecksPackages,
        candidate_id: str,
        tenant_alias: str,
        links: typing.Optional[typing.List[Links]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_background_check_mapped_args(
            author=author,
            application=application,
            status=status,
            order_number=order_number,
            packages=packages,
            candidate_id=candidate_id,
            tenant_alias=tenant_alias,
            links=links,
        )
        return self._add_background_check_oapg(
            body=args.body,
            path_params=args.path,
        )

