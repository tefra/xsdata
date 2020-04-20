from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://datypic.com/ord"


@dataclass
class RestrictedProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar dept:
    """
    number: Optional[str] = field(
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
            namespace="http://datypic.com/prod",
            required=True
        )
    )
