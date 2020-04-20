from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/prod"


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar dept:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://datypic.com/prod"
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://datypic.com/prod"
        )
    )
