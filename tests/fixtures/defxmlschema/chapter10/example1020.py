from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TwoDimensionalArray:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="List"
        )
    )
