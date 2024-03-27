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

from ukg_python_sdk.model.employee_pay_statement_get_by_date_range200_response import EmployeePayStatementGetByDateRange200Response as EmployeePayStatementGetByDateRange200ResponseSchema
from ukg_python_sdk.model.employee_identifier import EmployeeIdentifier as EmployeeIdentifierSchema
from ukg_python_sdk.model.employee_pay_statement_get_by_date_range_response import EmployeePayStatementGetByDateRangeResponse as EmployeePayStatementGetByDateRangeResponseSchema
from ukg_python_sdk.model.employee_pay_statement_range_filter import EmployeePayStatementRangeFilter as EmployeePayStatementRangeFilterSchema

from ukg_python_sdk.type.employee_pay_statement_get_by_date_range200_response import EmployeePayStatementGetByDateRange200Response
from ukg_python_sdk.type.employee_identifier import EmployeeIdentifier
from ukg_python_sdk.type.employee_pay_statement_range_filter import EmployeePayStatementRangeFilter
from ukg_python_sdk.type.employee_pay_statement_get_by_date_range_response import EmployeePayStatementGetByDateRangeResponse

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.employee_identifier import EmployeeIdentifier as EmployeeIdentifierPydantic
from ukg_python_sdk.pydantic.employee_pay_statement_get_by_date_range200_response import EmployeePayStatementGetByDateRange200Response as EmployeePayStatementGetByDateRange200ResponsePydantic
from ukg_python_sdk.pydantic.employee_pay_statement_get_by_date_range_response import EmployeePayStatementGetByDateRangeResponse as EmployeePayStatementGetByDateRangeResponsePydantic
from ukg_python_sdk.pydantic.employee_pay_statement_range_filter import EmployeePayStatementRangeFilter as EmployeePayStatementRangeFilterPydantic

# body param
SchemaForRequestBodyApplicationJson = EmployeePayStatementRangeFilterSchema
SchemaForRequestBodyTextJson = EmployeePayStatementRangeFilterSchema


request_body_employee_pay_statement_range_filter = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = EmployeePayStatementGetByDateRangeResponseSchema
SchemaFor200ResponseBodyTextJson = EmployeePayStatementGetByDateRange200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeePayStatementGetByDateRangeResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeePayStatementGetByDateRangeResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
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
_all_accept_content_types = (
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):

    def _get_by_date_range_mapped_args(
        self,
        employee_identifier: typing.Optional[EmployeeIdentifier] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if employee_identifier is not None:
            _body["employeeIdentifier"] = employee_identifier
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        if page is not None:
            _body["page"] = page
        if per_page is not None:
            _body["per_Page"] = per_page
        if pages_count is not None:
            _body["pagesCount"] = pages_count
        args.body = _body
        return args

    async def _aget_by_date_range_oapg(
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
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get employee pay statement(s) based on the passed employee identifier for a given date range.
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
            path_template='/payroll/v1/employees/pay-statements',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_employee_pay_statement_range_filter.serialize(body, content_type)
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


    def _get_by_date_range_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get employee pay statement(s) based on the passed employee identifier for a given date range.
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
            path_template='/payroll/v1/employees/pay-statements',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_employee_pay_statement_range_filter.serialize(body, content_type)
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


class GetByDateRangeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_by_date_range(
        self,
        employee_identifier: typing.Optional[EmployeeIdentifier] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_date_range_mapped_args(
            employee_identifier=employee_identifier,
            start_date=start_date,
            end_date=end_date,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        return await self._aget_by_date_range_oapg(
            body=args.body,
            **kwargs,
        )
    
    def get_by_date_range(
        self,
        employee_identifier: typing.Optional[EmployeeIdentifier] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_date_range_mapped_args(
            employee_identifier=employee_identifier,
            start_date=start_date,
            end_date=end_date,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        return self._get_by_date_range_oapg(
            body=args.body,
        )

class GetByDateRange(BaseApi):

    async def aget_by_date_range(
        self,
        employee_identifier: typing.Optional[EmployeeIdentifier] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeePayStatementGetByDateRangeResponsePydantic:
        raw_response = await self.raw.aget_by_date_range(
            employee_identifier=employee_identifier,
            start_date=start_date,
            end_date=end_date,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
            **kwargs,
        )
        if validate:
            return RootModel[EmployeePayStatementGetByDateRangeResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(EmployeePayStatementGetByDateRangeResponsePydantic, raw_response.body)
    
    
    def get_by_date_range(
        self,
        employee_identifier: typing.Optional[EmployeeIdentifier] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
        validate: bool = False,
    ) -> EmployeePayStatementGetByDateRangeResponsePydantic:
        raw_response = self.raw.get_by_date_range(
            employee_identifier=employee_identifier,
            start_date=start_date,
            end_date=end_date,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        if validate:
            return RootModel[EmployeePayStatementGetByDateRangeResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(EmployeePayStatementGetByDateRangeResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        employee_identifier: typing.Optional[EmployeeIdentifier] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_date_range_mapped_args(
            employee_identifier=employee_identifier,
            start_date=start_date,
            end_date=end_date,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        return await self._aget_by_date_range_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        employee_identifier: typing.Optional[EmployeeIdentifier] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[datetime] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_date_range_mapped_args(
            employee_identifier=employee_identifier,
            start_date=start_date,
            end_date=end_date,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        return self._get_by_date_range_oapg(
            body=args.body,
        )

