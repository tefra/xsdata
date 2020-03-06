from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar size:
    :ivar color:
    :ivar other_element:
    :ivar eff_date:
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
    size: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="size",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=3
        )
    )
    color: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="color",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=3
        )
    )
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Any",
            namespace="##other",
            required=True
        )
    )
    eff_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="effDate",
            type="Attribute"
        )
    )
