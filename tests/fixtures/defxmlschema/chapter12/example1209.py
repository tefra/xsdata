from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescType:
    """
    :ivar i:
    :ivar b:
    :ivar u:
    """
    i: Optional[str] = field(
        default=None,
        metadata=dict(
            name="i",
            type="Element"
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            name="b",
            type="Element"
        )
    )
    u: Optional[str] = field(
        default=None,
        metadata=dict(
            name="u",
            type="Element"
        )
    )


@dataclass
class Desc(DescType):
    class Meta:
        name = "desc"
