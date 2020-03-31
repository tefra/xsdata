from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.defxmlschema.chapter16.example1602 import (
    Hat,
    Shirt,
    Umbrella,
)


@dataclass
class ColorType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Attribute"
        )
    )


@dataclass
class HatSizeType:
    """
    :ivar value:
    :ivar system:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            name="system",
            type="Attribute"
        )
    )


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class ShirtSizeType:
    """
    :ivar value:
    :ivar system:
    """
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            name="system",
            type="Attribute"
        )
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"



@dataclass
class ItemsType:
    """
    :ivar umbrella:
    :ivar hat:
    :ivar shirt:
    :ivar product:
    """
    umbrella: List[Umbrella] = field(
        default_factory=list,
        metadata=dict(
            name="umbrella",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    hat: List[Hat] = field(
        default_factory=list,
        metadata=dict(
            name="hat",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    shirt: List[Shirt] = field(
        default_factory=list,
        metadata=dict(
            name="shirt",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    product: List[Product] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
