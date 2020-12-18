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
    Generic model to bind xml document data to wildcard fields.

    :param qname: The element's qualified name
    :param text: The element's text content
    :param tail: The element's tail content
    :param children: The element's list of child elements.
    :param attributes: The element's key-value attribute mappings.
    """

    qname: Optional[str] = field(default=None)
    text: Optional[str] = field(default=None)
    tail: Optional[str] = field(default=None)
    children: List[object] = field(
        default_factory=list, metadata={"type": XmlType.WILDCARD}
    )
    attributes: Dict = field(
        default_factory=dict, metadata={"type": XmlType.ATTRIBUTES}
    )


@dataclass
class DerivedElement(Generic[T]):
    """
    Generic model wrapper for inline declared elements, eg. <b
    xsi:type="a">...</b>

    :param qname: The element's qualified name
    :param value: The wrapped value
    """

    qname: str
    value: T
