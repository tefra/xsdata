from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Attributes:
    """
    :ivar anything:
    :ivar color:
    :ivar dim:
    :ivar system:
    """
    class Meta:
        name = "attributes"

    anything: Optional[str] = field(
        default=None,
        metadata=dict(
            name="anything",
            type="Attribute"
        )
    )
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Attribute"
        )
    )
    dim: Optional[int] = field(
        default=None,
        metadata=dict(
            name="dim",
            type="Attribute"
        )
    )
    system: Optional["Attributes.Type"] = field(
        default=None,
        metadata=dict(
            name="system",
            type="Attribute"
        )
    )

    class Type(Enum):
        """
        :cvar US_DRESS:
        """
        US_DRESS = "US-DRESS"
