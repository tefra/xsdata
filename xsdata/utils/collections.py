from typing import Any
from typing import List
from typing import Optional
from typing import Sequence


def unique_sequence(items: Sequence, key: Optional[str] = None) -> List:
    seen = set()

    def is_new(val: Any) -> bool:
        if key:
            val = getattr(val, key)

        if val in seen:
            return False

        seen.add(val)
        return True

    return [item for item in items if is_new(item)]
