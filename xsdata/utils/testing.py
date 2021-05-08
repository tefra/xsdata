import abc
import copy
import importlib
import random
import unittest
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Type
from typing import TypeVar

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.models import Import
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.namespaces import build_qname

T = TypeVar("T")

DEFAULT_NS_MAP = {
    Namespace.XS.prefix: Namespace.XS.uri,
    Namespace.XSI.prefix: Namespace.XSI.uri,
    Namespace.XML.prefix: Namespace.XML.uri,
    Namespace.XLINK.prefix: Namespace.XLINK.uri,
}


def load_class(output: str, clazz_name: str) -> T:
    search = "Generating package: "
    start = len(search)
    packages = [line[start:] for line in output.splitlines() if line.startswith(search)]

    for package in reversed(packages):
        try:
            module = importlib.import_module(package)
            return getattr(module, clazz_name)
        except (ModuleNotFoundError, AttributeError):
            pass

    raise ModuleNotFoundError(f"Class `{clazz_name}` not found.")


class FactoryTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        ClassFactory.reset()
        AttrFactory.reset()
        AttrTypeFactory.reset()
        ExtensionFactory.reset()
        PackageFactory.reset()
        XmlVarFactory.reset()
        XmlMetaFactory.reset()


class Factory(abc.ABC):
    counter = 0
    model: Type

    @classmethod
    @abc.abstractmethod
    def create(cls, **kwargs: Any) -> Any:
        """Abstract method create."""

    @classmethod
    def reset(cls):
        cls.counter = 65

    @classmethod
    def next_letter(cls) -> str:
        cls.counter += 1
        return chr(cls.counter)

    @classmethod
    def list(cls, number: int, **kwargs: Any) -> List:
        return [cls.create(**kwargs) for _ in range(number)]


class ClassFactory(Factory):
    tags = [Tag.ELEMENT, Tag.ATTRIBUTE, Tag.COMPLEX_TYPE, Tag.SIMPLE_TYPE]
    counter = 65

    @classmethod
    def create(
        cls,
        qname: Optional[str] = None,
        meta_name: Optional[str] = None,
        namespace: Optional[str] = None,
        tag: Optional[str] = None,
        abstract: bool = False,
        mixed: bool = False,
        nillable: bool = False,
        extensions: Optional[List[Extension]] = None,
        substitutions: Optional[List[str]] = None,
        attrs: Optional[List[Attr]] = None,
        inner: Optional[List[Class]] = None,
        ns_map: Optional[Dict] = None,
        package: Optional[str] = None,
        module: str = "tests",
        status: Status = Status.RAW,
        container: Optional[str] = None,
        default: Any = None,
        fixed: bool = False,
        **kwargs: Any,
    ) -> Class:
        if not qname:
            qname = build_qname("xsdata", f"class_{cls.next_letter()}")

        if ns_map is None:
            ns_map = copy.deepcopy(DEFAULT_NS_MAP)

        return Class(
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
            package=package,
            module=module,
            ns_map=ns_map,
            status=status,
            container=container,
            default=default,
            fixed=fixed,
            **kwargs,
        )

    @classmethod
    def simple_type(cls, **kwargs: Any) -> Class:
        return cls.create(
            tag=Tag.SIMPLE_TYPE,
            attrs=AttrFactory.list(1, tag=Tag.EXTENSION),
            **kwargs,
        )

    @classmethod
    def enumeration(cls, attributes: int, **kwargs: Any) -> Class:
        return cls.create(
            tag=Tag.SIMPLE_TYPE,
            attrs=AttrFactory.list(attributes, tag=Tag.ENUMERATION),
            **kwargs,
        )

    @classmethod
    def elements(cls, attributes: int, **kwargs: Any) -> Class:
        return cls.create(
            tag=Tag.COMPLEX_TYPE,
            attrs=AttrFactory.list(attributes, tag=Tag.ELEMENT),
            **kwargs,
        )

    @classmethod
    def service(cls, attributes: int, **kwargs: Any) -> Class:
        return cls.create(
            tag=Tag.BINDING_OPERATION,
            attrs=AttrFactory.list(attributes, tag=Tag.ELEMENT),
            **kwargs,
        )


class ExtensionFactory(Factory):
    counter = 65

    @classmethod
    def create(
        cls,
        attr_type: Optional[AttrType] = None,
        restrictions: Optional[Restrictions] = None,
        **kwargs: Any,
    ) -> Extension:
        return Extension(
            type=attr_type or AttrTypeFactory.create(),
            restrictions=restrictions or Restrictions(),
        )

    @classmethod
    def reference(cls, qname: str, **kwargs: Any) -> Extension:
        restrictions = kwargs.pop("restrictions", None)
        return cls.create(
            AttrTypeFactory.create(qname=qname, **kwargs), restrictions=restrictions
        )

    @classmethod
    def native(cls, datatype: DataType, **kwargs: Any) -> Extension:
        return cls.create(AttrTypeFactory.native(datatype), **kwargs)


class AttrTypeFactory(Factory):
    counter = 65

    @classmethod
    def create(
        cls,
        qname: Optional[str] = None,
        alias: Optional[str] = None,
        native: bool = False,
        forward: bool = False,
        circular: bool = False,
        reference: int = 0,
        **kwargs: Any,
    ) -> AttrType:
        if not qname:
            qname = build_qname("xsdata", f"attr_{cls.next_letter()}")

        return AttrType(
            qname=str(qname),
            alias=alias,
            native=native,
            circular=circular,
            forward=forward,
            reference=reference,
        )

    @classmethod
    def native(cls, datatype: DataType, **kwargs: Any) -> AttrType:
        return cls.create(qname=str(datatype), native=True, **kwargs)


class AttrFactory(Factory):
    tags = [Tag.ATTRIBUTE, Tag.ELEMENT, Tag.RESTRICTION]
    counter = 65

    @classmethod
    def create(
        cls,
        name: Optional[str] = None,
        index: Optional[int] = None,
        types: Optional[List[AttrType]] = None,
        choices: Optional[List[Attr]] = None,
        tag: Optional[str] = None,
        namespace: Optional[str] = None,
        default: Any = None,
        fixed: bool = False,
        mixed: bool = False,
        restrictions: Optional[Restrictions] = None,
        **kwargs: Any,
    ) -> Attr:
        name = name or f"attr_{cls.next_letter()}"
        return Attr(
            name=name,
            index=cls.counter if index is None else index,
            types=types or [AttrTypeFactory.native(DataType.STRING)],
            choices=choices or [],
            tag=tag or random.choice(cls.tags),
            namespace=namespace or None,
            default=default or None,
            fixed=fixed,
            mixed=mixed,
            restrictions=restrictions or Restrictions(),
            **kwargs,
        )

    @classmethod
    def native(cls, datatype: DataType, tag: str = Tag.ELEMENT, **kwargs: Any) -> Attr:
        return cls.create(tag=tag, types=[AttrTypeFactory.native(datatype)], **kwargs)

    @classmethod
    def enumeration(cls, **kwargs: Any) -> Attr:
        return cls.create(tag=Tag.ENUMERATION, **kwargs)

    @classmethod
    def element(cls, **kwargs: Any) -> Attr:
        return cls.create(tag=Tag.ELEMENT, **kwargs)

    @classmethod
    def any(cls, **kwargs: Any) -> Attr:
        return cls.create(
            tag=Tag.ANY, types=[AttrTypeFactory.native(DataType.ANY_TYPE)], **kwargs
        )

    @classmethod
    def any_attribute(cls, **kwargs: Any) -> Attr:
        return cls.create(
            tag=Tag.ANY_ATTRIBUTE,
            types=[AttrTypeFactory.native(DataType.ANY_TYPE)],
            **kwargs,
        )

    @classmethod
    def attribute(cls, **kwargs: Any) -> Attr:
        return cls.create(tag=Tag.ATTRIBUTE, **kwargs)

    @classmethod
    def attribute_group(cls, **kwargs: Any) -> Attr:
        return cls.create(
            tag=Tag.ATTRIBUTE_GROUP,
            types=[AttrTypeFactory.create(qname=kwargs.get("name"))],
            **kwargs,
        )

    @classmethod
    def group(cls, **kwargs: Any) -> Attr:
        return cls.create(tag=Tag.GROUP, **kwargs)


class PackageFactory(Factory):
    counter = 65

    @classmethod
    def create(
        cls,
        name: str = "package",
        source: str = "target",
        alias: Optional[str] = None,
        **kwargs: Any,
    ) -> Import:
        return Import(name=name, source=source, alias=alias)


class XmlVarFactory(Factory):
    counter = 65

    @classmethod
    def create(
        cls,
        name: Optional[str] = None,
        qname: Optional[str] = None,
        index: int = 0,
        types: Optional[Sequence[Type]] = None,
        init: bool = True,
        mixed: bool = False,
        tokens: bool = False,
        format: Optional[str] = None,
        derived: bool = False,
        any_type: bool = False,
        nillable: bool = False,
        sequential: bool = False,
        list_element: bool = False,
        default: Any = None,
        xml_type: str = XmlType.ELEMENT,
        namespaces: Optional[Sequence[str]] = None,
        elements: Optional[Dict[str, XmlVar]] = None,
        wildcards: Optional[Sequence[XmlVar]] = None,
        **kwargs: Any,
    ) -> XmlVar:

        name = name or f"field_{cls.next_letter()}"

        if qname is None:
            qname = name

        if types is None:
            types = ()
        if namespaces is None:
            namespaces = ()
        if elements is None:
            elements = {}
        if wildcards is None:
            wildcards = []

        return XmlVar(
            index=index,
            name=name,
            qname=qname,
            types=types,
            init=init,
            mixed=mixed,
            tokens=tokens,
            format=format,
            derived=derived,
            any_type=any_type,
            nillable=nillable,
            sequential=sequential,
            list_element=list_element,
            default=default,
            xml_type=xml_type,
            namespaces=namespaces,
            elements=elements,
            wildcards=wildcards,
        )


class XmlMetaFactory(Factory):
    counter = 65

    @classmethod
    def create(  # type: ignore
        cls,
        clazz: Type,
        qname: Optional[str] = None,
        source_qname: Optional[str] = None,
        nillable: bool = False,
        text: Optional[XmlVar] = None,
        choices: Optional[Sequence[XmlVar]] = None,
        elements: Optional[Dict[str, Sequence[XmlVar]]] = None,
        wildcards: Optional[Sequence[XmlVar]] = None,
        attributes: Optional[Dict[str, XmlVar]] = None,
        any_attributes: Optional[Sequence[XmlVar]] = None,
        **kwargs: Any,
    ) -> XmlMeta:

        if qname is None:
            qname = clazz.__name__

        if source_qname is None:
            source_qname = qname

        if choices is None:
            choices = []

        if elements is None:
            elements = {}

        if wildcards is None:
            wildcards = []

        if any_attributes is None:
            any_attributes = []

        if attributes is None:
            attributes = {}

        return XmlMeta(
            clazz=clazz,
            qname=qname,
            source_qname=source_qname,
            nillable=nillable,
            text=text,
            choices=choices,
            elements=elements,
            wildcards=wildcards,
            attributes=attributes,
            any_attributes=any_attributes,
        )
