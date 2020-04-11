from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MediumDressSize:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=8.0,
            max_inclusive=12.0,
            pattern=r"\d{1,2}"
        )
    )
