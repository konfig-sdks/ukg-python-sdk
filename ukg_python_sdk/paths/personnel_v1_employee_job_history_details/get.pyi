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

from ukg_python_sdk.model.employee_job_history_detail import EmployeeJobHistoryDetail as EmployeeJobHistoryDetailSchema

from ukg_python_sdk.type.employee_job_history_detail import EmployeeJobHistoryDetail

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.employee_job_history_detail import EmployeeJobHistoryDetail as EmployeeJobHistoryDetailPydantic

# Query params
CompanyIdSchema = schemas.StrSchema
EmployeeIdSchema = schemas.StrSchema
IsOrgChangeSchema = schemas.StrSchema
IsJobChangeSchema = schemas.StrSchema
IsRateChangeSchema = schemas.StrSchema
IsPromotionSchema = schemas.StrSchema
SystemIdSchema = schemas.StrSchema
JobEffectiveDateSchema = schemas.StrSchema
DateTimeCreatedSchema = schemas.StrSchema


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
        'companyId': typing.Union[CompanyIdSchema, str, ],
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
        'isOrgChange': typing.Union[IsOrgChangeSchema, str, ],
        'isJobChange': typing.Union[IsJobChangeSchema, str, ],
        'isRateChange': typing.Union[IsRateChangeSchema, str, ],
        'isPromotion': typing.Union[IsPromotionSchema, str, ],
        'systemId': typing.Union[SystemIdSchema, str, ],
        'jobEffectiveDate': typing.Union[JobEffectiveDateSchema, str, ],
        'dateTimeCreated': typing.Union[DateTimeCreatedSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'per_Page': typing.Union[PerPageSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_company_id = api_client.QueryParameter(
    name="companyId",
    style=api_client.ParameterStyle.FORM,
    schema=CompanyIdSchema,
    explode=True,
)
request_query_employee_id = api_client.QueryParameter(
    name="employeeId",
    style=api_client.ParameterStyle.FORM,
    schema=EmployeeIdSchema,
    explode=True,
)
request_query_is_org_change = api_client.QueryParameter(
    name="isOrgChange",
    style=api_client.ParameterStyle.FORM,
    schema=IsOrgChangeSchema,
    explode=True,
)
request_query_is_job_change = api_client.QueryParameter(
    name="isJobChange",
    style=api_client.ParameterStyle.FORM,
    schema=IsJobChangeSchema,
    explode=True,
)
request_query_is_rate_change = api_client.QueryParameter(
    name="isRateChange",
    style=api_client.ParameterStyle.FORM,
    schema=IsRateChangeSchema,
    explode=True,
)
request_query_is_promotion = api_client.QueryParameter(
    name="isPromotion",
    style=api_client.ParameterStyle.FORM,
    schema=IsPromotionSchema,
    explode=True,
)
request_query_system_id = api_client.QueryParameter(
    name="systemId",
    style=api_client.ParameterStyle.FORM,
    schema=SystemIdSchema,
    explode=True,
)
request_query_job_effective_date = api_client.QueryParameter(
    name="jobEffectiveDate",
    style=api_client.ParameterStyle.FORM,
    schema=JobEffectiveDateSchema,
    explode=True,
)
request_query_date_time_created = api_client.QueryParameter(
    name="dateTimeCreated",
    style=api_client.ParameterStyle.FORM,
    schema=DateTimeCreatedSchema,
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
SchemaFor200ResponseBodyApplicationJson = EmployeeJobHistoryDetailSchema
SchemaFor200ResponseBodyTextJson = EmployeeJobHistoryDetailSchema
SchemaFor200ResponseBodyApplicationProblemjson = EmployeeJobHistoryDetailSchema
SchemaFor200ResponseBodyApplicationXml = EmployeeJobHistoryDetailSchema
SchemaFor200ResponseBodyTextXml = EmployeeJobHistoryDetailSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeeJobHistoryDetail


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeeJobHistoryDetail


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
_all_accept_content_types = (
    'application/json',
    'text/json',
    'application/problem+json',
    'application/xml',
    'text/xml',
)


class BaseApi(api_client.Api):

    def _get_mapped_args(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        is_org_change: typing.Optional[str] = None,
        is_job_change: typing.Optional[str] = None,
        is_rate_change: typing.Optional[str] = None,
        is_promotion: typing.Optional[str] = None,
        system_id: typing.Optional[str] = None,
        job_effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if company_id is not None:
            _query_params["companyId"] = company_id
        if employee_id is not None:
            _query_params["employeeId"] = employee_id
        if is_org_change is not None:
            _query_params["isOrgChange"] = is_org_change
        if is_job_change is not None:
            _query_params["isJobChange"] = is_job_change
        if is_rate_change is not None:
            _query_params["isRateChange"] = is_rate_change
        if is_promotion is not None:
            _query_params["isPromotion"] = is_promotion
        if system_id is not None:
            _query_params["systemId"] = system_id
        if job_effective_date is not None:
            _query_params["jobEffectiveDate"] = job_effective_date
        if date_time_created is not None:
            _query_params["dateTimeCreated"] = date_time_created
        if page is not None:
            _query_params["page"] = page
        if per_page is not None:
            _query_params["per_Page"] = per_page
        args.query = _query_params
        return args

    async def _aget_oapg(
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
        Get all employee job history details
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_company_id,
            request_query_employee_id,
            request_query_is_org_change,
            request_query_is_job_change,
            request_query_is_rate_change,
            request_query_is_promotion,
            request_query_system_id,
            request_query_job_effective_date,
            request_query_date_time_created,
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
            path_template='/personnel/v1/employee-job-history-details',
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


    def _get_oapg(
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
        Get all employee job history details
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_company_id,
            request_query_employee_id,
            request_query_is_org_change,
            request_query_is_job_change,
            request_query_is_rate_change,
            request_query_is_promotion,
            request_query_system_id,
            request_query_job_effective_date,
            request_query_date_time_created,
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
            path_template='/personnel/v1/employee-job-history-details',
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


class GetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        is_org_change: typing.Optional[str] = None,
        is_job_change: typing.Optional[str] = None,
        is_rate_change: typing.Optional[str] = None,
        is_promotion: typing.Optional[str] = None,
        system_id: typing.Optional[str] = None,
        job_effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            is_org_change=is_org_change,
            is_job_change=is_job_change,
            is_rate_change=is_rate_change,
            is_promotion=is_promotion,
            system_id=system_id,
            job_effective_date=job_effective_date,
            date_time_created=date_time_created,
            page=page,
            per_page=per_page,
        )
        return await self._aget_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        is_org_change: typing.Optional[str] = None,
        is_job_change: typing.Optional[str] = None,
        is_rate_change: typing.Optional[str] = None,
        is_promotion: typing.Optional[str] = None,
        system_id: typing.Optional[str] = None,
        job_effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            is_org_change=is_org_change,
            is_job_change=is_job_change,
            is_rate_change=is_rate_change,
            is_promotion=is_promotion,
            system_id=system_id,
            job_effective_date=job_effective_date,
            date_time_created=date_time_created,
            page=page,
            per_page=per_page,
        )
        return self._get_oapg(
            query_params=args.query,
        )

class Get(BaseApi):

    async def aget(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        is_org_change: typing.Optional[str] = None,
        is_job_change: typing.Optional[str] = None,
        is_rate_change: typing.Optional[str] = None,
        is_promotion: typing.Optional[str] = None,
        system_id: typing.Optional[str] = None,
        job_effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeeJobHistoryDetailPydantic:
        raw_response = await self.raw.aget(
            company_id=company_id,
            employee_id=employee_id,
            is_org_change=is_org_change,
            is_job_change=is_job_change,
            is_rate_change=is_rate_change,
            is_promotion=is_promotion,
            system_id=system_id,
            job_effective_date=job_effective_date,
            date_time_created=date_time_created,
            page=page,
            per_page=per_page,
            **kwargs,
        )
        if validate:
            return EmployeeJobHistoryDetailPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeJobHistoryDetailPydantic, raw_response.body)
    
    
    def get(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        is_org_change: typing.Optional[str] = None,
        is_job_change: typing.Optional[str] = None,
        is_rate_change: typing.Optional[str] = None,
        is_promotion: typing.Optional[str] = None,
        system_id: typing.Optional[str] = None,
        job_effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> EmployeeJobHistoryDetailPydantic:
        raw_response = self.raw.get(
            company_id=company_id,
            employee_id=employee_id,
            is_org_change=is_org_change,
            is_job_change=is_job_change,
            is_rate_change=is_rate_change,
            is_promotion=is_promotion,
            system_id=system_id,
            job_effective_date=job_effective_date,
            date_time_created=date_time_created,
            page=page,
            per_page=per_page,
        )
        if validate:
            return EmployeeJobHistoryDetailPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeJobHistoryDetailPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        is_org_change: typing.Optional[str] = None,
        is_job_change: typing.Optional[str] = None,
        is_rate_change: typing.Optional[str] = None,
        is_promotion: typing.Optional[str] = None,
        system_id: typing.Optional[str] = None,
        job_effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            is_org_change=is_org_change,
            is_job_change=is_job_change,
            is_rate_change=is_rate_change,
            is_promotion=is_promotion,
            system_id=system_id,
            job_effective_date=job_effective_date,
            date_time_created=date_time_created,
            page=page,
            per_page=per_page,
        )
        return await self._aget_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        is_org_change: typing.Optional[str] = None,
        is_job_change: typing.Optional[str] = None,
        is_rate_change: typing.Optional[str] = None,
        is_promotion: typing.Optional[str] = None,
        system_id: typing.Optional[str] = None,
        job_effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            is_org_change=is_org_change,
            is_job_change=is_job_change,
            is_rate_change=is_rate_change,
            is_promotion=is_promotion,
            system_id=system_id,
            job_effective_date=job_effective_date,
            date_time_created=date_time_created,
            page=page,
            per_page=per_page,
        )
        return self._get_oapg(
            query_params=args.query,
        )

