from dataclasses import dataclass, field
from typing import List


@dataclass
class VectorType:
    """
    :ivar e:
    """
    e: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class ArrayType:
    """
    :ivar r:
    """
    r: List[VectorType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Array(ArrayType):
    class Meta:
        name = "array"
