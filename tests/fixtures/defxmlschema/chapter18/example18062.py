from dataclasses import dataclass, field
from typing import Optional


@dataclass
class IdentifierGroup:
    """
    :ivar id:
    :ivar version:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    version: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
