from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.defxmlschema.chapter16.example1601 import (
    Items,
    Product,
)


@dataclass
class DescribedType:
    """
    :ivar description:
    :ivar comment:
    """
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            required=True
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element"
        )
    )


@dataclass
class ItemsType(DescribedType):
    """
    :ivar product:
    """
    product: List[Product] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class PurchaseOrderType(DescribedType):
    """
    :ivar items:
    """
    items: Optional[Items] = field(
        default=None,
        metadata=dict(
            name="items",
            type="Element",
            required=True
        )
    )
