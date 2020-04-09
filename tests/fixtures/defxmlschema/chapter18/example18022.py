from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NewSize:
    """
    :ivar value:
    """
    class Meta:
        name = "newSize"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
