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
            type="Element",
            namespace=""
        )
    )
    shirt: Optional[ShirtType] = field(
        default=None,
        metadata=dict(
            name="shirt",
            type="Element",
            namespace=""
        )
    )
    hat: Optional[HatType] = field(
        default=None,
        metadata=dict(
            name="hat",
            type="Element",
            namespace=""
        )
    )
    umbrella: Optional[ProductType] = field(
        default=None,
        metadata=dict(
            name="umbrella",
            type="Element",
            namespace=""
        )
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
