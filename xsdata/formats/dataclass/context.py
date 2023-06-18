import sys
from collections import defaultdict
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Type

from xsdata.exceptions import XmlContextError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.compat import class_types
from xsdata.formats.dataclass.models.builders import XmlMetaBuilder
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.models.enums import DataType
from xsdata.utils.constants import return_input


class XmlContext:
    """
    The service provider for binding operations' metadata.

    :param element_name_generator: Default element name generator
    :param attribute_name_generator: Default attribute name generator
    :param class_type: Default class type `dataclasses`
    :param models_package: Restrict auto locate to a specific package
    """

    __slots__ = (
        "element_name_generator",
        "attribute_name_generator",
        "class_type",
        "cache",
        "xsi_cache",
        "sys_modules",
        "models_package",
    )

    def __init__(
        self,
        element_name_generator: Callable = return_input,
        attribute_name_generator: Callable = return_input,
        class_type: str = "dataclasses",
        models_package: Optional[str] = None,
    ):
        self.element_name_generator = element_name_generator
        self.attribute_name_generator = attribute_name_generator
        self.class_type = class_types.get_type(class_type)

        self.cache: Dict[Type, XmlMeta] = {}
        self.xsi_cache: Dict[str, List[Type]] = defaultdict(list)
        self.models_package = models_package
        self.sys_modules = 0

    def reset(self):
        self.cache.clear()
        self.xsi_cache.clear()
        self.sys_modules = 0

    def get_builder(
        self, globalns: Optional[Dict[str, Callable]] = None
    ) -> XmlMetaBuilder:
        return XmlMetaBuilder(
            class_type=self.class_type,
            element_name_generator=self.element_name_generator,
            attribute_name_generator=self.attribute_name_generator,
            globalns=globalns,
        )

    def fetch(
        self,
        clazz: Type,
        parent_ns: Optional[str] = None,
        xsi_type: Optional[str] = None,
    ) -> XmlMeta:
        """
        Fetch the model metadata of the given dataclass type, namespace and xsi
        type.

        :param clazz: The requested dataclass type
        :param parent_ns: The inherited parent namespace
        :param xsi_type: if present it means that the given clazz is
            derived and the lookup procedure needs to check and match a
            dataclass model to the qualified name instead
        """
        meta = self.build(clazz, parent_ns)
        subclass = None
        if xsi_type and meta.target_qname != xsi_type:
            subclass = self.find_subclass(clazz, xsi_type)

        return self.build(subclass, parent_ns) if subclass else meta

    def build_xsi_cache(self):
        """Index all imported dataclasses by their xsi:type qualified name."""
        if len(sys.modules) == self.sys_modules:
            return

        self.xsi_cache.clear()
        builder = self.get_builder()
        for clazz in self.get_subclasses(object):
            if self.is_binding_model(clazz):
                meta = builder.build_class_meta(clazz)

                if meta.target_qname:
                    self.xsi_cache[meta.target_qname].append(clazz)

        self.sys_modules = len(sys.modules)

    def is_binding_model(self, clazz: Type[T]) -> bool:
        if not self.class_type.is_model(clazz):
            return False

        return not self.models_package or (
            hasattr(clazz, "__module__")
            and isinstance(clazz.__module__, str)
            and clazz.__module__.startswith(self.models_package)
        )

    def find_types(self, qname: str) -> List[Type[T]]:
        """
        Find all classes that match the given xsi:type qname.

        - Ignores native schema types, xs:string, xs:float, xs:int, ...
        - Rebuild cache if new modules were imported since last run

        :param qname: Qualified name
        """
        if not DataType.from_qname(qname):
            self.build_xsi_cache()
            if qname in self.xsi_cache:
                return self.xsi_cache[qname]

        return []

    def find_type(self, qname: str) -> Optional[Type[T]]:
        """
        Return the most recently imported class that matches the given xsi:type
        qname.

        :param qname: Qualified name
        """
        types: List[Type] = self.find_types(qname)
        return types[-1] if types else None

    def find_type_by_fields(self, field_names: Set[str]) -> Optional[Type[T]]:
        """
        Find a dataclass from all the imported modules that matches the given
        list of field names.

        :param field_names: A unique list of field names
        """

        def get_field_diff(clazz: Type) -> int:
            meta = self.cache[clazz]
            local_names = {var.local_name for var in meta.get_all_vars()}
            return len(local_names - field_names)

        self.build_xsi_cache()
        choices = [
            (clazz, get_field_diff(clazz))
            for types in self.xsi_cache.values()
            for clazz in types
            if self.local_names_match(field_names, clazz)
        ]

        choices.sort(key=lambda x: (x[1], x[0].__name__))
        return choices[0][0] if len(choices) > 0 else None

    def find_subclass(self, clazz: Type, qname: str) -> Optional[Type]:
        """
        Compare all classes that match the given xsi:type qname and return the
        first one that is either a subclass or shares the same parent class as
        the original class.

        :param clazz: The search dataclass type
        :param qname: Qualified name
        """
        types: List[Type] = self.find_types(qname)
        for tp in types:
            # Why would an xml node with have an xsi:type that points
            # to parent class is beyond me but it happens, let's protect
            # against that scenario <node xsi:type="nodeAbstract" />
            if issubclass(clazz, tp):
                continue

            for tp_mro in tp.__mro__:
                if tp_mro is not object and tp_mro in clazz.__mro__:
                    return tp

        return None

    def build(
        self,
        clazz: Type,
        parent_ns: Optional[str] = None,
        globalns: Optional[Dict[str, Callable]] = None,
    ) -> XmlMeta:
        """
        Fetch from cache or build the binding metadata for the given class and
        parent namespace.

        :param clazz: A dataclass type
        :param parent_ns: The inherited parent namespace
        """
        if clazz not in self.cache:
            builder = self.get_builder(globalns)
            self.cache[clazz] = builder.build(clazz, parent_ns)
        return self.cache[clazz]

    def build_recursive(self, clazz: Type, parent_ns: Optional[str] = None):
        """Build the binding metadata for the given class and all of its
        dependencies."""
        if clazz not in self.cache:
            meta = self.build(clazz, parent_ns)
            for var in meta.get_all_vars():
                types = var.element_types if var.elements else var.types
                for tp in types:
                    if self.class_type.is_model(tp):
                        self.build_recursive(tp, meta.namespace)

    def local_names_match(self, names: Set[str], clazz: Type) -> bool:
        try:
            meta = self.build(clazz)
            local_names = {var.local_name for var in meta.get_all_vars()}
            return not names.difference(local_names)
        except (XmlContextError, NameError):
            # The dataclass includes unsupported typing annotations
            # Let's remove it from xsi_cache
            builder = self.get_builder()
            target_qname = builder.build_class_meta(clazz).target_qname
            if target_qname and target_qname in self.xsi_cache:
                self.xsi_cache[target_qname].remove(clazz)

            return False

    @classmethod
    def is_derived(cls, obj: Any, clazz: Type) -> bool:
        """
        Return whether the given obj is derived from the given dataclass type.

        :param obj: A dataclass instance
        :param clazz: A dataclass type
        """
        if obj is None:
            return False

        if isinstance(obj, clazz):
            return True

        return any(x is not object and isinstance(obj, x) for x in clazz.__bases__)

    @classmethod
    def get_subclasses(cls, clazz: Type):
        try:
            for subclass in clazz.__subclasses__():
                yield from cls.get_subclasses(subclass)
                yield subclass
        except TypeError:
            pass
