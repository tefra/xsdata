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
class Umbrella:
    """
    :ivar value:
    """
    class Meta:
        name = "umbrella"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class ShirtType(ProductType):
    """
    :ivar size:
    :ivar color:
    """
    size: Optional[ShirtSizeType] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace="",
            required=True
        )
    )
    color: Optional[ColorType] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Hat(ProductType):
    """
    :ivar size:
    """
    class Meta:
        name = "hat"

    size: Optional[HatSizeType] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Product(ProductType):
    class Meta:
        name = "product"



@dataclass
class ItemsType:
    """
    :ivar product:
    """
    product: List[Product] = field(
        default_factory=list,
        metadata=dict(
            name="product",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Shirt(ShirtType):
    class Meta:
        name = "shirt"



@dataclass
class Items(ItemsType):
    class Meta:
        name = "items"
