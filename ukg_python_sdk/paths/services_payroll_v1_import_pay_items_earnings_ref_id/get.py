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

from ukg_python_sdk.model.earning_status_response import EarningStatusResponse as EarningStatusResponseSchema

from ukg_python_sdk.type.earning_status_response import EarningStatusResponse

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.earning_status_response import EarningStatusResponse as EarningStatusResponsePydantic

from . import path

# Header params
XCorrelationIdSchema = schemas.UUIDSchema
USClientIdSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'X-Correlation-Id': typing.Union[XCorrelationIdSchema, str, uuid.UUID, ],
        'US-Client-Id': typing.Union[USClientIdSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_correlation_id = api_client.HeaderParameter(
    name="X-Correlation-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XCorrelationIdSchema,
    required=True,
)
request_header_us_client_id = api_client.HeaderParameter(
    name="US-Client-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=USClientIdSchema,
    required=True,
)
# Path params
RefIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'refId': typing.Union[RefIdSchema, str, ],
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


request_path_ref_id = api_client.PathParameter(
    name="refId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RefIdSchema,
    required=True,
)
_auth = [
    'basicAuth',
]
SchemaFor200ResponseBodyApplicationJson = EarningStatusResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EarningStatusResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EarningStatusResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '200': _response_for_200,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_status_details_mapped_args(
        self,
        x_correlation_id: str,
        us_client_id: str,
        ref_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        if x_correlation_id is not None:
            _header_params["X-Correlation-Id"] = x_correlation_id
        if us_client_id is not None:
            _header_params["US-Client-Id"] = us_client_id
        if ref_id is not None:
            _path_params["refId"] = ref_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aget_status_details_oapg(
        self,
            header_params: typing.Optional[dict] = {},
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
        Get status details for specified earning
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_ref_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_correlation_id,
            request_header_us_client_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/services/payroll/v1/import-pay-items/earnings/{refId}',
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


    def _get_status_details_oapg(
        self,
            header_params: typing.Optional[dict] = {},
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
        Get status details for specified earning
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_ref_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_correlation_id,
            request_header_us_client_id,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/services/payroll/v1/import-pay-items/earnings/{refId}',
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


class GetStatusDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_status_details(
        self,
        x_correlation_id: str,
        us_client_id: str,
        ref_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_status_details_mapped_args(
            x_correlation_id=x_correlation_id,
            us_client_id=us_client_id,
            ref_id=ref_id,
        )
        return await self._aget_status_details_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get_status_details(
        self,
        x_correlation_id: str,
        us_client_id: str,
        ref_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_status_details_mapped_args(
            x_correlation_id=x_correlation_id,
            us_client_id=us_client_id,
            ref_id=ref_id,
        )
        return self._get_status_details_oapg(
            header_params=args.header,
            path_params=args.path,
        )

class GetStatusDetails(BaseApi):

    async def aget_status_details(
        self,
        x_correlation_id: str,
        us_client_id: str,
        ref_id: str,
        validate: bool = False,
        **kwargs,
    ) -> EarningStatusResponsePydantic:
        raw_response = await self.raw.aget_status_details(
            x_correlation_id=x_correlation_id,
            us_client_id=us_client_id,
            ref_id=ref_id,
            **kwargs,
        )
        if validate:
            return EarningStatusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EarningStatusResponsePydantic, raw_response.body)
    
    
    def get_status_details(
        self,
        x_correlation_id: str,
        us_client_id: str,
        ref_id: str,
        validate: bool = False,
    ) -> EarningStatusResponsePydantic:
        raw_response = self.raw.get_status_details(
            x_correlation_id=x_correlation_id,
            us_client_id=us_client_id,
            ref_id=ref_id,
        )
        if validate:
            return EarningStatusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EarningStatusResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        x_correlation_id: str,
        us_client_id: str,
        ref_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_status_details_mapped_args(
            x_correlation_id=x_correlation_id,
            us_client_id=us_client_id,
            ref_id=ref_id,
        )
        return await self._aget_status_details_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        x_correlation_id: str,
        us_client_id: str,
        ref_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_status_details_mapped_args(
            x_correlation_id=x_correlation_id,
            us_client_id=us_client_id,
            ref_id=ref_id,
        )
        return self._get_status_details_oapg(
            header_params=args.header,
            path_params=args.path,
        )

