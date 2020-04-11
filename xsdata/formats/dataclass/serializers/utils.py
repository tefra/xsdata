from typing import Any

from lxml.etree import Element
from lxml.etree import QName

from xsdata.formats.converters import to_xml
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames


class SerializeUtils:
    @staticmethod
    def set_attributes(element: Element, values: Any, namespaces: Namespaces):
        for key, value in values.items():
            SerializeUtils.set_attribute(element, key, value, namespaces)

    @staticmethod
    def set_attribute(element: Element, key: Any, value: Any, namespaces: Namespaces):
        if key == QNames.XSI_NIL and (element.text or len(element) > 0):
            return

        if isinstance(key, QName):
            namespaces.add(key.namespace)

        value = to_xml(value, namespaces)
        if not value:
            return

        element.set(key, value)

    @staticmethod
    def set_nil_attribute(element: Element, nillable: bool, namespaces: Namespaces):
        if nillable and element.text is None and len(element) == 0:
            namespaces.add(Namespace.XSI.uri, Namespace.XSI.prefix)
            element.set(QNames.XSI_NIL, "true")

    @staticmethod
    def set_text(element: Element, value: Any, namespaces: Namespaces):
        value = to_xml(value, namespaces)
        if isinstance(value, str) and len(value) == 0:
            value = None
        element.text = value

    @staticmethod
    def set_tail(element: Element, value: Any, namespaces: Namespaces):
        value = to_xml(value, namespaces)
        if isinstance(value, str) and len(value) == 0:
            value = None
        element.tail = to_xml(value, namespaces)
