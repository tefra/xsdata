from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any
from typing import Dict

import requests


class Transport(ABC):
    @abstractmethod
    def get(self, url: str, params: Dict, headers: Dict) -> bytes:
        """Send a GET request."""

    @abstractmethod
    def post(self, url: str, data: Any, headers: Dict) -> bytes:
        """Send a POST request."""


@dataclass
class DefaultTransport(Transport):
    """
    Default transport based on the requests library.

    :param timeout: Read timeout
    """

    timeout: float = 2.0

    def get(self, url: str, params: Dict, headers: Dict) -> bytes:
        r = requests.get(url, params=params, headers=headers, timeout=self.timeout)
        r.raise_for_status()
        return r.content

    def post(self, url: str, data: Any, headers: Dict) -> bytes:
        r = requests.post(url, data=data, headers=headers, timeout=self.timeout)
        r.raise_for_status()
        return r.content
