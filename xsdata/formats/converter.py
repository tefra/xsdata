import abc
import base64
import binascii
import math
import warnings
from datetime import date, datetime, time
from decimal import Decimal, InvalidOperation
from enum import Enum, EnumMeta
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)
from xml.etree.ElementTree import QName

from xsdata.exceptions import ConverterError, ConverterWarning
from xsdata.models.datatype import (
    XmlBase64Binary,
    XmlDate,
    XmlDateTime,
    XmlDuration,
    XmlHexBinary,
    XmlPeriod,
    XmlTime,
)
from xsdata.utils import collections, namespaces, text


class Converter(abc.ABC):
    """Abstract converter class."""

    @abc.abstractmethod
    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """Convert a value to a python type.

        Args:
            value: The input value
            **kwargs: Additional keyword arguments needed per converter

        Returns:
            The converted value.

        Raises:
            ConverterError: if the value can't be converted.
        """

    @abc.abstractmethod
    def serialize(self, value: Any, **kwargs: Any) -> str:
        """Convert value to string for serialization.

        Args:
            value: The input value
            **kwargs: Additional keyword arguments needed per converter

        Returns:
            The converted string value.
        """

    @classmethod
    def validate_input_type(cls, value: Any, tp: Type):
        """Validate the input value type matches the required type."""
        if not isinstance(value, tp):
            raise ConverterError(
                f"Input value must be '{tp.__name__}' got '{type(value).__name__}'"
            )


class ConverterFactory:
    """Converter factory class.

    Attributes:
        registry: The registered converters
    """

    __slots__ = "registry"

    def __init__(self):
        self.registry: Dict[Type, Converter] = {}

    def deserialize(self, value: Any, types: Sequence[Type], **kwargs: Any) -> Any:
        """Attempt to convert any value to one of the given types.

        If all attempts fail return the value input value and emit a
        warning.

        Args:
            value: The input value
            types: The target candidate types
            **kwargs: Additional keyword arguments needed per converter

        Returns:
            The converted value or the input value.
        """
        for data_type in types:
            try:
                instance = self.type_converter(data_type)
                return instance.deserialize(value, data_type=data_type, **kwargs)
            except ConverterError:
                pass

        warnings.warn(
            f"Failed to convert value `{value}` to one of {types}", ConverterWarning
        )
        return value

    def serialize(self, value: Any, **kwargs: Any) -> Any:
        """Convert the given value to string.

        If the value is a list assume the value is a list of tokens.

        Args:
            value: The input value
            **kwargs: Additional keyword arguments needed per converter

        Returns:
            The converted string value or None if the input value is None.

        """
        if value is None:
            return None

        if isinstance(value, list):
            return " ".join(self.serialize(val, **kwargs) for val in value)

        instance = self.value_converter(value)
        return instance.serialize(value, **kwargs)

    def test(
        self,
        value: Optional[str],
        types: Sequence[Type],
        strict: bool = False,
        **kwargs: Any,
    ) -> bool:
        """Test the given string value can be converted to one of the given types.

        Args:
            value: The input value
            types: The candidate target types
            strict: validate the string output also matches the original input
            **kwargs: Additional keyword arguments needed per converter

        Returns:
            The bool result.
        """
        if not isinstance(value, str):
            return False

        with warnings.catch_warnings(record=True) as w:
            decoded = self.deserialize(value, types, **kwargs)

        if w and w[-1].category is ConverterWarning:
            return False

        if strict and isinstance(decoded, (float, int, Decimal, XmlPeriod)):
            encoded = self.serialize(decoded, **kwargs)
            return value.strip() == encoded

        return True

    def register_converter(self, data_type: Type, func: Union[Callable, Converter]):
        """Register a callable or converter for the given data type.

        Args:
            data_type: The data type
            func: The callable or converter instance
        """
        if isinstance(func, Converter):
            self.registry[data_type] = func
        else:
            self.registry[data_type] = ProxyConverter(func)

    def unregister_converter(self, data_type: Type):
        """Unregister the converter for the given data type.

        Args:
            data_type: The data type

        Raises:
            KeyError: if the data type is not registered.
        """
        self.registry.pop(data_type)

    def type_converter(self, data_type: Type) -> Converter:
        """Find a suitable converter for given data type.

        Iterate over all but last mro items and check for registered
        converters, fall back to str and issue a warning if there are
        no matches.

        Args:
            data_type: The data type

        Returns:
            A converter instance
        """
        try:
            # Quick in and out, without checking the whole mro.
            return self.registry[data_type]
        except KeyError:
            pass

        # We tested the first, ignore the object
        for mro in data_type.__mro__[1:-1]:
            if mro in self.registry:
                return self.registry[mro]

        warnings.warn(f"No converter registered for `{data_type}`", ConverterWarning)
        return self.registry[str]

    def value_converter(self, value: Any) -> Converter:
        """Get a suitable converter for the given value."""
        return self.type_converter(value.__class__)

    @classmethod
    def sort_types(cls, types: Sequence[Type]) -> List[Type]:
        """Sort a list of types by giving priority to strict types first."""
        if len(types) < 2:
            return list(types)

        return sorted(types, key=lambda x: __PYTHON_TYPES_SORTED__.get(x, 0))

    @classmethod
    def explicit_types(cls) -> Tuple[Type, ...]:
        """Get a list of types that need strict test."""
        return __EXPLICIT_TYPES__


__PYTHON_TYPES_SORTED__ = {
    int: 1,
    bool: 2,
    float: 3,
    Decimal: 4,
    datetime: 5,
    date: 6,
    time: 7,
    XmlTime: 8,
    XmlDate: 9,
    XmlDateTime: 10,
    XmlDuration: 11,
    XmlPeriod: 12,
    QName: 13,
    str: 14,
}

__EXPLICIT_TYPES__ = (
    int,
    bool,
    float,
    Decimal,
    XmlTime,
    XmlDate,
    XmlDateTime,
    XmlDuration,
    XmlPeriod,
)


class StringConverter(Converter):
    """A str converter."""

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """Convert a value to string."""
        return value if isinstance(value, str) else str(value)

    def serialize(self, value: Any, **kwargs: Any) -> str:
        """Convert a value to string."""
        return value if isinstance(value, str) else str(value)


class BoolConverter(Converter):
    """A bool converter."""

    def deserialize(self, value: Any, **kwargs: Any) -> bool:
        """Convert a value to bool.

        Args:
            value: The input value
            **kwargs: Unused keyword arguments

        Returns:
            True if the value is in (True, "true", "1")
            False if the value is in (False, "false", "0")

        Raises:
            ConverterError: if the value can't be converted to bool.
        """
        if isinstance(value, str):
            val = value.strip()

            if val in ("true", "1"):
                return True

            if val in ("false", "0"):
                return False

            raise ConverterError(f"Invalid bool literal '{value}'")

        if value is True or value is False:
            return value

        raise ConverterError(f"Invalid bool literal '{value}'")

    def serialize(self, value: bool, **kwargs: Any) -> str:
        """Convert a bool value to string.

        Args:
            value: The input bool value
            **kwargs: Unused keyword arguments

        Returns:
            "true" or "false"
        """
        return "true" if value else "false"


class IntConverter(Converter):
    """An int converter."""

    def deserialize(self, value: Any, **kwargs: Any) -> int:
        """Convert a value to int.

        Args:
            value: The input value
            **kwargs: Unused keyword arguments

        Returns:
            The int converted value.

        Raises:
            ConverterError: on value or type errors.
        """
        try:
            return int(value)
        except (ValueError, TypeError) as e:
            raise ConverterError(e)

    def serialize(self, value: int, **kwargs: Any) -> str:
        """Convert an int value sto string.

        Args:
            value: The input int value
            **kwargs: Unused keyword arguments

        Returns:
            The str converted value.
        """
        return str(value)


class FloatConverter(Converter):
    """A float converter."""

    INF = float("inf")

    def deserialize(self, value: Any, **kwargs: Any) -> float:
        """Convert a value to float.

        Args:
            value: The input value
            **kwargs: Unused keyword arguments

        Returns:
            The float converted value.

        Raises:
            ConverterError: on value errors.
        """
        try:
            return float(value)
        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: float, **kwargs: Any) -> str:
        """Convert a float value sto string.

        Args:
            value: The input int value
            **kwargs: Unused keyword arguments

        Returns:
            The str converted value.
        """
        if math.isnan(value):
            return "NaN"

        if value == self.INF:
            return "INF"

        if value == -self.INF:
            return "-INF"

        return repr(value).upper().replace("E+", "E")


class BytesConverter(Converter):
    """A bytes converter for base16 and base64 formats."""

    def deserialize(self, value: Any, **kwargs: Any) -> bytes:
        """Convert a string value to base16 or base64 format.

        Args:
            value: The input string value
            **kwargs: Additional keyword arguments
                format: The target output format (base16|base64)

        Returns:
            The bytes converted value.

        Raises:
            ConverterError: If format is empty or not supported or the value
                contains invalid characters.
        """
        self.validate_input_type(value, str)

        try:
            fmt = kwargs.get("format")

            if fmt == "base16":
                return binascii.unhexlify(value)

            if fmt == "base64":
                return base64.b64decode(value, validate=True)

            raise ConverterError(f"Unknown format '{fmt}'")
        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: bytes, **kwargs: Any) -> str:
        """Convert a bytes value sto string.

        Args:
            value: The input bytes value
            **kwargs: Additional keyword arguments
                format: The input value format (base16|base64)

        Returns:
            The str converted value.

        Raises:
            ConverterError: If format doesn't match the value type or
                it's not supported.
        """
        fmt = kwargs.get("format")

        if isinstance(value, XmlHexBinary) or fmt == "base16":
            return base64.b16encode(value).decode()

        if isinstance(value, XmlBase64Binary) or fmt == "base64":
            return base64.b64encode(value).decode()

        raise ConverterError(f"Unknown format '{fmt}'")


class DecimalConverter(Converter):
    """A decimal converter."""

    def deserialize(self, value: Any, **kwargs: Any) -> Decimal:
        """Convert a value to decimal.

        Args:
            value: The input value
            **kwargs: Unused keyword arguments

        Returns:
            The decimal converted value.

        Raises:
            ConverterError: on InvalidOperation errors.
        """
        try:
            return Decimal(value)
        except InvalidOperation:
            raise ConverterError()

    def serialize(self, value: Decimal, **kwargs: Any) -> str:
        """Convert a decimal value sto string.

        Args:
            value: The input decimal value
            **kwargs: Unused keyword arguments

        Returns:
            The str converted value.
        """
        if value.is_infinite():
            return str(value).replace("Infinity", "INF")

        return f"{value:f}"


class QNameConverter(Converter):
    """A QName converter."""

    def deserialize(
        self,
        value: str,
        ns_map: Optional[Dict] = None,
        **kwargs: Any,
    ) -> QName:
        """Convert a string value to QName instance.

        The method supports strings with namespace prefixes
        or fully namespace qualified strings.

        Examples:
            - xs:string -> QName("http://www.w3.org/2001/XMLSchema", "string")
            - {foo}bar -> QName("foo", "bar"

        Args:
            value: The input str value
            ns_map: A namespace prefix-URI map
            **kwargs: Unused keyword arguments

        Returns:
            A QName instance

        Raises:
            ConverterError: If the prefix can't be resolved.
        """
        self.validate_input_type(value, str)
        namespace, tag = self.resolve(value, ns_map)

        return QName(namespace, tag) if namespace else QName(tag)

    def serialize(
        self,
        value: QName,
        ns_map: Optional[Dict] = None,
        **kwargs: Any,
    ) -> str:
        """Convert a QName instance value sto string.

        Convert a QName instance to string either with a namespace prefix if a
        prefix-URI namespaces mapping is provided or to a fully qualified name
        with the namespace.

        Examples:
            - QName("http://www.w3.org/2001/XMLSchema", "int") & ns_map -> xs:int
            - QName("foo, "bar") -> {foo}bar

        Args:
            value: The qname instance to convert
            ns_map: A namespace prefix-URI map, if we want to use prefixes
            **kwargs: Unused keyword arguments

        Returns:
            The str converted value.
        """
        if ns_map is None:
            return value.text

        namespace, tag = namespaces.split_qname(value.text)

        if not namespace:
            return tag

        prefix = namespaces.load_prefix(namespace, ns_map)

        return f"{prefix}:{tag}" if prefix else tag

    @staticmethod
    def resolve(value: str, ns_map: Optional[Dict] = None) -> Tuple[str, str]:
        """Split a qname or ns prefixed string value or a uri, name pair.

        Args:
            value: the input value to resolve
            ns_map: A namespace prefix-URI map

        Returns:
            A tuple of uri and name strings.

        Raises:
            ConverterError: if the uri is not valid,
                if the prefix can't be resolved to a URI,
                if the name is not a valid NCName
        """
        value = value.strip()

        if not value:
            raise ConverterError()

        if value[0] == "{":
            uri, name = text.split(value[1:], "}")

            if not namespaces.is_uri(uri):
                raise ConverterError()
        else:
            prefix, name = text.split(value, ":")
            uri = ns_map.get(prefix) if ns_map else None
            if prefix and not uri:
                raise ConverterError(f"Unknown namespace prefix: `{prefix}`")

        if " " in name or not namespaces.is_ncname(name):
            raise ConverterError()

        return uri, name


class EnumConverter(Converter):
    """An enum converter."""

    def serialize(self, value: Enum, **kwargs: Any) -> str:
        """Convert an enum member to a string."""
        return converter.serialize(value.value, **kwargs)

    def deserialize(
        self,
        value: Any,
        data_type: Optional[EnumMeta] = None,
        **kwargs: Any,
    ) -> Enum:
        """Convert a value to an enum member.

        Args:
            value: The input value
            data_type: The enumeration class
            **kwargs: Additional keyword arguments needed
                for parsing the value to a python type.

        Returns:
            The enum member.

        Raises:
            ConverterError: if the data type is not an enum, or the value
                doesn't match any of the enum members.
        """
        if data_type is None or not isinstance(data_type, EnumMeta):
            raise ConverterError(f"'{data_type}' is not an enum")

        if collections.is_array(value):
            values = value
        elif isinstance(value, str):
            value = value.strip()
            values = value.split()
        else:
            values = [value]

        length = len(values)
        for member in cast(Type[Enum], data_type):
            if self.match(value, values, length, member.value, **kwargs):
                return member

        raise ConverterError()

    @classmethod
    def match(
        cls,
        value: Any,
        values: Sequence,
        length: int,
        real: Any,
        **kwargs: Any,
    ) -> bool:
        """Match a value to one of the enumeration values.

        Args:
            value: The input value
            values: The input value as a sequence, in case of NMTokens
            length: The length of the sequence values
            real: The enumeration value
            **kwargs: Additional keyword arguments needed
                for parsing the value to a python type.

        Returns:
            Whether the value or values matches the enumeration member value.
        """
        if isinstance(value, str) and isinstance(real, str):
            return value == real or " ".join(values) == real

        if isinstance(real, (tuple, list)) and not hasattr(real, "_fields"):
            if len(real) == length and cls._match_list(values, real, **kwargs):
                return True
        elif length == 1 and cls._match_atomic(value, real, **kwargs):
            return True

        return False

    @classmethod
    def _match_list(cls, raw: Sequence, real: Sequence, **kwargs: Any) -> bool:
        for index, val in enumerate(real):
            if not cls._match_atomic(raw[index], val, **kwargs):
                return False

        return True

    @classmethod
    def _match_atomic(cls, raw: Any, real: Any, **kwargs: Any) -> bool:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cmp = converter.deserialize(raw, [type(real)], **kwargs)

        if isinstance(real, float):
            return cmp == real or repr(cmp) == repr(real)

        return cmp == real


class DateTimeBase(Converter, metaclass=abc.ABCMeta):
    """An abstract datetime converter."""

    @classmethod
    def parse(cls, value: Any, **kwargs: Any) -> datetime:
        """Parse a str into a datetime instance.

        Args:
            value: The input string value
            **kwargs: Additional keyword argument
                format: The datetime format to use

        Returns:
            The datetime instance

        Raises:
            ConverterError: If no format was provided or the value
                could not be converted.
        """
        try:
            return datetime.strptime(value, kwargs["format"])
        except KeyError:
            raise ConverterError("Missing format keyword argument")
        except Exception as e:
            raise ConverterError(e)

    def serialize(self, value: Union[date, time], **kwargs: Any) -> str:
        """Convert a datetime instance to string.

        Args:
            value: The input datetime instance
            **kwargs: Additional keyword argument
                format: The datetime format to use

        Returns:
            The converted str value.

        Raises:
            ConverterError: If no format was provided or the value
                could not be converted.
        """
        try:
            return value.strftime(kwargs["format"])
        except KeyError:
            raise ConverterError("Missing format keyword argument")
        except Exception as e:
            raise ConverterError(e)

    @abc.abstractmethod
    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """Parse string literal value into python."""


class TimeConverter(DateTimeBase):
    """A datetime.time converter."""

    def deserialize(self, value: Any, **kwargs: Any) -> time:
        """Convert the input str to a time instance.

        Args:
            value: The input string value
            **kwargs: Additional keyword argument
                format: The time format to use

        Returns:
            The time instance

        Raises:
            ConverterError: If no format was provided or the value
                could not be converted.
        """
        return self.parse(value, **kwargs).time()


class DateConverter(DateTimeBase):
    """A datetime.date converter."""

    def deserialize(self, value: Any, **kwargs: Any) -> date:
        """Convert the input str to a date instance.

        Args:
            value: The input string value
            **kwargs: Additional keyword argument
                format: The time format to use

        Returns:
            The date instance

        Raises:
            ConverterError: If no format was provided or the value
                could not be converted.
        """
        return self.parse(value, **kwargs).date()


class DateTimeConverter(DateTimeBase):
    """A datetime.datetime converter."""

    def deserialize(self, value: Any, **kwargs: Any) -> datetime:
        """Convert the input str to a datetime instance.

        Args:
            value: The input string value
            **kwargs: Additional keyword argument
                format: The time format to use

        Returns:
            The datetime instance

        Raises:
            ConverterError: If no format was provided or the value
                could not be converted.
        """
        return self.parse(value, **kwargs)


class ProxyConverter(Converter):
    """Proxy wrapper to treat callables as converters.

    Args:
        factory: The callable factory
    """

    __slots__ = "factory"

    def __init__(self, factory: Callable):
        self.factory = factory

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """Call the instance factory and return the result.

        Args:
            value: The input value to convert
            **kwargs: Unused keyword arguments

        Returns:
            The return result of the callable.

        Raises:
            ConverterError: on value errors.
        """
        try:
            return self.factory(value)
        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: Any, **kwargs: Any) -> str:
        """Cast value to str."""
        return str(value)


converter = ConverterFactory()
converter.register_converter(str, StringConverter())
converter.register_converter(int, IntConverter())
converter.register_converter(bool, BoolConverter())
converter.register_converter(float, FloatConverter())
converter.register_converter(bytes, BytesConverter())
converter.register_converter(object, converter.type_converter(str))
converter.register_converter(time, TimeConverter())
converter.register_converter(date, DateConverter())
converter.register_converter(datetime, DateTimeConverter())
converter.register_converter(XmlTime, ProxyConverter(XmlTime.from_string))
converter.register_converter(XmlDate, ProxyConverter(XmlDate.from_string))
converter.register_converter(XmlDateTime, ProxyConverter(XmlDateTime.from_string))
converter.register_converter(XmlDuration, ProxyConverter(XmlDuration))
converter.register_converter(XmlPeriod, ProxyConverter(XmlPeriod))
converter.register_converter(QName, QNameConverter())
converter.register_converter(Decimal, DecimalConverter())
converter.register_converter(Enum, EnumConverter())
