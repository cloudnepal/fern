# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from .errors.movie_does_not_exist_error import MovieDoesNotExistError
from .types.movie import Movie
from .types.movie_id import MovieId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ImdbClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_movie(
        self, *, title: str, rating: float, request_options: typing.Optional[RequestOptions] = None
    ) -> MovieId:
        """
        Add a movie to the database

        Parameters
        ----------
        title : str

        rating : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MovieId

        Examples
        --------
        from seed.client import SeedApi

        client = SeedApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.imdb.create_movie(
            title="string",
            rating=1.1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "movies/create-movie",
            method="POST",
            json={"title": title, "rating": rating},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(MovieId, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_movie(self, movie_id: MovieId, *, request_options: typing.Optional[RequestOptions] = None) -> Movie:
        """
        Parameters
        ----------
        movie_id : MovieId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Movie

        Examples
        --------
        from seed.client import SeedApi

        client = SeedApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.imdb.get_movie(
            movie_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"movies/{jsonable_encoder(movie_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Movie, _response.json())  # type: ignore
            if _response.status_code == 404:
                raise MovieDoesNotExistError(pydantic_v1.parse_obj_as(MovieId, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncImdbClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_movie(
        self, *, title: str, rating: float, request_options: typing.Optional[RequestOptions] = None
    ) -> MovieId:
        """
        Add a movie to the database

        Parameters
        ----------
        title : str

        rating : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MovieId

        Examples
        --------
        from seed.client import AsyncSeedApi

        client = AsyncSeedApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.imdb.create_movie(
            title="string",
            rating=1.1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "movies/create-movie",
            method="POST",
            json={"title": title, "rating": rating},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(MovieId, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_movie(self, movie_id: MovieId, *, request_options: typing.Optional[RequestOptions] = None) -> Movie:
        """
        Parameters
        ----------
        movie_id : MovieId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Movie

        Examples
        --------
        from seed.client import AsyncSeedApi

        client = AsyncSeedApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.imdb.get_movie(
            movie_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"movies/{jsonable_encoder(movie_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Movie, _response.json())  # type: ignore
            if _response.status_code == 404:
                raise MovieDoesNotExistError(pydantic_v1.parse_obj_as(MovieId, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
