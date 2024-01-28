import abc
import io
import pathlib
from typing import Any, Optional, Type, TypeVar

T = TypeVar("T")


class AbstractSerializer(abc.ABC):
    """Abstract serializer class."""

    @abc.abstractmethod
    def render(self, obj: Any) -> str:
        """Serialize the input model instance to the output string format.

        Args:
            obj: The input model instance to serialize

        Returns:
            The serialized string output format.
        """


class AbstractParser(abc.ABC):
    """Abstract parser class."""

    def from_path(self, path: pathlib.Path, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input file into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            path: The path to the input file
            clazz: The target class type to parse the file into

        Returns:
            An instance of the specified class representing the parsed content.
        """
        return self.parse(str(path.resolve()), clazz)

    def from_string(self, source: str, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input source string into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            source: The source string to parse
            clazz: The target class type to parse the source string into

        Returns:
            An instance of the specified class representing the parsed content.
        """
        return self.from_bytes(source.encode(), clazz)

    def from_bytes(self, source: bytes, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input source bytes object into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            source: The source bytes object to parse
            clazz: The target class type to parse the source bytes object

        Returns:
            An instance of the specified class representing the parsed content.
        """
        return self.parse(io.BytesIO(source), clazz)

    @abc.abstractmethod
    def parse(self, source: Any, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input file or stream into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            source: The source stream object to parse
            clazz: The target class type to parse the source bytes object

        Returns:
            An instance of the specified class representing the parsed content.
        """
