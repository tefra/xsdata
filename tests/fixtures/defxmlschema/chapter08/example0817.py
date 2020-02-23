from dataclasses import dataclass, field
from typing import Optional


@dataclass
class EvenDress:
    """
    :ivar value:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension",
            min_inclusive=2.0,
            max_inclusive=18.0,
            pattern=r"\d{1,2}"
        )
    )
