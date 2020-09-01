import abc
import io
import pathlib
from typing import Any
from typing import Type
from typing import TypeVar

T = TypeVar("T")


class AbstractSerializer(abc.ABC):
    @abc.abstractmethod
    def render(self, obj: object) -> object:
        """Render the given object to the target output format."""


class AbstractParser(abc.ABC):
    def from_path(self, path: pathlib.Path, clazz: Type[T]) -> T:
        """Parse the input file path and return the resulting object tree."""
        return self.parse(str(path.resolve()), clazz)

    def from_string(self, source: str, clazz: Type[T]) -> T:
        """Parse the input string and return the resulting object tree."""
        return self.from_bytes(source.encode(), clazz)

    def from_bytes(self, source: bytes, clazz: Type[T]) -> T:
        """Parse the input bytes array return the resulting object tree."""
        return self.parse(io.BytesIO(source), clazz)

    @abc.abstractmethod
    def parse(self, source: Any, clazz: Type[T]) -> T:
        """Parse the input stream and return the resulting object tree."""
