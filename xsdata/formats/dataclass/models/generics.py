from dataclasses import dataclass, field
from typing import Dict, Generic, List, Optional, TypeVar

from xsdata.formats.dataclass.models.elements import XmlType

T = TypeVar("T", bound=object)


@dataclass
class AnyElement:
    """Generic model to bind xml document data to wildcard fields.

    Args:
        qname: The element's qualified name
        text: The element's text content
        tail: The element's tail content
        children: The element's list of child elements.
        attributes: The element's key-value attribute mappings.
    """

    qname: Optional[str] = field(default=None)
    text: Optional[str] = field(default=None)
    tail: Optional[str] = field(default=None)
    children: List[object] = field(
        default_factory=list, metadata={"type": XmlType.WILDCARD}
    )
    attributes: Dict[str, str] = field(
        default_factory=dict, metadata={"type": XmlType.ATTRIBUTES}
    )


@dataclass
class DerivedElement(Generic[T]):
    """Generic model wrapper for type substituted elements.

    Example: eg. <b xsi:type="a">...</b>

    Args:
        qname: The element's qualified name
        value: The wrapped value
        type: The real xsi:type
    """

    qname: str
    value: T
    type: Optional[str] = None
