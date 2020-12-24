import abc
import math
import warnings
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timedelta
from datetime import timezone
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
    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """
        Convert any type to the converter dedicated type.

        :raises ConverterError: if converter fails with and expected ValueError
        """

    @abc.abstractmethod
    def serialize(self, value: Any, **kwargs: Any) -> str:
        """Convert value to string."""

    def encode(self, value: Any, **kwargs: Any) -> Any:
        """Encode value for representation."""
        return value


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

    def encode(self, value: Any, **kwargs: Any) -> Any:
        """
        Encode the given value for representation, ignore None values.

        If the value is a list assume the value is a list of tokens.
        """
        if value is None:
            return None

        if isinstance(value, list):
            return [self.encode(val, **kwargs) for val in value]

        instance = self.value_converter(value)
        return instance.encode(value, **kwargs)

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
    str: 6,
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

    def encode(self, value: Any, **kwargs: Any) -> Any:
        return self.serialize(value)


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

    def encode(self, value: Any, **kwargs: Any) -> Any:
        return str(value)


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

    def encode(self, value: Any, **kwargs: Any) -> Any:
        return str(value)


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

    def encode(self, value: Any, **kwargs: Any) -> Any:
        return converter.encode(value.value)


class DatetimeConverter(Converter):
    """
    Converter for iso 8061 xml subset datetime strings.

    Format: YYYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
    """

    def deserialize(self, value: Any, **kwargs: Any) -> datetime:
        if not isinstance(value, str):
            raise ConverterError("Value must be str")

        try:
            if (
                value[4] != "-"
                or value[7] != "-"
                or value[10] != "T"
                or value[13] != ":"
                or value[16] != ":"
            ):
                raise IndexError()

            year, month, day = int(value[:4]), int(value[5:7]), int(value[8:10])
            length = len(value)
            hour = int(value[11:13])
            minute = int(value[14:16])
            second = int(value[17:19])
            microsecond = 0

            delta = None
            if hour == 24:
                hour = 0
                delta = timedelta(days=1)

            index = 19
            if length > index and value[index] == ".":
                microseconds = ""
                index += 1
                while length > index and value[index].isdigit():
                    microseconds += value[index]
                    index += 1

                microsecond = int(microseconds.ljust(6, "0"))

            tz_info = self.parse_timezone(value, index) if length > index else None

            result = datetime(
                year=year,
                month=month,
                day=day,
                hour=hour,
                minute=minute,
                second=second,
                microsecond=microsecond,
                tzinfo=tz_info,
            )

            return result + delta if delta else result
        except (IndexError, TypeError, ValueError):
            raise ConverterError(f"Invalid isoformat string: '{value}'")

    def serialize(self, value: datetime, **kwargs: Any) -> str:
        return value.isoformat().replace("+00:00", "Z")

    def encode(self, value: Any, **kwargs: Any) -> Any:
        return self.serialize(value)

    @classmethod
    def parse_timezone(cls, string: str, index: int) -> timezone:
        if string[index] == "Z":
            return timezone.utc

        if string[index] in ("-", "+"):
            offset = int(string[index + 1 : index + 3]) * 60
            offset += int(string[index + 4 :])

            if string[index] == "-":
                offset = -offset

            return timezone(timedelta(minutes=offset))

        raise ValueError(f"Invalid timezone '{string[index:]}'")


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
converter.register_converter(object, StrConverter())
converter.register_converter(datetime, DatetimeConverter())
converter.register_converter(etree.QName, LxmlQNameConverter())
converter.register_converter(QName, QNameConverter())
converter.register_converter(Decimal, DecimalConverter())
converter.register_converter(type(Enum), EnumConverter())
