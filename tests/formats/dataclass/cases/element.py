from typing import Dict, List, Set, Tuple, Union

from tests.formats.dataclass.cases import PY39

tokens = [
    (Set, False),
    (Dict[str, int], False),
    (Tuple[str, str], False),
    (List[str], ((str,), None, list)),
    (Tuple[str, ...], ((str,), None, tuple)),
    (List[List[str]], ((str,), list, list)),
    (List[Tuple[str, ...]], ((str,), list, tuple)),
    (Tuple[List[str], ...], ((str,), tuple, list)),
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
    (Tuple[str, ...], ((str,), tuple, None)),
]

if PY39:
    tokens.extend(
        [
            (list[str], ((str,), None, list)),
            (tuple[str, ...], ((str,), None, tuple)),
            (list[list[str]], ((str,), list, list)),
            (list[tuple[str, ...]], ((str,), list, tuple)),
            (tuple[list[str], ...], ((str,), tuple, list)),
        ]
    )

    not_tokens.extend(
        [
            (list[str], ((str,), list, None)),
            (tuple[str, ...], ((str,), tuple, None)),
        ]
    )
