from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/ord"


@dataclass
class OrderType:
    """
    :ivar number:
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"
        namespace = "http://datypic.com/ord"
