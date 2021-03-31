import json
import warnings
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from dataclasses import is_dataclass
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.exceptions import ConverterWarning
from xsdata.exceptions import ParserError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.utils.constants import EMPTY_MAP

ANY_KEYS = {f.name for f in fields(AnyElement)}
DERIVED_KEYS = {f.name for f in fields(DerivedElement)}


@dataclass
class JsonParser(AbstractParser):
    """
    Json parser for dataclasses.

    :param context: Model context provider
    :param load_factory: Replace the default json.load call with another implementation
    """

    context: XmlContext = field(default_factory=XmlContext)
    load_factory: Callable = field(default=json.load)

    def parse(self, source: Any, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input stream or filename and return the resulting object
        tree."""

        if not hasattr(source, "read"):
            with open(source, "rb") as fp:
                ctx = self.load_factory(fp)
        else:
            ctx = self.load_factory(source)

        if clazz is None:
            clazz = self.context.find_type_by_fields(set(ctx.keys()))

        if clazz is None:
            raise ParserError(
                f"No class found matching the document keys({list(ctx.keys())})"
            )

        return self.bind_dataclass(ctx, clazz)

    def bind_value(self, var: XmlVar, value: Any) -> Any:
        """Bind value according to the class var."""

        if var.attributes:
            return dict(value)

        if var.is_clazz_union:
            if isinstance(value, dict):
                return self.bind_dataclass_union(value, var)

            return self.bind_type_union(value, var)

        if var.clazz:
            return self.bind_dataclass(value, var.clazz)

        if var.elements:
            return self.bind_choice(value, var)

        if var.wildcard or var.any_type:
            return self.bind_wildcard(value)

        return self.parse_value(value, var.types, var.default, var.tokens, var.format)

    def bind_dataclass(self, data: Dict, clazz: Type[T]) -> T:
        """Recursively build the given model from the input dict data."""
        params = {}
        for var in self.context.build(clazz).vars:
            value = data.get(var.lname)

            if value is None or not var.init:
                continue

            if var.list_element:
                if not isinstance(value, list):
                    raise ParserError(f"Key `{var.name}` value is not iterable")

                params[var.name] = [self.bind_value(var, val) for val in value]
            else:
                params[var.name] = self.bind_value(var, value)

        return clazz(**params)  # type: ignore

    def maybe_bind_dataclass(self, data: Dict, clazz: Type[T]) -> Optional[T]:
        """Recursively build the given model from the input dict data but fail
        on any converter warnings."""
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=ConverterWarning)
                return self.bind_dataclass(data, clazz)
        except ConverterWarning:
            return None

    def bind_dataclass_union(self, value: Dict, var: XmlVar) -> Any:
        """Bind data to all possible models and return the best candidate."""
        obj = None
        max_score = -1.0
        for clazz in var.types:
            if not is_dataclass(clazz):
                continue

            candidate = self.maybe_bind_dataclass(value, clazz)
            score = ParserUtils.score_object(candidate)
            if score > max_score:
                max_score = score
                obj = candidate

        return obj

    def bind_type_union(self, value: Any, var: XmlVar) -> Any:
        types = [tp for tp in var.types if not is_dataclass(tp)]
        return self.parse_value(value, types, var.default, var.tokens, var.format)

    def bind_wildcard(self, value: Any) -> Any:
        """Bind data to a wildcard model."""
        if isinstance(value, Dict):
            keys = set(value.keys())

            if not (keys - ANY_KEYS):
                return self.bind_dataclass(value, AnyElement)

            if not (keys - DERIVED_KEYS):
                return self.bind_dataclass(value, DerivedElement)

            clazz: Optional[Type] = self.context.find_type_by_fields(keys)
            if clazz:
                return self.bind_dataclass(value, clazz)

        return value

    def bind_choice(self, value: Any, var: XmlVar) -> Any:
        """Bind data to one of the choice models."""
        if not isinstance(value, dict):
            return self.bind_choice_simple(value, var)

        if "qname" in value:
            return self.bind_choice_generic(value, var)

        return self.bind_choice_dataclass(value, var)

    def bind_choice_simple(self, value: Any, var: XmlVar) -> Any:
        """Bind data to one of the simple choice types and return the first
        that succeeds."""
        choice = var.find_value_choice(value)
        if choice:
            return self.bind_value(choice, value)

        # Sometimes exact type match doesn't work, eg Decimals, try all of them
        is_list = isinstance(value, list)
        for choice in var.choices:
            if choice.dataclass or choice.tokens != is_list:
                continue

            with warnings.catch_warnings(record=True) as w:
                result = self.bind_value(choice, value)
                if not w:
                    return result

        return value

    def bind_choice_generic(self, value: Dict, var: XmlVar) -> Any:
        """Bind data to a either a derived or a user derived model."""
        qname = value["qname"]
        choice = var.find_choice(qname)

        if not choice:
            raise ParserError(
                f"XmlElements undefined choice: `{var.name}` for qname `{qname}`"
            )

        if "value" in value:
            obj = self.bind_value(choice, value["value"])
            substituted = value.get("substituted", False)

            return DerivedElement(qname=qname, value=obj, substituted=substituted)

        return self.bind_dataclass(value, AnyElement)

    def bind_choice_dataclass(self, value: Dict, var: XmlVar) -> Any:
        """Bind data to the best matching choice model."""
        keys = set(value.keys())
        for choice in var.choices:
            if choice.clazz:
                meta = self.context.build(choice.clazz)
                attrs = {var.lname for var in meta.vars}
                if attrs == keys:
                    return self.bind_value(choice, value)

        raise ParserError(f"XmlElements undefined choice: `{var.name}` for `{value}`")

    @classmethod
    def parse_value(
        cls,
        value: Any,
        types: List[Type],
        default: Any,
        tokens: bool,
        fmt: Optional[str],
    ) -> Any:
        """Convert any value to one of the given var types."""
        return ParserUtils.parse_value(value, types, default, EMPTY_MAP, tokens, fmt)


@dataclass
class DictConverter(JsonParser):
    def convert(self, data: Dict, clazz: Type[T]) -> T:
        return self.bind_dataclass(data, clazz)
