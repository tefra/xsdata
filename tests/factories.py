import random
import unittest
from abc import ABC
from abc import abstractmethod
from typing import Type

from xsdata.codegen.models import Attr
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
    tags = [Tag.ELEMENT, Tag.ATTRIBUTE, Tag.COMPLEX_TYPE, Tag.SIMPLE_TYPE]
    counter = 65

    @classmethod
    def create(
        cls,
        qname=None,
        meta_name=None,
        namespace=None,
        tag=None,
        abstract=False,
        mixed=False,
        nillable=False,
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
        default=None,
        fixed=False,
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
            tag=tag or random.choice(cls.tags),
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
            default=default,
            fixed=fixed,
        )

    @classmethod
    def simple_type(cls, **kwargs) -> Class:
        return ClassFactory.create(
            tag=Tag.SIMPLE_TYPE,
            attrs=AttrFactory.list(1, tag=Tag.EXTENSION),
            **kwargs,
        )

    @classmethod
    def enumeration(cls, attributes: int, **kwargs) -> Class:
        return ClassFactory.create(
            tag=Tag.SIMPLE_TYPE,
            attrs=AttrFactory.list(attributes, tag=Tag.ENUMERATION),
            **kwargs,
        )

    @classmethod
    def elements(cls, attributes: int, **kwargs) -> Class:
        return ClassFactory.create(
            tag=Tag.COMPLEX_TYPE,
            attrs=AttrFactory.list(attributes, tag=Tag.ELEMENT),
            **kwargs,
        )

    @classmethod
    def service(cls, attributes: int, **kwargs) -> Class:
        return ClassFactory.create(
            tag=Tag.BINDING_OPERATION,
            attrs=AttrFactory.list(attributes, tag=Tag.ELEMENT),
            **kwargs,
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

    @classmethod
    def reference(cls, qname: str):
        return cls.create(AttrTypeFactory.create(qname=qname))


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
            qname=str(qname),
            alias=alias,
            native=native,
            circular=circular,
            forward=forward,
        )

    @classmethod
    def native(cls, datatype: DataType) -> AttrType:
        return cls.create(qname=str(datatype), native=True)


class AttrFactory(Factory):
    model: Type = Attr
    tags = [Tag.ATTRIBUTE, Tag.ELEMENT, Tag.RESTRICTION]
    counter = 65

    @classmethod
    def create(
        cls,
        name=None,
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
            index=cls.counter if index is None else index,
            types=types or [AttrTypeFactory.native(DataType.STRING)],
            choices=choices or [],
            tag=tag or random.choice(cls.tags),
            namespace=namespace or None,
            help=help or None,
            default=default or None,
            fixed=fixed,
            mixed=mixed,
            restrictions=restrictions or Restrictions(),
        )

    @classmethod
    def native(cls, datatype: DataType, tag: str = Tag.ELEMENT, **kwargs) -> Attr:
        return cls.create(tag=tag, types=[AttrTypeFactory.native(datatype)], **kwargs)

    @classmethod
    def enumeration(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.ENUMERATION, **kwargs)

    @classmethod
    def element(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.ELEMENT, **kwargs)

    @classmethod
    def any(cls, **kwargs) -> Attr:
        return cls.create(
            tag=Tag.ANY, types=[AttrTypeFactory.native(DataType.ANY_TYPE)], **kwargs
        )

    @classmethod
    def any_attribute(cls, **kwargs) -> Attr:
        return cls.create(
            tag=Tag.ANY_ATTRIBUTE,
            types=[AttrTypeFactory.native(DataType.ANY_TYPE)],
            **kwargs,
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
