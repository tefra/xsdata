from dataclasses import dataclass, field
from typing import Optional


@dataclass
class VectorType:
    """
    :ivar value:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            pattern=r"\d+\s+\d+\s+((\d+\s+){3})*\d+"
        )
    )
