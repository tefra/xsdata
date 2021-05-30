import abc
from typing import Any
from typing import Dict

import requests


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

    __slots__ = "timeout"

    def __init__(self, timeout: float = 2.0):
        self.timeout = timeout

    def get(self, url: str, params: Dict, headers: Dict) -> bytes:
        """
        :raises HTTPError: if status code is not valid for content unmarshalling.
        """
        res = requests.get(url, params=params, headers=headers, timeout=self.timeout)
        return self.handle_response(res)

    def post(self, url: str, data: Any, headers: Dict) -> Any:
        """
        :raises HTTPError: if status code is not valid for content unmarshalling.
        """
        res = requests.post(url, data=data, headers=headers, timeout=self.timeout)
        return self.handle_response(res)

    @classmethod
    def handle_response(cls, response: requests.Response) -> bytes:
        """
        Status codes 200 or 500 means that we can unmarshall the response.

        :raises HTTPError: If the response status code is not 200 or 500
        """
        if response.status_code not in (200, 500):
            response.raise_for_status()

        return response.content
