import random
import unittest
from abc import ABC
from abc import abstractmethod

from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Package
from xsdata.models.elements import Attribute
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Restriction
from xsdata.models.elements import SimpleType


class FactoryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super(FactoryTestCase, self).setUp()
        ClassFactory.reset()
        AttrFactory.reset()


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
        **kwargs,
    ):

        return cls.model(
            name=name or f"attr_{cls.next_letter()}",
            index=cls.counter if index is None else index,
            types=types or AttrTypeFactory.list(1, name="string", native=True),
            local_type=local_type or random.choice(cls.types).__name__,
            namespace=namespace or None,
            help=help or None,
            default=default or None,
            **kwargs,
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
