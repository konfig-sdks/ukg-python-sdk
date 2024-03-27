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

from ukg_python_sdk.model.result_dto_clock_transaction_dto import ResultDtoClockTransactionDto as ResultDtoClockTransactionDtoSchema

from ukg_python_sdk.type.result_dto_clock_transaction_dto import ResultDtoClockTransactionDto

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.result_dto_clock_transaction_dto import ResultDtoClockTransactionDto as ResultDtoClockTransactionDtoPydantic

from . import path

# Query params
EmpNameSchema = schemas.StrSchema
EmpIdSchema = schemas.Int64Schema
DateSchema = schemas.DateTimeSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'date': typing.Union[DateSchema, str, datetime, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'emp_name': typing.Union[EmpNameSchema, str, ],
        'emp_id': typing.Union[EmpIdSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_emp_name = api_client.QueryParameter(
    name="emp_name",
    style=api_client.ParameterStyle.FORM,
    schema=EmpNameSchema,
    explode=True,
)
request_query_emp_id = api_client.QueryParameter(
    name="emp_id",
    style=api_client.ParameterStyle.FORM,
    schema=EmpIdSchema,
    explode=True,
)
request_query_date = api_client.QueryParameter(
    name="date",
    style=api_client.ParameterStyle.FORM,
    schema=DateSchema,
    required=True,
    explode=True,
)
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = ResultDtoClockTransactionDtoSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ResultDtoClockTransactionDto


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ResultDtoClockTransactionDto


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '429': _response_for_429,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_processed_transactions_mapped_args(
        self,
        date: datetime,
        emp_name: typing.Optional[str] = None,
        emp_id: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if emp_name is not None:
            _query_params["emp_name"] = emp_name
        if emp_id is not None:
            _query_params["emp_id"] = emp_id
        if date is not None:
            _query_params["date"] = date
        args.query = _query_params
        return args

    async def _aget_processed_transactions_oapg(
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
        Get processed clock transactions.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_emp_name,
            request_query_emp_id,
            request_query_date,
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
            path_template='/time/clock_transactions',
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


    def _get_processed_transactions_oapg(
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
        Get processed clock transactions.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_emp_name,
            request_query_emp_id,
            request_query_date,
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
            path_template='/time/clock_transactions',
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


class GetProcessedTransactionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_processed_transactions(
        self,
        date: datetime,
        emp_name: typing.Optional[str] = None,
        emp_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_processed_transactions_mapped_args(
            date=date,
            emp_name=emp_name,
            emp_id=emp_id,
        )
        return await self._aget_processed_transactions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_processed_transactions(
        self,
        date: datetime,
        emp_name: typing.Optional[str] = None,
        emp_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_processed_transactions_mapped_args(
            date=date,
            emp_name=emp_name,
            emp_id=emp_id,
        )
        return self._get_processed_transactions_oapg(
            query_params=args.query,
        )

class GetProcessedTransactions(BaseApi):

    async def aget_processed_transactions(
        self,
        date: datetime,
        emp_name: typing.Optional[str] = None,
        emp_id: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ResultDtoClockTransactionDtoPydantic:
        raw_response = await self.raw.aget_processed_transactions(
            date=date,
            emp_name=emp_name,
            emp_id=emp_id,
            **kwargs,
        )
        if validate:
            return ResultDtoClockTransactionDtoPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultDtoClockTransactionDtoPydantic, raw_response.body)
    
    
    def get_processed_transactions(
        self,
        date: datetime,
        emp_name: typing.Optional[str] = None,
        emp_id: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ResultDtoClockTransactionDtoPydantic:
        raw_response = self.raw.get_processed_transactions(
            date=date,
            emp_name=emp_name,
            emp_id=emp_id,
        )
        if validate:
            return ResultDtoClockTransactionDtoPydantic(**raw_response.body)
        return api_client.construct_model_instance(ResultDtoClockTransactionDtoPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        date: datetime,
        emp_name: typing.Optional[str] = None,
        emp_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_processed_transactions_mapped_args(
            date=date,
            emp_name=emp_name,
            emp_id=emp_id,
        )
        return await self._aget_processed_transactions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        date: datetime,
        emp_name: typing.Optional[str] = None,
        emp_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_processed_transactions_mapped_args(
            date=date,
            emp_name=emp_name,
            emp_id=emp_id,
        )
        return self._get_processed_transactions_oapg(
            query_params=args.query,
        )

