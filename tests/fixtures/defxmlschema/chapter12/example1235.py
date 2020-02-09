from dataclasses import dataclass, field
from typing import List


@dataclass
class DescriptionType:
    """
    :ivar elements:
    """
    class Meta:
        mixed = True

    elements: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="elements",
            type="Any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
