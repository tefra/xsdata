from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SmallSizeType:
    """
    :ivar value:
    :ivar system:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            min_inclusive=2.0,
            max_inclusive=6.0
        )
    )
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
