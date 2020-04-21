from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"


@dataclass
class ItemsType:
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
class Items(ItemsType):
    class Meta:
        name = "items"
