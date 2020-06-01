from collections import defaultdict
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence


def unique_sequence(items: Sequence, key: Optional[str] = None) -> List:
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
