from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescriptionType:
    """
    :ivar source:
    :ivar content:
    """
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    content: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Description(DescriptionType):
    class Meta:
        name = "description"
