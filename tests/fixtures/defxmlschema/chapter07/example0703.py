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
            type="Attribute"
        )
    )
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    dim: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    system: Optional["Attributes.Value"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Value(Enum):
        """
        :cvar US_DRESS:
        """
        US_DRESS = "US-DRESS"
