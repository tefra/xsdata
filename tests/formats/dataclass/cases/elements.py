from typing import Dict, List, Optional, Tuple, Union

from tests.formats.dataclass.cases import PY39, PY310

cases = [
    (Dict, False),
    (str, ((object,), None, None)),
    (List[str], ((object,), list, None)),
    (Tuple[str, ...], ((object,), tuple, None)),
    (Optional[Union[str, int]], ((object,), None, None)),
    (Union[str, int, None], ((object,), None, None)),
    (List[Union[List[str], Tuple[str, ...]]], ((object,), list, None)),
]


if PY39:
    cases.extend(
        [
            (list[str], ((object,), list, None)),
            (tuple[str, ...], ((object,), tuple, None)),
            (list[Union[list[str], tuple[str, ...]]], ((object,), list, None)),
        ]
    )


if PY310:
    cases.extend(
        [
            (str | int | None, ((object,), None, None)),
            (list[list[str] | tuple[str, ...]], ((object,), list, None)),
        ]
    )
