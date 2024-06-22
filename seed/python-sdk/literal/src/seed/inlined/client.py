# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.send_response import SendResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InlinedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def send(
        self,
        *,
        query: str,
        temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> SendResponse:
        """
        Parameters
        ----------
        query : str

        temperature : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendResponse

        Examples
        --------
        from seed.client import SeedLiteral

        client = SeedLiteral(
            base_url="https://yourhost.com/path/to/api",
        )
        client.inlined.send(
            temperature=10.1,
            query="What is the weather today",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "inlined",
            method="POST",
            json={"query": query, "temperature": temperature, "prompt": "You are a helpful assistant", "stream": False},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SendResponse, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInlinedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def send(
        self,
        *,
        query: str,
        temperature: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> SendResponse:
        """
        Parameters
        ----------
        query : str

        temperature : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendResponse

        Examples
        --------
        from seed.client import AsyncSeedLiteral

        client = AsyncSeedLiteral(
            base_url="https://yourhost.com/path/to/api",
        )
        await client.inlined.send(
            temperature=10.1,
            query="What is the weather today",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inlined",
            method="POST",
            json={"query": query, "temperature": temperature, "prompt": "You are a helpful assistant", "stream": False},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SendResponse, _response.json())  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
