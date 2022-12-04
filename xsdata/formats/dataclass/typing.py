from typing import _eval_type  # type: ignore
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

NONE_TYPE = type(None)
EMPTY_ARGS = ()


def get_origin(tp: Any) -> Any:
    if tp is Dict:
        return Dict

    if tp in (Tuple, List, Union):
        raise TypeError()

    if isinstance(tp, TypeVar):
        return TypeVar

    origin = getattr(tp, "__origin__", None)
    if origin:
        if origin in (list, List):
            return List

        if origin in (tuple, Tuple):
            return Tuple

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


def evaluate(
    tp: Any, globalns: Optional[Any] = None, localns: Optional[Any] = None
) -> Tuple[Type, ...]:
    return tuple(_evaluate(_eval_type(tp, globalns, localns)))


def _evaluate(tp: Any) -> Iterator[Type]:
    origin = get_origin(tp)

    func = __evaluations__.get(origin)
    if func:
        yield from func(tp)
    else:
        yield tp


def _evaluate_type(tp: Any) -> Iterator[Type]:
    args = get_args(tp)
    if not args or isinstance(args[0], TypeVar):
        raise TypeError()
    yield from _evaluate(args[0])


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
        elif origin in (Union, List, Tuple, TypeVar):
            yield from __evaluations__[origin](arg)
        else:
            raise TypeError()


def _evaluate_tuple(tp: Any) -> Iterator[Type]:
    yield tuple

    args = get_args(tp)
    for arg in args:

        if arg is Ellipsis:
            continue

        origin = get_origin(arg)
        if origin is None:
            yield arg
        elif origin in (Union, List, Tuple, TypeVar):
            yield from __evaluations__[origin](arg)
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


__evaluations__ = {
    Tuple: _evaluate_tuple,
    List: _evaluate_list,
    Dict: _evaluate_mapping,
    Union: _evaluate_union,
    Type: _evaluate_type,
    TypeVar: _evaluate_typevar,
}
