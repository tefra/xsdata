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
            type="Element",
            namespace="",
            required=True
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
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
            type="Element",
            required=True
        )
    )
