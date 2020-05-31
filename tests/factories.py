import random
import unittest
from abc import ABC
from abc import abstractmethod

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.models import Package
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import QNames
from xsdata.models.enums import Tag
from xsdata.models.xsd import Attribute
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType

NSMAP = {ns.prefix: ns.uri for ns in Namespace}


class FactoryTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        ClassFactory.reset()
        AttrFactory.reset()
        AttrTypeFactory.reset()
        ExtensionFactory.reset()
        RestrictionsFactory.reset()
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
        return [cls.create(**kwargs) for i in range(number)]


class ClassFactory(Factory):
    model = Class
    types = [Element, Attribute, ComplexType, SimpleType]
    counter = 65

    @classmethod
    def create(
        cls,
        name=None,
        namespace=None,
        source_namespace="xsdata",
        type=None,
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
    ):
        name = name or f"class_{cls.next_letter()}"
        return cls.model(
            name=name,
            namespace=namespace,
            source_namespace=source_namespace,
            abstract=abstract,
            mixed=mixed,
            nillable=nillable,
            type=type or random.choice(cls.types),
            extensions=extensions or [],
            substitutions=substitutions or [],
            attrs=attrs or [],
            inner=inner or [],
            help=help,
            package=package,
            module=module,
            ns_map=ns_map if isinstance(ns_map, dict) else NSMAP,
            status=status,
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


class RestrictionsFactory(Factory):
    model = Restrictions
    counter = 65

    @classmethod
    def create(
        cls,
        required=None,
        min_occurs=None,
        max_occurs=None,
        min_exclusive=None,
        min_inclusive=None,
        min_length=None,
        max_exclusive=None,
        max_inclusive=None,
        max_length=None,
        total_digits=None,
        fraction_digits=None,
        length=None,
        white_space=None,
        pattern=None,
        explicit_timezone=None,
        nillable=None,
    ):
        return cls.model(
            required=required,
            min_occurs=min_occurs,
            max_occurs=max_occurs,
            min_exclusive=min_exclusive,
            min_inclusive=min_inclusive,
            min_length=min_length,
            max_exclusive=max_exclusive,
            max_inclusive=max_inclusive,
            max_length=max_length,
            total_digits=total_digits,
            fraction_digits=fraction_digits,
            length=length,
            white_space=white_space,
            pattern=pattern,
            explicit_timezone=explicit_timezone,
            nillable=nillable,
        )


class ExtensionFactory(Factory):
    model = Extension
    counter = 65

    @classmethod
    def create(cls, type=None, restrictions=None):
        return cls.model(
            type=type or AttrTypeFactory.create(),
            restrictions=restrictions or RestrictionsFactory.create(),
        )


class AttrTypeFactory(Factory):
    model = AttrType
    counter = 65

    @classmethod
    def create(
        cls,
        name=None,
        index=None,
        alias=None,
        native=False,
        forward=False,
        circular=False,
    ):

        return cls.model(
            name=name or f"attr_{cls.next_letter()}",
            index=index or 0,
            alias=alias,
            native=native,
            circular=circular,
            forward=forward,
        )

    @classmethod
    def xs_string(cls):
        return cls.create(name=DataType.STRING.code, native=True)

    @classmethod
    def xs_int(cls):
        return cls.create(name=DataType.INTEGER.code, native=True)

    @classmethod
    def xs_positive_int(cls):
        return cls.create(name=DataType.POSITIVE_INTEGER.code, native=True)

    @classmethod
    def xs_float(cls):
        return cls.create(name=DataType.FLOAT.code, native=True)

    @classmethod
    def xs_decimal(cls):
        return cls.create(name=DataType.DECIMAL.code, native=True)

    @classmethod
    def xs_bool(cls):
        return cls.create(name=DataType.BOOLEAN.code, native=True)

    @classmethod
    def xs_any(cls):
        return cls.create(name=DataType.ANY_TYPE.code, native=True)

    @classmethod
    def xs_qmap(cls):
        return cls.create(name=DataType.QMAP.code, native=True)

    @classmethod
    def xs_qname(cls):
        return cls.create(name=DataType.QNAME.code, native=True)

    @classmethod
    def xs_tokens(cls):
        return cls.create(name=DataType.NMTOKENS.code, native=True)


class AttrFactory(Factory):
    model = Attr
    types = [Attribute, Element, Restriction]
    counter = 65

    @classmethod
    def create(
        cls,
        name=None,
        local_name=None,
        index=None,
        types=None,
        tag=None,
        namespace=None,
        help=None,
        default=None,
        fixed=False,
        restrictions=None,
    ):
        name = name or f"attr_{cls.next_letter()}"
        return cls.model(
            name=name,
            local_name=local_name or name,
            index=cls.counter if index is None else index,
            types=types or [AttrTypeFactory.xs_string()],
            tag=tag or random.choice(cls.types).__name__,
            namespace=namespace or None,
            help=help or None,
            default=default or None,
            fixed=fixed,
            restrictions=restrictions or RestrictionsFactory.create(),
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
            tag=Tag.ANY_ATTRIBUTE, types=[AttrTypeFactory.xs_qmap()], **kwargs,
        )

    @classmethod
    def attribute(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.ATTRIBUTE, **kwargs)

    @classmethod
    def attribute_group(cls, **kwargs) -> Attr:
        return cls.create(tag=Tag.ATTRIBUTE_GROUP, **kwargs)

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
    model = Package
    counter = 65

    @classmethod
    def create(cls, name=None, source=None, alias=None):

        return cls.model(
            name=name or f"package_{cls.next_letter()}",
            source=source or "target",
            alias=alias or None,
        )
