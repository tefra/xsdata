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
class ShirtType(ProductType):
    """
    :ivar size:
    :ivar color:
    """
    size: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    color: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"


@dataclass
class Shirt(ShirtType):
    class Meta:
        name = "shirt"
