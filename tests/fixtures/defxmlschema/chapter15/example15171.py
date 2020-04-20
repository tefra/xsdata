from decimal import Decimal
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional

__NAMESPACE__ = "http://datypic.com/ord"


@dataclass
class PurchaseOrderType:
    """
    :ivar description:
    :ivar comment:
    :ivar id:
    :ivar version:
    :ivar other_attributes:
    """
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/prod"
        )
    )
    comment: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/prod"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    other_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )
