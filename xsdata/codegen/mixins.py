import abc
from abc import ABCMeta
from typing import Callable, Dict, Iterator, List, Optional

from xsdata.codegen.models import Attr, Class
from xsdata.models.config import GeneratorConfig
from xsdata.utils.constants import return_true


class ContainerInterface(abc.ABC):
    """A class list wrapper with an easy access api.

    Args:
        config: The generator configuration instance
    """

    __slots__ = ("config", "data")

    def __init__(self, config: GeneratorConfig):
        self.config = config
        self.data: Dict[str, List[Class]] = {}

    @abc.abstractmethod
    def __iter__(self) -> Iterator[Class]:
        """Yield an iterator for the class map values."""

    @abc.abstractmethod
    def find(self, qname: str, condition: Callable = return_true) -> Optional[Class]:
        """Find class that matches the given qualified name and condition callable.

        Classes are allowed to have the same qualified name, e.g. xsd:Element
        extending xsd:ComplexType with the same name, you can provide and additional
        callback to filter the classes like the tag.

        Args:
            qname: The qualified name of the class
            condition: A user callable to filter further

        Returns:
            A class instance or None if no match found.
        """

    @abc.abstractmethod
    def find_inner(self, source: Class, qname: str) -> Class:
        """Search by qualified name for a specific inner class or fail.

        Args:
            source: The source class to search for the inner class
            qname: The qualified name of the inner class to look up

        Returns:
            The inner class instance

        Raises:
            CodeGenerationError: If the inner class is not found.
        """

    @abc.abstractmethod
    def first(self, qname: str) -> Class:
        """Return the first class that matches the qualified name.

        Args:
            qname: The qualified name of the class

        Returns:
            The first matching class

        Raises:
            KeyError: If no class matches the qualified name
        """

    @abc.abstractmethod
    def add(self, item: Class):
        """Add class instance to the container.

        Args:
            item: The class instance to add
        """

    @abc.abstractmethod
    def remove(self, *items: Class):
        """Safely remove classes from the container.

        Args:
            items: The classes to remove
        """

    @abc.abstractmethod
    def extend(self, items: List[Class]):
        """Add a list of classes to the container.

        Args:
            items: The list of class instances to add
        """

    @abc.abstractmethod
    def reset(self, item: Class, qname: str):
        """Update the given class qualified name.

        Args:
            item: The target class instance to update
            qname: The new qualified name of the class
        """

    @abc.abstractmethod
    def set(self, items: List[Class]):
        """Set the list of classes to the container.

        Args:
            items: The list of classes
        """


class HandlerInterface(abc.ABC):
    """Class handler interface."""

    __slots__ = ()

    @abc.abstractmethod
    def process(self, target: Class):
        """Process the given target class.

        Args:
            target: The target class instance
        """


class RelativeHandlerInterface(HandlerInterface, metaclass=ABCMeta):
    """An interface for codegen handlers with class container access.

    Args:
        container: The container instance
    """

    __slots__ = "container"

    def __init__(self, container: ContainerInterface):
        self.container = container

    def base_attrs(self, target: Class) -> List[Attr]:
        """Return a list of all parent attrs recursively.

        Args:
            target: The target class

        Returns:
            A list of attr instances.

        """
        attrs: List[Attr] = []
        for extension in target.extensions:
            base = self.container.find(extension.type.qname)

            assert base is not None

            attrs.extend(self.base_attrs(base))

            for attr in base.attrs:
                attr.parent = base.qname
                attrs.append(attr)

        return attrs

    @abc.abstractmethod
    def process(self, target: Class):
        """Process entrypoint for a class.

        Args:
            target: The target class instance
        """


class ContainerHandlerInterface(abc.ABC):
    """A codegen interface for processing the whole class container.

    Args:
        container: The class container instance
    """

    __slots__ = "container"

    def __init__(self, container: ContainerInterface):
        self.container = container

    @abc.abstractmethod
    def run(self):
        """Run the process for the whole container."""
