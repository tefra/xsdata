from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SmallDressSizeType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2.0,
            max_inclusive=6.0,
            pattern=r"\d{1}"
        )
    )
