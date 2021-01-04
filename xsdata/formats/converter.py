import abc
import base64
import binascii
import math
import warnings
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import time
from datetime import timedelta
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
from xsdata.models.datatype import Duration
from xsdata.models.datatype import Period
from xsdata.utils import text
from xsdata.utils.dates import DateTimeParser
from xsdata.utils.namespaces import load_prefix
from xsdata.utils.namespaces import split_qname


class Converter(metaclass=abc.ABCMeta):
    """Abstract converter class."""

    @abc.abstractmethod
    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """
        Convert any type to the converter dedicated type.

        :raises ConverterError: if converter fails with and expected ValueError
        """

    @abc.abstractmethod
    def serialize(self, value: Any, **kwargs: Any) -> str:
        """Convert value to string."""


@dataclass
class ConverterAdapter:
    """
    :param registry: Converters registry
    """

    registry: Dict[Type, Converter] = field(default_factory=dict)

    def deserialize(self, value: Any, types: List[Type], **kwargs: Any) -> Any:
        """
        Attempt to convert a any value to one of the given types.

        If all attempts fail return the value input value and issue a warning.

        :return: The first successful converted value.
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
        """
        Convert the given value to string, ignore None values.

        If the value is a list assume the value is a list of tokens.
        """
        if value is None:
            return None

        if isinstance(value, list):
            return " ".join([self.serialize(val, **kwargs) for val in value])

        instance = self.value_converter(value)
        return instance.serialize(value, **kwargs)

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
        if len(types) < 2:
            return list(types)

        return sorted(types, key=lambda x: __PYTHON_TYPES_SORTED__.get(x, 0))


__PYTHON_TYPES_SORTED__ = {
    bool: 1,
    int: 2,
    float: 3,
    Decimal: 4,
    datetime: 5,
    time: 6,
    Duration: 7,
    Period: 8,
    QName: 9,
    str: 10,
}


class BoolConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> bool:
        if isinstance(value, str):

            val = value.strip()

            if val in ("true", "1"):
                return True

            if val in ("false", "0"):
                return False

            raise ConverterError(f"Invalid bool literal '{value}'")

        return True if value else False

    def serialize(self, value: bool, **kwargs: Any) -> str:
        return "true" if value else "false"


class IntConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> int:
        try:
            return int(value)
        except (ValueError, TypeError) as e:
            raise ConverterError(e)

    def serialize(self, value: int, **kwargs: Any) -> str:
        return str(value)


class StrConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> str:
        return str(value)

    def serialize(self, value: str, **kwargs: Any) -> str:
        return str(value)


class FloatConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> float:
        try:
            return float(value)
        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: float, **kwargs: Any) -> str:
        return "NaN" if math.isnan(value) else str(value).upper()


class BytesConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> bytes:
        if not isinstance(value, str):
            raise ConverterError("Value must be str")

        try:
            fmt = kwargs.get("format")

            if fmt == "base16":
                return binascii.unhexlify(value)

            if fmt == "base64":
                return base64.b64decode(value)

            raise ConverterError(f"Unknown format '{fmt}'")
        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: bytes, **kwargs: Any) -> str:
        fmt = kwargs.get("format")

        if fmt == "base16":
            return base64.b16encode(value).decode()

        if fmt == "base64":
            return base64.b64encode(value).decode()

        raise ConverterError(f"Unknown format '{fmt}'")


class DecimalConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> Decimal:
        try:
            return Decimal(value)
        except InvalidOperation:
            raise ConverterError()

    def serialize(self, value: Decimal, **kwargs: Any) -> str:
        if value.is_infinite():
            return str(value).replace("Infinity", "INF")

        return str(value)


class QNameConverter(Converter):
    def deserialize(
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

    def serialize(
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
            raise ConverterError("Value is empty")

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
    def deserialize(
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
        except ValueError as e:
            raise ConverterError(e)

    def serialize(
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
    def deserialize(
        self, value: Any, data_type: Optional[Type[Enum]] = None, **kwargs: Any
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
            real_value = converter.deserialize(value, [value_type], **kwargs)

        # Raise exception if the real value doesn't match the expected type.
        if not isinstance(real_value, value_type):
            raise ConverterError(f"Value must be {value_type}")

        try:
            # Attempt no1 use the enum constructor
            return data_type(real_value)
        except ValueError:
            pass

        try:
            # Attempt no2 the enum might be derived from
            # xs:NMTOKENS or xs:list removing excess whitespace.
            if isinstance(real_value, str):
                return data_type(" ".join(real_value.split()))

            # Attempt #3 some values are never equal try to match
            # canonical representations.
            repr_value = repr(real_value)
            return next(x for x in data_type if repr(x.value) == repr_value)
        except (ValueError, StopIteration) as e:
            raise ConverterError(e)

    def serialize(self, value: Enum, **kwargs: Any) -> str:
        return converter.serialize(value.value, **kwargs)


class TimeConverter(Converter):
    """
    Converter for iso 8061 xml subset time strings.

    Format: hh:mm:ss[Z|(+|-)hh:mm]
    """

    format = "%h:%m:%s%z"

    def deserialize(self, value: Any, **kwargs: Any) -> time:
        if not isinstance(value, str):
            raise ConverterError("Value must be str")

        try:
            fmt = kwargs.get("format")
            if fmt:
                return datetime.strptime(value, fmt).time()

            fmt = self.format
            parser = DateTimeParser(value, self.format)
            parser.parse()

            assert (
                parser.hour is not None
                and parser.minute is not None
                and parser.second is not None
            )

            return time(
                hour=0 if parser.hour == 24 else parser.hour,
                minute=parser.minute,
                second=parser.second,
                microsecond=parser.microsecond or 0,
                tzinfo=parser.tz_info,
            )
        except (IndexError, TypeError, ValueError):
            raise ConverterError(f"String '{value}' does not match format '{fmt}'")

    def serialize(self, value: time, **kwargs: Any) -> str:
        fmt = kwargs.get("format")
        if fmt:
            return value.strftime(fmt)

        result = value.isoformat().replace("+00:00", "Z")
        if len(result) > 14 and result[12:15] == "000":
            result = result[:12] + result[15:]
        return result


class DatetimeConverter(Converter):
    """
    Converter for iso 8061 xml subset datetime strings.

    Format: YYYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
    """

    format = "%Y-%M-%DT%h:%m:%s%z"

    def deserialize(self, value: Any, **kwargs: Any) -> datetime:
        if not isinstance(value, str):
            raise ConverterError("Value must be str")

        try:

            fmt = kwargs.get("format")
            if fmt:
                return datetime.strptime(value, fmt)

            fmt = self.format
            parser = DateTimeParser(value, fmt)
            parser.parse()

            assert (
                parser.year is not None
                and parser.month is not None
                and parser.day is not None
                and parser.hour is not None
                and parser.minute is not None
                and parser.second is not None
            )

            delta = None
            hour = parser.hour
            if hour == 24:
                hour = 0
                delta = timedelta(days=1)

            result = datetime(
                year=parser.year,
                month=parser.month,
                day=parser.day,
                hour=hour,
                minute=parser.minute,
                second=parser.second,
                microsecond=parser.microsecond or 0,
                tzinfo=parser.tz_info,
            )

            return result + delta if delta else result
        except (IndexError, TypeError, ValueError):
            raise ConverterError(f"String '{value}' does not match format '{fmt}'")

    def serialize(self, value: datetime, **kwargs: Any) -> str:
        fmt = kwargs.get("format")
        if fmt:
            return value.strftime(fmt)

        result = value.isoformat().replace("+00:00", "Z")
        if len(result) > 26 and result[23:26] == "000":
            result = result[:23] + result[26:]
        return result


@dataclass
class ProxyConverter(Converter):
    """
    :param func: the callable to convert from string
    """

    func: Callable

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        try:
            return self.func(value)
        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: Any, **kwargs: Any) -> str:
        return str(value)


converter = ConverterAdapter()
converter.register_converter(str, StrConverter())
converter.register_converter(int, IntConverter())
converter.register_converter(bool, BoolConverter())
converter.register_converter(float, FloatConverter())
converter.register_converter(bytes, BytesConverter())
converter.register_converter(object, StrConverter())
converter.register_converter(time, TimeConverter())
converter.register_converter(datetime, DatetimeConverter())
converter.register_converter(Duration, ProxyConverter(Duration))
converter.register_converter(Period, ProxyConverter(Period))
converter.register_converter(etree.QName, LxmlQNameConverter())
converter.register_converter(QName, QNameConverter())
converter.register_converter(Decimal, DecimalConverter())
converter.register_converter(type(Enum), EnumConverter())
