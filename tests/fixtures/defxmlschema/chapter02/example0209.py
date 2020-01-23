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
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class ShirtType(ProductType):
    """
    :ivar color:
    :ivar id:
    """
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id",
            type="Attribute",
            required=True
        )
    )
