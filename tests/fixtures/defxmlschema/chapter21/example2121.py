from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter17.chapter17 import (
    ItemsType,
    OrderType,
    ProductType,
)


@dataclass
class Size:
    """
    :ivar value:
    """
    class Meta:
        name = "size"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"
