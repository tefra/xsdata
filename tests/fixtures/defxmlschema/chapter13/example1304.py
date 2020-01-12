from dataclasses import dataclass, field
from typing import Optional


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
            name="number",
            type="Element",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            required=True
        )
    )
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
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
    shirt: Optional[Shirt] = field(
        default=None,
        metadata=dict(
            name="shirt",
            type="Element"
        )
    )
    hat: Optional[Hat] = field(
        default=None,
        metadata=dict(
            name="hat",
            type="Element"
        )
    )
    umbrella: Optional[Umbrella] = field(
        default=None,
        metadata=dict(
            name="umbrella",
            type="Element"
        )
    )


@dataclass
class ExpandedItemsType(ItemsType):
    """
    :ivar sweater:
    :ivar suit:
    """
    sweater: Optional[Sweater] = field(
        default=None,
        metadata=dict(
            name="sweater",
            type="Element"
        )
    )
    suit: Optional[Suit] = field(
        default=None,
        metadata=dict(
            name="suit",
            type="Element"
        )
    )
