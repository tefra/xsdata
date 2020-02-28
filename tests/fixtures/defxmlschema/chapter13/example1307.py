from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar elements:
    :ivar number:
    :ivar name:
    """
    elements: Optional[object] = field(
        default=None,
        metadata=dict(
            name="elements",
            type="Any",
            required=True
        )
    )
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
class ShirtType(ProductType):
    """
    :ivar elements:
    :ivar size:
    :ivar color:
    """
    elements: Optional[object] = field(
        default=None,
        metadata=dict(
            name="elements",
            type="Any",
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
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Element",
            namespace="",
            required=True
        )
    )
