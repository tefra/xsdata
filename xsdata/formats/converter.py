import abc
import contextlib
import math
import warnings
from dataclasses import dataclass
from dataclasses import field
from decimal import Decimal
from decimal import InvalidOperation
from enum import Enum
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union
from xml.etree.ElementTree import QName

from lxml import etree

from xsdata.exceptions import ConverterError
from xsdata.exceptions import ConverterWarning
from xsdata.utils import text
from xsdata.utils.namespaces import load_prefix
from xsdata.utils.namespaces import split_qname


class Converter(metaclass=abc.ABCMeta):
    """Abstract converter class."""

    @abc.abstractmethod
    def from_string(self, value: str, **kwargs: Any) -> Any:
        """
        Convert from string.

        :raises ConverterError: if converter fails with and expected ValueError
        """

    @abc.abstractmethod
    def to_string(self, value: Any, **kwargs: Any) -> str:
        """Convert to string."""


@dataclass
class ConverterAdapter:
    """
    :param registry: Converters registry
    """

    registry: Dict[Type, Converter] = field(default_factory=dict)

    def from_string(self, value: Any, types: List[Type], **kwargs: Any) -> Any:
        """
        Attempt to convert a string to one of the given types.

        If the input is not a string return the input value.
        If all attempts fail return the value input value and issue a warning.

        :return: The first successful converted value.
        """
        if not isinstance(value, str):
            return value

        for data_type in types:
            with contextlib.suppress(ConverterError):
                instance = self.type_converter(data_type)
                return instance.from_string(value, data_type=data_type, **kwargs)

        warnings.warn(
            f"Failed to convert value `{value}` to one of {types}", ConverterWarning
        )
        return value

    def to_string(self, value: Any, **kwargs: Any) -> Any:
        """
        Convert the given value to string, ignore None values.

        If the value is a list assume the value is a list of tokens.
        """
        if value is None:
            return None

        if isinstance(value, list):
            return " ".join([self.to_string(val, **kwargs) for val in value])

        instance = self.value_converter(value)
        return instance.to_string(value, **kwargs)

    def register_converter(self, data_type: Type, func: Union[Callable, Converter]):
        """
        Register a callable or converter for the given data type.

        Callables will be wrapped in a
        :class:`xsdata.formats.converter.ProxyConverter`
        """
        if isinstance(func, Converter):
            self.registry[data_type] = func
        else:
            self.registry[data_type] = ProxyConverter(func)

    def unregister_converter(self, data_type: Type):
        """
        Unregister the converter for the given data type.

        :raises KeyError: if the data type is not registered.
        """
        self.registry.pop(data_type)

    def type_converter(self, data_type: Type) -> Converter:
        """
        Get a suitable converter for given data type.

        Try the parent type if the original doesn't exist, fall back to
        str and issue a warning if no converter matches.
        """
        try:
            return self.registry[data_type]
        except KeyError:
            pass

        try:
            return self.registry[type(data_type)]
        except KeyError:
            pass

        warnings.warn(f"No converter registered for `{data_type}`", ConverterWarning)
        return self.registry[str]

    def value_converter(self, value: Any) -> Converter:
        """Get a suitable converter for the given value."""
        return self.type_converter(type(value))

    @classmethod
    def sort_types(cls, types: List[Type]) -> List[Type]:
        """Sort a list of types by giving priority to strict types first."""
        in_order = (bool, int, float, Decimal, str)

        sorted_types = []
        for ordered in in_order:
            if ordered in types:
                types.remove(ordered)
                sorted_types.append(ordered)

        types.extend(sorted_types)
        return types


class BoolConverter(Converter):
    def from_string(self, value: str, **kwargs: Any) -> bool:
        val = value.strip()

        if val in ("true", "1"):
            return True

        if val in ("false", "0"):
            return False

        raise ConverterError(f"Invalid bool literal '{value}'")

    def to_string(self, value: bool, **kwargs: Any) -> str:
        return "true" if value else "false"


class IntConverter(Converter):
    def from_string(self, value: str, **kwargs: Any) -> int:
        try:
            return int(value)
        except ValueError:
            raise ConverterError()

    def to_string(self, value: int, **kwargs: Any) -> str:
        return str(value)


class StrConverter(Converter):
    def from_string(self, value: str, **kwargs: Any) -> str:
        return value

    def to_string(self, value: str, **kwargs: Any) -> str:
        return value


class FloatConverter(Converter):
    def from_string(self, value: str, **kwargs: Any) -> float:
        try:
            return float(value)
        except ValueError:
            raise ConverterError()

    def to_string(self, value: float, **kwargs: Any) -> str:
        return "NaN" if math.isnan(value) else str(value).upper()


class DecimalConverter(Converter):
    def from_string(self, value: str, **kwargs: Any) -> Decimal:
        try:
            return Decimal(value)
        except InvalidOperation:
            raise ConverterError()

    def to_string(self, value: Decimal, **kwargs: Any) -> str:
        if value.is_infinite():
            return str(value).replace("Infinity", "INF")

        return str(value)


class QNameConverter(Converter):
    def from_string(
        self, value: str, ns_map: Optional[Dict] = None, **kwargs: Any
    ) -> QName:
        """
        Convert namespace prefixed strings, or fully qualified strings to
        QNames.

        examples:
            - xs:string -> QName("http://www.w3.org/2001/XMLSchema", "string")
            - {foo}bar -> QName("foo", "bar"
        """

        text_or_uri, tag = self.resolve(value, ns_map)

        if text_or_uri:
            return QName(text_or_uri, tag)

        return QName(tag)

    def to_string(
        self, value: QName, ns_map: Optional[Dict] = None, **kwargs: Any
    ) -> str:
        """
        Convert a QName instance to string either with a namespace prefix if a
        prefix-URI namespaces mapping is provided or to a fully qualified name
        with the namespace.

        examples:
            - QName("http://www.w3.org/2001/XMLSchema", "int") & ns_map -> xs:int
            - QName("foo, "bar") -> {foo}bar
        """

        if ns_map is None:
            return value.text

        namespace, tag = split_qname(value.text)

        if not namespace:
            return tag

        prefix = load_prefix(namespace, ns_map)

        return f"{prefix}:{tag}" if prefix else tag

    @staticmethod
    def resolve(value: str, ns_map: Optional[Dict]) -> Tuple:
        if not value:
            raise ConverterError("Invalid QName")

        if value[0] == "{":
            return value, None

        if ns_map is None:
            raise ConverterError("QName converter needs ns_map to support prefixes")

        prefix, suffix = text.split(value.strip())
        namespace = ns_map.get(prefix)

        if prefix and not namespace:
            raise ConverterError(f"Unknown namespace prefix: `{prefix}`")

        return namespace, suffix


class LxmlQNameConverter(Converter):
    def from_string(
        self, value: str, ns_map: Optional[Dict] = None, **kwargs: Any
    ) -> etree.QName:
        """
        Convert namespace prefixed strings, or fully qualified strings to
        QNames.

        examples:
            - xs:string -> QName("http://www.w3.org/2001/XMLSchema", "string")
            - {foo}bar -> QName("foo", "bar"
        """
        try:

            text_or_uri, tag = QNameConverter.resolve(value, ns_map)
            return etree.QName(text_or_uri, tag)
        except ValueError:
            raise ConverterError()

    def to_string(
        self, value: etree.QName, ns_map: Optional[Dict] = None, **kwargs: Any
    ) -> str:
        """
        Convert a QName instance to string either with a namespace prefix if a
        prefix-URI namespaces mapping is provided or to a fully qualified name
        with the namespace.

        examples:
            - QName("http://www.w3.org/2001/XMLSchema", "int") & ns_map -> xs:int
            - QName("foo, "bar") -> {foo}bar
        """

        if ns_map is None or not value.namespace:
            return value.text

        prefix = load_prefix(value.namespace, ns_map)
        return f"{prefix}:{value.localname}" if prefix else value.localname


class EnumConverter(Converter):
    def from_string(
        self, value: str, data_type: Optional[Type[Enum]] = None, **kwargs: Any
    ) -> Enum:
        if data_type is None or not issubclass(data_type, Enum):
            raise ConverterError("Provide a target data type enum class.")

        # Convert string value to the type of the first enum member first, otherwise
        # more complex types like QName, Decimals will fail.
        member: Enum = list(data_type)[0]
        value_type = type(member.value)

        # Suppress warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            real_value = converter.from_string(value, [value_type], **kwargs)

        # Raise exception if the real value doesn't match the expected type.
        if not isinstance(real_value, value_type):
            raise ConverterError()

        # Attempt #1 use the enum constructor
        with contextlib.suppress(ValueError):
            return data_type(real_value)

        try:
            # Attempt #2 the enum might be derived from
            # xs:NMTOKENS or xs:list removing excess whitespace.
            if isinstance(real_value, str):
                return data_type(" ".join(value.split()))

            # Attempt #3 some values are never equal try to match
            # canonical representations.
            repr_value = repr(real_value)
            return next(x for x in data_type if repr(x.value) == repr_value)
        except (ValueError, StopIteration):
            raise ConverterError()

    def to_string(self, value: Enum, **kwargs: Any) -> str:
        return converter.to_string(value.value, **kwargs)


@dataclass
class ProxyConverter(Converter):
    """
    :param func: the callable to convert from string
    """

    func: Callable

    def from_string(self, value: str, **kwargs: Any) -> Any:
        try:
            return self.func(value)
        except ValueError:
            raise ConverterError

    def to_string(self, value: Any, **kwargs: Any) -> str:
        return str(value)


converter = ConverterAdapter()
converter.register_converter(str, StrConverter())
converter.register_converter(int, IntConverter())
converter.register_converter(bool, BoolConverter())
converter.register_converter(float, FloatConverter())
converter.register_converter(object, StrConverter())
converter.register_converter(etree.QName, LxmlQNameConverter())
converter.register_converter(QName, QNameConverter())
converter.register_converter(Decimal, DecimalConverter())
converter.register_converter(type(Enum), EnumConverter())
