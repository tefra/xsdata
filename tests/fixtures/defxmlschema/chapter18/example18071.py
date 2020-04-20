from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class IdentifierGroup:
    """
    :ivar id:
    :ivar version:
    :ivar lang:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
