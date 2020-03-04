import io
import json
from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import Type
from typing import TypeVar

from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.mixins import ClassVar
from xsdata.formats.dataclass.mixins import ModelInspect
from xsdata.formats.dataclass.models import AnyElement
from xsdata.formats.mixins import AbstractParser

T = TypeVar("T")


@dataclass
class JsonParser(AbstractParser, ModelInspect):
    def parse(self, source: io.BytesIO, clazz: Type[T]) -> T:
        """Parse the JSON input stream and return the resulting object tree."""
        ctx = json.load(source)
        return self.parse_context(ctx, clazz)

    def parse_context(self, data: Dict, clazz: Type[T]) -> T:
        """
        Recursively build the given model from the input dict data.

        :raise TypeError: When parsing fails for any reason
        """
        params = {}

        if isinstance(data, list) and len(data) == 1:
            data = data[0]

        for var in self.class_meta(clazz).vars.values():
            value = self.get_value(data, var)

            if value is None:
                continue
            elif var.is_list:
                params[var.name] = [self.bind_value(var, val) for val in value]
            else:
                params[var.name] = self.bind_value(var, value)

        try:
            return clazz(**params)  # type: ignore
        except Exception:
            raise ParserError("Parsing failed")

    def bind_value(self, var: ClassVar, value) -> Any:
        """
        Bind value according to the class var.

        The return value can be:
        - a dataclass instance
        - a dictionary with unknown attributes
        - a list of unknown elements
        - an enumeration
        - a primitive value
        """
        if var.is_dataclass:
            return self.parse_context(value, var.clazz)
        elif var.is_any_attribute:
            return dict(value)
        elif var.is_any_element:
            return (
                value
                if isinstance(value, str)
                else self.parse_context(value, AnyElement)
            )
        else:
            return self.parse_value(var.types, value, var.default)

    @staticmethod
    def get_value(data: Dict, field: ClassVar):
        """Find the field value in the given dictionary or return the default
        field value."""
        if field.qname.localname in data:
            value = data[field.qname.localname]
        elif field.name in data:
            value = data[field.name]
        else:
            return None

        if field.is_list and not isinstance(value, list):
            value = [value]

        return value
