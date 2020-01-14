from dataclasses import dataclass, field
from typing import Optional
from tests.fixtures.defxmlschema.chapter16.example1607 import (
    HatType,
    ShirtType,
)
from tests.fixtures.defxmlschema.chapter22.example2207 import (
    ProductType,
)


@dataclass
class ItemsType:
    """
    :ivar product:
    :ivar shirt:
    :ivar hat:
    :ivar umbrella:
    """
    product: Optional[ProductType] = field(
        default=None,
        metadata=dict(
            name="product",
            type="Element"
        )
    )
    shirt: Optional[ShirtType] = field(
        default=None,
        metadata=dict(
            name="shirt",
            type="Element"
        )
    )
    hat: Optional[HatType] = field(
        default=None,
        metadata=dict(
            name="hat",
            type="Element"
        )
    )
    umbrella: Optional[ProductType] = field(
        default=None,
        metadata=dict(
            name="umbrella",
            type="Element"
        )
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
