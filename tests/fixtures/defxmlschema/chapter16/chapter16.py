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
    :ivar any_element:
    """
    class Meta:
        name = "umbrella"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            required=True
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
class Shirt(ShirtType):
    class Meta:
        name = "shirt"



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
