from dataclasses import dataclass, field
from typing import List
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
    product: List[ProductType] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    shirt: List[ShirtType] = field(
        default_factory=list,
        metadata=dict(
            name="shirt",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hat: List[HatType] = field(
        default_factory=list,
        metadata=dict(
            name="hat",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    umbrella: List[ProductType] = field(
        default_factory=list,
        metadata=dict(
            name="umbrella",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
