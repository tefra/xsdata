from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar

from xsdata.formats.dataclass.models.constants import XmlType

T = TypeVar("T")


@dataclass
class AnyElement:
    """
    Generic ElementNode dataclass to bind xml document data to wildcard fields.

    :param qname: The namespace qualified name.
    :param text: Element text content.
    :param tail: Element tail content.
    :param ns_map: The prefix-URI Namespace mapping
    :param children: A list of child elements.
    :param attributes: The element key-value attribute mapping.
    """

    qname: Optional[str] = field(default=None)
    text: Optional[str] = field(default=None)
    tail: Optional[str] = field(default=None)
    ns_map: Dict = field(default_factory=dict)
    children: List[object] = field(
        default_factory=list, metadata={"type": XmlType.WILDCARD}
    )
    attributes: Dict = field(
        default_factory=dict, metadata={"type": XmlType.ATTRIBUTES}
    )


@dataclass
class DerivedElement(Generic[T]):
    """
    Derived element wrapper for base types, eg. <b xsi:type="a">...</b>

    :param qname: The namespace qualified name of the base type.
    :param value: A dataclass instance
    """

    qname: str
    value: T
