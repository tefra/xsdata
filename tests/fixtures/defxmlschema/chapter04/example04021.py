from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter04.example04022 import (
    CustomerType,
)


@dataclass
class OrderType:
    """
    :ivar number:
    :ivar customer:
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    customer: Optional[CustomerType] = field(
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
