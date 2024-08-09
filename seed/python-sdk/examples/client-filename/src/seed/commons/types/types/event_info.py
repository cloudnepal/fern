# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from .tag import Tag


class EventInfo_Metadata(UniversalBaseModel):
    """
    Examples
    --------
    from seed.commons.types import EventInfo_Metadata

    EventInfo_Metadata(
        id="metadata-alskjfg8",
        data={"one": "two"},
        json_string='{"one": "two"}',
    )
    """

    type: typing.Literal["metadata"] = "metadata"
    id: str
    data: typing.Optional[typing.Dict[str, str]] = None
    json_string: typing.Optional[str] = pydantic.Field(alias="jsonString", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class EventInfo_Tag(UniversalBaseModel):
    value: Tag
    type: typing.Literal["tag"] = "tag"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True


"""
from seed.commons.types import EventInfo_Metadata

EventInfo_Metadata(
    id="metadata-alskjfg8",
    data={"one": "two"},
    json_string='{"one": "two"}',
)
"""
EventInfo = typing.Union[EventInfo_Metadata, EventInfo_Tag]
