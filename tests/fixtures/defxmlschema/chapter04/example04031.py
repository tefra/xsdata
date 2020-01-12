from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter04.example04032 import (
    ItemsType,
)


@dataclass
class OrderType:
    """
    :ivar number:
    :ivar items:
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            required=True
        )
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata=dict(
            name="items",
            type="Element",
            required=True
        )
    )


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"
