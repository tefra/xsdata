from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter21.example21162 import (
    ItemsType,
)


@dataclass
class OrderType:
    """
    :ivar number:
    :ivar items:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="http://datypic.com/ord",
            required=True
        )
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata=dict(
            name="items",
            type="Element",
            namespace="http://datypic.com/ord",
            required=True
        )
    )


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"
        namespace = "http://datypic.com/ord"
