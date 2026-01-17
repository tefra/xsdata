from collections.abc import Iterable
from typing import Dict, List, Literal, Optional, Set, Tuple, Union

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
    (list[int, int], False),
    (dict[str, str], False),
    (dict, False),
    (set[str], False),
    (tuple[int, ...], ((int,), None, tuple)),
    (list[int], ((int,), None, list)),
    (list[Union[str, int]], ((str, int), None, list)),
    (tuple[int | str], ((int, str), None, tuple)),
]

not_tokens = [
    (List[int], False),
    (Dict[int, str], False),
    (int, ((int,), None, None)),
    (str, ((str,), None, None)),
    (Union[str, Mode], ((str, Mode), None, None)),
    (int | str, ((int, str), None, None)),
]
