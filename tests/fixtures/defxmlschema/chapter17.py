from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ColorType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class PriceType:
    """
    :ivar value:
    :ivar currency:
    """
    value: Optional[Decimal] = field(
        default=None,
    )
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ProductOrderType:
    """
    :ivar quantity:
    :ivar color:
    :ivar number:
    """
    quantity: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    color: Optional[ColorType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    number: Optional[int] = field(
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
    :ivar price:
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
    price: Optional[PriceType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class ItemsType:
    """
    :ivar shirt:
    :ivar hat:
    """
    shirt: List[ProductOrderType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hat: List[ProductOrderType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class ProductsType:
    """
    :ivar product:
    """
    product: List[ProductType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class OrderType:
    """
    :ivar number:
    :ivar items:
    :ivar products:
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
    products: Optional[ProductsType] = field(
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
