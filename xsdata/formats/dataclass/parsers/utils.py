from dataclasses import fields
from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Type

from xsdata.formats.converter import converter
from xsdata.formats.converter import QNameConverter
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.logger import logger
from xsdata.models.enums import QNames
from xsdata.utils import constants
from xsdata.utils import text
from xsdata.utils.namespaces import build_qname


class ParserUtils:
    @classmethod
    def xsi_type(cls, attrs: Dict, ns_map: Dict) -> Optional[str]:
        """Parse the xsi:type attribute if present."""
        xsi_type = attrs.get(QNames.XSI_TYPE)
        if not xsi_type:
            return None

        namespace, name = QNameConverter.resolve(xsi_type, ns_map)
        return build_qname(namespace, name)

    @classmethod
    def is_nillable(cls, attrs: Dict) -> bool:
        """Return whether the element attrs has xsi:nil="false"."""
        return attrs.get(QNames.XSI_NIL) != constants.XML_FALSE

    @classmethod
    def parse_value(
        cls,
        value: Any,
        types: Sequence[Type],
        default: Any = None,
        ns_map: Optional[Dict] = None,
        tokens: bool = False,
        _format: Optional[str] = None,
    ) -> Any:
        """Convert xml string values to s python primitive type."""

        if value is None:

            if callable(default):
                return default() if tokens else None

            return default

        if tokens:
            value = value if isinstance(value, list) else value.split()
            return [
                converter.deserialize(val, types, ns_map=ns_map, format=_format)
                for val in value
            ]

        return converter.deserialize(value, types, ns_map=ns_map, format=_format)

    @classmethod
    def bind_objects(cls, params: Dict, meta: XmlMeta, position: int, objects: List):
        """Return a dictionary of qualified object names and their values for
        the given queue item."""

        for qname, value in objects[position:]:
            if not cls.bind_object(params, meta, qname, value):
                logger.warning("Unassigned parsed object %s", qname)

        del objects[position:]

    @classmethod
    def bind_object(cls, params: Dict, meta: XmlMeta, qname: str, value: Any) -> bool:
        for var in meta.find_children(qname):
            if var.is_wildcard:
                return cls.bind_wild_var(params, var, qname, value)

            if cls.bind_var(params, var, value):
                return True

        return False

    @classmethod
    def bind_mixed_objects(cls, params: Dict, var: XmlVar, pos: int, objects: List):
        """Return a dictionary of qualified object names and their values for
        the given mixed content xml var."""

        params[var.name] = [
            cls.prepare_generic_value(qname, value) for qname, value in objects[pos:]
        ]
        del objects[pos:]

    @classmethod
    def bind_var(cls, params: Dict, var: XmlVar, value: Any) -> bool:
        """
        Add the given value to the params dictionary with the var name as key.

        Wrap the value to a list if var is a list. If the var name already exists it
        means we have a name conflict and the parser needs to lookup for any available
        wildcard fields.

        :return: Whether the binding process was successful or not.
        """
        if var.init:
            if var.list_element:
                items = params.get(var.name)
                if items is None:
                    params[var.name] = [value]
                else:
                    items.append(value)
            elif var.name not in params:
                params[var.name] = value
            else:
                return False

        return True

    @classmethod
    def bind_wild_var(cls, params: Dict, var: XmlVar, qname: str, value: Any) -> bool:
        """
        Add the given value to the params dictionary with the wildcard var name
        as key.

        If the key is already present wrap the previous value into a
        generic AnyElement instance. If the previous value is already a
        generic instance add the current value as a child object.
        """

        value = cls.prepare_generic_value(qname, value)

        if var.list_element:
            items = params.get(var.name)
            if items is None:
                params[var.name] = [value]
            else:
                items.append(value)
        elif var.name in params:
            previous = params[var.name]
            if previous.qname:
                params[var.name] = AnyElement(children=[previous])

            params[var.name].children.append(value)
        else:
            params[var.name] = value

        return True

    @classmethod
    def bind_wild_content(
        cls,
        params: Dict,
        var: XmlVar,
        txt: Optional[str],
        tail: Optional[str],
        attrs: Dict,
        ns_map: Dict,
    ) -> bool:
        """
        Extract the text and tail content and bind it accordingly in the params
        dictionary. Return if any data was bound.

        - var is a list prepend the text and append the tail.
        - var is present in the params assign the text and tail to the generic object.
        - Otherwise bind the given element to a new generic object.
        """

        txt = cls.normalize_content(txt)
        tail = cls.normalize_content(tail)
        if txt is None and tail is None:
            return False

        if var.list_element:
            items = params.get(var.name)
            if items is None:
                params[var.name] = items = []

            if txt:
                items.insert(0, txt)
            if tail:
                items.append(tail)
        else:
            previous = params.get(var.name, None)
            generic = AnyElement(
                text=txt,
                tail=tail,
                attributes=cls.parse_any_attributes(attrs, ns_map),
            )
            if previous:
                generic.children.append(previous)

            params[var.name] = generic

        return True

    @classmethod
    def bind_content(
        cls,
        params: Dict,
        metadata: XmlMeta,
        txt: Optional[str],
        ns_map: Dict,
    ) -> bool:
        """
        Add the given element's text content if any to the params dictionary
        with the text var name as key.

        Return if any data was bound.
        """

        if txt is not None:
            var = metadata.text
            if var and var.init:
                params[var.name] = cls.parse_value(
                    txt, var.types, var.default, ns_map, var.tokens, var.format
                )
                return True

        return False

    @classmethod
    def bind_attrs(cls, params: Dict, metadata: XmlMeta, attrs: Dict, ns_map: Dict):
        """Parse the given element's attributes and any text content and return
        a dictionary of field names and values based on the given class
        metadata."""

        if not attrs:
            return

        for qname, value in attrs.items():
            var = metadata.find_attribute(qname)
            if var and var.name not in params:
                cls.bind_attr(params, var, value, ns_map)
            else:
                var = metadata.find_any_attributes(qname)
                if var:
                    cls.bind_any_attr(params, var, qname, value, ns_map)

    @classmethod
    def bind_attr(cls, params: Dict, var: XmlVar, value: Any, ns_map: Dict):
        if var.init:
            params[var.name] = cls.parse_value(
                value,
                var.types,
                var.default,
                ns_map,
                var.tokens,
                var.format,
            )

    @classmethod
    def bind_any_attr(
        cls, params: Dict, var: XmlVar, qname: str, value: Any, ns_map: Dict
    ):
        if var.name not in params:
            params[var.name] = {}

        params[var.name][qname] = cls.parse_any_attribute(value, ns_map)

    @classmethod
    def prepare_generic_value(cls, qname: Optional[str], value: Any) -> Any:
        """Prepare parsed value before binding to a wildcard field."""

        if qname:
            if not is_dataclass(value):
                value = AnyElement(qname=qname, text=converter.serialize(value))
            elif not isinstance(value, (AnyElement, DerivedElement)):
                value = DerivedElement(qname=qname, value=value)

        return value

    @classmethod
    def normalize_content(cls, value: Optional[str]) -> Optional[str]:
        """
        Normalize element text or tail content.

        If content is just whitespace return None, otherwise preserve
        the original content.
        """
        if value and value.strip():
            return value

        return None

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
            value = build_qname(ns_map[prefix], suffix)

        return value

    @classmethod
    def fetch_any_children(cls, position: int, objects: List) -> List:
        """Fetch the children of a wildcard node."""
        children = [value for _, value in objects[position:]]

        del objects[position:]

        return children

    @classmethod
    def score_object(cls, obj: Any) -> float:
        """
        Score a dataclass instance by the field values types.

        Weights:
            1. None: 0
            2. str: 1
            3. *: 1.5
        """

        if not obj:
            return -1.0

        def score(value: Any) -> float:
            if isinstance(value, str):
                return 1.0

            if value is not None:
                return 1.5

            return 0.0

        if is_dataclass(obj):
            return sum(score(getattr(obj, var.name)) for var in fields(obj))

        return score(obj)
