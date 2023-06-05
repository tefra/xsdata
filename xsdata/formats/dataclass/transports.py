import abc
from typing import Any
from typing import Dict
from typing import Optional

from requests import Response
from requests import Session


class Transport(abc.ABC):
    __slots__ = ()

    @abc.abstractmethod
    def get(self, url: str, params: Dict, headers: Dict) -> bytes:
        """Send a GET request."""

    @abc.abstractmethod
    def post(self, url: str, data: Any, headers: Dict) -> bytes:
        """Send a POST request."""


class DefaultTransport(Transport):
    """
    Default transport based on the requests library.

    :param timeout: Read timeout
    """

    __slots__ = "timeout", "session"

    def __init__(self, timeout: float = 2.0, session: Optional[Session] = None):
        self.timeout = timeout
        self.session = session or Session()

    def get(self, url: str, params: Dict, headers: Dict) -> bytes:
        """
        :raises HTTPError: if status code is not valid for content unmarshalling.
        """
        res = self.session.get(
            url, params=params, headers=headers, timeout=self.timeout
        )
        return self.handle_response(res)

    def post(self, url: str, data: Any, headers: Dict) -> Any:
        """
        :raises HTTPError: if status code is not valid for content unmarshalling.
        """
        res = self.session.post(url, data=data, headers=headers, timeout=self.timeout)
        return self.handle_response(res)

    @classmethod
    def handle_response(cls, response: Response) -> bytes:
        """
        Status codes 200 or 500 means that we can unmarshall the response.

        :raises HTTPError: If the response status code is not 200 or 500
        """
        if response.status_code not in (200, 500):
            response.raise_for_status()

        return response.content
