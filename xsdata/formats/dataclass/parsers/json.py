import io
import json
import pathlib
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Type

from xsdata.formats.bindings import AbstractParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.utils import ParserUtils


@dataclass
class JsonParser(AbstractParser):
    """
    Json parsing and binding for dataclasses.

    :param context: Model metadata builder
    """

    context: XmlContext = field(default_factory=XmlContext)

    def from_path(self, path: pathlib.Path, clazz: Type[T]) -> T:
        return self.from_bytes(path.read_bytes(), clazz)

    def parse(self, source: io.BytesIO, clazz: Type[T]) -> T:
        """Parse the JSON input stream and return the resulting object tree."""
        ctx = json.load(source)
        return self.parse_context(ctx, clazz)

    def parse_context(self, data: Dict, clazz: Type[T]) -> T:
        """
        Recursively build the given model from the input dict data.

        :raise ParserError: When parsing fails for any reason
        """
        params = {}
        for var in self.context.build(clazz).vars:
            value = self.get_value(data, var)

            if value is None:
                continue
            elif var.is_list:
                params[var.name] = [self.bind_value(var, val) for val in value]
            else:
                params[var.name] = self.bind_value(var, value)

        return clazz(**params)  # type: ignore

    def bind_value(self, var: XmlVar, value: Any) -> Any:
        """
        Bind value according to the class var.

        The return value can be:
        - a dataclass instance
        - a dictionary with unknown attributes
        - a list of unknown elements
        - an enumeration
        - a primitive value
        """
        if var.dataclass and var.clazz:
            return self.parse_context(value, var.clazz)

        if var.is_attributes:
            return dict(value)

        if var.is_wildcard:
            return (
                value
                if isinstance(value, str)
                else self.parse_context(value, AnyElement)
            )

        return ParserUtils.parse_value(value, var.types, var.default, tokens=var.tokens)

    @staticmethod
    def get_value(data: Dict, var: XmlVar) -> Any:
        """Find the var value in the given dictionary or return the default var
        value."""

        local_name = var.local_name
        if local_name in data:
            value = data[local_name]
        elif var.name in data:
            value = data[var.name]
        else:
            return None

        if var.is_list and not isinstance(value, list):
            value = [value]

        return value


@dataclass
class DictConverter(JsonParser):
    def convert(self, data: Dict, clazz: Type[T]) -> T:
        return self.parse_context(data, clazz)
