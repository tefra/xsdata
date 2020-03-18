from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OpenProductType:
    """
    :ivar number:
    :ivar name:
    :ivar local_element:
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
    local_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="##local",
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
