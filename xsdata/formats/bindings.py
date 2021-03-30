import abc
import io
import pathlib
from typing import Any
from typing import Optional
from typing import Type
from typing import TypeVar

T = TypeVar("T")


class AbstractSerializer(abc.ABC):
    @abc.abstractmethod
    def render(self, obj: object) -> object:
        """Render the given object to the target output format."""


class AbstractParser(abc.ABC):
    def from_path(self, path: pathlib.Path, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input file path and return the resulting object tree."""
        return self.parse(str(path.resolve()), clazz)

    def from_string(self, source: str, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input string and return the resulting object tree."""
        return self.from_bytes(source.encode(), clazz)

    def from_bytes(self, source: bytes, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input bytes array return the resulting object tree."""
        return self.parse(io.BytesIO(source), clazz)

    @abc.abstractmethod
    def parse(self, source: Any, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input stream or filename and return the resulting object
        tree."""
