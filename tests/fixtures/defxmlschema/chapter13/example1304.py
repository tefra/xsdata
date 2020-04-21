from dataclasses import dataclass, field
from typing import List, Optional


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
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Hat(ProductType):
    class Meta:
        name = "hat"


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"


@dataclass
class Shirt(ProductType):
    class Meta:
        name = "shirt"


@dataclass
class Suit(ProductType):
    class Meta:
        name = "suit"


@dataclass
class Sweater(ProductType):
    class Meta:
        name = "sweater"


@dataclass
class Umbrella(ProductType):
    class Meta:
        name = "umbrella"


@dataclass
class ItemsType:
    """
    :ivar shirt:
    :ivar hat:
    :ivar umbrella:
    """
    shirt: List[Shirt] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    hat: List[Hat] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    umbrella: List[Umbrella] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class ExpandedItemsType(ItemsType):
    """
    :ivar sweater:
    :ivar suit:
    """
    sweater: List[Sweater] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    suit: List[Suit] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
