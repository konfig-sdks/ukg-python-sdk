# coding: utf-8

"""
    User Profile Details

    Configure your UKG Pro Configuration Codes through UKG Pro APIs. Status: R1 deployment

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from ukg_python_sdk.pydantic.state_dto import StateDto

class ScheduleModelStateDto(BaseModel):
    operation_type: typing.Optional[typing.List[StateDto]] = Field(None, alias='operationType')

    emp_name: typing.Optional[typing.List[StateDto]] = Field(None, alias='empName')

    skd_date: typing.Optional[typing.List[StateDto]] = Field(None, alias='skdDate')

    skd_start_time: typing.Optional[typing.List[StateDto]] = Field(None, alias='skdStartTime')

    skd_end_time: typing.Optional[typing.List[StateDto]] = Field(None, alias='skdEndTime')

    skd_time: typing.Optional[typing.List[StateDto]] = Field(None, alias='skdTime')

    wbt_name: typing.Optional[typing.List[StateDto]] = Field(None, alias='wbtName')

    tcode_name: typing.Optional[typing.List[StateDto]] = Field(None, alias='tcodeName')

    job_name: typing.Optional[typing.List[StateDto]] = Field(None, alias='jobName')

    htype_name: typing.Optional[typing.List[StateDto]] = Field(None, alias='htypeName')

    act_name: typing.Optional[typing.List[StateDto]] = Field(None, alias='actName')

    no_details: typing.Optional[typing.List[StateDto]] = Field(None, alias='noDetails')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
