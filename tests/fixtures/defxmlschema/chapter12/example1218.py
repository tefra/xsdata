from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar color:
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
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            required=True
        )
    )
    color: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="color",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=3
        )
    )
