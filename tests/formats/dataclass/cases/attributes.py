from typing import Dict, List, Set, Tuple

from tests.formats.dataclass.cases import PY39

cases = [
    (int, False),
    (Set, False),
    (List, False),
    (Tuple, False),
    (Dict[str, int], False),
    (Dict, ((str,), dict, None)),
    (Dict[str, str], ((str,), dict, None)),
]

if PY39:
    cases.extend(
        [
            (dict[str, str], ((str,), dict, None)),
        ]
    )
