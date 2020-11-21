from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from io import StringIO
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import TextIO
from typing import Type
from xml.etree.ElementTree import QName

from xsdata.exceptions import SerializerError
from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.serializers.mixins import XmlWriter
from xsdata.formats.dataclass.serializers.mixins import XmlWriterEvent
from xsdata.formats.dataclass.serializers.writers import LxmlEventWriter
from xsdata.models.enums import DataType
from xsdata.models.enums import QNames
from xsdata.utils import namespaces
from xsdata.utils.constants import EMPTY_MAP
from xsdata.utils.namespaces import split_qname

NoneStr = Optional[str]


@dataclass
class XmlSerializer(AbstractSerializer):
    """
    Xml serialize for dataclasses.

    :param encoding: Text encoding
    :param pretty_print: Enable pretty output
    :param context: XmlContext instance
    :param writer: xml writer type
    """

    encoding: str = field(default="UTF-8")
    pretty_print: bool = field(default=False)
    context: XmlContext = field(default_factory=XmlContext)
    writer: Type[XmlWriter] = field(default=LxmlEventWriter)

    def render(self, obj: Any, ns_map: Optional[Dict] = None) -> str:
        """
        Convert and return the given object tree as xml string.

        Optionally provide a prefix-URI namespaces mapping.
        """
        output = StringIO()
        self.write(output, obj, ns_map)
        return output.getvalue()

    def write(self, out: TextIO, obj: Any, ns_map: Optional[Dict] = None):
        """
        Write the given object tree to output text stream.

        Optionally provide a prefix-URI namespaces mapping.
        """
        events = self.write_object(obj)
        handler = self.writer(
            output=out,
            ns_map=namespaces.clean_prefixes(ns_map) if ns_map else {},
            encoding=self.encoding,
            pretty_print=self.pretty_print,
        )
        handler.write(events)

    def write_object(self, obj: Any):
        """Produce an events stream from a dataclass or a derived element."""
        qname = xsi_type = None
        if isinstance(obj, DerivedElement):
            meta = self.context.build(obj.value.__class__)
            xsi_type = QName(meta.source_qname)
            qname = obj.qname
            obj = obj.value

        yield from self.write_dataclass(obj, qname=qname, xsi_type=xsi_type)

    def write_dataclass(
        self,
        obj: Any,
        namespace: NoneStr = None,
        qname: NoneStr = None,
        nillable: bool = False,
        xsi_type: Optional[QName] = None,
    ) -> Generator:
        """
        Produce an events stream from a dataclass.

        Optionally override the qualified name and the xsi properties
        type and nil.
        """

        meta = self.context.build(obj.__class__, namespace)
        qname = qname or meta.qname
        nillable = nillable or meta.nillable
        namespace, tag = split_qname(qname)

        yield XmlWriterEvent.START, qname

        for key, value in self.next_attribute(obj, meta, nillable, xsi_type):
            yield XmlWriterEvent.ATTR, key, value

        for var, value in self.next_value(obj, meta):
            if value is not None:
                yield from self.write_value(value, var, namespace)

        yield XmlWriterEvent.END, qname

    def write_xsi_type(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an events stream from a dataclass for the given var with
        with xsi abstract type check for non wildcards."""

        if var.is_wildcard:
            yield from self.write_dataclass(value, namespace)
        else:
            xsi_type = self.xsi_type(var, value, namespace)
            yield from self.write_dataclass(
                value, namespace, var.qname, var.nillable, xsi_type
            )

    def write_value(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """
        Delegates the given value to the correct writer according to the
        variable metadata.

        The order of the checks is important as more than one condition
        can be true.
        """
        if var.is_mixed_content:
            yield from self.write_mixed_content(value, var, namespace)
        elif var.is_text:
            yield from self.write_data(value, var, namespace)
        elif var.tokens:
            yield from self.write_tokens(value, var, namespace)
        elif var.is_elements:
            yield from self.write_elements(value, var, namespace)
        elif var.is_list and isinstance(value, list):
            yield from self.write_list(value, var, namespace)
        elif var.is_any_type or var.is_wildcard:
            yield from self.write_any_type(value, var, namespace)
        elif var.dataclass:
            yield from self.write_xsi_type(value, var, namespace)
        elif var.is_element:
            yield from self.write_element(value, var, namespace)
        else:
            raise SerializerError(f"Unhandled xml var: `{var.__class__.__name__}`")

    def write_list(self, values: List, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an events stream for the given list of values."""
        for value in values:
            yield from self.write_value(value, var, namespace)

    def write_tokens(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an events stream for the given tokens list or list of tokens
        lists."""
        if value:
            if isinstance(value[0], list):
                for val in value:
                    yield from self.write_element(val, var, namespace)
            else:
                yield from self.write_element(value, var, namespace)

    def write_mixed_content(
        self, values: List, var: XmlVar, namespace: NoneStr
    ) -> Generator:
        """Produce an events stream for the given list of mixed type
        objects."""
        for value in values:
            yield from self.write_any_type(value, var, namespace)

    def write_any_type(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """
        Produce an events stream for the given object.

        The object can be a dataclass or a generic object or any other
        simple type.
        """
        if isinstance(value, AnyElement):
            yield from self.write_wildcard(value, var, namespace)
        elif isinstance(value, DerivedElement):
            yield from self.write_dataclass(value.value, namespace, qname=value.qname)
        elif is_dataclass(value):
            yield from self.write_xsi_type(value, var, namespace)
        elif var.is_element:
            yield from self.write_element(value, var, namespace)
        else:
            yield from self.write_data(value, var, namespace)

    def write_wildcard(
        self, value: AnyElement, var: XmlVar, namespace: NoneStr
    ) -> Generator:
        """Produce an element events stream for the given generic object."""
        if value.qname:
            namespace, tag = split_qname(value.qname)
            yield XmlWriterEvent.START, value.qname

        for key, val in value.attributes.items():
            yield XmlWriterEvent.ATTR, key, val

        yield XmlWriterEvent.DATA, value.text

        for child in value.children:
            yield from self.write_any_type(child, var, namespace)

        if value.qname:
            yield XmlWriterEvent.END, value.qname

        if value.tail:
            yield XmlWriterEvent.DATA, value.tail

    def xsi_type(self, var: XmlVar, value: Any, namespace: NoneStr) -> Optional[QName]:
        """Get xsi:type if the given value is a derived instance."""
        if not value or value.__class__ in var.types:
            return None

        clazz = var.clazz
        if clazz is None or self.context.is_derived(value, clazz):
            meta = self.context.fetch(value.__class__, namespace)
            return QName(meta.source_qname)

        raise SerializerError(
            f"{value.__class__.__name__} is not derived from {clazz.__name__}"
        )

    def write_elements(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an events stream from compound elements field."""
        if isinstance(value, list):
            for choice in value:
                yield from self.write_choice(choice, var, namespace)
        else:
            yield from self.write_choice(value, var, namespace)

    def write_choice(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """
        Produce an events stream for the given value of a compound elements
        field.

        The value can be anything as long as we can match the qualified
        name or its type to a choice.
        """
        if isinstance(value, DerivedElement):
            choice = var.find_choice(value.qname)
            value = value.value
            func = self.write_xsi_type if is_dataclass(value) else self.write_element
        elif isinstance(value, AnyElement) and value.qname:
            choice = var.find_choice(value.qname)
            func = self.write_any_type
        else:
            choice = var.find_value_choice(value)
            func = self.write_value

        if not choice:
            raise SerializerError(
                f"XmlElements undefined choice: `{var.name}` for `{type(value)}`"
            )

        yield from func(value, choice, namespace)

    @classmethod
    def write_element(cls, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an element events stream for the given simple type value."""
        yield XmlWriterEvent.START, var.qname

        if var.nillable:
            yield XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"

        if value is not None and var.is_any_type:
            datatype = DataType.from_value(value)
            if datatype != DataType.STRING:
                yield XmlWriterEvent.ATTR, QNames.XSI_TYPE, datatype.qname

        yield XmlWriterEvent.DATA, value
        yield XmlWriterEvent.END, var.qname

    @classmethod
    def write_data(cls, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce a data event for the given value."""
        yield XmlWriterEvent.DATA, value

    @classmethod
    def next_value(cls, obj: Any, meta: XmlMeta):
        """
        Return the non attribute variables with their object values in the
        correct order according to their definition and the sequential metadata
        property.

        Sequential fields need to be rendered together in parallel order
        eg: <a1/><a2/><a1/><a/2></a1>
        """
        index = 0
        attrs = meta.vars
        stop = len(attrs)
        while index < stop:
            var = attrs[index]
            if var.is_attribute or var.is_attributes:
                index += 1
                continue

            if not var.sequential:
                yield var, getattr(obj, var.name)
                index += 1
                continue

            indices = range(index + 1, stop)
            end = next((i for i in indices if not attrs[i].sequential), stop)
            sequence = attrs[index:end]
            index = end
            j = 0

            rolling = True
            while rolling:
                rolling = False
                for var in sequence:
                    values = getattr(obj, var.name)
                    if j < len(values):
                        rolling = True
                        yield var, values[j]
                j += 1

    @classmethod
    def next_attribute(
        cls, obj: Any, meta: XmlMeta, xsi_nil: bool, xsi_type: Optional[QName]
    ) -> Generator:
        """
        Return the attribute variables with their object values.

        Ignores None values and empty lists. Optionally include the xsi
        properties type and nil.
        """
        for var in meta.vars:
            if var.is_attribute:
                value = getattr(obj, var.name)
                if value is None or isinstance(value, list) and not value:
                    continue

                yield var.qname, value
            elif var.is_attributes:
                yield from getattr(obj, var.name, EMPTY_MAP).items()

        if xsi_type:
            yield QNames.XSI_TYPE, xsi_type

        if xsi_nil:
            yield QNames.XSI_NIL, "true"
