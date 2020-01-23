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
            namespace=""
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace=""
        )
    )
    size: Optional[str] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace=""
        )
    )


@dataclass
class RestrictedProductType(ProductType):
    """
    :ivar number:
    :ivar size:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace=""
        )
    )
    size: Optional[str] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace=""
        )
    )


@dataclass
class ShirtType(ProductType):
    """
    :ivar color:
    """
    color: Optional[int] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Element",
            namespace="",
            required=True
        )
    )
