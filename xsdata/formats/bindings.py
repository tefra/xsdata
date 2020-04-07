import io
import pathlib
from abc import ABC
from abc import abstractmethod
from typing import Type
from typing import TypeVar


class AbstractSerializer(ABC):
    @abstractmethod
    def render(self, obj: object) -> object:
        """Render the given object to the target output format."""


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
