from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ProductType:
    """
    :ivar other_element:
    :ivar number:
    :ivar name:
    """
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="##other",
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
    :ivar any_element:
    :ivar size:
    :ivar color:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="##any",
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
