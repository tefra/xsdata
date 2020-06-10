from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from lxml.etree import Element
from lxml.etree import QName

from xsdata.exceptions import ParserError
from xsdata.formats.converters import to_python
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.logger import logger
from xsdata.models.enums import QNames
from xsdata.utils import text


class ParserUtils:
    @classmethod
    def parse_xsi_type(cls, element: Element) -> Optional[QName]:
        """Parse the elements xsi:type attribute if present."""
        xsi_type = element.attrib.get(QNames.XSI_TYPE)
        return (
            cls.parse_value([QName], xsi_type, None, element.nsmap)
            if xsi_type
            else None
        )

    @classmethod
    def parse_value(
        cls,
        types: List[Type],
        value: Any,
        default: Any = None,
        ns_map: Optional[Dict] = None,
        tokens: bool = False,
    ) -> Any:
        """Convert xml string values to s python primitive type."""

        if value is None:
            return None if callable(default) else default

        if tokens:
            value = value if isinstance(value, list) else filter(None, value.split(" "))
            return list(map(lambda x: to_python(types, x, ns_map), value))

        return to_python(types, value, ns_map)

    @classmethod
    def bind_element_children(
        cls, params: Dict, meta: XmlMeta, position: int, objects: List,
    ):
        """Return a dictionary of qualified object names and their values for
        the given queue item."""

        while len(objects) > position:
            qname, value = objects.pop(position)
            arg = meta.find_var(qname, FindMode.NOT_WILDCARD) or meta.find_var(
                qname, FindMode.WILDCARD
            )

            if not arg:
                raise ParserError("Impossible exception!")

            if not arg.init:
                continue

            if value is None:
                value = ""

            if not cls.bind_element_param(params, arg, value):
                lookup = QName(value.qname) if isinstance(value, AnyElement) else qname
                wild = cls.find_eligible_wildcard(meta, lookup, params)

                if not wild:
                    logger.warning("Unassigned parsed object %s", qname)
                else:
                    cls.bind_element_wildcard_param(params, wild, qname, value)

    @classmethod
    def fetch_any_children(cls, position: int, objects: List) -> List[object]:
        """Fetch the children of a wildcard node."""
        children = []
        while len(objects) > position:
            _, value = objects.pop(position)
            children.append(value)
        return children

    @classmethod
    def bind_element_param(cls, params: Dict, var: XmlVar, value: Any) -> bool:
        """
        Add the given value to the params dictionary with the var name as key.

        Wrap the value to a list if var is a list. If the var name already exists it
        means we have a name conflict and the parser needs to lookup for any available
        wildcard fields.

        :return: Whether the binding process was successful or not.
        """
        if var.is_list:
            params.setdefault(var.name, []).append(value)
        elif var.name not in params:
            params[var.name] = value
        else:
            return False

        return True

    @classmethod
    def bind_element_wildcard_param(
        cls, params: Dict, var: XmlVar, qname: QName, value: Any
    ):
        """
        Add the given value to the params dictionary with the wildcard var name
        as key.

        If the key is already present wrap the previous value into a
        generic AnyElement instance. If the previous value is already a
        generic instance add the current value as a child object.
        """
        if is_dataclass(value):
            if not isinstance(value, AnyElement):
                value.qname = qname
        else:
            value = AnyElement(qname=qname, text=value)

        if var.name in params:
            previous = params[var.name]
            if previous.qname:
                params[var.name] = AnyElement(children=[previous])

            params[var.name].children.append(value)
        else:
            params[var.name] = value

    @classmethod
    def bind_element_wild_text(cls, params: Dict, meta: XmlMeta, element: Element):
        """
        Extract the text and tail content and bind it accordingly in the params
        dictionary.

        - var is a list prepend the text and append the tail.
        - var is present in the params assign the text and tail to the generic object.
        - Otherwise bind the given element to a new generic object.
        """
        var = meta.find_var(mode=FindMode.WILDCARD)
        if not var:
            return

        txt, tail = cls.element_text_and_tail(element)
        if not txt and not tail:
            return

        if var.is_list:
            if var.name not in params:
                params[var.name] = []
            if txt:
                params[var.name].insert(0, txt)
            if tail:
                params[var.name].append(tail)
        elif var.name in params:
            params[var.name].text = txt
            params[var.name].tail = tail
        else:
            params[var.name] = cls.parse_any_element(element, False)

    @classmethod
    def element_text_and_tail(cls, element: Element) -> Tuple:
        """Extract the text and tail content if any and return them both."""
        txt = element.text.strip() if element.text else None
        tail = element.tail.strip() if element.tail else None

        return txt or None, tail or None

    @classmethod
    def parse_any_element(cls, element: Element, qname: bool = True) -> AnyElement:
        """Bind the given element content to a new generic object."""
        txt, tail = cls.element_text_and_tail(element)
        return AnyElement(
            qname=element.tag if qname else None,
            text=txt,
            tail=tail,
            ns_map=element.nsmap,
            attributes=cls.parse_any_attributes(element),
        )

    @classmethod
    def parse_any_attributes(cls, element: Element) -> Dict[QName, Any]:
        """Extract the given element's attributes into the dictionary with keys
        the fully qualified attribute names."""

        def qname(value: Any) -> Any:
            prefix, suffix = text.split(value)
            if prefix and prefix in element.nsmap:
                return QName(element.nsmap[prefix], suffix)
            return value

        return {QName(key): qname(value) for key, value in element.attrib.items()}

    @classmethod
    def bind_element_text(cls, params: Dict, metadata: XmlMeta, element: Element):
        """Add the given element's text content if any to the params dictionary
        with the text var name as key."""
        var = metadata.find_var(mode=FindMode.TEXT)
        if var and element.text is not None and var.init:
            params[var.name] = cls.parse_value(
                var.types, element.text, var.default, element.nsmap, var.is_tokens
            )

    @classmethod
    def bind_element_attrs(cls, params: Dict, metadata: XmlMeta, element: Element):
        """Parse the given element's attributes and any text content and return
        a dictionary of field names and values based on the given class
        metadata."""

        if not element.attrib:
            return

        wildcard = metadata.find_var(mode=FindMode.ATTRIBUTES)
        for key, value in element.attrib.items():
            var = metadata.find_var(QName(key), FindMode.ATTRIBUTE)

            if var and var.name not in params:
                if var.init:
                    params[var.name] = cls.parse_value(
                        var.types, value, var.default, element.nsmap, var.is_tokens
                    )
            elif wildcard:
                if wildcard.name not in params:
                    params[wildcard.name] = {}
                params[wildcard.name][key] = value

    @classmethod
    def find_eligible_wildcard(
        cls, meta: XmlMeta, qname: QName, params: Dict
    ) -> Optional[XmlVar]:
        """
        Last resort lookup for a suitable wildcard var.

        Search for a list wildcard or a wildcard that already exists in
        the params dictionary.
        """
        return next(
            (
                var
                for var in meta.vars
                if var.is_wildcard
                and var.matches(qname)
                and (
                    (var.is_list or var.name not in params)
                    or (not var.is_list and var.name in params)
                )
            ),
            None,
        )
