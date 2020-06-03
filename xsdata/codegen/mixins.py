import abc
from typing import Callable
from typing import Iterator
from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.codegen.models import Class

Condition = Optional[Callable]


class ContainerInterface(metaclass=abc.ABCMeta):
    """Wrap a list of classes and expose a simple api for easy access and
    process."""

    @abc.abstractmethod
    def iterate(self) -> Iterator[Class]:
        """Create an iterator for the class map values."""

    @abc.abstractmethod
    def find(self, qname: QName, condition: Condition = None) -> Optional[Class]:
        """Search by qualified name for a specific class with an optional
        condition callable."""

    @abc.abstractmethod
    def add(self, item: Class):
        """Add class item to the container."""

    @abc.abstractmethod
    def extend(self, items: List[Class]):
        """Add a list of classes the container."""


class HandlerInterface(metaclass=abc.ABCMeta):
    """Class handler interface."""

    @abc.abstractmethod
    def process(self, target: Class):
        """Process the given target class."""
