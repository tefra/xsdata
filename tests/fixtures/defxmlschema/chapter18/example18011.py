from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/prod"


@dataclass
class Color:
    """
    :ivar value:
    """
    class Meta:
        name = "color"
        namespace = "http://datypic.com/prod"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Size:
    """
    :ivar value:
    """
    class Meta:
        name = "size"
        namespace = "http://datypic.com/prod"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2.0,
            max_inclusive=16.0
        )
    )
