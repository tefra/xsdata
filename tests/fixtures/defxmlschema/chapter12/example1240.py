from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OpenProductType:
    """
    :ivar other_element:
    :ivar number:
    :ivar name:
    """
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            required=True
        )
    )
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


@dataclass
class Product(OpenProductType):
    class Meta:
        name = "product"
