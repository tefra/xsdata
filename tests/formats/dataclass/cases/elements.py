from typing import Dict, List, Optional, Tuple, Union

cases = [
    (Dict, False),
    (str, ((object,), None, None)),
    (List[str], ((object,), list, None)),
    (Tuple[str, ...], ((object,), tuple, None)),
    (Optional[Union[str, int]], ((object,), None, None)),
    (Union[str, int, None], ((object,), None, None)),
    (List[Union[List[str], Tuple[str, ...]]], ((object,), list, None)),
    (list[str], ((object,), list, None)),
    (tuple[str, ...], ((object,), tuple, None)),
    (list[Union[list[str], tuple[str, ...]]], ((object,), list, None)),
    (str | int | None, ((object,), None, None)),
    (list[list[str] | tuple[str, ...]], ((object,), list, None)),
]
