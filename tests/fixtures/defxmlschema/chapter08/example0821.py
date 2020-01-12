from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DressSize:
    """
    :ivar value:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
