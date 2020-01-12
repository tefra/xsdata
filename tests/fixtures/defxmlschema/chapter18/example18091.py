from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Size:
    """
    :ivar value:
    """
    class Meta:
        name = "size"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_inclusive=0.0,
            max_inclusive=18.0
        )
    )
