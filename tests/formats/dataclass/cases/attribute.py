from collections.abc import Iterable
from typing import Dict, List, Literal, Optional, Set, Tuple, Union

from tests.formats.dataclass.cases import PY39, PY310
from xsdata.models.enums import Mode

tokens = [
    (int, False),
    (Dict[int, int], False),
    (Dict, False),
    (Literal["foo"], False),
    (Set[str], False),
    (List[Union[List[int], int]], False),
    (List[List[int]], False),
    (Tuple[int, ...], ((int,), None, tuple)),
    (Iterable[int], ((int,), None, list)),
    (List[int], ((int,), None, list)),
    (List[Union[str, int]], ((str, int), None, list)),
    (Optional[List[Union[str, int]]], ((str, int), None, list)),
]

not_tokens = [
    (List[int], False),
    (Dict[int, str], False),
    (int, ((int,), None, None)),
    (str, ((str,), None, None)),
    (Union[str, Mode], ((str, Mode), None, None)),
]

if PY39:
    tokens.extend(
        [
            (list[int, int], False),
            (dict[str, str], False),
            (dict, False),
            (set[str], False),
            (tuple[int, ...], ((int,), None, tuple)),
            (list[int], ((int,), None, list)),
            (list[Union[str, int]], ((str, int), None, list)),
        ]
    )

if PY310:
    tokens.extend(
        [
            (tuple[int | str], ((int, str), None, tuple)),
        ]
    )

    not_tokens.extend(
        [
            (int | str, ((int, str), None, None)),
        ]
    )
