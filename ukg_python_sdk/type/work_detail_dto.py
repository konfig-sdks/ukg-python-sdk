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

from ukg_python_sdk.type.department_dto import DepartmentDto
from ukg_python_sdk.type.docket_dto import DocketDto
from ukg_python_sdk.type.hour_type_dto import HourTypeDto
from ukg_python_sdk.type.job_dto import JobDto
from ukg_python_sdk.type.project_dto import ProjectDto
from ukg_python_sdk.type.team_dto import TeamDto
from ukg_python_sdk.type.time_code_dto import TimeCodeDto

class RequiredWorkDetailDto(TypedDict):
    pass

class OptionalWorkDetailDto(TypedDict, total=False):
    id: int

    workSummaryId: int

    startTime: datetime

    endTime: datetime

    minutes: int

    rate: typing.Union[int, float]

    timecode: TimeCodeDto

    hourType: HourTypeDto

    job: JobDto

    department: DepartmentDto

    project: ProjectDto

    docket: DocketDto

    team: TeamDto

    workType: str

    flag1: str

    flag2: str

    flag3: str

    flag4: str

    flag5: str

    flag6: str

    flag7: str

    flag8: str

    flag9: str

    flag10: str

    udf1: str

    udf2: str

    udf3: str

    udf4: str

    udf5: str

    udf6: str

    udf7: str

    udf8: str

    udf9: str

    udf10: str

class WorkDetailDto(RequiredWorkDetailDto, OptionalWorkDetailDto):
    pass
