import io
import json
import pathlib
import warnings
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from typing import Any
from typing import Dict
from typing import Optional
from typing import Type

from xsdata.exceptions import ParserError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.utils.constants import EMPTY_MAP


@dataclass
class JsonParser(AbstractParser):
    """
    Json parsing and binding for dataclasses.

    :param context: Model metadata builder
    """

    context: XmlContext = field(default_factory=XmlContext)

    def from_path(self, path: pathlib.Path, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input file path and return the resulting object tree."""
        return self.from_bytes(path.read_bytes(), clazz)

    def parse(self, source: io.BytesIO, clazz: Optional[Type[T]] = None) -> T:
        """Parse the JSON input stream and return the resulting object tree."""
        ctx = json.load(source)

        if clazz is None:
            clazz = self.context.find_type_by_fields(set(ctx.keys()))

        if clazz is None:
            raise ParserError(
                f"No class found matching the document keys({list(ctx.keys())})"
            )

        return self.bind_dataclass(ctx, clazz)

    def bind_value(self, var: XmlVar, value: Any) -> Any:
        """Bind value according to the class var."""

        if var.is_attributes:
            return dict(value)

        if var.is_clazz_union:
            return self.bind_dataclass_union(value, var)

        if var.clazz:
            return self.bind_dataclass(value, var.clazz)

        if var.is_wildcard:
            return self.bind_wildcard(value)

        if var.is_elements:
            return self.bind_choice(value, var)

        return self.parse_value(value, var)

    def bind_dataclass(self, data: Dict, clazz: Type[T]) -> T:
        """
        Recursively build the given model from the input dict data.

        :raise ParserError: When parsing fails for any reason
        """
        params = {}
        for var in self.context.build(clazz).vars:
            value = self.get_value(data, var)

            if value is None or not var.init:
                continue

            if var.is_list:
                params[var.name] = [self.bind_value(var, val) for val in value]
            else:
                params[var.name] = self.bind_value(var, value)

        return clazz(**params)  # type: ignore

    def bind_dataclass_union(self, value: Dict, var: XmlVar) -> Any:
        obj = None
        max_score = -1.0
        for clazz in var.types:
            candidate = self.bind_dataclass(value, clazz)
            score = ParserUtils.score_object(candidate)
            if score > max_score:
                max_score = score
                obj = candidate

        return obj

    def bind_wildcard(self, value: Any) -> Any:
        return (
            value if isinstance(value, str) else self.bind_dataclass(value, AnyElement)
        )

    def bind_choice(self, value: Any, var: XmlVar) -> Any:
        if not isinstance(value, dict):
            return self.bind_choice_simple(value, var)

        if "qname" in value:
            return self.bind_choice_generic(value, var)

        return self.bind_choice_dataclass(value, var)

    def bind_choice_simple(self, value: Any, var: XmlVar) -> Any:
        orig_type = type(value)
        for choice in var.choices:
            if choice.dataclass:
                continue

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")

                result = self.bind_value(choice, value)
                if not isinstance(result, orig_type):
                    return result

        return value

    def bind_choice_generic(self, value: Dict, var: XmlVar) -> Any:
        qname = value["qname"]
        choice = var.find_choice(qname)

        if not choice:
            raise ParserError(
                f"XmlElements undefined choice: `{var.name}` for qname `{qname}`"
            )

        if "value" in value:
            return DerivedElement(qname, self.bind_value(choice, value["value"]))

        return self.bind_dataclass(value, AnyElement)

    def bind_choice_dataclass(self, value: Dict, var: XmlVar) -> Any:
        keys = set(value.keys())
        for choice in var.choices:
            if choice.clazz:
                attrs = {f.name for f in fields(choice.clazz)}
                if attrs == keys:
                    return self.bind_value(choice, value)

        raise ParserError(f"XmlElements undefined choice: `{var.name}` for `{value}`")

    @classmethod
    def parse_value(cls, value: Any, var: XmlVar) -> Any:
        return ParserUtils.parse_value(
            value, var.types, var.default, ns_map=EMPTY_MAP, tokens=var.tokens
        )

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
        return self.bind_dataclass(data, clazz)
