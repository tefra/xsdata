from dataclasses import is_dataclass
from decimal import Decimal
from enum import Enum
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Type


def sort_types(types: List[Type]):
    in_order = (bool, int, str, float, Decimal)

    sorted_types = []
    for ordered in in_order:
        if ordered in types:
            types.remove(ordered)
            sorted_types.append(ordered)

    types.extend(sorted_types)
    return types


def to_python(types: List[Type], value: Any, in_order=True) -> Any:
    if not isinstance(value, str):
        return value

    if not in_order and len(types) > 1:
        types = sort_types(list(types))

    for clazz in types:
        try:
            if clazz.__name__ in func_map:
                return func_map[clazz.__name__](value)
            else:
                return to_class(clazz, value)
        except ValueError:
            pass

    return value


def to_class(clazz: Any, value: Any) -> Any:
    try:
        if issubclass(clazz, Enum):
            return to_enum(clazz, value)
        elif is_dataclass(clazz):
            return clazz(value)
    except KeyError:
        raise ValueError(f"Unhandled class type {clazz.__name__}")


def to_enum(clazz: Type[Enum], value: Any) -> Enum:
    enumeration = next(enumeration for enumeration in clazz)
    return clazz(type(enumeration.value)(value))


def to_bool(value: Any) -> bool:
    if value in ("true", "1"):
        return True
    if value in ("false", "0"):
        return False

    raise ValueError(f"Invalid bool literal '{value}'")


def to_xml(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, Enum):
        return str(value.value)

    return str(value)


func_map: Dict[str, Callable] = {
    "str": str,
    "int": int,
    "float": float,
    "bool": to_bool,
    "Decimal": Decimal,
}
