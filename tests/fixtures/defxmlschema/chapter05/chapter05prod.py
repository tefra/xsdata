from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://example.org/prod"


@dataclass
class SizeType:
    """
    :ivar value:
    :ivar system:
    """
    value: Optional[int] = field(
        default=None,
    )
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
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
    size: Optional[SizeType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True,
            nillable=True
        )
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"
        namespace = "http://example.org/prod"
