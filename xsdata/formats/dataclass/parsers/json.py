import io
import json
import pathlib
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.types import T


@dataclass
class JsonParser(DictDecoder):
    """Json parser for data classes.

    Args:
        config: Parser configuration
        context: The models context instance
        load_factory: Json loader factory
    """

    load_factory: Callable = field(default=json.load)

    def from_path(self, path: pathlib.Path, clazz: type[T] | None = None) -> T:
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

    def from_string(self, source: str, clazz: type[T] | None = None) -> T:
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

    def from_bytes(self, source: bytes, clazz: type[T] | None = None) -> T:
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

    def parse(self, source: Any, clazz: type[T] | None = None) -> T:
        """Parse the input stream into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            source: The source file name or stream to parse
            clazz: The target class type to parse the source object

        Returns:
            An instance of the specified class representing the parsed content.
        """
        data = self.load_json(source)
        return self.decode(data, clazz)

    def load_json(self, source: Any) -> dict | list:
        """Load the given json source filename or stream.

        Args:
            source: A file name or file stream

        Returns:
            The loaded dictionary or list of dictionaries.
        """
        if not hasattr(source, "read"):
            with open(source, "rb") as fp:
                return self.load_factory(fp)

        return self.load_factory(source)
