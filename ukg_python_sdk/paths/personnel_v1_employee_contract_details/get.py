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

from ukg_python_sdk.model.employee_contract import EmployeeContract as EmployeeContractSchema

from ukg_python_sdk.type.employee_contract import EmployeeContract

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.employee_contract import EmployeeContract as EmployeeContractPydantic

from . import path

# Query params
CompanyIdSchema = schemas.StrSchema
EmployeeIdSchema = schemas.StrSchema
ContractNumberSchema = schemas.StrSchema
ContractTypeCodeSchema = schemas.StrSchema
EffectiveDateSchema = schemas.StrSchema
DateTimeCreatedSchema = schemas.StrSchema
RowLastChangedSchema = schemas.StrSchema


class PageSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 2147483647
        inclusive_minimum = 1


class PerPageSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 2147483647
        inclusive_minimum = 1
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
        'contractNumber': typing.Union[ContractNumberSchema, str, ],
        'contractTypeCode': typing.Union[ContractTypeCodeSchema, str, ],
        'effectiveDate': typing.Union[EffectiveDateSchema, str, ],
        'dateTimeCreated': typing.Union[DateTimeCreatedSchema, str, ],
        'rowLastChanged': typing.Union[RowLastChangedSchema, str, ],
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
request_query_contract_number = api_client.QueryParameter(
    name="contractNumber",
    style=api_client.ParameterStyle.FORM,
    schema=ContractNumberSchema,
    explode=True,
)
request_query_contract_type_code = api_client.QueryParameter(
    name="contractTypeCode",
    style=api_client.ParameterStyle.FORM,
    schema=ContractTypeCodeSchema,
    explode=True,
)
request_query_effective_date = api_client.QueryParameter(
    name="effectiveDate",
    style=api_client.ParameterStyle.FORM,
    schema=EffectiveDateSchema,
    explode=True,
)
request_query_date_time_created = api_client.QueryParameter(
    name="dateTimeCreated",
    style=api_client.ParameterStyle.FORM,
    schema=DateTimeCreatedSchema,
    explode=True,
)
request_query_row_last_changed = api_client.QueryParameter(
    name="rowLastChanged",
    style=api_client.ParameterStyle.FORM,
    schema=RowLastChangedSchema,
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
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = EmployeeContractSchema
SchemaFor200ResponseBodyTextJson = EmployeeContractSchema
SchemaFor200ResponseBodyApplicationProblemjson = EmployeeContractSchema
SchemaFor200ResponseBodyApplicationXml = EmployeeContractSchema
SchemaFor200ResponseBodyTextXml = EmployeeContractSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeeContract


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeeContract


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

    def _get_mapped_args(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        contract_number: typing.Optional[str] = None,
        contract_type_code: typing.Optional[str] = None,
        effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        row_last_changed: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if company_id is not None:
            _query_params["companyId"] = company_id
        if employee_id is not None:
            _query_params["employeeId"] = employee_id
        if contract_number is not None:
            _query_params["contractNumber"] = contract_number
        if contract_type_code is not None:
            _query_params["contractTypeCode"] = contract_type_code
        if effective_date is not None:
            _query_params["effectiveDate"] = effective_date
        if date_time_created is not None:
            _query_params["dateTimeCreated"] = date_time_created
        if row_last_changed is not None:
            _query_params["rowLastChanged"] = row_last_changed
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
        Get all employment contract details
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
            request_query_contract_number,
            request_query_contract_type_code,
            request_query_effective_date,
            request_query_date_time_created,
            request_query_row_last_changed,
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
            path_template='/personnel/v1/employee-contract-details',
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
        Get all employment contract details
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
            request_query_contract_number,
            request_query_contract_type_code,
            request_query_effective_date,
            request_query_date_time_created,
            request_query_row_last_changed,
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
            path_template='/personnel/v1/employee-contract-details',
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
        contract_number: typing.Optional[str] = None,
        contract_type_code: typing.Optional[str] = None,
        effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        row_last_changed: typing.Optional[str] = None,
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
            contract_number=contract_number,
            contract_type_code=contract_type_code,
            effective_date=effective_date,
            date_time_created=date_time_created,
            row_last_changed=row_last_changed,
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
        contract_number: typing.Optional[str] = None,
        contract_type_code: typing.Optional[str] = None,
        effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        row_last_changed: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            contract_number=contract_number,
            contract_type_code=contract_type_code,
            effective_date=effective_date,
            date_time_created=date_time_created,
            row_last_changed=row_last_changed,
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
        contract_number: typing.Optional[str] = None,
        contract_type_code: typing.Optional[str] = None,
        effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        row_last_changed: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeeContractPydantic:
        raw_response = await self.raw.aget(
            company_id=company_id,
            employee_id=employee_id,
            contract_number=contract_number,
            contract_type_code=contract_type_code,
            effective_date=effective_date,
            date_time_created=date_time_created,
            row_last_changed=row_last_changed,
            page=page,
            per_page=per_page,
            **kwargs,
        )
        if validate:
            return EmployeeContractPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeContractPydantic, raw_response.body)
    
    
    def get(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        contract_number: typing.Optional[str] = None,
        contract_type_code: typing.Optional[str] = None,
        effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        row_last_changed: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        validate: bool = False,
    ) -> EmployeeContractPydantic:
        raw_response = self.raw.get(
            company_id=company_id,
            employee_id=employee_id,
            contract_number=contract_number,
            contract_type_code=contract_type_code,
            effective_date=effective_date,
            date_time_created=date_time_created,
            row_last_changed=row_last_changed,
            page=page,
            per_page=per_page,
        )
        if validate:
            return EmployeeContractPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeContractPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        contract_number: typing.Optional[str] = None,
        contract_type_code: typing.Optional[str] = None,
        effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        row_last_changed: typing.Optional[str] = None,
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
            contract_number=contract_number,
            contract_type_code=contract_type_code,
            effective_date=effective_date,
            date_time_created=date_time_created,
            row_last_changed=row_last_changed,
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
        contract_number: typing.Optional[str] = None,
        contract_type_code: typing.Optional[str] = None,
        effective_date: typing.Optional[str] = None,
        date_time_created: typing.Optional[str] = None,
        row_last_changed: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_mapped_args(
            company_id=company_id,
            employee_id=employee_id,
            contract_number=contract_number,
            contract_type_code=contract_type_code,
            effective_date=effective_date,
            date_time_created=date_time_created,
            row_last_changed=row_last_changed,
            page=page,
            per_page=per_page,
        )
        return self._get_oapg(
            query_params=args.query,
        )

