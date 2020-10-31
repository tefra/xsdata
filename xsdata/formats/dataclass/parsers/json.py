import io
import json
import pathlib
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from typing import Any
from typing import Dict
from typing import Type

from xsdata.exceptions import ParserError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
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
            if not var.init:
                continue

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
            return self.bind_wildcard(value)

        if var.is_elements:
            return self.bind_choice(value, var)

        return ParserUtils.parse_value(value, var.types, var.default, tokens=var.tokens)

    def bind_wildcard(self, value: Any) -> Any:
        return (
            value if isinstance(value, str) else self.parse_context(value, AnyElement)
        )

    def bind_choice(self, value: Any, var: XmlVar) -> Any:
        if not isinstance(value, dict):
            return value

        if "qname" in value:
            qname = value["qname"]
            choice = var.find_choice(qname)

            if not choice:
                raise ParserError(
                    f"XmlElements undefined choice: `{var.name}` for qname `{qname}`"
                )

            if "value" in value:
                return DerivedElement(qname, self.bind_value(choice, value["value"]))

            return self.parse_context(value, AnyElement)

        keys = set(value.keys())
        for choice in var.choices:
            if not choice.dataclass:
                continue

            attrs = {f.name for f in fields(choice.clazz)}
            if attrs == keys:
                return self.bind_value(choice, value)

        raise ParserError(f"XmlElements undefined choice: `{var.name}` for `{value}`")

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
