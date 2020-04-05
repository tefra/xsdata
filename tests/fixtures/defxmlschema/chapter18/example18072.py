from dataclasses import dataclass, field
from typing import Optional


@dataclass
class IdentifierGroup:
    """
    :ivar eff_date:
    """
    eff_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
