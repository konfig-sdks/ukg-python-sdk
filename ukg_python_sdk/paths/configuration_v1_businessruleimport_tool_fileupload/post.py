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

from ukg_python_sdk.model.business_rule_import_request import BusinessRuleImportRequest as BusinessRuleImportRequestSchema
from ukg_python_sdk.model.business_rule_file_upload import BusinessRuleFileUpload as BusinessRuleFileUploadSchema
from ukg_python_sdk.model.business_rule_import_tool_business_rule_import_file_upload500_response import BusinessRuleImportToolBusinessRuleImportFileUpload500Response as BusinessRuleImportToolBusinessRuleImportFileUpload500ResponseSchema

from ukg_python_sdk.type.business_rule_import_request import BusinessRuleImportRequest
from ukg_python_sdk.type.business_rule_import_tool_business_rule_import_file_upload500_response import BusinessRuleImportToolBusinessRuleImportFileUpload500Response
from ukg_python_sdk.type.business_rule_file_upload import BusinessRuleFileUpload

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.business_rule_import_tool_business_rule_import_file_upload500_response import BusinessRuleImportToolBusinessRuleImportFileUpload500Response as BusinessRuleImportToolBusinessRuleImportFileUpload500ResponsePydantic
from ukg_python_sdk.pydantic.business_rule_file_upload import BusinessRuleFileUpload as BusinessRuleFileUploadPydantic
from ukg_python_sdk.pydantic.business_rule_import_request import BusinessRuleImportRequest as BusinessRuleImportRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = BusinessRuleImportRequestSchema
SchemaForRequestBodyTextJson = BusinessRuleImportRequestSchema
SchemaForRequestBodyApplicationProblemjson = BusinessRuleImportRequestSchema
SchemaForRequestBodyApplicationXml = BusinessRuleImportRequestSchema
SchemaForRequestBodyTextXml = BusinessRuleImportRequestSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = BusinessRuleImportRequestSchema


request_body_business_rule_import_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationProblemjson),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaForRequestBodyTextXml),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = schemas.DictSchema
SchemaFor200ResponseBodyTextJson = schemas.DictSchema
SchemaFor200ResponseBodyApplicationProblemjson = schemas.DictSchema
SchemaFor200ResponseBodyApplicationXml = schemas.DictSchema
SchemaFor200ResponseBodyTextXml = schemas.DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


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
SchemaFor201ResponseBodyApplicationJson = BusinessRuleFileUploadSchema
SchemaFor201ResponseBodyTextJson = BusinessRuleFileUploadSchema
SchemaFor201ResponseBodyApplicationProblemjson = BusinessRuleFileUploadSchema
SchemaFor201ResponseBodyApplicationXml = BusinessRuleFileUploadSchema
SchemaFor201ResponseBodyTextXml = BusinessRuleFileUploadSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: BusinessRuleFileUpload


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: BusinessRuleFileUpload


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyTextJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationProblemjson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaFor201ResponseBodyTextXml),
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
SchemaFor500ResponseBodyApplicationJson = BusinessRuleImportToolBusinessRuleImportFileUpload500ResponseSchema
SchemaFor500ResponseBodyTextJson = BusinessRuleImportToolBusinessRuleImportFileUpload500ResponseSchema
SchemaFor500ResponseBodyApplicationProblemjson = BusinessRuleImportToolBusinessRuleImportFileUpload500ResponseSchema
SchemaFor500ResponseBodyApplicationXml = BusinessRuleImportToolBusinessRuleImportFileUpload500ResponseSchema
SchemaFor500ResponseBodyTextXml = BusinessRuleImportToolBusinessRuleImportFileUpload500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: BusinessRuleImportToolBusinessRuleImportFileUpload500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: BusinessRuleImportToolBusinessRuleImportFileUpload500Response


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
    '201': _response_for_201,
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

    def _business_rule_import_file_upload_mapped_args(
        self,
        transaction: typing.Optional[str] = None,
        unique_file_name: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if transaction is not None:
            _body["transaction"] = transaction
        if unique_file_name is not None:
            _body["uniqueFileName"] = unique_file_name
        args.body = _body
        return args

    async def _abusiness_rule_import_file_upload_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Takes an XML transaction and feeds it into the Business Rule Import Tool
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/configuration/v1/businessruleimport-tool/fileupload',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_business_rule_import_request.serialize(body, content_type)
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


    def _business_rule_import_file_upload_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Takes an XML transaction and feeds it into the Business Rule Import Tool
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/configuration/v1/businessruleimport-tool/fileupload',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_business_rule_import_request.serialize(body, content_type)
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


class BusinessRuleImportFileUploadRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def abusiness_rule_import_file_upload(
        self,
        transaction: typing.Optional[str] = None,
        unique_file_name: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._business_rule_import_file_upload_mapped_args(
            transaction=transaction,
            unique_file_name=unique_file_name,
        )
        return await self._abusiness_rule_import_file_upload_oapg(
            body=args.body,
            **kwargs,
        )
    
    def business_rule_import_file_upload(
        self,
        transaction: typing.Optional[str] = None,
        unique_file_name: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._business_rule_import_file_upload_mapped_args(
            transaction=transaction,
            unique_file_name=unique_file_name,
        )
        return self._business_rule_import_file_upload_oapg(
            body=args.body,
        )

class BusinessRuleImportFileUpload(BaseApi):

    async def abusiness_rule_import_file_upload(
        self,
        transaction: typing.Optional[str] = None,
        unique_file_name: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.abusiness_rule_import_file_upload(
            transaction=transaction,
            unique_file_name=unique_file_name,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def business_rule_import_file_upload(
        self,
        transaction: typing.Optional[str] = None,
        unique_file_name: typing.Optional[str] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.business_rule_import_file_upload(
            transaction=transaction,
            unique_file_name=unique_file_name,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        transaction: typing.Optional[str] = None,
        unique_file_name: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._business_rule_import_file_upload_mapped_args(
            transaction=transaction,
            unique_file_name=unique_file_name,
        )
        return await self._abusiness_rule_import_file_upload_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        transaction: typing.Optional[str] = None,
        unique_file_name: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._business_rule_import_file_upload_mapped_args(
            transaction=transaction,
            unique_file_name=unique_file_name,
        )
        return self._business_rule_import_file_upload_oapg(
            body=args.body,
        )

