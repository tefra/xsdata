import sys
from typing import _eval_type  # type: ignore
from typing import Any
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union

import typing_extensions


NONE_TYPE = type(None)

try:
    from types import UnionType
except ImportError:

    class UnionType:  # type: ignore
        pass


get_origin = typing_extensions.get_origin
get_args = typing_extensions.get_args

if (3, 9) < sys.version_info < (3, 11):
    from typing import ForwardRef

    try:
        from typing import GenericAlias  # type: ignore
    except ImportError:

        class GenericAlias:  # type: ignore
            pass

    def eval_strings_as_forward_refs(tp: Any) -> Any:
        if isinstance(tp, GenericAlias):
            args = tuple(
                ForwardRef(arg) if isinstance(arg, str) else arg for arg in tp.__args__
            )
            tp = tp.__origin__[args]  # type: ignore

        return tp

else:

    def eval_strings_as_forward_refs(tp: Any) -> Any:
        return tp


def evaluate(
    tp: Any, globalns: Optional[Any] = None, localns: Optional[Any] = None
) -> Tuple[Type, ...]:
    tp = eval_strings_as_forward_refs(tp)
    return tuple(_evaluate(_eval_type(tp, globalns, localns)))


def _evaluate(tp: Any) -> Iterator[Type]:
    if isinstance(tp, TypeVar):
        yield from _evaluate_typevar(tp)
    else:
        origin = tp if tp in (dict, set, list, tuple) else get_origin(tp)

        if origin is None:
            yield tp
        else:
            func = __evaluations__.get(origin)
            if func:
                yield from func(tp)
            else:
                raise TypeError()


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
        elif arg is Any or get_origin(arg):
            raise TypeError()
        else:
            yield arg


def _evaluate_list(tp: Any) -> Iterator[Type]:
    args = get_args(tp)
    if not args:
        raise TypeError()

    yield list
    for arg in args:
        yield from _evaluate_array_arg(arg)


def _evaluate_tuple(tp: Any) -> Iterator[Type]:
    args = get_args(tp)
    if not args:
        raise TypeError()

    yield tuple
    for arg in args:
        if arg is Ellipsis:
            continue

        yield from _evaluate_array_arg(arg)


def _evaluate_array_arg(arg: Any) -> Iterator[Type]:
    if isinstance(arg, TypeVar):
        yield from _evaluate_typevar(arg)
    else:
        origin = get_origin(arg)
        if origin is None:
            yield arg
        elif origin in (Union, UnionType, list, tuple):
            yield from __evaluations__[origin](arg)
        else:
            raise TypeError()


def _evaluate_union(tp: Any) -> Iterator[Type]:
    args = get_args(tp)
    if not args:
        raise TypeError()

    origin_locked = False
    for arg in args:
        if arg is NONE_TYPE:
            continue

        if isinstance(arg, TypeVar):
            raise TypeError()

        origin = get_origin(arg)
        if origin is None:
            yield arg
        elif origin is list and not origin_locked:
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
    tuple: _evaluate_tuple,
    list: _evaluate_list,
    dict: _evaluate_mapping,
    Union: _evaluate_union,
    UnionType: _evaluate_union,
    type: _evaluate_type,
    TypeVar: _evaluate_typevar,
}
