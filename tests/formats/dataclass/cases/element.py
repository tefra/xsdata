from collections.abc import Iterable
from typing import Dict, List, Optional, Set, Tuple, Union

tokens = [
    (Set, False),
    (Dict[str, int], False),
    (Tuple[str, str], False),
    (List[str], ((str,), None, list)),
    (Optional[List[str]], ((str,), None, list)),
    (Tuple[str, ...], ((str,), None, tuple)),
    (List[List[str]], ((str,), list, list)),
    (Optional[List[List[Union[str, int]]]], ((str, int), list, list)),
    (List[Tuple[str, ...]], ((str,), list, tuple)),
    (Iterable[Iterable[str, ...]], ((str,), list, list)),
    (Tuple[List[str], ...], ((str,), tuple, list)),
    (Optional[Tuple[List[str], ...]], ((str,), tuple, list)),
    (list[str], ((str,), None, list)),
    (tuple[str, ...], ((str,), None, tuple)),
    (list[list[str]], ((str,), list, list)),
    (list[tuple[str, ...]], ((str,), list, tuple)),
    (tuple[list[str], ...], ((str,), tuple, list)),
]

not_tokens = [
    (Set, False),
    (Dict[str, int], False),
    (Tuple[str, int], False),
    (List[List[str]], False),
    (List[Tuple[str, ...]], False),
    (Tuple[List[str], ...], False),
    (str, ((str,), None, None)),
    (List[str], ((str,), list, None)),
    (List[Union[str, int]], ((str, int), list, None)),
    (Optional[List[Union[str, int]]], ((str, int), list, None)),
    (Tuple[str, ...], ((str,), tuple, None)),
    (list[str], ((str,), list, None)),
    (tuple[str, ...], ((str,), tuple, None)),
]
