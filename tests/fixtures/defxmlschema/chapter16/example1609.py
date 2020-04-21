from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter16.example1606 import (
    ItemsType,
)
from tests.fixtures.defxmlschema.chapter22.example2207 import (
    ProductType,
)
from tests.fixtures.defxmlschema.chapter13.example13011 import (
    SizeType,
)


@dataclass
class Color:
    """
    :ivar value:
    """
    class Meta:
        name = "color"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"


@dataclass
class Size(SizeType):
    class Meta:
        name = "size"
