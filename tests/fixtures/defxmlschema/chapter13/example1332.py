from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


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
class DerivedType:
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
