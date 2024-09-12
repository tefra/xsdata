import sys
from typing import (
    Any,
    Callable,
    NamedTuple,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from typing_extensions import get_args, get_origin

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
elif sys.version_info[:2] >= (3, 13):
    # python 3.13+ requires type_params argument
    from typing import _eval_type as __eval_type  # type: ignore

    def _eval_type(tp: Any, globalns: Any, localns: Any) -> Any:
        return __eval_type(tp, globalns, localns, type_params=())
else:
    from typing import _eval_type  # type: ignore


NONE_TYPE = type(None)
UNION_TYPES = (Union, UnionType)
ITERABLE_TYPES = (list, tuple)


def evaluate(tp: Any, globalns: Any, localns: Any = None) -> Any:
    """Analyze/Validate the typing annotation."""
    result = _eval_type(tp, globalns, localns)

    # Ugly hack for the Type["str"]
    # Let's switch to ForwardRef("str")
    if get_origin(result) is type:
        args = get_args(result)
        if len(args) != 1:
            raise TypeError

        return args[0]

    return result


class Result(NamedTuple):
    types: Tuple[Type[Any], ...]
    factory: Optional[Callable] = None
    tokens_factory: Optional[Callable] = None


def analyze_token_args(origin: Any, args: Tuple[Any, ...]) -> Tuple[Any]:
    """Analyze token arguments.

    Ensure it only has one argument, filter out ellipsis.

    Args
        origin: The annotation origin
        args: The annotation arguments

    Returns:
        A tuple that contains only one arg

    Raises:
        TypeError: If the origin is not list or tuple,
            and it has more than one argument

    """
    if origin in ITERABLE_TYPES:
        args = filter_ellipsis(args)
        if len(args) == 1:
            return args

    raise TypeError


def analyze_optional_origin(
    origin: Any, args: Tuple[Any, ...], types: Tuple[Any, ...]
) -> Tuple[Any, ...]:
    """Analyze optional type annotations.

    Remove the NoneType, adjust and return the origin, args and types.

    Args
        origin: The annotation origin
        args: The annotation arguments
        types: The annotation types

    Returns:
        The old or new origin args and types.
    """
    if origin in UNION_TYPES:
        new_args = filter_none_type(args)
        if len(new_args) == 1:
            return get_origin(new_args[0]), get_args(new_args[0]), new_args

    return origin, args, types


def filter_none_type(args: Tuple[Any, ...]) -> Tuple[Any, ...]:
    return tuple(arg for arg in args if arg is not NONE_TYPE)


def filter_ellipsis(args: Tuple[Any, ...]) -> Tuple[Any]:
    return tuple(arg for arg in args if arg is not Ellipsis)


def evaluate_text(annotation: Any, tokens: bool = False) -> Result:
    """Run exactly the same validations with attribute."""
    return evaluate_attribute(annotation, tokens)


def evaluate_attribute(annotation: Any, tokens: bool = False) -> Result:
    """Validate annotations for a xml attribute."""
    types = (annotation,)
    origin = get_origin(annotation)
    args = get_args(annotation)
    tokens_factory = None

    if tokens:
        origin, args, types = analyze_optional_origin(origin, args, types)

        args = analyze_token_args(origin, args)
        tokens_factory = origin
        origin = get_origin(args[0])

        if origin in UNION_TYPES:
            args = get_args(args[0])
        elif origin:
            raise TypeError

    if origin in UNION_TYPES:
        types = filter_none_type(args)
    elif origin is None:
        types = args or (annotation,)
    else:
        raise TypeError

    if any(get_origin(tp) for tp in types):
        raise TypeError

    return Result(types=types, tokens_factory=tokens_factory)


def evaluate_attributes(annotation: Any, **_: Any) -> Result:
    """Validate annotations for xml wildcard attributes."""
    if annotation is dict:
        args = ()
    else:
        origin = get_origin(annotation)
        args = get_args(annotation)

        if origin is not dict and annotation is not dict:
            raise TypeError

    if args and not all(arg is str for arg in args):
        raise TypeError

    return Result(types=(str,), factory=dict)


def evaluate_element(annotation: Any, tokens: bool = False) -> Result:
    """Validate annotations for a xml element."""

    # Only the derived element value field is allowed a typevar
    if isinstance(annotation, TypeVar) and annotation.__bound__ is object:
        annotation = object

    types = (annotation,)
    origin = get_origin(annotation)
    args = get_args(annotation)
    tokens_factory = factory = None

    origin, args, types = analyze_optional_origin(origin, args, types)

    if tokens:
        args = analyze_token_args(origin, args)

        tokens_factory = origin
        origin = get_origin(args[0])
        types = args
        args = get_args(args[0])

    if origin in ITERABLE_TYPES:
        args = tuple(arg for arg in args if arg is not Ellipsis)
        if len(args) != 1:
            raise TypeError

        if tokens_factory:
            factory = tokens_factory
            tokens_factory = origin
        else:
            factory = origin

        types = args
        origin = get_origin(args[0])
        args = get_args(args[0])

    if origin in UNION_TYPES:
        types = filter_none_type(args)
    elif origin:
        raise TypeError

    return Result(types=types, factory=factory, tokens_factory=tokens_factory)


def evaluate_elements(annotation: Any, **_: Any) -> Result:
    """Validate annotations for a xml compound field."""
    (
        types,
        factory,
        __,
    ) = evaluate_element(annotation, tokens=False)

    for tp in types:
        evaluate_element(tp, tokens=False)

    return Result(types=(object,), factory=factory)


def evaluate_wildcard(annotation: Any, **_: Any) -> Result:
    """Validate annotations for a xml wildcard."""
    origin = get_origin(annotation)
    factory = None

    if origin in UNION_TYPES:
        types = filter_none_type(get_args(annotation))
    elif origin in ITERABLE_TYPES:
        factory = origin
        types = filter_ellipsis(get_args(annotation))
    elif origin is None:
        types = (annotation,)
    else:
        raise TypeError

    if len(types) != 1 or object not in types:
        raise TypeError

    return Result(types=types, factory=factory)
