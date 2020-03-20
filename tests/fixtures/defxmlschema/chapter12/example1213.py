from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2
        )
    )
