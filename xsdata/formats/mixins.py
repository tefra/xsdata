import io
import pathlib
from abc import ABC, abstractmethod
from typing import Type


class AbstractParser(ABC):
    def from_path(self, path: pathlib.Path, clazz: Type) -> Type:
        """Parse the input file path and return the resulting object tree."""
        if isinstance(path, str):
            path = pathlib.Path(path).resolve()

        return self.from_bytes(path.read_bytes(), clazz)

    def from_string(self, source: str, clazz: Type) -> Type:
        """Parse the input string and return the resulting object tree."""
        return self.from_bytes(source.encode(), clazz)

    def from_bytes(self, source: bytes, clazz: Type) -> Type:
        """Parse the input bytes array return the resulting object tree."""
        return self.parse(io.BytesIO(source), clazz)

    @abstractmethod
    def parse(self, source: io.BytesIO, clazz: Type) -> Type:
        """Parse the input stream and return the resulting object tree."""


class AbstractSerializer(ABC):
    @abstractmethod
    def render(self, obj: object) -> object:
        pass
