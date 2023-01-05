# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.key_value_pair import KeyValuePair
from ...commons.types.map_value import MapValue
from ...commons.types.variable_value import VariableValue
from .test_case_grade import TestCaseGrade
from .test_case_result_with_stdout import TestCaseResultWithStdout
from .traced_test_case import TracedTestCase

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def graded(self, value: TestCaseResultWithStdout) -> SubmissionStatusForTestCase:
        return SubmissionStatusForTestCase(__root__=_SubmissionStatusForTestCase.Graded(**dict(value), type="graded"))

    def graded_v_2(self, value: TestCaseGrade) -> SubmissionStatusForTestCase:
        return SubmissionStatusForTestCase(__root__=_SubmissionStatusForTestCase.GradedV2(type="gradedV2", value=value))

    def traced(self, value: TracedTestCase) -> SubmissionStatusForTestCase:
        return SubmissionStatusForTestCase(__root__=_SubmissionStatusForTestCase.Traced(**dict(value), type="traced"))


class SubmissionStatusForTestCase(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _SubmissionStatusForTestCase.Graded, _SubmissionStatusForTestCase.GradedV2, _SubmissionStatusForTestCase.Traced
    ]:
        return self.__root__

    def visit(
        self,
        graded: typing.Callable[[TestCaseResultWithStdout], T_Result],
        graded_v_2: typing.Callable[[TestCaseGrade], T_Result],
        traced: typing.Callable[[TracedTestCase], T_Result],
    ) -> T_Result:
        if self.__root__.type == "graded":
            return graded(self.__root__)
        if self.__root__.type == "gradedV2":
            return graded_v_2(self.__root__.value)
        if self.__root__.type == "traced":
            return traced(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[
            _SubmissionStatusForTestCase.Graded,
            _SubmissionStatusForTestCase.GradedV2,
            _SubmissionStatusForTestCase.Traced,
        ],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionStatusForTestCase.Validators.validate
            def validate(value: typing.Union[_SubmissionStatusForTestCase.Graded, _SubmissionStatusForTestCase.GradedV2, _SubmissionStatusForTestCase.Traced]) -> typing.Union[_SubmissionStatusForTestCase.Graded, _SubmissionStatusForTestCase.GradedV2, _SubmissionStatusForTestCase.Traced]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _SubmissionStatusForTestCase.Graded,
                            _SubmissionStatusForTestCase.GradedV2,
                            _SubmissionStatusForTestCase.Traced,
                        ]
                    ],
                    typing.Union[
                        _SubmissionStatusForTestCase.Graded,
                        _SubmissionStatusForTestCase.GradedV2,
                        _SubmissionStatusForTestCase.Traced,
                    ],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _SubmissionStatusForTestCase.Graded,
                        _SubmissionStatusForTestCase.GradedV2,
                        _SubmissionStatusForTestCase.Traced,
                    ]
                ],
                typing.Union[
                    _SubmissionStatusForTestCase.Graded,
                    _SubmissionStatusForTestCase.GradedV2,
                    _SubmissionStatusForTestCase.Traced,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _SubmissionStatusForTestCase.Graded,
                _SubmissionStatusForTestCase.GradedV2,
                _SubmissionStatusForTestCase.Traced,
            ],
            values.get("__root__"),
        )
        for validator in SubmissionStatusForTestCase.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid


class _SubmissionStatusForTestCase:
    class Graded(TestCaseResultWithStdout):
        type: typing_extensions.Literal["graded"]

        class Config:
            frozen = True

    class GradedV2(pydantic.BaseModel):
        type: typing_extensions.Literal["gradedV2"]
        value: TestCaseGrade

        class Config:
            frozen = True

    class Traced(TracedTestCase):
        type: typing_extensions.Literal["traced"]

        class Config:
            frozen = True


_SubmissionStatusForTestCase.Graded.update_forward_refs(
    KeyValuePair=KeyValuePair, MapValue=MapValue, VariableValue=VariableValue
)
_SubmissionStatusForTestCase.Traced.update_forward_refs(
    KeyValuePair=KeyValuePair, MapValue=MapValue, VariableValue=VariableValue
)
SubmissionStatusForTestCase.update_forward_refs()
