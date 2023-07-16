import abc
import base64
import binascii
import math
import warnings
from datetime import date
from datetime import datetime
from datetime import time
from decimal import Decimal
from decimal import InvalidOperation
from enum import Enum
from enum import EnumMeta
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import Union
from xml.etree.ElementTree import QName

from xsdata.exceptions import ConverterError
from xsdata.exceptions import ConverterWarning
from xsdata.models.datatype import XmlBase64Binary
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlHexBinary
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime
from xsdata.utils import collections
from xsdata.utils import namespaces
from xsdata.utils import text


class Converter(abc.ABC):
    """Abstract converter class."""

    @abc.abstractmethod
    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        """
        Convert any type to the converter dedicated type.

        :raises ConverterError: if converter fails with and expected
            ValueError
        """

    @abc.abstractmethod
    def serialize(self, value: Any, **kwargs: Any) -> str:
        """Convert value to string."""

    @classmethod
    def validate_input_type(cls, value: Any, tp: Type):
        if not isinstance(value, tp):
            raise ConverterError(
                f"Input value must be '{tp.__name__}' got '{type(value).__name__}'"
            )


class ConverterFactory:
    __slots__ = ("registry",)

    def __init__(self):
        self.registry: Dict[Type, Converter] = {}

    def deserialize(self, value: Any, types: Sequence[Type], **kwargs: Any) -> Any:
        """
        Attempt to convert a any value to one of the given types.

        If all attempts fail return the value input value and issue a
        warning.

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
        """
        Test the given string value can be parsed using the given list of types
        without warnings.

        If strict flag is enabled validate the textual representation
        also matches the original input.
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

    def type_converter(self, datatype: Type) -> Converter:
        """
        Find a suitable converter for given data type.

        Iterate over all but last mro items and check for registered
        converters, fall back to str and issue a warning if there are
        not matches.
        """
        try:
            # Quick in and out, without checking the whole mro.
            return self.registry[datatype]
        except KeyError:
            pass

        # We tested the first, ignore the object
        for mro in datatype.__mro__[1:-1]:
            if mro in self.registry:
                return self.registry[mro]

        warnings.warn(f"No converter registered for `{datatype}`", ConverterWarning)
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
    def explicit_types(cls) -> Tuple:
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
    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        return value if isinstance(value, str) else str(value)

    def serialize(self, value: Any, **kwargs: Any) -> str:
        return value if isinstance(value, str) else str(value)


class BoolConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> bool:
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
        return "true" if value else "false"


class IntConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> int:
        try:
            return int(value)
        except (ValueError, TypeError) as e:
            raise ConverterError(e)

    def serialize(self, value: int, **kwargs: Any) -> str:
        return str(value)


class FloatConverter(Converter):
    INF = float("inf")

    def deserialize(self, value: Any, **kwargs: Any) -> float:
        try:
            return float(value)
        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: float, **kwargs: Any) -> str:
        if math.isnan(value):
            return "NaN"

        if value == self.INF:
            return "INF"

        if value == -self.INF:
            return "-INF"

        return repr(value).upper().replace("E+", "E")


class BytesConverter(Converter):
    def deserialize(self, value: Any, **kwargs: Any) -> bytes:
        self.validate_input_type(value, str)

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

        if isinstance(value, XmlHexBinary) or fmt == "base16":
            return base64.b16encode(value).decode()

        if isinstance(value, XmlBase64Binary) or fmt == "base64":
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

        return f"{value:f}"


class QNameConverter(Converter):
    def deserialize(
        self,
        value: str,
        ns_map: Optional[Dict] = None,
        **kwargs: Any,
    ) -> QName:
        """
        Convert namespace prefixed strings, or fully qualified strings to
        QNames.

        examples:
            - xs:string -> QName("http://www.w3.org/2001/XMLSchema", "string")
            - {foo}bar -> QName("foo", "bar"
        """
        self.validate_input_type(value, str)
        namespace, tag = self.resolve(value, ns_map)

        return QName(namespace, tag) if namespace else QName(tag)

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

        namespace, tag = namespaces.split_qname(value.text)

        if not namespace:
            return tag

        prefix = namespaces.load_prefix(namespace, ns_map)

        return f"{prefix}:{tag}" if prefix else tag

    @staticmethod
    def resolve(value: str, ns_map: Optional[Dict] = None) -> Tuple:
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
    def serialize(self, value: Enum, **kwargs: Any) -> str:
        return converter.serialize(value.value, **kwargs)

    def deserialize(
        self, value: Any, data_type: Optional[EnumMeta] = None, **kwargs: Any
    ) -> Enum:
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
        cls, value: Any, values: Sequence, length: int, real: Any, **kwargs: Any
    ) -> bool:
        if isinstance(value, str) and isinstance(real, str):
            return value == real or " ".join(values) == real

        if isinstance(real, (tuple, list)) and not hasattr(real, "_fields"):
            if len(real) == length and cls.match_list(values, real, **kwargs):
                return True
        elif length == 1 and cls.match_atomic(value, real, **kwargs):
            return True

        return False

    @classmethod
    def match_list(cls, raw: Sequence, real: Sequence, **kwargs: Any) -> bool:
        for index, val in enumerate(real):
            if not cls.match_atomic(raw[index], val, **kwargs):
                return False

        return True

    @classmethod
    def match_atomic(cls, raw: Any, real: Any, **kwargs: Any) -> bool:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cmp = converter.deserialize(raw, [type(real)], **kwargs)

        if isinstance(real, float):
            return cmp == real or repr(cmp) == repr(real)

        return cmp == real


class DateTimeBase(Converter, metaclass=abc.ABCMeta):
    @classmethod
    def parse(cls, value: Any, **kwargs: Any) -> datetime:
        try:
            return datetime.strptime(value, kwargs["format"])
        except KeyError:
            raise ConverterError("Missing format keyword argument")
        except Exception as e:
            raise ConverterError(e)

    def serialize(self, value: Union[date, time], **kwargs: Any) -> str:
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
    def deserialize(self, value: Any, **kwargs: Any) -> time:
        return self.parse(value, **kwargs).time()


class DateConverter(DateTimeBase):
    def deserialize(self, value: Any, **kwargs: Any) -> date:
        return self.parse(value, **kwargs).date()


class DateTimeConverter(DateTimeBase):
    def deserialize(self, value: Any, **kwargs: Any) -> datetime:
        return self.parse(value, **kwargs)


class ProxyConverter(Converter):
    __slots__ = ("factory",)

    def __init__(self, factory: Callable):
        """
        :param factory: factory function used to parse string values
        """
        self.factory = factory

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        try:
            return self.factory(value)
        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: Any, **kwargs: Any) -> str:
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
