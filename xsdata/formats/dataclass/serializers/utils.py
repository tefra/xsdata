from typing import Any

from lxml.etree import Element
from lxml.etree import QName

from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames


class SerializeUtils:
    @staticmethod
    def set_attributes(element: Element, values: Any, namespaces: Namespaces):
        """Set multiple element attributes from the given values dictionary."""
        for key, value in values.items():
            SerializeUtils.set_attribute(element, key, value, namespaces)

    @staticmethod
    def set_attribute(element: Element, key: Any, value: Any, namespaces: Namespaces):
        """Set element attribute from the given key and value."""
        if (
            value is None
            or (key == QNames.XSI_NIL and (element.text or len(element) > 0))
            or (isinstance(value, list) and len(value) == 0)
        ):
            return

        key = SerializeUtils.resolve_qname(key, namespaces)
        value = SerializeUtils.resolve_qname(value, namespaces)
        element.set(key, converter.to_string(value, namespaces=namespaces))

    @staticmethod
    def resolve_qname(value: Any, namespaces: Namespaces) -> Any:
        if not isinstance(value, str) or not value or value[0] != "{":
            return value

        try:
            qname = QName(value)
            namespaces.add(qname.namespace)
            return qname
        except ValueError:
            return value

    @staticmethod
    def set_nil_attribute(element: Element, nillable: bool, namespaces: Namespaces):
        """Set element xs:nil attribute if necessary."""
        if nillable and element.text is None and len(element) == 0:
            namespaces.add(Namespace.XSI.uri, Namespace.XSI.prefix)
            element.set(QNames.XSI_NIL, "true")

    @staticmethod
    def set_text(element: Element, value: Any, namespaces: Namespaces):
        """Set element text optional content from the given value."""
        value = converter.to_string(value, namespaces=namespaces)
        if isinstance(value, str) and len(value) == 0:
            value = None
        element.text = value

    @staticmethod
    def set_tail(element: Element, value: Any, namespaces: Namespaces):
        """Set element tail optional content from the given value."""
        value = converter.to_string(value, namespaces=namespaces)
        if isinstance(value, str) and len(value) == 0:
            value = None
        element.tail = value
