import io
import pathlib
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

from lxml.etree import Element
from lxml.etree import iterparse

from xsdata.formats.converters import to_python
from xsdata.models.enums import EventType


class AbstractSerializer(ABC):
    @abstractmethod
    def render(self, obj: object) -> object:
        pass


T = TypeVar("T")


class AbstractParser(ABC):
    def from_path(self, path: pathlib.Path, clazz: Type[T]) -> T:
        """Parse the input file path and return the resulting object tree."""
        return self.from_bytes(path.read_bytes(), clazz)

    def from_string(self, source: str, clazz: Type[T]) -> T:
        """Parse the input string and return the resulting object tree."""
        return self.from_bytes(source.encode(), clazz)

    def from_bytes(self, source: bytes, clazz: Type[T]) -> T:
        """Parse the input bytes array return the resulting object tree."""
        return self.parse(io.BytesIO(source), clazz)

    @abstractmethod
    def parse(self, source: io.BytesIO, clazz: Type[T]) -> T:
        """Parse the input stream and return the resulting object tree."""

    @classmethod
    def parse_value(cls, types: List[Type], value: Any, default: Any = None) -> Any:
        """Convert xml string values to s python primitive type."""

        if value is None:
            return None if callable(default) else default

        return to_python(types, value)


class AbstractXmlParser(AbstractParser):
    def parse(self, source: io.BytesIO, clazz: Type[T]) -> T:
        """Parse the XML input stream and return the resulting object tree."""
        ctx = iterparse(
            source=source, events=(EventType.START, EventType.END), recover=True
        )
        return self.parse_context(ctx, clazz)

    def parse_context(self, context: iterparse, clazz: Type[T]) -> T:
        """
        Dispatch elements to handlers as they arrive and are fully parsed.

        :raises ValueError: When the requested type doesn't match the result object
        """

        for event, element in context:
            if event == EventType.START:
                self.queue_node(element)
            elif event == EventType.END:
                obj = self.dequeue_node(element)
                if obj is not None:
                    element.clear()

        if obj and not isinstance(obj, clazz):
            return clazz(obj)  # type: ignore

        if not obj or not isinstance(obj, clazz):
            raise ValueError(
                f"Failed to create target class {clazz.__class__.__name__}."
            )

        return obj

    @abstractmethod
    def queue_node(self, element: Element):
        """Prepare to create an object tree from the given starting element."""

    @abstractmethod
    def dequeue_node(self, element: Element) -> Optional[Type]:
        """Create an object tree from the given fully parsed element."""
