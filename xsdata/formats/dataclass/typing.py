from typing import _eval_type  # type: ignore
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

NONE_TYPE = type(None)
EMPTY_ARGS = ()


def get_origin(tp: Any) -> Any:

    if tp is Dict:
        return Dict

    if tp in (List, Union):
        raise TypeError()

    if isinstance(tp, TypeVar):
        return TypeVar

    origin = getattr(tp, "__origin__", None)
    if origin:
        if origin in (list, List):
            return List

        if origin in (dict, Dict):
            return Dict

        if origin is Union:
            return Union

        if origin in (type, Type):
            return Type

    if origin or str(tp).startswith("typing."):
        raise TypeError()

    return None


def get_args(tp: Any) -> Tuple:
    return getattr(tp, "__args__", EMPTY_ARGS) or EMPTY_ARGS


def evaluate(tp: Any, globalns: Any = None, localns: Any = None) -> Tuple[Type, ...]:
    return tuple(_evaluate(_eval_type(tp, globalns, localns)))


def _evaluate(tp: Any) -> Iterator[Type]:
    origin = get_origin(tp)
    if origin is List:
        yield from _evaluate_list(tp)
    elif origin is Dict:
        yield from _evaluate_mapping(tp)
    elif origin is Union:
        yield from _evaluate_union(tp)
    elif origin is Type:
        args = get_args(tp)
        if not args or isinstance(args[0], TypeVar):
            raise TypeError()
        yield from _evaluate(args[0])
    elif origin is TypeVar:
        yield from _evaluate_typevar(tp)
    else:
        yield tp


def _evaluate_mapping(tp: Any) -> Iterator[Type]:
    yield dict
    args = get_args(tp)

    if not args:
        yield str
        yield str

    for arg in args:
        origin = get_origin(arg)
        if origin is TypeVar:
            try:
                next(_evaluate_typevar(arg))
            except TypeError:
                yield str
            else:
                raise TypeError()
        elif origin is not None:
            raise TypeError()
        else:
            yield arg


def _evaluate_list(tp: Any) -> Iterator[Type]:
    yield list

    args = get_args(tp)
    for arg in args:
        origin = get_origin(arg)

        if origin is None:
            yield arg
        elif origin is Union:
            yield from _evaluate_union(arg)
        elif origin is List:
            yield from _evaluate_list(arg)
        elif origin is TypeVar:
            yield from _evaluate_typevar(arg)
        else:
            raise TypeError()


def _evaluate_union(tp: Any) -> Iterator[Type]:
    origin_locked = False
    for arg in get_args(tp):
        if arg is NONE_TYPE:
            continue

        origin = get_origin(arg)
        if origin is None:
            yield arg
        elif origin is List and not origin_locked:
            yield from _evaluate_list(arg)
            origin_locked = True
        else:
            raise TypeError()


def _evaluate_typevar(tp: TypeVar):
    if tp.__bound__:
        yield from _evaluate(tp.__bound__)
    elif tp.__constraints__:
        for arg in tp.__constraints__:
            yield from _evaluate(arg)
    else:
        raise TypeError()
