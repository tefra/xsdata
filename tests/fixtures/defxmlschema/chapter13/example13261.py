from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BaseType:
    """
    :ivar elements:
    :ivar a:
    """
    elements: Optional[object] = field(
        default=None,
        metadata=dict(
            name="elements",
            type="Any",
            required=True
        )
    )
    a: Optional[str] = field(
        default=None,
        metadata=dict(
            name="a",
            type="Element",
            namespace=""
        )
    )
