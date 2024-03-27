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

from ukg_python_sdk.model.company_pay_statement_get_pay_summaries_response import CompanyPayStatementGetPaySummariesResponse as CompanyPayStatementGetPaySummariesResponseSchema
from ukg_python_sdk.model.company_pay_statement_filter import CompanyPayStatementFilter as CompanyPayStatementFilterSchema
from ukg_python_sdk.model.company_pay_statement_get_pay_summaries200_response import CompanyPayStatementGetPaySummaries200Response as CompanyPayStatementGetPaySummaries200ResponseSchema

from ukg_python_sdk.type.company_pay_statement_filter import CompanyPayStatementFilter
from ukg_python_sdk.type.company_pay_statement_get_pay_summaries_response import CompanyPayStatementGetPaySummariesResponse
from ukg_python_sdk.type.company_pay_statement_get_pay_summaries200_response import CompanyPayStatementGetPaySummaries200Response

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.company_pay_statement_filter import CompanyPayStatementFilter as CompanyPayStatementFilterPydantic
from ukg_python_sdk.pydantic.company_pay_statement_get_pay_summaries200_response import CompanyPayStatementGetPaySummaries200Response as CompanyPayStatementGetPaySummaries200ResponsePydantic
from ukg_python_sdk.pydantic.company_pay_statement_get_pay_summaries_response import CompanyPayStatementGetPaySummariesResponse as CompanyPayStatementGetPaySummariesResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CompanyPayStatementFilterSchema
SchemaForRequestBodyTextJson = CompanyPayStatementFilterSchema


request_body_company_pay_statement_filter = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
    },
    required=True,
)
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = CompanyPayStatementGetPaySummariesResponseSchema
SchemaFor200ResponseBodyTextJson = CompanyPayStatementGetPaySummaries200ResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CompanyPayStatementGetPaySummariesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CompanyPayStatementGetPaySummariesResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
)


class BaseApi(api_client.Api):

    def _get_pay_summaries_mapped_args(
        self,
        start_date: datetime,
        end_date: datetime,
        company_id: typing.Optional[str] = None,
        pay_group: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if company_id is not None:
            _body["companyId"] = company_id
        if start_date is not None:
            _body["startDate"] = start_date
        if end_date is not None:
            _body["endDate"] = end_date
        if pay_group is not None:
            _body["payGroup"] = pay_group
        if page is not None:
            _body["page"] = page
        if per_page is not None:
            _body["per_Page"] = per_page
        if pages_count is not None:
            _body["pagesCount"] = pages_count
        args.body = _body
        return args

    async def _aget_pay_summaries_oapg(
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
        Get employee(s) pay statement(s) summary for a company or pay group for a given date range.
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
            path_template='/payroll/v1/companies/pay-statements-summary',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_company_pay_statement_filter.serialize(body, content_type)
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


    def _get_pay_summaries_oapg(
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
        Get employee(s) pay statement(s) summary for a company or pay group for a given date range.
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
            path_template='/payroll/v1/companies/pay-statements-summary',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_company_pay_statement_filter.serialize(body, content_type)
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


class GetPaySummariesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_pay_summaries(
        self,
        start_date: datetime,
        end_date: datetime,
        company_id: typing.Optional[str] = None,
        pay_group: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_pay_summaries_mapped_args(
            start_date=start_date,
            end_date=end_date,
            company_id=company_id,
            pay_group=pay_group,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        return await self._aget_pay_summaries_oapg(
            body=args.body,
            **kwargs,
        )
    
    def get_pay_summaries(
        self,
        start_date: datetime,
        end_date: datetime,
        company_id: typing.Optional[str] = None,
        pay_group: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_pay_summaries_mapped_args(
            start_date=start_date,
            end_date=end_date,
            company_id=company_id,
            pay_group=pay_group,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        return self._get_pay_summaries_oapg(
            body=args.body,
        )

class GetPaySummaries(BaseApi):

    async def aget_pay_summaries(
        self,
        start_date: datetime,
        end_date: datetime,
        company_id: typing.Optional[str] = None,
        pay_group: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> CompanyPayStatementGetPaySummariesResponsePydantic:
        raw_response = await self.raw.aget_pay_summaries(
            start_date=start_date,
            end_date=end_date,
            company_id=company_id,
            pay_group=pay_group,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
            **kwargs,
        )
        if validate:
            return RootModel[CompanyPayStatementGetPaySummariesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CompanyPayStatementGetPaySummariesResponsePydantic, raw_response.body)
    
    
    def get_pay_summaries(
        self,
        start_date: datetime,
        end_date: datetime,
        company_id: typing.Optional[str] = None,
        pay_group: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
        validate: bool = False,
    ) -> CompanyPayStatementGetPaySummariesResponsePydantic:
        raw_response = self.raw.get_pay_summaries(
            start_date=start_date,
            end_date=end_date,
            company_id=company_id,
            pay_group=pay_group,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        if validate:
            return RootModel[CompanyPayStatementGetPaySummariesResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CompanyPayStatementGetPaySummariesResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        start_date: datetime,
        end_date: datetime,
        company_id: typing.Optional[str] = None,
        pay_group: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_pay_summaries_mapped_args(
            start_date=start_date,
            end_date=end_date,
            company_id=company_id,
            pay_group=pay_group,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        return await self._aget_pay_summaries_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        start_date: datetime,
        end_date: datetime,
        company_id: typing.Optional[str] = None,
        pay_group: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        pages_count: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_pay_summaries_mapped_args(
            start_date=start_date,
            end_date=end_date,
            company_id=company_id,
            pay_group=pay_group,
            page=page,
            per_page=per_page,
            pages_count=pages_count,
        )
        return self._get_pay_summaries_oapg(
            body=args.body,
        )

