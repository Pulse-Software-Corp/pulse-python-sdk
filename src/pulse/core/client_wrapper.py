# This file is hand-maintained (listed in .fernignore). It accepts the
# `logging` and `max_retries` kwargs that the auto-generated `client.py`
# passes in fern-python-sdk >= 5.10. The auto-generated wrapper template
# in those Fern versions does NOT include those kwargs, which would break
# `Pulse(api_key=...)` at construction. Until upstream fixes the template
# mismatch, we accept the kwargs here and forward them where they belong.
#
# Tracked under AGENTS.md §4.2 in pulse-fern-config.

import typing

import httpx
from .http_client import AsyncHttpClient, HttpClient
from ..version import __version__


class BaseClientWrapper:
    def __init__(
        self,
        *,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        logging: typing.Optional[typing.Any] = None,
    ):
        self.api_key = api_key
        self._headers = headers
        self._base_url = base_url
        self._timeout = timeout
        # Store for future use; the underlying HttpClient handles retries
        # via httpx-level transports today, so these are accepted-but-unused
        # for now. Do NOT remove — `client.py` always passes them.
        self._max_retries = max_retries
        self._logging = logging

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "User-Agent": "pulse-python-sdk/1.0.8",
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "pulse-python-sdk",
            "X-Fern-SDK-Version": "1.0.8",
            "X-Pulse-Source": f"sdk-python-{__version__}",
            **(self.get_custom_headers() or {}),
        }
        headers["x-api-key"] = self.api_key
        return headers

    def get_custom_headers(self) -> typing.Optional[typing.Dict[str, str]]:
        return self._headers

    def get_base_url(self) -> str:
        return self._base_url

    def get_timeout(self) -> typing.Optional[float]:
        return self._timeout


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        logging: typing.Optional[typing.Any] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(
            api_key=api_key,
            headers=headers,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            logging=logging,
        )
        self.httpx_client = HttpClient(
            httpx_client=httpx_client,
            base_headers=self.get_headers,
            base_timeout=self.get_timeout,
            base_url=self.get_base_url,
        )


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        logging: typing.Optional[typing.Any] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(
            api_key=api_key,
            headers=headers,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            logging=logging,
        )
        self._async_token = async_token
        self.httpx_client = AsyncHttpClient(
            httpx_client=httpx_client,
            base_headers=self.get_headers,
            base_timeout=self.get_timeout,
            base_url=self.get_base_url,
            async_base_headers=self.async_get_headers,
        )

    async def async_get_headers(self) -> typing.Dict[str, str]:
        headers = self.get_headers()
        if self._async_token is not None:
            token = await self._async_token()
            headers["Authorization"] = f"Bearer {token}"
        return headers
