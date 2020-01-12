from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MediumDressSize:
    """
    :ivar value:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            min_inclusive=8.0,
            max_inclusive=12.0,
            pattern=r"\d{1,2}"
        )
    )
