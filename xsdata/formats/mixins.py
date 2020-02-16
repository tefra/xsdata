import io
import pathlib
from abc import ABC
from abc import abstractmethod
from enum import Enum
from typing import Any
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

from lxml.etree import Element
from lxml.etree import iterparse

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
    def parse_value(cls, types: List[Type], value: Any) -> Any:
        """Convert xml string values to s python primitive type."""

        if not isinstance(value, str):
            return value

        for cast in types:

            try:
                if issubclass(cast, Enum):
                    enumeration = next(enumeration for enumeration in cast)
                    return cast(type(enumeration.value)(value))
                elif cast is bool and value in ("true", "false"):
                    return value == "true"
                else:
                    return cast(value)
            except ValueError:
                pass

        return value


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
                self.start_node(element)
            elif event == EventType.END:
                obj = self.end_node(element)
                if obj is not None:
                    element.clear()

        if not obj or not isinstance(obj, clazz):
            raise ValueError(
                f"Failed to create target class {clazz.__class__.__name__}."
            )

        return obj

    @abstractmethod
    def start_node(self, element: Element):
        """Prepare to create an object tree from the given starting element."""

    @abstractmethod
    def end_node(self, element: Element) -> Optional[Type]:
        """Create an object tree from the given fully parsed element."""
