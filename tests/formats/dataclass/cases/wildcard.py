from collections.abc import Iterable
from typing import Dict, List, Literal, Optional, Set, Tuple

from tests.formats.dataclass.cases import PY310

cases = [
    (int, False),
    (Dict[int, int], False),
    (Dict, False),
    (Set, False),
    (Literal["foo"], False),
    (object, ((object,), None, None)),
    (List[object], ((object,), list, None)),
    (Tuple[object, ...], ((object,), tuple, None)),
    (Iterable[object, ...], ((object,), list, None)),
    (Optional[object], ((object,), None, None)),
]

if PY310:
    cases.extend(
        [
            (list[object], ((object,), list, None)),
            (tuple[object, ...], ((object,), tuple, None)),
            (object | None, ((object,), None, None)),
        ]
    )
