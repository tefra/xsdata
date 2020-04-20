from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/prod"


@dataclass
class SizeType:
    """
    :ivar system:
    :ivar dim:
    """
    system: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    dim: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://datypic.com/prod"
        )
    )
