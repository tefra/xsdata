from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BaseType:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class DerivedType(BaseType):
    """
    :ivar id:
    :ivar name:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id",
            type="Attribute",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Attribute"
        )
    )
