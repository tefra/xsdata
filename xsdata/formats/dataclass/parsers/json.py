import json
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Type, Union

from xsdata.formats.bindings import AbstractParser, T
from xsdata.formats.dataclass.parsers import DictDecoder


@dataclass
class JsonParser(DictDecoder, AbstractParser):
    """Json parser for data classes.

    Args:
        config: Parser configuration
        context: The models context instance
        load_factory: Json loader factory
    """

    load_factory: Callable = field(default=json.load)

    def parse(self, source: Any, clazz: Optional[Type[T]] = None) -> T:
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

    def load_json(self, source: Any) -> Union[Dict, List]:
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
