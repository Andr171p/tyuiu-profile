import aiohttp

import contextlib
from typing import Optional, Dict, Any, AsyncGenerator


class HTTPClient:
    def __init__(
            self,
            connector: aiohttp.TCPConnector = None,
            timeout: int = 60
            ) -> None:
        self._connector = connector or aiohttp.TCPConnector(limit_per_host=100)
        self._timeout = timeout
        self._session: Optional[aiohttp.ClientSession] = None

    def session(self) -> None:
        self._session = aiohttp.ClientSession(
            connector=self._connector,
            timeout=aiohttp.ClientTimeout(
                total=self._timeout
            )
        )

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()

    @staticmethod
    def is_ok(response: aiohttp.ClientResponse) -> bool:
        return True if response.status == 200 else False

    @contextlib.asynccontextmanager
    async def request(
            self,
            method: str,
            url: str,
            params: Dict[str, Any] = None,
            data: Any = None,
            json: Any = None,
            headers: Dict[str, str] = None,
            cookies: Dict[str, str] = None,
            allow_redirects: bool = True,
            max_redirects: int = 30
    ) -> AsyncGenerator[aiohttp.ClientResponse, None]:
        async with self.session.request(
            method=method.upper(),
            url=url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            cookies=cookies,
            allow_redirects=allow_redirects,
            max_redirects=max_redirects,
        ) as response:
            try:
                if self.is_ok(response=response):
                    yield await response
            except Exception as _ex:
                raise _ex
