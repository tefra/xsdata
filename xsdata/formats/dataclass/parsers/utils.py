from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from lxml.etree import QName

from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.logger import logger
from xsdata.models.enums import QNames
from xsdata.utils import text


class ParserUtils:
    @classmethod
    def parse_xsi_type(cls, attrs: Dict, ns_map: Dict) -> Optional[str]:
        """Parse the elements xsi:type attribute if present."""
        xsi_type = attrs.get(QNames.XSI_TYPE)
        if xsi_type:
            return cls.parse_value(xsi_type, [QName], None, ns_map).text

        return None

    @classmethod
    def parse_value(
        cls,
        value: Any,
        types: List[Type],
        default: Any = None,
        ns_map: Optional[Dict] = None,
        tokens: bool = False,
    ) -> Any:
        """Convert xml string values to s python primitive type."""

        if value is None:
            return None if callable(default) else default

        if tokens:
            value = value if isinstance(value, list) else value.split()
            return [converter.from_string(val, types, ns_map=ns_map) for val in value]

        return converter.from_string(value, types, ns_map=ns_map)

    @classmethod
    def bind_element_children(
        cls, params: Dict, meta: XmlMeta, position: int, objects: List
    ):
        """Return a dictionary of qualified object names and their values for
        the given queue item."""

        while len(objects) > position:
            qname, value = objects.pop(position)
            arg = meta.find_var(qname, FindMode.NOT_WILDCARD) or meta.find_var(
                qname, FindMode.WILDCARD
            )

            assert arg is not None

            if not arg.init:
                continue

            if value is None:
                value = ""

            if not cls.bind_element_param(params, arg, value):
                lookup = qname
                if isinstance(value, AnyElement) and value.qname:
                    lookup = value.qname

                wild = cls.find_eligible_wildcard(meta, lookup, params)

                if not wild:
                    logger.warning("Unassigned parsed object %s", qname)
                else:
                    cls.bind_element_wildcard_param(params, wild, qname, value)

    @classmethod
    def bind_mixed_content(cls, params: Dict, var: XmlVar, pos: int, objects: List):
        """Return a dictionary of qualified object names and their values for
        the given mixed content xml var."""

        params.setdefault(var.name, [])
        while len(objects) > pos:
            qname, value = objects.pop(pos)

            if value is None:
                value = ""

            params[var.name].append(cls.prepare_generic_value(qname, value))

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
    def prepare_generic_value(cls, qname: Optional[str], value: Any) -> Any:
        """Prepare parsed value before binding to a wildcard field."""

        if not qname:
            return value

        if not is_dataclass(value):
            value = AnyElement(qname=qname, text=value)
        elif not isinstance(value, AnyElement):
            value.qname = qname  # Deprecate this hack!

        return value

    @classmethod
    def bind_element_wildcard_param(
        cls, params: Dict, var: XmlVar, qname: str, value: Any
    ):
        """
        Add the given value to the params dictionary with the wildcard var name
        as key.

        If the key is already present wrap the previous value into a
        generic AnyElement instance. If the previous value is already a
        generic instance add the current value as a child object.
        """

        value = cls.prepare_generic_value(qname, value)

        if var.name in params:
            previous = params[var.name]
            if previous.qname:
                params[var.name] = AnyElement(children=[previous])

            params[var.name].children.append(value)
        else:
            params[var.name] = value

    @classmethod
    def bind_wildcard_element(
        cls,
        params: Dict,
        var: XmlVar,
        txt: Optional[str],
        tail: Optional[str],
        attrs: Dict,
        ns_map: Dict,
    ):
        """
        Extract the text and tail content and bind it accordingly in the params
        dictionary.

        - var is a list prepend the text and append the tail.
        - var is present in the params assign the text and tail to the generic object.
        - Otherwise bind the given element to a new generic object.
        """

        txt = cls.normalize_content(txt)
        tail = cls.normalize_content(tail)
        if txt is None and tail is None:
            return

        if var.is_list:
            params.setdefault(var.name, [])
            if txt:
                params[var.name].insert(0, txt)
            if tail:
                params[var.name].append(tail)
        else:
            previous = params.get(var.name, None)
            generic = AnyElement(
                text=txt,
                tail=tail,
                ns_map=ns_map,
                attributes=cls.parse_any_attributes(attrs, ns_map),
            )
            if previous:
                generic.children.append(previous)

            params[var.name] = generic

    @classmethod
    def normalize_content(cls, value: Optional[str]) -> Optional[str]:
        """
        Normalize element text or tail content.

        If content is just whitespace return None, otherwise preserve
        the original content.
        """
        if value is not None:
            clean_value = value.strip()
            if not clean_value:
                value = None

        return value

    @classmethod
    def parse_any_attributes(cls, attrs: Dict, ns_map: Dict) -> Dict:
        return {
            key: cls.parse_any_attribute(value, ns_map) for key, value in attrs.items()
        }

    @classmethod
    def parse_any_attribute(cls, value: str, ns_map: Dict) -> str:
        """Attempt to parse any attribute."""
        prefix, suffix = text.split(value)
        if prefix and prefix in ns_map and not suffix.startswith("//"):
            value = text.qname(ns_map[prefix], suffix)

        return value

    @classmethod
    def bind_element(
        cls,
        params: Dict,
        metadata: XmlMeta,
        txt: Optional[str],
        tail: Optional[str],
        attrs: Dict,
        ns_map: Dict,
    ):
        """Add the given element's text content if any to the params dictionary
        with the text var name as key."""
        var = metadata.find_var(mode=FindMode.TEXT)
        wildcard = None if var else metadata.find_var(mode=FindMode.WILDCARD)

        if var and var.init and txt is not None:
            params[var.name] = cls.parse_value(
                txt, var.types, var.default, ns_map, var.tokens
            )
        elif wildcard:
            cls.bind_wildcard_element(params, wildcard, txt, tail, attrs, ns_map)

    @classmethod
    def bind_element_attrs(
        cls, params: Dict, metadata: XmlMeta, attrs: Dict, ns_map: Dict
    ):
        """Parse the given element's attributes and any text content and return
        a dictionary of field names and values based on the given class
        metadata."""

        if not attrs:
            return

        wildcard = metadata.find_var(mode=FindMode.ATTRIBUTES)
        if wildcard:
            params[wildcard.name] = {}

        for qname, value in attrs.items():
            var = metadata.find_var(qname, FindMode.ATTRIBUTE)
            if var and var.name not in params:
                if var.init:
                    params[var.name] = cls.parse_value(
                        value, var.types, var.default, ns_map, var.tokens
                    )
            elif wildcard:
                params[wildcard.name][qname] = cls.parse_any_attribute(value, ns_map)

    @classmethod
    def find_eligible_wildcard(
        cls, meta: XmlMeta, qname: str, params: Dict
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
