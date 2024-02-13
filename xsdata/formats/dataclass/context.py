import sys
from collections import defaultdict
from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Type

from xsdata.exceptions import XmlContextError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.compat import class_types
from xsdata.formats.dataclass.models.builders import XmlMetaBuilder
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.models.enums import DataType
from xsdata.utils.constants import return_input


class XmlContext:
    """The models context class.

    The context is responsible to provide binding metadata
    for models and their fields.

    Args:
        element_name_generator: Default element name generator
        attribute_name_generator: Default attribute name generator
        class_type: Default class type `dataclasses`
        models_package: Restrict auto locate to a specific package

    Attributes:
        cache: Internal cache for binding metadata instances
        xsi_cache: Internal cache for xsi types to class locations
        sys_modules: The number of loaded sys modules
    """

    __slots__ = (
        "element_name_generator",
        "attribute_name_generator",
        "class_type",
        "models_package",
        "cache",
        "xsi_cache",
        "sys_modules",
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
        """Reset all internal caches."""
        self.cache.clear()
        self.xsi_cache.clear()
        self.sys_modules = 0

    def get_builder(
        self,
        globalns: Optional[Dict[str, Callable]] = None,
    ) -> XmlMetaBuilder:
        """Return a new xml meta builder instance."""
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
        """Build the model metadata for the given class.

        Args:
            clazz: The requested dataclass type
            parent_ns: The inherited parent namespace
            xsi_type: if present it means that the given clazz is
                derived and the lookup procedure needs to check and match a
                dataclass model to the qualified name instead.

        Returns:
            A xml meta instance
        """
        meta = self.build(clazz, parent_ns)
        subclass = None
        if xsi_type and meta.target_qname != xsi_type:
            subclass = self.find_subclass(clazz, xsi_type)

        return self.build(subclass, parent_ns) if subclass else meta

    def build_xsi_cache(self):
        """Index all imported data classes by their xsi:type qualified name."""
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
        """Return whether the clazz is a binding model.

        If the models package is not empty also validate
        the class is located within that package.

        Args:
            clazz: The class type to inspect

        Returns:
            The bool result.
        """
        if not self.class_type.is_model(clazz):
            return False

        return not self.models_package or (
            hasattr(clazz, "__module__")
            and isinstance(clazz.__module__, str)
            and clazz.__module__.startswith(self.models_package)
        )

    def find_types(self, qname: str) -> List[Type[T]]:
        """Find all classes that match the given xsi:type qname.

        - Ignores native schema types, xs:string, xs:float, xs:int, ...
        - Rebuild cache if new modules were imported since last run

        Args:
            qname: A namespace qualified name

        Returns:
            A list of the matched classes.
        """
        if not DataType.from_qname(qname):
            self.build_xsi_cache()
            if qname in self.xsi_cache:
                return self.xsi_cache[qname]

        return []

    def find_type(self, qname: str) -> Optional[Type[T]]:
        """Return the last imported class that matches the given xsi:type qname.

        Args:
            qname: A namespace qualified name

        Returns:
            A class type or None if no matches.
        """
        types: List[Type] = self.find_types(qname)
        return types[-1] if types else None

    def find_type_by_fields(self, field_names: Set[str]) -> Optional[Type[T]]:
        """Find a data class that matches best the given list of field names.

        Args:
            field_names: A set of field names

        Returns:
            The best matching class or None if no matches. The class must
            have all the fields. If more than one classes have all the given
            fields, return the one with the least extra fields.
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
        """Find a subclass for the given clazz and xsi:type qname.

        Compare all classes that match the given xsi:type qname and return the
        first one that is either a subclass or shares the same parent class as
        the original class.

        Args:
            clazz: The input clazz type
            qname: The xsi:type to lookup from cache

        Returns:
            The matching class type or None if no matches.
        """
        types: List[Type] = self.find_types(qname)
        for tp in types:
            # Why would a xml node with have a xsi:type that points
            # to parent class is beyond me, but it happens, let's protect
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
        """Fetch or build the binding metadata for the given class.

        Args:
            clazz: A class type
            parent_ns: The inherited parent namespace
            globalns: Override the global python namespace

        Returns:
            The class binding metadata instance.
        """
        if clazz not in self.cache:
            builder = self.get_builder(globalns)
            self.cache[clazz] = builder.build(clazz, parent_ns)
        return self.cache[clazz]

    def build_recursive(self, clazz: Type, parent_ns: Optional[str] = None):
        """Build the binding metadata for the given class and all of its dependencies.

        This method is used in benchmarks!

        Args:
            clazz: The class type
            parent_ns: The inherited parent namespace
        """
        if clazz not in self.cache:
            meta = self.build(clazz, parent_ns)
            for var in meta.get_all_vars():
                types = var.element_types if var.elements else var.types
                for tp in types:
                    if self.class_type.is_model(tp):
                        self.build_recursive(tp, meta.namespace)

    def local_names_match(self, names: Set[str], clazz: Type) -> bool:
        """Check if the given field names match the given class type.

        Silently ignore, typing errors. These classes are from third
        party libraries most of them time.

        Args:
            names: A set of field names
            clazz: The class type to inspect

        Returns:
            Whether the class contains all the field names.
        """
        try:
            meta = self.build(clazz)
            local_names = {var.local_name for var in meta.get_all_vars()}
            return not names.difference(local_names)
        except (XmlContextError, NameError, TypeError):
            # The dataclass includes unsupported typing annotations
            # Let's remove it from xsi_cache
            builder = self.get_builder()
            target_qname = builder.build_class_meta(clazz).target_qname
            if target_qname and target_qname in self.xsi_cache:
                self.xsi_cache[target_qname].remove(clazz)

            return False

    @classmethod
    def is_derived(cls, obj: Any, clazz: Type) -> bool:
        """Return whether the obj is a subclass or a parent of the given class type."""
        if obj is None:
            return False

        if isinstance(obj, clazz):
            return True

        return any(x is not object and isinstance(obj, x) for x in clazz.__bases__)

    @classmethod
    def get_subclasses(cls, clazz: Type) -> Iterator[Type]:
        """Return an iterator of the given class subclasses."""
        try:
            for subclass in clazz.__subclasses__():
                yield from cls.get_subclasses(subclass)
                yield subclass
        except TypeError:
            pass
