from dataclasses import dataclass, field
from typing import Optional


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
            name="number",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
    size: Optional[int] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace="http://datypic.com/prod"
        )
    )
    dept: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dept",
            type="Attribute",
            namespace="http://datypic.com/prod",
            required=True
        )
    )
