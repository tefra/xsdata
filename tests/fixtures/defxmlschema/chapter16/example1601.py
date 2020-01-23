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
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
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
            name="product",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
