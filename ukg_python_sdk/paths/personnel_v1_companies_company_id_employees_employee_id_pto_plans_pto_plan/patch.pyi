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

from ukg_python_sdk.model.error import Error as ErrorSchema
from ukg_python_sdk.model.pto_plans import PtoPlans as PtoPlansSchema

from ukg_python_sdk.type.error import Error
from ukg_python_sdk.type.pto_plans import PtoPlans

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.error import Error as ErrorPydantic
from ukg_python_sdk.pydantic.pto_plans import PtoPlans as PtoPlansPydantic

# Path params
CompanyIdSchema = schemas.StrSchema
EmployeeIdSchema = schemas.StrSchema
PtoPlanSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'companyId': typing.Union[CompanyIdSchema, str, ],
        'employeeId': typing.Union[EmployeeIdSchema, str, ],
        'ptoPlan': typing.Union[PtoPlanSchema, str, ],
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


request_path_company_id = api_client.PathParameter(
    name="companyId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyIdSchema,
    required=True,
)
request_path_employee_id = api_client.PathParameter(
    name="employeeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EmployeeIdSchema,
    required=True,
)
request_path_pto_plan = api_client.PathParameter(
    name="ptoPlan",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PtoPlanSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = PtoPlansSchema


request_body_pto_plans = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = PtoPlansSchema
SchemaFor200ResponseBodyApplicationProblemjson = PtoPlansSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PtoPlans


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PtoPlans


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationProblemjson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorSchema
SchemaFor400ResponseBodyApplicationProblemjson = ErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Error


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationProblemjson),
    },
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
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
class ApiResponseFor429(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
)
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _one_pto_plan_mapped_args(
        self,
        employee_id: str,
        company_id: str,
        pto_plan: str,
        company_id: str,
        employee_id: str,
        pto_plan: str,
        earned: typing.Optional[typing.Union[int, float]] = None,
        taken: typing.Optional[typing.Union[int, float]] = None,
        pending_balance: typing.Optional[typing.Union[int, float]] = None,
        earned_through_date: typing.Optional[str] = None,
        reset: typing.Optional[str] = None,
        pending_move_date: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if employee_id is not None:
            _body["employeeId"] = employee_id
        if company_id is not None:
            _body["companyId"] = company_id
        if pto_plan is not None:
            _body["ptoPlan"] = pto_plan
        if earned is not None:
            _body["earned"] = earned
        if taken is not None:
            _body["taken"] = taken
        if pending_balance is not None:
            _body["pendingBalance"] = pending_balance
        if earned_through_date is not None:
            _body["earnedThroughDate"] = earned_through_date
        if reset is not None:
            _body["reset"] = reset
        if pending_move_date is not None:
            _body["pendingMoveDate"] = pending_move_date
        args.body = _body
        if company_id is not None:
            _path_params["companyId"] = company_id
        if employee_id is not None:
            _path_params["employeeId"] = employee_id
        if pto_plan is not None:
            _path_params["ptoPlan"] = pto_plan
        args.path = _path_params
        return args

    async def _aone_pto_plan_oapg(
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
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Patch one PTO Plan
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
            request_path_employee_id,
            request_path_pto_plan,
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
        method = 'patch'.upper()
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
            path_template='/personnel/v1/companies/{companyId}/employees/{employeeId}/pto-plans/{ptoPlan}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pto_plans.serialize(body, content_type)
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


    def _one_pto_plan_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Patch one PTO Plan
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
            request_path_employee_id,
            request_path_pto_plan,
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
        method = 'patch'.upper()
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
            path_template='/personnel/v1/companies/{companyId}/employees/{employeeId}/pto-plans/{ptoPlan}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_pto_plans.serialize(body, content_type)
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


class OnePtoPlanRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aone_pto_plan(
        self,
        employee_id: str,
        company_id: str,
        pto_plan: str,
        company_id: str,
        employee_id: str,
        pto_plan: str,
        earned: typing.Optional[typing.Union[int, float]] = None,
        taken: typing.Optional[typing.Union[int, float]] = None,
        pending_balance: typing.Optional[typing.Union[int, float]] = None,
        earned_through_date: typing.Optional[str] = None,
        reset: typing.Optional[str] = None,
        pending_move_date: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._one_pto_plan_mapped_args(
            employee_id=employee_id,
            company_id=company_id,
            pto_plan=pto_plan,
            company_id=company_id,
            employee_id=employee_id,
            pto_plan=pto_plan,
            earned=earned,
            taken=taken,
            pending_balance=pending_balance,
            earned_through_date=earned_through_date,
            reset=reset,
            pending_move_date=pending_move_date,
        )
        return await self._aone_pto_plan_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def one_pto_plan(
        self,
        employee_id: str,
        company_id: str,
        pto_plan: str,
        company_id: str,
        employee_id: str,
        pto_plan: str,
        earned: typing.Optional[typing.Union[int, float]] = None,
        taken: typing.Optional[typing.Union[int, float]] = None,
        pending_balance: typing.Optional[typing.Union[int, float]] = None,
        earned_through_date: typing.Optional[str] = None,
        reset: typing.Optional[str] = None,
        pending_move_date: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._one_pto_plan_mapped_args(
            employee_id=employee_id,
            company_id=company_id,
            pto_plan=pto_plan,
            company_id=company_id,
            employee_id=employee_id,
            pto_plan=pto_plan,
            earned=earned,
            taken=taken,
            pending_balance=pending_balance,
            earned_through_date=earned_through_date,
            reset=reset,
            pending_move_date=pending_move_date,
        )
        return self._one_pto_plan_oapg(
            body=args.body,
            path_params=args.path,
        )

class OnePtoPlan(BaseApi):

    async def aone_pto_plan(
        self,
        employee_id: str,
        company_id: str,
        pto_plan: str,
        company_id: str,
        employee_id: str,
        pto_plan: str,
        earned: typing.Optional[typing.Union[int, float]] = None,
        taken: typing.Optional[typing.Union[int, float]] = None,
        pending_balance: typing.Optional[typing.Union[int, float]] = None,
        earned_through_date: typing.Optional[str] = None,
        reset: typing.Optional[str] = None,
        pending_move_date: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PtoPlansPydantic:
        raw_response = await self.raw.aone_pto_plan(
            employee_id=employee_id,
            company_id=company_id,
            pto_plan=pto_plan,
            company_id=company_id,
            employee_id=employee_id,
            pto_plan=pto_plan,
            earned=earned,
            taken=taken,
            pending_balance=pending_balance,
            earned_through_date=earned_through_date,
            reset=reset,
            pending_move_date=pending_move_date,
            **kwargs,
        )
        if validate:
            return PtoPlansPydantic(**raw_response.body)
        return api_client.construct_model_instance(PtoPlansPydantic, raw_response.body)
    
    
    def one_pto_plan(
        self,
        employee_id: str,
        company_id: str,
        pto_plan: str,
        company_id: str,
        employee_id: str,
        pto_plan: str,
        earned: typing.Optional[typing.Union[int, float]] = None,
        taken: typing.Optional[typing.Union[int, float]] = None,
        pending_balance: typing.Optional[typing.Union[int, float]] = None,
        earned_through_date: typing.Optional[str] = None,
        reset: typing.Optional[str] = None,
        pending_move_date: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PtoPlansPydantic:
        raw_response = self.raw.one_pto_plan(
            employee_id=employee_id,
            company_id=company_id,
            pto_plan=pto_plan,
            company_id=company_id,
            employee_id=employee_id,
            pto_plan=pto_plan,
            earned=earned,
            taken=taken,
            pending_balance=pending_balance,
            earned_through_date=earned_through_date,
            reset=reset,
            pending_move_date=pending_move_date,
        )
        if validate:
            return PtoPlansPydantic(**raw_response.body)
        return api_client.construct_model_instance(PtoPlansPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        employee_id: str,
        company_id: str,
        pto_plan: str,
        company_id: str,
        employee_id: str,
        pto_plan: str,
        earned: typing.Optional[typing.Union[int, float]] = None,
        taken: typing.Optional[typing.Union[int, float]] = None,
        pending_balance: typing.Optional[typing.Union[int, float]] = None,
        earned_through_date: typing.Optional[str] = None,
        reset: typing.Optional[str] = None,
        pending_move_date: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._one_pto_plan_mapped_args(
            employee_id=employee_id,
            company_id=company_id,
            pto_plan=pto_plan,
            company_id=company_id,
            employee_id=employee_id,
            pto_plan=pto_plan,
            earned=earned,
            taken=taken,
            pending_balance=pending_balance,
            earned_through_date=earned_through_date,
            reset=reset,
            pending_move_date=pending_move_date,
        )
        return await self._aone_pto_plan_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        employee_id: str,
        company_id: str,
        pto_plan: str,
        company_id: str,
        employee_id: str,
        pto_plan: str,
        earned: typing.Optional[typing.Union[int, float]] = None,
        taken: typing.Optional[typing.Union[int, float]] = None,
        pending_balance: typing.Optional[typing.Union[int, float]] = None,
        earned_through_date: typing.Optional[str] = None,
        reset: typing.Optional[str] = None,
        pending_move_date: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._one_pto_plan_mapped_args(
            employee_id=employee_id,
            company_id=company_id,
            pto_plan=pto_plan,
            company_id=company_id,
            employee_id=employee_id,
            pto_plan=pto_plan,
            earned=earned,
            taken=taken,
            pending_balance=pending_balance,
            earned_through_date=earned_through_date,
            reset=reset,
            pending_move_date=pending_move_date,
        )
        return self._one_pto_plan_oapg(
            body=args.body,
            path_params=args.path,
        )

