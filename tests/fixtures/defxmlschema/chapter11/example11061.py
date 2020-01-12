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
    :ivar refs:
    """
    class Meta:
        name = "quote"

    refs: Optional[str] = field(
        default=None,
        metadata=dict(
            name="refs",
            type="Attribute"
        )
    )
