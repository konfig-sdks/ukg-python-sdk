# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

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


class CountryQuestionResponses(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def question() -> typing.Type['CountryQuestionResponsesQuestion']:
                return CountryQuestionResponsesQuestion
            response = schemas.AnyTypeSchema
            __annotations__ = {
                "question": question,
                "response": response,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question"]) -> 'CountryQuestionResponsesQuestion': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response"]) -> MetaOapg.properties.response: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["question", "response", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question"]) -> typing.Union['CountryQuestionResponsesQuestion', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response"]) -> typing.Union[MetaOapg.properties.response, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["question", "response", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        question: typing.Union['CountryQuestionResponsesQuestion', schemas.Unset] = schemas.unset,
        response: typing.Union[MetaOapg.properties.response, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CountryQuestionResponses':
        return super().__new__(
            cls,
            *args,
            question=question,
            response=response,
            _configuration=_configuration,
            **kwargs,
        )

from ukg_python_sdk.model.country_question_responses_question import CountryQuestionResponsesQuestion
