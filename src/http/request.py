import aiohttp

from typing import Any, Dict

from src.http.client import HTTPClient


class HTTPRequests(HTTPClient):
    def __init__(self) -> None:
        super().__init__()
        self.session()

    async def get(
            self,
            url: str,
            params: Dict[str, Any] = None,
            headers: Dict[str, str] = None,
            cookies: Dict[str, str] = None,
            allow_redirects: bool = True,
            max_redirects: int = 30
    ) -> aiohttp.ClientResponse:
        async with self.request(
                method="GET",
                url=url,
                params=params,
                headers=headers,
                cookies=cookies,
                allow_redirects=allow_redirects,
                max_redirects=max_redirects
        ) as response:
            return await response

    async def post(
            self,
            url: str,
            data: Any = None,
            json: Any = None,
            headers: Dict[str, str] = None,
            cookies: Dict[str, str] = None,
            allow_redirects: bool = False,
            max_redirects: int = 0
    ) -> aiohttp.ClientResponse:
        async with self.request(
                method="POST",
                url=url,
                data=data,
                json=json,
                headers=headers,
                cookies=cookies,
                allow_redirects=allow_redirects,
                max_redirects=max_redirects,
        ) as response:
            return await response
