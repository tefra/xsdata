from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter04.example04032 import (
    ItemsType,
)

__NAMESPACE__ = "http://datypic.com/ord"


@dataclass
class OrderType:
    """
    :ivar number:
    :ivar items:
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    items: Optional[ItemsType] = field(
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
