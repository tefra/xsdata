from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from io import StringIO
from typing import Any
from typing import Dict
from typing import Generator
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import TextIO
from typing import Tuple
from typing import Type
from xml.etree.ElementTree import QName

from xsdata.exceptions import SerializerError
from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.mixins import XmlWriter
from xsdata.formats.dataclass.serializers.mixins import XmlWriterEvent
from xsdata.formats.dataclass.serializers.writers import default_writer
from xsdata.models.enums import DataType
from xsdata.models.enums import QNames
from xsdata.utils import collections
from xsdata.utils import namespaces
from xsdata.utils.constants import EMPTY_MAP

NoneStr = Optional[str]


@dataclass
class XmlSerializer(AbstractSerializer):
    """
    Xml serializer for dataclasses.

    :param config: Serializer configuration
    :param context: Model context provider
    :param writer: Override default XmlWriter
    """

    config: SerializerConfig = field(default_factory=SerializerConfig)
    context: XmlContext = field(default_factory=XmlContext)
    writer: Type[XmlWriter] = field(default=default_writer())

    def render(self, obj: Any, ns_map: Optional[Dict] = None) -> str:
        """
        Convert and return the given object tree as xml string.

        :param obj: The input dataclass instance
        :param ns_map: User defined namespace prefix-URI map
        """
        output = StringIO()
        self.write(output, obj, ns_map)
        return output.getvalue()

    def write(self, out: TextIO, obj: Any, ns_map: Optional[Dict] = None):
        """
        Write the given object tree to the output text stream.

        :param out: The output stream
        :param obj: The input dataclass instance
        :param ns_map: User defined namespace prefix-URI map
        """
        events = self.write_object(obj)
        handler = self.writer(
            config=self.config,
            output=out,
            ns_map=namespaces.clean_prefixes(ns_map) if ns_map else {},
        )
        handler.write(events)

    def write_object(self, obj: Any):
        """Produce an events stream from a dataclass or a derived element."""
        qname = xsi_type = None
        if isinstance(obj, self.context.class_type.derived_element):
            meta = self.context.build(
                obj.value.__class__, globalns=self.config.globalns
            )
            qname = obj.qname
            obj = obj.value
            xsi_type = namespaces.real_xsi_type(qname, meta.target_qname)

        yield from self.write_dataclass(obj, qname=qname, xsi_type=xsi_type)

    def write_dataclass(
        self,
        obj: Any,
        namespace: NoneStr = None,
        qname: NoneStr = None,
        nillable: bool = False,
        xsi_type: Optional[str] = None,
    ) -> Generator:
        """
        Produce an events stream from a dataclass.

        Optionally override the qualified name and the xsi properties
        type and nil.
        """
        meta = self.context.build(
            obj.__class__, namespace, globalns=self.config.globalns
        )
        qname = qname or meta.qname
        nillable = nillable or meta.nillable
        namespace, tag = namespaces.split_qname(qname)

        yield XmlWriterEvent.START, qname

        for key, value in self.next_attribute(
            obj, meta, nillable, xsi_type, self.config.ignore_default_attributes
        ):
            yield XmlWriterEvent.ATTR, key, value

        for var, value in self.next_value(obj, meta):
            yield from self.write_value(value, var, namespace)

        yield XmlWriterEvent.END, qname

    def write_xsi_type(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an events stream from a dataclass for the given var with xsi
        abstract type check for non wildcards."""

        if var.is_wildcard:
            choice = var.find_value_choice(value, True)
            if choice:
                yield from self.write_value(value, choice, namespace)
            else:
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
        if var.mixed:
            yield from self.write_mixed_content(value, var, namespace)
        elif var.is_text:
            yield from self.write_data(value, var, namespace)
        elif var.tokens:
            yield from self.write_tokens(value, var, namespace)
        elif var.is_elements:
            yield from self.write_elements(value, var, namespace)
        elif var.list_element and collections.is_array(value):
            yield from self.write_list(value, var, namespace)
        else:
            yield from self.write_any_type(value, var, namespace)

    def write_list(
        self, values: Iterable, var: XmlVar, namespace: NoneStr
    ) -> Generator:
        """Produce an events stream for the given list of values."""
        if var.wrapper is not None:
            yield XmlWriterEvent.START, var.wrapper
            for value in values:
                yield from self.write_value(value, var, namespace)
            yield XmlWriterEvent.END, var.wrapper
        else:
            for value in values:
                yield from self.write_value(value, var, namespace)

    def write_tokens(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an events stream for the given tokens list or list of tokens
        lists."""
        if value is not None or var.nillable:
            if value and collections.is_array(value[0]):
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
        if isinstance(value, self.context.class_type.any_element):
            yield from self.write_wildcard(value, var, namespace)
        elif isinstance(value, self.context.class_type.derived_element):
            yield from self.write_derived_element(value, namespace)
        elif self.context.class_type.is_model(value):
            yield from self.write_xsi_type(value, var, namespace)
        elif var.is_element:
            yield from self.write_element(value, var, namespace)
        else:
            yield from self.write_data(value, var, namespace)

    def write_derived_element(self, value: Any, namespace: NoneStr) -> Generator:
        if self.context.class_type.is_model(value.value):
            meta = self.context.fetch(value.value.__class__)
            qname = value.qname
            xsi_type = namespaces.real_xsi_type(qname, meta.target_qname)

            yield from self.write_dataclass(
                value.value, namespace, qname=qname, xsi_type=xsi_type
            )
        else:
            datatype = DataType.from_value(value.value)

            yield XmlWriterEvent.START, value.qname
            yield XmlWriterEvent.ATTR, QNames.XSI_TYPE, QName(str(datatype))
            yield XmlWriterEvent.DATA, value.value
            yield XmlWriterEvent.END, value.qname

    def write_wildcard(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an element events stream for the given generic object."""
        if value.qname:
            namespace, tag = namespaces.split_qname(value.qname)
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

    def xsi_type(self, var: XmlVar, value: Any, namespace: NoneStr) -> Optional[str]:
        """Get xsi:type if the given value is a derived instance."""
        if not value or value.__class__ in var.types:
            return None

        clazz = var.clazz
        if clazz is None or self.context.is_derived(value, clazz):
            meta = self.context.fetch(value.__class__, namespace)
            return meta.target_qname

        raise SerializerError(
            f"{value.__class__.__name__} is not derived from {clazz.__name__}"
        )

    def write_elements(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an events stream from compound elements field."""
        if collections.is_array(value):
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
        if isinstance(value, self.context.class_type.derived_element):
            choice = var.find_choice(value.qname)
            value = value.value

            if self.context.class_type.is_model(value):
                func = self.write_xsi_type
            else:
                func = self.write_element

        elif isinstance(value, self.context.class_type.any_element) and value.qname:
            choice = var.find_choice(value.qname)
            func = self.write_any_type
        else:
            check_subclass = self.context.class_type.is_model(value)
            choice = var.find_value_choice(value, check_subclass)
            func = self.write_value

        if not choice:
            raise SerializerError(
                f"XmlElements undefined choice: `{var.name}` for `{type(value)}`"
            )

        yield from func(value, choice, namespace)

    def write_element(self, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce an element events stream for the given simple type value."""
        yield XmlWriterEvent.START, var.qname

        if var.nillable:
            yield XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"

        if value is not None and value != "" and var.any_type:
            datatype = DataType.from_value(value)
            if datatype != DataType.STRING:
                yield XmlWriterEvent.ATTR, QNames.XSI_TYPE, QName(str(datatype))

        yield XmlWriterEvent.DATA, self.encode(value, var)
        yield XmlWriterEvent.END, var.qname

    @classmethod
    def write_data(cls, value: Any, var: XmlVar, namespace: NoneStr) -> Generator:
        """Produce a data event for the given value."""
        yield XmlWriterEvent.DATA, cls.encode(value, var)

    @classmethod
    def next_value(cls, obj: Any, meta: XmlMeta) -> Iterator[Tuple[XmlVar, Any]]:
        """
        Return the non attribute variables with their object values in the
        correct order according to their definition and the sequential metadata
        property.

        Sequential fields need to be rendered together in parallel order
        eg: <a1/><a2/><a1/><a/2></a1>
        """
        index = 0
        attrs = meta.get_element_vars()
        stop = len(attrs)
        while index < stop:
            var = attrs[index]

            if var.sequence is None:
                value = getattr(obj, var.name)
                if value is not None or var.nillable:
                    yield var, value
                index += 1
                continue

            indices = range(index, stop)
            end = next(i for i in indices[::-1] if attrs[i].sequence == var.sequence)
            sequence = attrs[index : end + 1]
            index = end + 1
            j = 0

            rolling = True
            while rolling:
                rolling = False
                for var in sequence:
                    values = getattr(obj, var.name)
                    if collections.is_array(values):
                        if j < len(values):
                            rolling = True
                            value = values[j]
                            if value is not None or var.nillable:
                                yield var, value
                    elif j == 0:
                        rolling = True
                        if values is not None or var.nillable:
                            yield var, values

                j += 1

    @classmethod
    def next_attribute(
        cls,
        obj: Any,
        meta: XmlMeta,
        nillable: bool,
        xsi_type: Optional[str],
        ignore_optionals: bool,
    ) -> Iterator[Tuple[str, Any]]:
        """
        Return the attribute variables with their object values if set and not
        empty iterables.

        :param obj: Input object
        :param meta: Object metadata
        :param nillable: Is model nillable
        :param xsi_type: The true xsi:type of the object
        :param ignore_optionals: Skip optional attributes with default
            value
        :return:
        """
        for var in meta.get_attribute_vars():
            if var.is_attribute:
                value = getattr(obj, var.name)
                if (
                    value is None
                    or (collections.is_array(value) and not value)
                    or (ignore_optionals and var.is_optional(value))
                ):
                    continue

                yield var.qname, cls.encode(value, var)
            else:
                yield from getattr(obj, var.name, EMPTY_MAP).items()

        if xsi_type:
            yield QNames.XSI_TYPE, QName(xsi_type)

        if nillable:
            yield QNames.XSI_NIL, "true"

    @classmethod
    def encode(cls, value: Any, var: XmlVar) -> Any:
        """
        Encode values for xml serialization.

        Converts values to strings. QName instances is an exception,
        those values need to wait until the XmlWriter assigns prefixes
        to namespaces per element node. Enums and Tokens may contain
        QName(s) so they also get a special treatment.

        We can't do all the conversions in the writer because we would
        need to carry the xml vars inside the writer. Instead of that we
        do the easy encoding here and leave the qualified names for
        later.
        """
        if isinstance(value, (str, QName)) or var is None:
            return value

        if collections.is_array(value):
            return [cls.encode(v, var) for v in value]

        if isinstance(value, Enum):
            return cls.encode(value.value, var)

        return converter.serialize(value, format=var.format)
