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
from xsdata.models.enums import Namespace


NSMAP = {ns.prefix: ns.uri for ns in Namespace}


class FactoryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super(FactoryTestCase, self).setUp()
        ClassFactory.reset()
        AttrFactory.reset()
        ExtensionFactory.reset()
        RestrictionsFactory.reset()


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
        type=None,
        is_abstract=False,
        is_mixed=False,
        help=None,
        extensions=None,
        attrs=None,
        inner=None,
        nsmap=None,
    ):
        return cls.model(
            name=name or f"class_{cls.next_letter()}",
            namespace=namespace,
            is_abstract=is_abstract,
            is_mixed=is_mixed,
            type=type or random.choice(cls.types),
            extensions=extensions or [],
            attrs=attrs or [],
            inner=inner or [],
            help=help,
            nsmap=nsmap if isinstance(nsmap, dict) else NSMAP,
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
        nsmap=None,
    ):

        return cls.model(
            name=name or f"attr_{cls.next_letter()}",
            index=cls.counter if index is None else index,
            types=types or AttrTypeFactory.list(1, name="string", native=True),
            local_type=local_type or random.choice(cls.types).__name__,
            namespace=namespace or None,
            help=help or None,
            default=default or None,
            fixed=fixed,
            wildcard=wildcard,
            restrictions=restrictions or RestrictionsFactory.create(),
            nsmap=nsmap if isinstance(nsmap, dict) else NSMAP,
        )


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
