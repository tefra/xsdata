from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Country:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension",
            required=True
        )
    )
