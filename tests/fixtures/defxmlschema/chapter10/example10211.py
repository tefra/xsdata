from dataclasses import dataclass, field
from typing import Optional


@dataclass
class VectorType:
    """
    :ivar e:
    """
    e: Optional[int] = field(
        default=None,
        metadata=dict(
            name="e",
            type="Element",
            required=True
        )
    )


@dataclass
class ArrayType:
    """
    :ivar r:
    """
    r: Optional[VectorType] = field(
        default=None,
        metadata=dict(
            name="r",
            type="Element",
            required=True
        )
    )


@dataclass
class Array(ArrayType):
    class Meta:
        name = "array"
