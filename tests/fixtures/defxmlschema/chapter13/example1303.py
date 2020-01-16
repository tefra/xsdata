from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ShirtType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar color:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            required=True
        )
    )
    size: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="size",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    color: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="color",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
