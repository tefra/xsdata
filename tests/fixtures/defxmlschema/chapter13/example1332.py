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
    pass
