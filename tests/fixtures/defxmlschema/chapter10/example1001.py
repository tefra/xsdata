from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Size:
    """
    :ivar value:
    """
    value: Optional[Union[int, str]] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Union",
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
