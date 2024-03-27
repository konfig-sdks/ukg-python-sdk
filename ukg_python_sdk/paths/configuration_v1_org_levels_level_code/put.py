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
from ukg_python_sdk.model.org_levels import OrgLevels as OrgLevelsSchema

from ukg_python_sdk.type.error import Error
from ukg_python_sdk.type.org_levels import OrgLevels

from ...api_client import Dictionary
from ukg_python_sdk.pydantic.error import Error as ErrorPydantic
from ukg_python_sdk.pydantic.org_levels import OrgLevels as OrgLevelsPydantic

from . import path

# Path params
LevelSchema = schemas.StrSchema
CodeSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'level': typing.Union[LevelSchema, str, ],
        'code': typing.Union[CodeSchema, str, ],
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


request_path_level = api_client.PathParameter(
    name="level",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LevelSchema,
    required=True,
)
request_path_code = api_client.PathParameter(
    name="code",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CodeSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = OrgLevelsSchema


request_body_org_levels = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'OauthSecurity',
]
SchemaFor200ResponseBodyApplicationJson = OrgLevelsSchema
SchemaFor200ResponseBodyApplicationProblemjson = OrgLevelsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OrgLevels


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OrgLevels


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
    '404': _response_for_404,
    '429': _response_for_429,
}
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _update_org_level_mapped_args(
        self,
        description: str,
        code: str,
        level: typing.Union[int, float],
        level: str,
        code: str,
        budget_group: typing.Optional[str] = None,
        current_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        current_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        gl_segment: typing.Optional[str] = None,
        last_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        last_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        level_description: typing.Optional[str] = None,
        reporting_category: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if budget_group is not None:
            _body["budgetGroup"] = budget_group
        if code is not None:
            _body["code"] = code
        if current_year_budget_fte is not None:
            _body["currentYearBudgetFTE"] = current_year_budget_fte
        if current_year_budget_salary is not None:
            _body["currentYearBudgetSalary"] = current_year_budget_salary
        if gl_segment is not None:
            _body["glSegment"] = gl_segment
        if last_year_budget_fte is not None:
            _body["lastYearBudgetFTE"] = last_year_budget_fte
        if last_year_budget_salary is not None:
            _body["lastYearBudgetSalary"] = last_year_budget_salary
        if level is not None:
            _body["level"] = level
        if level_description is not None:
            _body["levelDescription"] = level_description
        if reporting_category is not None:
            _body["reportingCategory"] = reporting_category
        if is_active is not None:
            _body["isActive"] = is_active
        args.body = _body
        if level is not None:
            _path_params["level"] = level
        if code is not None:
            _path_params["code"] = code
        args.path = _path_params
        return args

    async def _aupdate_org_level_oapg(
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
        Update one org-level
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_level,
            request_path_code,
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
        method = 'put'.upper()
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
            path_template='/configuration/v1/org-levels/{level}/{code}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_org_levels.serialize(body, content_type)
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


    def _update_org_level_oapg(
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
        Update one org-level
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_level,
            request_path_code,
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
        method = 'put'.upper()
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
            path_template='/configuration/v1/org-levels/{level}/{code}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_org_levels.serialize(body, content_type)
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


class UpdateOrgLevelRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_org_level(
        self,
        description: str,
        code: str,
        level: typing.Union[int, float],
        level: str,
        code: str,
        budget_group: typing.Optional[str] = None,
        current_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        current_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        gl_segment: typing.Optional[str] = None,
        last_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        last_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        level_description: typing.Optional[str] = None,
        reporting_category: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_org_level_mapped_args(
            description=description,
            code=code,
            level=level,
            level=level,
            code=code,
            budget_group=budget_group,
            current_year_budget_fte=current_year_budget_fte,
            current_year_budget_salary=current_year_budget_salary,
            gl_segment=gl_segment,
            last_year_budget_fte=last_year_budget_fte,
            last_year_budget_salary=last_year_budget_salary,
            level_description=level_description,
            reporting_category=reporting_category,
            is_active=is_active,
        )
        return await self._aupdate_org_level_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_org_level(
        self,
        description: str,
        code: str,
        level: typing.Union[int, float],
        level: str,
        code: str,
        budget_group: typing.Optional[str] = None,
        current_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        current_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        gl_segment: typing.Optional[str] = None,
        last_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        last_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        level_description: typing.Optional[str] = None,
        reporting_category: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_org_level_mapped_args(
            description=description,
            code=code,
            level=level,
            level=level,
            code=code,
            budget_group=budget_group,
            current_year_budget_fte=current_year_budget_fte,
            current_year_budget_salary=current_year_budget_salary,
            gl_segment=gl_segment,
            last_year_budget_fte=last_year_budget_fte,
            last_year_budget_salary=last_year_budget_salary,
            level_description=level_description,
            reporting_category=reporting_category,
            is_active=is_active,
        )
        return self._update_org_level_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateOrgLevel(BaseApi):

    async def aupdate_org_level(
        self,
        description: str,
        code: str,
        level: typing.Union[int, float],
        level: str,
        code: str,
        budget_group: typing.Optional[str] = None,
        current_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        current_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        gl_segment: typing.Optional[str] = None,
        last_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        last_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        level_description: typing.Optional[str] = None,
        reporting_category: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> OrgLevelsPydantic:
        raw_response = await self.raw.aupdate_org_level(
            description=description,
            code=code,
            level=level,
            level=level,
            code=code,
            budget_group=budget_group,
            current_year_budget_fte=current_year_budget_fte,
            current_year_budget_salary=current_year_budget_salary,
            gl_segment=gl_segment,
            last_year_budget_fte=last_year_budget_fte,
            last_year_budget_salary=last_year_budget_salary,
            level_description=level_description,
            reporting_category=reporting_category,
            is_active=is_active,
            **kwargs,
        )
        if validate:
            return OrgLevelsPydantic(**raw_response.body)
        return api_client.construct_model_instance(OrgLevelsPydantic, raw_response.body)
    
    
    def update_org_level(
        self,
        description: str,
        code: str,
        level: typing.Union[int, float],
        level: str,
        code: str,
        budget_group: typing.Optional[str] = None,
        current_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        current_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        gl_segment: typing.Optional[str] = None,
        last_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        last_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        level_description: typing.Optional[str] = None,
        reporting_category: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> OrgLevelsPydantic:
        raw_response = self.raw.update_org_level(
            description=description,
            code=code,
            level=level,
            level=level,
            code=code,
            budget_group=budget_group,
            current_year_budget_fte=current_year_budget_fte,
            current_year_budget_salary=current_year_budget_salary,
            gl_segment=gl_segment,
            last_year_budget_fte=last_year_budget_fte,
            last_year_budget_salary=last_year_budget_salary,
            level_description=level_description,
            reporting_category=reporting_category,
            is_active=is_active,
        )
        if validate:
            return OrgLevelsPydantic(**raw_response.body)
        return api_client.construct_model_instance(OrgLevelsPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        description: str,
        code: str,
        level: typing.Union[int, float],
        level: str,
        code: str,
        budget_group: typing.Optional[str] = None,
        current_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        current_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        gl_segment: typing.Optional[str] = None,
        last_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        last_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        level_description: typing.Optional[str] = None,
        reporting_category: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_org_level_mapped_args(
            description=description,
            code=code,
            level=level,
            level=level,
            code=code,
            budget_group=budget_group,
            current_year_budget_fte=current_year_budget_fte,
            current_year_budget_salary=current_year_budget_salary,
            gl_segment=gl_segment,
            last_year_budget_fte=last_year_budget_fte,
            last_year_budget_salary=last_year_budget_salary,
            level_description=level_description,
            reporting_category=reporting_category,
            is_active=is_active,
        )
        return await self._aupdate_org_level_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        description: str,
        code: str,
        level: typing.Union[int, float],
        level: str,
        code: str,
        budget_group: typing.Optional[str] = None,
        current_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        current_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        gl_segment: typing.Optional[str] = None,
        last_year_budget_fte: typing.Optional[typing.Union[int, float]] = None,
        last_year_budget_salary: typing.Optional[typing.Union[int, float]] = None,
        level_description: typing.Optional[str] = None,
        reporting_category: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_org_level_mapped_args(
            description=description,
            code=code,
            level=level,
            level=level,
            code=code,
            budget_group=budget_group,
            current_year_budget_fte=current_year_budget_fte,
            current_year_budget_salary=current_year_budget_salary,
            gl_segment=gl_segment,
            last_year_budget_fte=last_year_budget_fte,
            last_year_budget_salary=last_year_budget_salary,
            level_description=level_description,
            reporting_category=reporting_category,
            is_active=is_active,
        )
        return self._update_org_level_oapg(
            body=args.body,
            path_params=args.path,
        )

