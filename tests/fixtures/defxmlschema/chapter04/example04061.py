from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter04.example04053 import (
    OrderDetails,
)
from tests.fixtures.defxmlschema.chapter04.example04052 import (
    OrderSummary,
)

__NAMESPACE__ = "http://datypic.com/root"


@dataclass
class RootType:
    """
    :ivar order_summary:
    :ivar order_details:
    """
    order_summary: Optional[OrderSummary] = field(
        default=None,
        metadata=dict(
            name="orderSummary",
            type="Element",
            namespace="http://datypic.com/ord",
            required=True
        )
    )
    order_details: Optional[OrderDetails] = field(
        default=None,
        metadata=dict(
            name="orderDetails",
            type="Element",
            namespace="http://datypic.com/ord",
            required=True
        )
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://datypic.com/root"
