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
            namespace="",
            required=True
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element",
            namespace=""
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lang",
            type="Attribute"
        )
    )
