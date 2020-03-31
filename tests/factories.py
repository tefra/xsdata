import random
import unittest
from abc import ABC
from abc import abstractmethod

from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.codegen import Package
from xsdata.models.codegen import Restrictions
from xsdata.models.elements import Attribute
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Restriction
from xsdata.models.elements import SimpleType
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import TagType

NSMAP = {ns.prefix: ns.uri for ns in Namespace}


class FactoryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super(FactoryTestCase, self).setUp()
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
        nsmap=None,
        package="foo",
        module="tests",
    ):
        return cls.model(
            name=name or f"class_{cls.next_letter()}",
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
            nsmap=nsmap if isinstance(nsmap, dict) else NSMAP,
        )

    @classmethod
    def enumeration(cls, attributes: int, **kwargs) -> Class:
        return ClassFactory.create(
            type=SimpleType,
            attrs=AttrFactory.list(attributes, local_type=TagType.ENUMERATION),
            **kwargs,
        )

    @classmethod
    def elements(cls, attributes: int, **kwargs) -> Class:
        return ClassFactory.create(
            type=ComplexType,
            attrs=AttrFactory.list(attributes, local_type=TagType.ELEMENT),
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
    def create(cls, name=None, index=None, alias=None, native=False, forward_ref=False):

        return cls.model(
            name=name or f"attr_{cls.next_letter()}",
            index=index or 0,
            alias=alias,
            native=native,
            forward_ref=forward_ref,
        )

    @classmethod
    def xs_string(cls):
        return cls.create(name=DataType.STRING.code, native=True)

    @classmethod
    def xs_int(cls):
        return cls.create(name=DataType.INTEGER.code, native=True)

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


class AttrFactory(Factory):
    model = Attr
    types = [Attribute, Element, Restriction]
    counter = 65

    @classmethod
    def create(
        cls,
        name=None,
        index=None,
        types=None,
        local_type=None,
        namespace=None,
        help=None,
        default=None,
        fixed=False,
        wildcard=False,
        restrictions=None,
    ):
        name = name or f"attr_{cls.next_letter()}"
        return cls.model(
            name=name,
            local_name=name,
            index=cls.counter if index is None else index,
            types=types or [AttrTypeFactory.xs_string()],
            local_type=local_type or random.choice(cls.types).__name__,
            namespace=namespace or None,
            help=help or None,
            default=default or None,
            fixed=fixed,
            wildcard=wildcard,
            restrictions=restrictions or RestrictionsFactory.create(),
        )

    @classmethod
    def enumeration(cls, **kwargs) -> Attr:
        return cls.create(local_type=TagType.ENUMERATION, **kwargs)

    @classmethod
    def element(cls, **kwargs) -> Attr:
        return cls.create(local_type=TagType.ELEMENT, **kwargs)

    @classmethod
    def any(cls, **kwargs) -> Attr:
        return cls.create(
            local_type=TagType.ANY, types=[AttrTypeFactory.xs_any()], **kwargs
        )

    @classmethod
    def any_attribute(cls, **kwargs) -> Attr:
        return cls.create(
            local_type=TagType.ANY_ATTRIBUTE,
            types=[AttrTypeFactory.xs_qmap()],
            **kwargs,
        )

    @classmethod
    def attribute(cls, **kwargs) -> Attr:
        return cls.create(local_type=TagType.ATTRIBUTE, **kwargs)

    @classmethod
    def attribute_group(cls, **kwargs) -> Attr:
        return cls.create(local_type=TagType.ATTRIBUTE_GROUP, **kwargs)

    @classmethod
    def group(cls, **kwargs) -> Attr:
        return cls.create(local_type=TagType.GROUP, **kwargs)


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
