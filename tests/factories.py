import random
import unittest
from abc import ABC, abstractmethod

from xsdata.models.codegen import Attr, Class, Package
from xsdata.models.elements import (
    Attribute,
    ComplexType,
    Element,
    Restriction,
    SimpleType,
)
from xsdata.models.enums import XSDType


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
    def next(self):
        self.counter += 1
        return chr(self.counter)

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
        type=None,
        help=None,
        extensions=None,
        attrs=None,
        inner=None,
    ):

        return cls.model(
            name=name or f"class_{cls.next()}",
            type=type or random.choice(cls.types),
            extensions=extensions or [],
            attrs=attrs or [],
            inner=inner or [],
            help=help,
        )


class AttrFactory(Factory):
    model = Attr
    types = [Attribute, Element, Restriction]
    counter = 65

    @classmethod
    def create(
        cls,
        name=None,
        type=None,
        local_type=None,
        type_alias=None,
        namespace=None,
        help=None,
        forward_ref=False,
        restrictions=None,
        default=None,
    ):

        return cls.model(
            name=name or f"attr_{cls.next()}",
            type=type or XSDType.STRING.code,
            local_type=local_type or random.choice(cls.types).__name__,
            type_alias=type_alias or None,
            namespace=namespace or None,
            help=help or None,
            forward_ref=forward_ref,
            restrictions=restrictions or {},
            default=default or None,
        )


class PackageFactory(Factory):
    model = Package
    counter = 65

    @classmethod
    def create(
        cls, name=None, source=None, alias=None,
    ):

        return cls.model(
            name=name or f"package_{cls.next()}",
            source=source or "target",
            alias=alias or None,
        )
