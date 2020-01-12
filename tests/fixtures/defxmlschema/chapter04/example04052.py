from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OrderSummary:
    """
    :ivar value:
    """
    class Meta:
        name = "orderSummary"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
