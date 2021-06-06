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
    Return a new list with the unique values from an iterable.

    Optionally you can also provide a lambda to generate the unique key
    of each item in the iterable object.
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
    """Group the items of an iterable object by the result of the callable."""
    result = defaultdict(list)
    for item in items:
        result[key(item)].append(item)
    return result


def apply(items: Iterable, func: Callable):
    """Apply the given function to each item of the iterable object."""
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


def prepend(target: List, *args: Any):
    """Prepend items to the target list."""
    target[:0] = args
