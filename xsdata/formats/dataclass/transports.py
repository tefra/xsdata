import abc
from typing import Any, Dict, Optional

from requests import Response, Session


class Transport(abc.ABC):
    """An HTTP transport interface."""

    __slots__ = ()

    @abc.abstractmethod
    def get(self, url: str, params: Dict, headers: Dict) -> bytes:
        """Send a GET request."""

    @abc.abstractmethod
    def post(self, url: str, data: Any, headers: Dict) -> bytes:
        """Send a POST request."""


class DefaultTransport(Transport):
    """Default transport based on the `requests` library.

    Args:
        timeout: Read timeout in seconds
    """

    __slots__ = "timeout", "session"

    def __init__(self, timeout: float = 2.0, session: Optional[Session] = None):
        self.timeout = timeout
        self.session = session or Session()

    def get(self, url: str, params: Dict, headers: Dict) -> bytes:
        """Send a GET request.

        Args:
            url: The base URL
            params: The query parameters
            headers: A key-value map of HTTP headers

        Returns:
            The encoded response content.

        Raises:
            HTTPError: if status code is not valid for content unmarshalling.
        """
        res = self.session.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
        )
        return self.handle_response(res)

    def post(self, url: str, data: Any, headers: Dict) -> Any:
        """Send a POST request.

        Args:
            url: The base URL
            data: The request body payload
            headers: A key-value map of HTTP headers

        Returns:
            The encoded response content.

        Raises:
            HTTPError: if status code is not valid for content unmarshalling.
        """
        res = self.session.post(url, data=data, headers=headers, timeout=self.timeout)
        return self.handle_response(res)

    @classmethod
    def handle_response(cls, response: Response) -> bytes:
        """Return the response content or raise an exception.

        Status codes 200 or 500 means that we can unmarshall the response.

        Args:
            response: The response instance

        Returns:
            The encoded response content.

        Raises:
            HTTPError: If the response status code is not 200 or 500
        """
        if response.status_code not in (200, 500):
            response.raise_for_status()

        return response.content
