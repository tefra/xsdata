from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AvailableSizesType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            max_length=3.0
        )
    )
