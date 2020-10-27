import random
import unittest
from abc import ABC
from abc import abstractmethod
from typing import Type

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrChoice
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.models import Import
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames
from xsdata.models.enums import Tag
from xsdata.models.wsdl import BindingOperation
from xsdata.models.xsd import Attribute
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType
from xsdata.utils.namespaces import build_qname

DEFAULT_NS_MAP = {
    Namespace.XS.prefix: Namespace.XS.uri,
    Namespace.XSI.prefix: Namespace.XSI.uri,
    Namespace.XML.prefix: Namespace.XML.uri,
    Namespace.XLINK.prefix: Namespace.XLINK.uri,
}


class FactoryTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        ClassFactory.reset()
        AttrFactory.reset()
        AttrChoiceFactory.reset()
        AttrTypeFactory.reset()
        ExtensionFactory.reset()
        PackageFactory.reset()


class Factory(ABC):
    counter = 0

    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        pass

    @classmethod
    def reset(cls):
        cls.counter = 65

    @classmethod
    def next_letter(cls):
        cls.counter += 1
        return chr(cls.counter)

    @classmethod
    def list(cls, number: int, **kwargs):
        return [cls.create(**kwargs) for _ in range(number)]


class ClassFactory(Factory):
    model = Class
    types = [Element, Attribute, ComplexType, SimpleType]
    counter = 65

    @classmethod
    def create(
        cls,
        qname=None,
        meta_name=None,
        namespace=None,
        type=None,
        abstract=False,
        mixed=False,
        nillable=False,
        strict_type=False,
        help=None,
        extensions=None,
        substitutions=None,
        attrs=None,
        inner=None,
        ns_map=None,
        package="foo",
        module="tests",
        status=Status.RAW,
        container=None,
    ):
        if not qname:
            qname = build_qname("xsdata", f"class_{cls.next_letter()}")

        return cls.model(
            qname=qname,
            meta_name=meta_name,
            namespace=namespace,
            abstract=abstract,
            mixed=mixed,
            nillable=nillable,
            strict_type=strict_type,
            type=type or random.choice(cls.types),
            extensions=extensions or [],
            substitutions=substitutions or [],
            attrs=attrs or [],
            inner=inner or [],
            help=help,
            package=package,
            module=module,
            ns_map=ns_map if isinstance(ns_map, dict) else DEFAULT_NS_MAP,
            status=status,
            container=container,
        )

    @classmethod
    def simple_type(cls, **kwargs) -> Class:
        return ClassFactory.create(
            type=SimpleType,
            attrs=AttrFactory.list(1, tag=Tag.EXTENSION),
            **kwargs,
        )

    @classmethod
    def enumeration(cls, attributes: int, **kwargs) -> Class:
        return ClassFactory.create(
            type=SimpleType,
            attrs=AttrFactory.list(attributes, tag=Tag.ENUMERATION),
            **kwargs,
        )

    @classmethod
    def elements(cls, attributes: int, **kwargs) -> Class:
        return ClassFactory.create(
            type=ComplexType,
            attrs=AttrFactory.list(attributes, tag=Tag.ELEMENT),
            **kwargs,
        )

    @classmethod
    def service(cls, attributes: int, **kwargs) -> Class:
        return ClassFactory.create(
            type=BindingOperation, attrs=AttrFactory.list(attributes, tag=Tag.ELEMENT)
        )


class ExtensionFactory(Factory):
    model = Extension
    counter = 65

    @classmethod
    def create(cls, type=None, restrictions=None):
        return cls.model(
            type=type or AttrTypeFactory.create(),
            restrictions=restrictions or Restrictions(),
        )


class AttrTypeFactory(Factory):
    model = AttrType
    counter = 65

    @classmethod
    def create(
        cls,
        qname=None,
        alias=None,
        native=False,
        forward=False,
        circular=False,
    ):
        if not qname:
            qname = build_qname("xsdata", f"attr_{cls.next_letter()}")

        return cls.model(
            qname=qname,
            alias=alias,
            native=native,
            circular=circular,
            forward=forward,
        )

    @classmethod
    def xs_string(cls):
        return cls.create(qname=DataType.STRING.qname, native=True)

    @classmethod
    def xs_int(cls):
        return cls.create(qname=DataType.INTEGER.qname, native=True)

    @classmethod
    def xs_positive_int(cls):
        return cls.create(qname=DataType.POSITIVE_INTEGER.qname, native=True)

    @classmethod
    def xs_float(cls):
        return cls.create(qname=DataType.FLOAT.qname, native=True)

    @classmethod
    def xs_decimal(cls):
        return cls.create(qname=DataType.DECIMAL.qname, native=True)

    @classmethod
    def xs_bool(cls):
        return cls.create(qname=DataType.BOOLEAN.qname, native=True)

    @classmethod
    def xs_any(cls):
        return cls.create(qname=DataType.ANY_TYPE.qname, native=True)

    @classmethod
    def xs_qname(cls):
        return cls.create(qname=DataType.QNAME.qname, native=True)

    @classmethod
    def xs_tokens(cls):
        return cls.create(qname=DataType.NMTOKENS.qname, native=True)

    @classmethod
    def xs_error(cls):
        return cls.create(qname=DataType.ERROR.qname, native=True)


class AttrFactory(Factory):
    model: Type = Attr
    types = [Attribute, Element, Restriction]
    counter = 65

    @classmethod
    def create(
        cls,
        name=None,
        local_name=None,
        index=None,
        types=None,
        choices=None,
        tag=None,
        namespace=None,
        help=None,
        default=None,
        fixed=False,
        mixed=False,
        restrictions=None,
    ):
        name = name or f"attr_{cls.next_letter()}"
        return cls.model(
            name=name,
            local_name=name if local_name is None else local_name,
            index=cls.counter if index is None else index,
            types=types or [AttrTypeFactory.xs_string()],
            choices=choices or [],
            tag=tag or random.choice(cls.types).__name__,
            namespace=namespace or None,
            help=help or None,
            default=default or None,
            fixed=fixed,
            mixed=mixed,
            restrictions=restrictions or Restrictions(),
        )

    @classmethod
    def enumeration(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.ENUMERATION, **kwargs)

    @classmethod
    def element(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.ELEMENT, **kwargs)

    @classmethod
    def any(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.ANY, types=[AttrTypeFactory.xs_any()], **kwargs)

    @classmethod
    def any_attribute(cls, **kwargs) -> Attr:
        return cls.create(
            tag=Tag.ANY_ATTRIBUTE, types=[AttrTypeFactory.xs_any()], **kwargs
        )

    @classmethod
    def attribute(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.ATTRIBUTE, **kwargs)

    @classmethod
    def attribute_group(cls, **kwargs) -> Attr:
        return cls.create(
            tag=Tag.ATTRIBUTE_GROUP,
            types=[AttrTypeFactory.create(qname=kwargs.get("name"))],
            **kwargs,
        )

    @classmethod
    def group(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.GROUP, **kwargs)

    @classmethod
    def xsi_type(cls, **kwargs):
        kwargs.update(
            dict(name=QNames.XSI_TYPE.localname, namespace=QNames.XSI_TYPE.namespace)
        )
        return cls.attribute(**kwargs)


class AttrChoiceFactory(AttrFactory):
    model: Type = AttrChoice
    tags = [Tag.ELEMENT, Tag.ANY]
    counter = 65

    @classmethod
    def create(
        cls,
        name=None,
        types=None,
        tag=None,
        namespace=None,
        default=None,
        restrictions=None,
    ):
        name = name or f"choice_{cls.next_letter()}"
        return cls.model(
            name=name,
            types=types or [AttrTypeFactory.xs_string()],
            tag=tag or random.choice(cls.tags),
            namespace=namespace or None,
            default=default or None,
            restrictions=restrictions or Restrictions(),
        )


class PackageFactory(Factory):
    model = Import
    counter = 65

    @classmethod
    def create(cls, name=None, source=None, alias=None):

        return cls.model(
            name=name or f"package_{cls.next_letter()}",
            source=source or "target",
            alias=alias or None,
        )
