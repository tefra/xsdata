from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SmallDressSizeType:
    """
    :ivar value:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension",
            required=True,
            min_inclusive=2.0,
            max_inclusive=6.0,
            pattern=r"\d{1}"
        )
    )
