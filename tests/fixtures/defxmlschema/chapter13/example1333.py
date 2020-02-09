from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class BaseType:
    """
    :ivar attributes:
    """
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class DerivedType(BaseType):
    """
    :ivar id:
    :ivar name:
    """
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id",
            type="Attribute",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Attribute"
        )
    )
