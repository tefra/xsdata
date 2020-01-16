from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar size:
    :ivar color:
    :ivar eff_date:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
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
            max_occurs=3
        )
    )
    color: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="color",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    eff_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
