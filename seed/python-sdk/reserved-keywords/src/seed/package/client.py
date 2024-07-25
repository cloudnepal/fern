# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions


class PackageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def test(self, *, for_: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        for_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from seed import SeedNurseryApi

        client = SeedNurseryApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.package.test(
            for_="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST", params={"for": for_}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPackageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def test(self, *, for_: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        for_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from seed import AsyncSeedNurseryApi

        client = AsyncSeedNurseryApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.package.test(
                for_="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST", params={"for": for_}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
