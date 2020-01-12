from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DescriptionType:
    """
    :ivar description:
    :ivar comment:
    :ivar lang:
    """
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            required=True
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lang",
            type="Attribute"
        )
    )
