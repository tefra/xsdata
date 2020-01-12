from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Comment:
    """
    :ivar value:
    """
    class Meta:
        name = "comment"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class Description:
    """
    :ivar value:
    """
    class Meta:
        name = "description"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class DescriptionGroup:
    """
    :ivar description:
    :ivar comment:
    """
    description: Optional[Description] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            required=True
        )
    )
    comment: Optional[Comment] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element"
        )
    )
