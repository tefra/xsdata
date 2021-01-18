import abc
import base64
import binascii
import math
import warnings
from abc import ABCMeta
from dataclasses import dataclass
from dataclasses import field
from datetime import date
from datetime import datetime
from datetime import time
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
from xsdata.models.datatype import XmlBase64Binary
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlHexBinary
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime
from xsdata.utils import text
from xsdata.utils.namespaces import load_prefix
from xsdata.utils.namespaces import split_qname

NOT_A_STRING = "Value must be str"


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
class ConverterFactory:
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
    XmlDuration: 7,
    XmlPeriod: 8,
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
            raise ConverterError(NOT_A_STRING)

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

            # Attempt #3 some times enum member init values don't match
            # Try matching canonical repr or member values directly
            repr_value = repr(real_value)
            for x in data_type:
                if repr(x.value) == repr_value or x.value == real_value:
                    return x

            raise ConverterError("Not enum member matched")

        except ValueError as e:
            raise ConverterError(e)

    def serialize(self, value: Enum, **kwargs: Any) -> str:
        return converter.serialize(value.value, **kwargs)


class DateTimeBase(Converter, metaclass=ABCMeta):
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


class TimeConverter(DateTimeBase):
    def deserialize(self, value: Any, **kwargs: Any) -> time:
        return self.parse(value, **kwargs).time()


class DateConverter(DateTimeBase):
    def deserialize(self, value: Any, **kwargs: Any) -> date:
        return self.parse(value, **kwargs).date()


class DateTimeConverter(DateTimeBase):
    def deserialize(self, value: Any, **kwargs: Any) -> datetime:
        return self.parse(value, **kwargs)


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


converter = ConverterFactory()
converter.register_converter(str, ProxyConverter(str))
converter.register_converter(int, IntConverter())
converter.register_converter(bool, BoolConverter())
converter.register_converter(float, FloatConverter())
converter.register_converter(bytes, BytesConverter())
converter.register_converter(object, ProxyConverter(str))
converter.register_converter(time, TimeConverter())
converter.register_converter(date, DateConverter())
converter.register_converter(datetime, DateTimeConverter())
converter.register_converter(XmlTime, ProxyConverter(XmlTime.from_string))
converter.register_converter(XmlDate, ProxyConverter(XmlDate.from_string))
converter.register_converter(XmlDateTime, ProxyConverter(XmlDateTime.from_string))
converter.register_converter(XmlDuration, ProxyConverter(XmlDuration))
converter.register_converter(XmlPeriod, ProxyConverter(XmlPeriod))
converter.register_converter(etree.QName, LxmlQNameConverter())
converter.register_converter(QName, QNameConverter())
converter.register_converter(Decimal, DecimalConverter())
converter.register_converter(Enum, EnumConverter())
