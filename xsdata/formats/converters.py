import contextlib
import math
import warnings
from dataclasses import is_dataclass
from decimal import Decimal
from decimal import InvalidOperation
from enum import Enum
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from lxml.etree import QName

from xsdata.exceptions import ConverterError
from xsdata.exceptions import ConverterWarning
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.utils import text


def sort_types(types: List[Type]) -> List[Type]:
    in_order = (bool, int, float, Decimal, str)

    sorted_types = []
    for ordered in in_order:
        if ordered in types:
            types.remove(ordered)
            sorted_types.append(ordered)

    types.extend(sorted_types)
    return types


def to_python(
    value: Any, types: List[Type], ns_map: Optional[Dict] = None, in_order: bool = True
) -> Any:

    if not isinstance(value, str):
        return value

    if not in_order and len(types) > 1:
        types = sort_types(list(types))

    for clazz in types:
        with contextlib.suppress(ValueError, InvalidOperation, TypeError):
            func = func_map.get(clazz.__name__)
            return func(value) if func else to_class(clazz, value, ns_map)

    warnings.warn(
        f"Failed to convert value `{value}` to one of {types}", ConverterWarning
    )
    return value


def to_qname(value: str, ns_map: Optional[Dict]) -> QName:
    if ns_map is None:
        return QName(value)

    prefix, suffix = text.split(value)
    namespace = ns_map.get(prefix)
    return QName(namespace, suffix)


def to_class(clazz: Any, value: str, ns_map: Optional[Dict]) -> Any:
    if clazz is QName:
        return to_qname(value.strip(), ns_map)
    if issubclass(clazz, Enum):
        return to_enum(clazz, value.strip(), ns_map)
    if is_dataclass(clazz):
        return clazz(value)

    raise ConverterError(f"Unhandled class type {clazz.__name__}")


def to_enum(clazz: Type[Enum], value: str, ns_map: Optional[Dict]) -> Enum:
    enumeration: Enum = list(clazz)[0]

    if isinstance(enumeration.value, QName):
        value = to_qname(value, ns_map)

    try:
        return clazz(type(enumeration.value)(value))
    except ValueError:
        # restriction base="xsd:token"
        return clazz(" ".join(value.split()))


def to_bool(value: Any) -> bool:
    val = value.strip()
    if val in ("true", "1"):
        return True
    if val in ("false", "0"):
        return False

    raise ConverterError(f"Invalid bool literal '{value}'")


def to_xml(value: Any, namespaces: Optional[Namespaces] = None) -> Any:
    if value is None:
        return None
    if isinstance(value, list):
        return " ".join(map(lambda x: to_xml(x, namespaces), value))
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, Enum):
        return to_xml(value.value, namespaces)
    if isinstance(value, float):
        return "NaN" if math.isnan(value) else str(value).upper()
    if isinstance(value, Decimal) and value.is_infinite():
        return str(value).replace("Infinity", "INF")
    if isinstance(value, QName):
        return qname_to_xml(value, namespaces) if namespaces else value.text
    if is_dataclass(value):
        raise ConverterError("Text nodes can't be dataclasses!")
    return str(value)


def qname_to_xml(qname: QName, namespaces: Namespaces) -> str:
    namespaces.add(qname.namespace)
    prefix = namespaces.prefix(qname.namespace)

    return f"{prefix}:{qname.localname}" if prefix else qname.localname


func_map: Dict[str, Callable] = {
    "str": str,
    "int": int,
    "float": float,
    "bool": to_bool,
    "Decimal": Decimal,
    "object": str,
}
