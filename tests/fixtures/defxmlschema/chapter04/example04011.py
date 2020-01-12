from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OrderType:
    """
    :ivar number:
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            required=True
        )
    )


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"
