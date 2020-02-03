from dataclasses import dataclass, field
from typing import List


@dataclass
class DescType:
    """
    :ivar i:
    :ivar b:
    :ivar u:
    """
    class Meta:
        mixed = True

    i: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="i",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="b",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    u: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="u",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Desc(DescType):
    class Meta:
        name = "desc"
