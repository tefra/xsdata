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
from typing import Type
from typing import Union

from lxml.etree import QName

from xsdata.exceptions import ConverterError
from xsdata.exceptions import ConverterWarning
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.utils import text


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
        try:
            if ns_map is None or value[0] == "{":
                return QName(value)

            prefix, suffix = text.split(value.strip())
            return QName(ns_map.get(prefix), suffix)
        except ValueError:
            raise ConverterError()

    def to_string(
        self, value: QName, namespaces: Optional[Namespaces] = None, **kwargs: Any
    ) -> str:
        """
        Convert a QName instance to string either with a namespace prefix if
        context namespaces are provided or as fully qualified with the
        namespace uri.

        examples:
            - QName("http://www.w3.org/2001/XMLSchema", "int") & namespaces -> xs:int
            - QName("foo, "bar") -> {foo}bar
        """

        if namespaces is None:
            return value.text

        namespaces.add(value.namespace)
        prefix = namespaces.prefix(value.namespace)

        return f"{prefix}:{value.localname}" if prefix else value.localname


class EnumConverter(Converter):
    def from_string(
        self, value: str, data_type: Optional[Type[Enum]] = None, **kwargs: Any
    ) -> Enum:
        if data_type is None or not issubclass(data_type, Enum):
            raise ConverterError("Provide a target data type enum class.")

        # Convert string value to the type of the first enum member first, otherwise
        # more complex types like QName, Decimals will fail.
        enum_member: Enum = list(data_type)[0]
        real_value = converter.from_string(value, [type(enum_member.value)], **kwargs)

        try:
            try:
                return data_type(real_value)
            except ValueError:
                # enums may be derived from xs:NMTOKENS or xs:list
                # try again after removing excess whitespace.
                return data_type(" ".join(value.split()))
        except ValueError:
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
converter.register_converter(QName, QNameConverter())
converter.register_converter(Decimal, DecimalConverter())
converter.register_converter(type(Enum), EnumConverter())
