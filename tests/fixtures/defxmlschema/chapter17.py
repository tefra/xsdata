from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class ColorType:
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PriceType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProductOrderType:
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    color: Optional[ColorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProductType:
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    price: Optional[PriceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ItemsType:
    shirt_or_hat: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "shirt",
                    "type": ProductOrderType,
                    "namespace": "",
                },
                {
                    "name": "hat",
                    "type": ProductOrderType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class ProductsType:
    product: List[ProductType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderType:
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    products: Optional[ProductsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"
