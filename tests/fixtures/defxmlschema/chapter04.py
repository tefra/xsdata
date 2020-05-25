from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter04cust import (
    CustomerType,
)
from tests.fixtures.defxmlschema.chapter04prod import (
    ItemsType,
)

__NAMESPACE__ = "http://example.org/ord"


@dataclass
class OrderType:
    """
    :ivar number:
    :ivar customer:
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
    customer: Optional[CustomerType] = field(
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
        namespace = "http://example.org/ord"
