from collections.abc import Mapping
from typing import Dict, List, Set, Tuple

cases = [
    (int, False),
    (Set, False),
    (List, False),
    (Tuple, False),
    (Dict[str, int], False),
    (Dict, ((str,), dict, None)),
    (Dict[str, str], ((str,), dict, None)),
    (Mapping[str, str], ((str,), dict, None)),
    (dict[str, str], ((str,), dict, None)),
]
