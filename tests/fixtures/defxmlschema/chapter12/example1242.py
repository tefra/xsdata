from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OpenProductType:
    """
    :ivar local_element:
    :ivar number:
    :ivar name:
    """
    local_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="##local",
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
class Something:
    """
    :ivar value:
    """
    class Meta:
        name = "something"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension",
            required=True
        )
    )


@dataclass
class Product(OpenProductType):
    class Meta:
        name = "product"
