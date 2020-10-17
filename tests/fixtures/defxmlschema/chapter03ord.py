from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.defxmlschema.chapter03prod import Product

__NAMESPACE__ = "http://example.org/ord"


@dataclass
class ItemsType:
    """
    :ivar product:
    """
    product: List[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/prod",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderType:
    """
    :ivar number:
    :ivar items:
    """
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ord",
            "required": True,
        }
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ord",
            "required": True,
        }
    )


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"
        namespace = "http://example.org/ord"
