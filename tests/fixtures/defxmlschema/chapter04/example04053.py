from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OrderDetails:
    """
    :ivar value:
    """
    class Meta:
        name = "orderDetails"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
