from decimal import Decimal
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class PurchaseOrderType:
    """
    :ivar description:
    :ivar comment:
    :ivar id:
    :ivar version:
    :ivar attributes:
    """
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
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id",
            type="Attribute",
            required=True
        )
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )
