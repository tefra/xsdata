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


def group_by(items: Sequence, key: Callable) -> Dict[Any, List]:
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


def concat(*args: Iterable) -> Iterator:
    """Concatenate iterables into a single iterator."""
    for arg in args:
        yield from arg


def map_key(dictionary: Dict, search: Any) -> Any:
    """Find and return they key for given search value."""
    return next((key for key, val in dictionary.items() if val == search), None)


def prepend(target: List, *args: Any):
    """Prepend items to the target list."""
    target[:0] = args
