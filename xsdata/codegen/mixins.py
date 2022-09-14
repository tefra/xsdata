import abc
from abc import ABCMeta
from typing import Callable
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.codegen.models import Attr
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
    def __iter__(self) -> Iterator[Class]:
        """Create an iterator for the class map values."""

    @abc.abstractmethod
    def find(self, qname: str, condition: Callable = return_true) -> Optional[Class]:
        """Search by qualified name for a specific class with an optional
        condition callable."""

    @abc.abstractmethod
    def find_inner(self, source: Class, qname: str) -> Class:
        """Search by qualified name for a specific inner class or fail."""

    @abc.abstractmethod
    def first(self, qname: str) -> Class:
        """Search by qualified name for a specific class and return the first
        available."""

    @abc.abstractmethod
    def add(self, item: Class):
        """Add class item to the container."""

    @abc.abstractmethod
    def extend(self, items: List[Class]):
        """Add a list of classes to the container."""

    @abc.abstractmethod
    def reset(self, item: Class, qname: str):
        """Update the given class qualified name."""

    @abc.abstractmethod
    def set(self, items: List[Class]):
        """Set the list of classes to the container."""


class HandlerInterface(abc.ABC):
    """Class handler interface."""

    __slots__ = ()

    @abc.abstractmethod
    def process(self, target: Class):
        """Process the given target class."""


class RelativeHandlerInterface(HandlerInterface, metaclass=ABCMeta):
    """Class handler interface with access to the complete classes'
    container."""

    __slots__ = "container"

    def __init__(self, container: ContainerInterface):
        self.container = container

    def base_attrs(self, target: Class) -> List[Attr]:
        attrs: List[Attr] = []
        for extension in target.extensions:
            base = self.container.find(extension.type.qname)

            assert base is not None

            attrs.extend(self.base_attrs(base))
            attrs.extend(base.attrs)

        return attrs

    @abc.abstractmethod
    def process(self, target: Class):
        """Process class."""


class ContainerHandlerInterface(abc.ABC):
    """Class container."""

    __slots__ = "container"

    def __init__(self, container: ContainerInterface):
        self.container = container

    @abc.abstractmethod
    def run(self):
        """Run the process for the whole container."""
