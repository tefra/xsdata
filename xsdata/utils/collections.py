from typing import Any
from typing import List
from typing import Sequence


def unique_sequence(items: Sequence, key: str) -> List:
    seen = set()

    def is_new(val: Any) -> bool:
        if val in seen:
            return False

        seen.add(val)
        return True

    return [item for item in items if is_new(getattr(item, key))]
