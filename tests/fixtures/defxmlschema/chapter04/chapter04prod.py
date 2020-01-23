from dataclasses import dataclass, field
from typing import Optional


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
class SizeType:
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
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar color:
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
    size: Optional[SizeType] = field(
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
class ItemsType:
    """
    :ivar product:
    """
    product: Optional[ProductType] = field(
        default=None,
        metadata=dict(
            name="product",
            type="Element",
            namespace="",
            required=True
        )
    )
