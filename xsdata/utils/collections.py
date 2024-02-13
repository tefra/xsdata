from collections import defaultdict
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Set,
    TypeVar,
)

T = TypeVar("T")


def is_array(value: Any) -> bool:
    """Return whether the value is a list style type."""
    if isinstance(value, tuple):
        return not hasattr(value, "_fields")

    return isinstance(value, (list, set, frozenset))


def unique_sequence(items: Iterable[T], key: Optional[str] = None) -> List[T]:
    """Return a new unique list, preserving the original order.

    Args:
        items: The iterable to filter
        key: An optional callable to generate the unique keys

    Returns:
        A new unique list.
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


def remove(items: Iterable[T], predicate: Callable) -> List[T]:
    """Return a new list without the items that match the predicate."""
    return [x for x in items if not predicate(x)]


def group_by(items: Iterable[T], key: Callable) -> Dict[Any, List[T]]:
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
    """Return the index of the value in the given sequence.

    Args:
        items: The sequence to search in
        value: The value to search for

    Returns:
        The index in the sequence or -1 if the value is not found.
    """
    try:
        return items.index(value)
    except ValueError:
        return -1


def first(items: Iterator[T]) -> Optional[T]:
    """Return the first item of the iterator."""
    return next(items, None)


def prepend(target: List, *args: Any):
    """Prepend items to the target list."""
    target[:0] = args


def connected_components(lists: List[List[Any]]) -> Iterator[List[Any]]:
    """Merge lists of lists that share common elements."""
    neighbors = defaultdict(set)
    for each in lists:
        for item in each:
            neighbors[item].update(each)

    def component(node: Any, neigh: Dict[Any, Set], see: Set[Any]):
        nodes = {node}
        while nodes:
            next_node = nodes.pop()
            see.add(next_node)
            nodes |= neigh[next_node] - see
            yield next_node

    seen: Set[Any] = set()
    for item in neighbors:
        if item not in seen:
            yield sorted(component(item, neighbors, seen))


def find_connected_component(groups: List[List[Any]], value: Any) -> int:
    """Find the list index that contains the given value."""
    for index, group in enumerate(groups):
        if value in group:
            return index

    return -1
