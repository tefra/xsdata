import sys
from typing import Any
from typing import Iterator
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

from typing_extensions import get_args
from typing_extensions import get_origin

NONE_TYPE = type(None)


try:
    from types import UnionType  # type: ignore
except ImportError:
    UnionType = ()  # type: ignore


if (3, 9) <= sys.version_info[:2] <= (3, 10):
    # Backport this fix for python 3.9 and 3.10
    # https://github.com/python/cpython/pull/30900

    from types import GenericAlias
    from typing import ForwardRef
    from typing import _eval_type as __eval_type  # type: ignore

    def _eval_type(tp: Any, globalns: Any, localns: Any) -> Any:
        if isinstance(tp, GenericAlias):
            args = tuple(
                ForwardRef(arg) if isinstance(arg, str) else arg for arg in tp.__args__
            )
            tp = tp.__origin__[args]  # type: ignore

        return __eval_type(tp, globalns, localns)

else:
    from typing import _eval_type  # type: ignore


intern_typing = sys.intern("typing.")


def is_from_typing(tp: Any) -> bool:
    return str(tp).startswith(intern_typing)


def evaluate(
    tp: Any,
    globalns: Any = None,
    localns: Any = None,
) -> Tuple[Type, ...]:
    return tuple(_evaluate(_eval_type(tp, globalns, localns)))


def _evaluate(tp: Any) -> Iterator[Type]:
    if tp in (dict, list, tuple):
        origin = tp
    elif isinstance(tp, TypeVar):
        origin = TypeVar
    else:
        origin = get_origin(tp)

    if origin:
        try:
            yield from __evaluations__[origin](tp)
        except KeyError:
            raise TypeError()
    elif is_from_typing(tp):
        raise TypeError()
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
        if isinstance(arg, TypeVar):
            try:
                next(_evaluate_typevar(arg))
            except TypeError:
                yield str
            else:
                raise TypeError()
        elif is_from_typing(arg) or get_origin(arg) is not None:
            raise TypeError()
        else:
            yield arg


def _evaluate_list(tp: Any) -> Iterator[Type]:
    yield list

    args = get_args(tp)
    if not args:
        yield str

    for arg in args:
        yield from _evaluate_array_arg(arg)


def _evaluate_array_arg(arg: Any) -> Iterator[Type]:
    if isinstance(arg, TypeVar):
        yield from _evaluate_typevar(arg)
    else:
        origin = get_origin(arg)

        if origin is None and not is_from_typing(arg):
            yield arg
        elif origin in (Union, UnionType, list, tuple):
            yield from __evaluations__[origin](arg)
        else:
            raise TypeError()


def _evaluate_tuple(tp: Any) -> Iterator[Type]:
    yield tuple

    args = get_args(tp)
    if not args:
        yield str

    for arg in args:
        if arg is Ellipsis:
            continue

        yield from _evaluate_array_arg(arg)


def _evaluate_union(tp: Any) -> Iterator[Type]:
    origin_locked = False
    for arg in get_args(tp):
        if arg is NONE_TYPE:
            continue

        if isinstance(arg, TypeVar):
            yield from _evaluate_typevar(arg)
        else:
            origin = get_origin(arg)
            if origin is list and not origin_locked:
                yield from _evaluate_list(arg)
                origin_locked = True
            elif origin is None and not is_from_typing(arg):
                yield arg
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
    tuple: _evaluate_tuple,
    list: _evaluate_list,
    dict: _evaluate_mapping,
    Union: _evaluate_union,
    UnionType: _evaluate_union,
    type: _evaluate_type,
    TypeVar: _evaluate_typevar,
}
