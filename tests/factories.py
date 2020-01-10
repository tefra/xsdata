import random
import unittest
from abc import ABC, abstractmethod

from xsdata.models.codegen import Attr, Class, Extension, Package
from xsdata.models.elements import (
    Attribute,
    ComplexType,
    Element,
    Restriction,
    SimpleType,
    Union,
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
        is_abstract=False,
        help=None,
        extensions=None,
        attrs=None,
        inner=None,
    ):

        return cls.model(
            name=name or f"class_{cls.next()}",
            is_abstract=is_abstract,
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
        index=None,
        type=None,
        local_type=None,
        type_aliases=None,
        namespace=None,
        help=None,
        forward_ref=False,
        default=None,
        **kwargs,
    ):

        return cls.model(
            name=name or f"attr_{cls.next()}",
            index=cls.counter if index is None else index,
            type=type or XSDType.STRING.code,
            local_type=local_type or random.choice(cls.types).__name__,
            type_aliases=type_aliases or {},
            namespace=namespace or None,
            help=help or None,
            forward_ref=forward_ref,
            default=default or None,
            **kwargs,
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


class ExtensionFactory(Factory):
    types = [Union, Restriction, Extension]
    model = Extension
    counter = 65

    @classmethod
    def create(cls, name=None, index=None, type=None):

        return cls.model(
            name=name or f"ext_{cls.next()}",
            index=cls.counter if index is None else index,
            type=type or random.choice(cls.types).__name__,
        )
