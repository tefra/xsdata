import abc
from abc import ABCMeta
from typing import Callable
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.codegen.models import Class
from xsdata.models.config import GeneratorConfig
from xsdata.utils.constants import return_true


class ContainerInterface(abc.ABC):
    """Wrap a list of classes and expose a simple api for easy access and
    process."""

    __slots__ = ("config",)

    def __init__(self, config: GeneratorConfig):
        self.config = config

    @abc.abstractmethod
    def iterate(self) -> Iterator[Class]:
        """Create an iterator for the class map values."""

    @abc.abstractmethod
    def find(self, qname: str, condition: Callable = return_true) -> Optional[Class]:
        """Search by qualified name for a specific class with an optional
        condition callable."""

    @abc.abstractmethod
    def find_inner(self, source: Class, qname: str) -> Class:
        """Search by qualified name for a specific inner class or fail."""

    @abc.abstractmethod
    def add(self, item: Class):
        """Add class item to the container."""

    @abc.abstractmethod
    def extend(self, items: List[Class]):
        """Add a list of classes the container."""

    @abc.abstractmethod
    def reset(self, item: Class, qname: str):
        """Update the given class qualified name."""


class HandlerInterface(abc.ABC):
    """Class handler interface."""

    __slots__ = ()

    @abc.abstractmethod
    def process(self, target: Class):
        """Process the given target class."""


class ContainerHandlerInterface(HandlerInterface, metaclass=ABCMeta):
    """Class handler interface with access to the complete classes
    container."""

    __slots__ = ("container",)

    def __init__(self, container: ContainerInterface):
        self.container = container
