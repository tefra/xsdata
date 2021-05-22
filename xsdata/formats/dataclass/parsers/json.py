import json
import warnings
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from dataclasses import is_dataclass
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Sequence
from typing import Type
from typing import Union

from xsdata.exceptions import ConverterWarning
from xsdata.exceptions import ParserError
from xsdata.formats.bindings import AbstractParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.formats.dataclass.typing import get_args
from xsdata.formats.dataclass.typing import get_origin
from xsdata.utils.constants import EMPTY_MAP

ANY_KEYS = {f.name for f in fields(AnyElement)}
DERIVED_KEYS = {f.name for f in fields(DerivedElement)}


@dataclass
class JsonParser(AbstractParser):
    """
    Json parser for dataclasses.

    :param config: Parser configuration
    :param context: Model context provider
    :param load_factory: Replace the default json.load call with another implementation
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    context: XmlContext = field(default_factory=XmlContext)
    load_factory: Callable = field(default=json.load)

    def parse(self, source: Any, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input stream or filename and return the resulting object
        tree."""

        data = self.load_json(source)
        tp = self.verify_type(clazz, data)

        if isinstance(data, list):
            return [self.bind_dataclass(obj, tp) for obj in data]  # type: ignore

        return self.bind_dataclass(data, tp)

    def load_json(self, source: Any) -> Union[Dict, List]:
        if not hasattr(source, "read"):
            with open(source, "rb") as fp:
                return self.load_factory(fp)

        return self.load_factory(source)

    def verify_type(self, clazz: Optional[Type[T]], data: Union[Dict, List]) -> Type[T]:
        if clazz is None:
            return self.detect_type(data)

        try:
            origin = get_origin(clazz)
            list_type = False
            if origin is List:
                list_type = True
                args = get_args(clazz)

                if len(args) != 1 or not is_dataclass(args[0]):
                    raise TypeError()

                clazz = args[0]
            elif origin is not None:
                raise TypeError()
        except TypeError:
            raise ParserError(f"Invalid clazz argument: {clazz}")

        if list_type != isinstance(data, list):
            if list_type:
                raise ParserError("Document is object, expected array")
            else:
                raise ParserError("Document is array, expected object")

        return clazz  # type: ignore

    def detect_type(self, data: Union[Dict, List]) -> Type[T]:
        if not data:
            raise ParserError("Document is empty, can not detect type")

        keys = data[0].keys() if isinstance(data, list) else data.keys()
        clazz: Optional[Type[T]] = self.context.find_type_by_fields(set(keys))

        if clazz:
            return clazz

        raise ParserError(f"Unable to locate model with properties({list(keys)})")

    def bind_dataclass(self, data: Dict, clazz: Type[T]) -> T:
        """Recursively build the given model from the input dict data."""

        if set(data.keys()) == DERIVED_KEYS:
            return self.bind_derived_dataclass(data, clazz)

        meta = self.context.build(clazz)
        xml_vars = meta.get_all_vars()

        params = {}
        for key, value in data.items():
            is_list = isinstance(value, list)
            var = self.find_var(xml_vars, key, is_list)

            if var is None and self.config.fail_on_unknown_properties:
                raise ParserError(f"Unknown property {clazz.__qualname__}.{key}")

            if var and var.init:
                params[var.name] = self.bind_value(meta, var, value)

        try:
            return clazz(**params)  # type: ignore
        except TypeError as e:
            raise ParserError(e)

    def bind_derived_dataclass(self, data: Dict, clazz: Type[T]) -> Any:
        qname = data["qname"]
        xsi_type = data["type"]
        params = data["value"]

        if clazz is DerivedElement:
            real_clazz: Optional[Type[T]] = None
            if xsi_type:
                real_clazz = self.context.find_type(xsi_type)

            if real_clazz is None:
                raise ParserError(
                    f"Unable to locate derived model "
                    f"with properties({list(params.keys())})"
                )

            value = self.bind_dataclass(params, real_clazz)
        else:
            value = self.bind_dataclass(params, clazz)

        return DerivedElement(qname=qname, type=xsi_type, value=value)

    def bind_best_dataclass(self, data: Dict, classes: Iterable[Type[T]]) -> T:
        """Attempt to bind the given data to one possible models, if more than
        one is successful return the object with the highest score."""
        obj = None
        keys = set(data.keys())
        max_score = -1.0
        for clazz in classes:
            if is_dataclass(clazz) and self.context.local_names_match(keys, clazz):
                candidate = self.bind_optional_dataclass(data, clazz)
                score = ParserUtils.score_object(candidate)
                if score > max_score:
                    max_score = score
                    obj = candidate

        if obj:
            return obj

        raise ParserError(
            f"Failed to bind object with properties({list(data.keys())}) "
            f"to any of the {[cls.__qualname__ for cls in classes]}"
        )

    def bind_optional_dataclass(self, data: Dict, clazz: Type[T]) -> Optional[T]:
        """Recursively build the given model from the input dict data but fail
        on any converter warnings."""
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=ConverterWarning)
                return self.bind_dataclass(data, clazz)
        except Exception:
            return None

    def bind_value(
        self, meta: XmlMeta, var: XmlVar, value: Any, recursive: bool = False
    ) -> Any:
        """Main entry point for binding values."""

        # xs:anyAttributes get it out of the way, it's the mapping exception!
        if var.is_attributes:
            return dict(value)

        # Repeating element, recursively bind the values
        if not recursive and var.list_element and isinstance(value, list):
            return [self.bind_value(meta, var, val, True) for val in value]

        # If not dict this is an text or tokens value.
        if not isinstance(value, dict):
            return self.bind_text(meta, var, value)

        keys = value.keys()
        if keys == ANY_KEYS:
            # Bind data to AnyElement dataclass
            return self.bind_dataclass(value, AnyElement)

        if keys == DERIVED_KEYS:
            # Bind data to AnyElement dataclass
            return self.bind_derived_value(meta, var, value)

        # Bind data to a user defined dataclass
        return self.bind_complex_type(meta, var, value)

    def bind_text(self, meta: XmlMeta, var: XmlVar, value: Any) -> Any:
        """Bind text/tokens value entrypoint."""

        if var.elements:
            # Compound field we need to match the value to one of the choice elements
            choice = var.find_value_choice(value)
            if choice:
                return self.bind_text(meta, choice, value)

            raise ParserError(
                f"Failed to bind '{value}' "
                f"to {meta.clazz.__qualname__}.{var.name} field"
            )

        if var.any_type or var.is_wildcard:
            # field can support any object return the value as it is
            return value

        # Convert value according to the field types
        return ParserUtils.parse_value(
            value, var.types, var.default, EMPTY_MAP, var.tokens, var.format
        )

    def bind_complex_type(self, meta: XmlMeta, var: XmlVar, data: Dict) -> Any:
        """Bind data to a user defined dataclass."""

        if var.is_clazz_union:
            # Union of dataclasses
            return self.bind_best_dataclass(data, var.types)
        elif var.elements:
            # Compound field with multiple choices
            return self.bind_best_dataclass(data, var.element_types)
        elif var.any_type or var.is_wildcard:
            # xs:anyType element, check all meta classes
            return self.bind_best_dataclass(data, meta.element_types)
        else:
            return self.bind_dataclass(data, var.clazz)

    def bind_derived_value(
        self, meta: XmlMeta, var: XmlVar, data: Dict
    ) -> DerivedElement:
        """Bind derived element entry point."""

        qname = data["qname"]
        xsi_type = data["type"]
        params = data["value"]

        if var.elements:
            choice = var.find_choice(qname)
            if choice is None:
                raise ParserError(
                    f"Unable to locate compound element"
                    f" {meta.clazz.__qualname__}.{var.name}[{qname}]"
                )
            return self.bind_derived_value(meta, choice, data)

        if not isinstance(params, dict):
            value = self.bind_text(meta, var, params)
        elif var.clazz:
            value = self.bind_complex_type(meta, var, params)
        elif xsi_type:
            clazz: Optional[Type] = self.context.find_type(xsi_type)

            if clazz is None:
                raise ParserError(f"Unable to locate xsi:type `{xsi_type}`")

            value = self.bind_dataclass(params, clazz)
        else:
            value = self.bind_best_dataclass(params, meta.element_types)

        return DerivedElement(qname=qname, value=value, type=xsi_type)

    @classmethod
    def find_var(
        cls, xml_vars: Sequence[XmlVar], local_name: str, is_list: bool = False
    ) -> Optional[XmlVar]:
        for var in xml_vars:
            if var.local_name == local_name:
                var_is_list = var.list_element or var.tokens
                if is_list == var_is_list or var.clazz is None:
                    return var

        return None


@dataclass
class DictConverter(JsonParser):
    def convert(self, data: Dict, clazz: Type[T]) -> T:
        return self.bind_dataclass(data, clazz)
