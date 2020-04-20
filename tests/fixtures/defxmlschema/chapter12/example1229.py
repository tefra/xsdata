from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AorBorBothType:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "AOrBOrBothType"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2
        )
    )
