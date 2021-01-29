from collections import defaultdict
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import Sequence


def unique_sequence(items: Iterable, key: Optional[str] = None) -> List:
    """
    Return a new list with the unique values from the sequence.

    Optionally you can also provide a lambda to generate the unique key
    of each item in the sequence.
    """
    seen = set()

    def is_new(val: Any) -> bool:
        if key:
            val = getattr(val, key)

        if val in seen:
            return False

        seen.add(val)
        return True

    return [item for item in items if is_new(item)]


def remove(items: Iterable, predicate: Callable) -> List:
    """Return a new list without the items that match the predicate."""
    return [x for x in items if not predicate(x)]


def group_by(items: Iterable, key: Callable) -> Dict[Any, List]:
    """Group the items of a sequence by the result of the callable."""
    result = defaultdict(list)
    for item in items:
        result[key(item)].append(item)
    return result


def apply(items: Iterable, func: Callable):
    """Apply the given function to each item of the sequence."""
    for item in items:
        func(item)


def find(items: Sequence, value: Any) -> int:
    """Return the index of the value in the given sequence without raising
    exception in case of failure."""
    try:
        return items.index(value)
    except ValueError:
        return -1


def first(items: Iterator) -> Any:
    """Return the first item of the iterator."""
    return next(items, None)


def concat(*args: Iterable) -> Iterator:
    """Concatenate iterables into a single iterator."""
    for arg in args:
        yield from arg


def map_key(dictionary: Dict, search: Any) -> Any:
    """Find and return they key for given search value."""
    for key, value in dictionary.items():
        if value == search:
            return key

    return None


def prepend(target: List, *args: Any):
    """Prepend items to the target list."""
    target[:0] = args


class Immutable:
    """
    Immutable base class.

    Subclasses must initialize with -1 the `_hashcode` attribute after
    at the end of all other attributes to lock the instance from any
    further modifications.
    """

    __slots__ = ("_hashcode",)

    def __setattr__(self, *args: Any):
        try:
            object.__getattribute__(self, "_hashcode")
            raise TypeError(f"{self.__class__.__name__} is immutable")
        except AttributeError:
            object.__setattr__(self, *args)

    def __delattr__(self, *args: Any):
        raise TypeError(f"{self.__class__.__name__} is immutable")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.__cmp_value__() == other.__cmp_value__()

        return NotImplemented

    def __ne__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.__cmp_value__() != other.__cmp_value__()

        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.__cmp_value__() < other.__cmp_value__()

        return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.__cmp_value__() <= other.__cmp_value__()

        return NotImplemented

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.__cmp_value__() > other.__cmp_value__()

        return NotImplemented

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.__cmp_value__() >= other.__cmp_value__()

        return NotImplemented

    def __iter__(self) -> Iterator:
        for field_name in self.__slots__:
            if field_name[0] != "_":
                yield getattr(self, field_name)

    def __hash__(self) -> int:
        hashcode = object.__getattribute__(self, "_hashcode")

        if hashcode == -1:
            hashcode = hash(tuple(self))
            object.__setattr__(self, "_hashcode", hashcode)

        return hashcode

    def __cmp_value__(self) -> Any:
        return tuple(self)

    def as_dict(self) -> dict:
        """Return arguments as dictionary."""
        return dict(zip(self.__slots__, self))
