from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PurchaseOrderType:
    """
    :ivar id:
    :ivar version:
    :ivar description:
    :ivar comment:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id",
            type="Attribute",
            required=True
        )
    )
    version: Optional[float] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="comment",
            type="Element",
            namespace="http://datypic.com/prod"
        )
    )
