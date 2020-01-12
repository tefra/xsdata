from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Name:
    """
    :ivar value:
    """
    class Meta:
        name = "name"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class Size:
    """
    :ivar value:
    """
    class Meta:
        name = "size"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class ProductType:
    """
    :ivar name:
    :ivar size:
    """
    name: Optional[Name] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            required=True
        )
    )
    size: Optional[Size] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element"
        )
    )
