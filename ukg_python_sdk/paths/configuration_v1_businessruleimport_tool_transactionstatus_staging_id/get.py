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

from ukg_python_sdk.model.business_rule_import_file_staging_status import BusinessRuleImportFileStagingStatus as BusinessRuleImportFileStagingStatusSchema
from ukg_python_sdk.model.business_rule_import_tool_get_staging_status500_response import BusinessRuleImportToolGetStagingStatus500Response as BusinessRuleImportToolGetStagingStatus500ResponseSchema
from ukg_python_sdk.model.business_rule_import_tool_get_staging_status_response import BusinessRuleImportToolGetStagingStatusResponse as BusinessRuleImportToolGetStagingStatusResponseSchema

from ukg_python_sdk.type.business_rule_import_tool_get_staging_status_response import BusinessRuleImportToolGetStagingStatusResponse
from ukg_python_sdk.type.business_rule_import_file_staging_status import BusinessRuleImportFileStagingStatus
from ukg_python_sdk.type.business_rule_import_tool_get_staging_status500_response import BusinessRuleImportToolGetStagingStatus500Response

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.business_rule_import_tool_get_staging_status_response import BusinessRuleImportToolGetStagingStatusResponse as BusinessRuleImportToolGetStagingStatusResponsePydantic
from ukg_python_sdk.pydantic.business_rule_import_tool_get_staging_status500_response import BusinessRuleImportToolGetStagingStatus500Response as BusinessRuleImportToolGetStagingStatus500ResponsePydantic
from ukg_python_sdk.pydantic.business_rule_import_file_staging_status import BusinessRuleImportFileStagingStatus as BusinessRuleImportFileStagingStatusPydantic

from . import path

# Path params
StagingIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'stagingId': typing.Union[StagingIdSchema, str, ],
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


request_path_staging_id = api_client.PathParameter(
    name="stagingId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=StagingIdSchema,
    required=True,
)
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = BusinessRuleImportFileStagingStatusSchema
SchemaFor200ResponseBodyTextJson = BusinessRuleImportFileStagingStatusSchema
SchemaFor200ResponseBodyApplicationProblemjson = BusinessRuleImportFileStagingStatusSchema
SchemaFor200ResponseBodyApplicationXml = BusinessRuleImportFileStagingStatusSchema
SchemaFor200ResponseBodyTextXml = BusinessRuleImportFileStagingStatusSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BusinessRuleImportFileStagingStatus


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BusinessRuleImportFileStagingStatus


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
SchemaFor500ResponseBodyApplicationJson = BusinessRuleImportToolGetStagingStatusResponseSchema
SchemaFor500ResponseBodyTextJson = BusinessRuleImportToolGetStagingStatus500ResponseSchema
SchemaFor500ResponseBodyApplicationProblemjson = BusinessRuleImportToolGetStagingStatus500ResponseSchema
SchemaFor500ResponseBodyApplicationXml = BusinessRuleImportToolGetStagingStatus500ResponseSchema
SchemaFor500ResponseBodyTextXml = BusinessRuleImportToolGetStagingStatus500ResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: BusinessRuleImportToolGetStagingStatusResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: BusinessRuleImportToolGetStagingStatusResponse


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

    def _get_staging_status_mapped_args(
        self,
        staging_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if staging_id is not None:
            _path_params["stagingId"] = staging_id
        args.path = _path_params
        return args

    async def _aget_staging_status_oapg(
        self,
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
        Retrieves the status of an Business Rule Import Tool transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_staging_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/configuration/v1/businessruleimport-tool/transactionstatus/{stagingId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_staging_status_oapg(
        self,
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
        Retrieves the status of an Business Rule Import Tool transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_staging_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/configuration/v1/businessruleimport-tool/transactionstatus/{stagingId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetStagingStatusRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_staging_status(
        self,
        staging_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_staging_status_mapped_args(
            staging_id=staging_id,
        )
        return await self._aget_staging_status_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_staging_status(
        self,
        staging_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_staging_status_mapped_args(
            staging_id=staging_id,
        )
        return self._get_staging_status_oapg(
            path_params=args.path,
        )

class GetStagingStatus(BaseApi):

    async def aget_staging_status(
        self,
        staging_id: str,
        validate: bool = False,
        **kwargs,
    ) -> BusinessRuleImportFileStagingStatusPydantic:
        raw_response = await self.raw.aget_staging_status(
            staging_id=staging_id,
            **kwargs,
        )
        if validate:
            return BusinessRuleImportFileStagingStatusPydantic(**raw_response.body)
        return api_client.construct_model_instance(BusinessRuleImportFileStagingStatusPydantic, raw_response.body)
    
    
    def get_staging_status(
        self,
        staging_id: str,
        validate: bool = False,
    ) -> BusinessRuleImportFileStagingStatusPydantic:
        raw_response = self.raw.get_staging_status(
            staging_id=staging_id,
        )
        if validate:
            return BusinessRuleImportFileStagingStatusPydantic(**raw_response.body)
        return api_client.construct_model_instance(BusinessRuleImportFileStagingStatusPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        staging_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_staging_status_mapped_args(
            staging_id=staging_id,
        )
        return await self._aget_staging_status_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        staging_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_staging_status_mapped_args(
            staging_id=staging_id,
        )
        return self._get_staging_status_oapg(
            path_params=args.path,
        )

