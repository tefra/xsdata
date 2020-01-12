from dataclasses import dataclass, field
from typing import Optional


@dataclass
class InternationalSizeType:
    """
    :ivar value:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Union",
            min_inclusive=24.0,
            max_inclusive=54.0
        )
    )
