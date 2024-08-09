# This file was auto-generated by Fern from our API Definition.

from .movie import Movie
import typing
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ExtendedMovie(Movie):
    """
    Examples
    --------
    from seed.types import ExtendedMovie

    ExtendedMovie(
        id="movie-sda231x",
        title="Pulp Fiction",
        from_="Quentin Tarantino",
        rating=8.5,
        tag="tag-12efs9dv",
        cast=["John Travolta", "Samuel L. Jackson", "Uma Thurman", "Bruce Willis"],
        metadata={
            "academyAward": true,
            "releaseDate": "2023-12-08",
            "ratings": {"rottenTomatoes": 97, "imdb": 7.6},
        },
    )
    """

    cast: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
