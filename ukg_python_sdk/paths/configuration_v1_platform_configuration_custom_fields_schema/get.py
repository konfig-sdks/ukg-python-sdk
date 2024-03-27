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

from ukg_python_sdk.model.ultimate_software_foundation_services_api_ulti_pro_configuration_platform_configuration_models_pc_field_schema import UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchema as UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaSchema

from ukg_python_sdk.type.ultimate_software_foundation_services_api_ulti_pro_configuration_platform_configuration_models_pc_field_schema import UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchema

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.ultimate_software_foundation_services_api_ulti_pro_configuration_platform_configuration_models_pc_field_schema import UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchema as UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaPydantic

from . import path

# Query params
ClassNameSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'className': typing.Union[ClassNameSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_class_name = api_client.QueryParameter(
    name="className",
    style=api_client.ParameterStyle.FORM,
    schema=ClassNameSchema,
    explode=True,
)
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaSchema
SchemaFor200ResponseBodyTextJson = UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaSchema
SchemaFor200ResponseBodyApplicationProblemjson = UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaSchema
SchemaFor200ResponseBodyApplicationXml = UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaSchema
SchemaFor200ResponseBodyTextXml = UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchema


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchema


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

    def _get_fields_schema_mapped_args(
        self,
        class_name: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if class_name is not None:
            _query_params["className"] = class_name
        args.query = _query_params
        return args

    async def _aget_fields_schema_oapg(
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
        Gets Platform Configuration standard classes custom fields schema
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_class_name,
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
            path_template='/configuration/v1/platform-configuration/custom-fields-schema',
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


    def _get_fields_schema_oapg(
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
        Gets Platform Configuration standard classes custom fields schema
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_class_name,
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
            path_template='/configuration/v1/platform-configuration/custom-fields-schema',
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


class GetFieldsSchemaRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_fields_schema(
        self,
        class_name: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_fields_schema_mapped_args(
            class_name=class_name,
        )
        return await self._aget_fields_schema_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_fields_schema(
        self,
        class_name: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_fields_schema_mapped_args(
            class_name=class_name,
        )
        return self._get_fields_schema_oapg(
            query_params=args.query,
        )

class GetFieldsSchema(BaseApi):

    async def aget_fields_schema(
        self,
        class_name: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaPydantic:
        raw_response = await self.raw.aget_fields_schema(
            class_name=class_name,
            **kwargs,
        )
        if validate:
            return UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaPydantic(**raw_response.body)
        return api_client.construct_model_instance(UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaPydantic, raw_response.body)
    
    
    def get_fields_schema(
        self,
        class_name: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaPydantic:
        raw_response = self.raw.get_fields_schema(
            class_name=class_name,
        )
        if validate:
            return UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaPydantic(**raw_response.body)
        return api_client.construct_model_instance(UltimateSoftwareFoundationServicesApiUltiProConfigurationPlatformConfigurationModelsPcFieldSchemaPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        class_name: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_fields_schema_mapped_args(
            class_name=class_name,
        )
        return await self._aget_fields_schema_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        class_name: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_fields_schema_mapped_args(
            class_name=class_name,
        )
        return self._get_fields_schema_oapg(
            query_params=args.query,
        )

