from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    """
    :ivar name:
    :ivar size:
    """
    class Meta:
        name = "product"

    name: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    size: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
