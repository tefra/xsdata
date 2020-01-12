from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Footnote:
    """
    :ivar id:
    """
    class Meta:
        name = "footnote"

    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id",
            type="Attribute",
            required=True
        )
    )


@dataclass
class Quote:
    """
    :ivar ref:
    """
    class Meta:
        name = "quote"

    ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ref",
            type="Attribute"
        )
    )
