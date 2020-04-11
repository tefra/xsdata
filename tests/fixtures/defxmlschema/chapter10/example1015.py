from dataclasses import dataclass, field
from typing import List


@dataclass
class VectorType:
    """
    :ivar value:
    """
    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
