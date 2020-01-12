import logging
from dataclasses import dataclass, field
from typing import Dict, Iterator, List, Optional, Set

from lxml import etree
from toposort import toposort_flatten

from xsdata.models.codegen import Class, Package
from xsdata.models.elements import Schema
from xsdata.models.enums import XSDType
from xsdata.utils import text
from xsdata.utils.text import split

logger = logging.getLogger(__name__)


@dataclass
class DependenciesResolver:
    processed: Dict[str, str] = field(default_factory=dict)
    aliases: Dict[str, str] = field(default_factory=dict)
    imports: List[Package] = field(default_factory=list)
    class_list: List[str] = field(init=False)
    class_map: Dict[str, Class] = field(init=False)
    schema: Schema = field(init=False)
    package: str = field(init=False)

    def process(self, classes: List[Class], schema: Schema, package: str):
        """
        Process a list of classes for the given schema and package.

        Reset aliases and imports from any previous runs keep the record
        of the processed class names
        """
        self.schema = schema
        self.class_map = self.create_class_map(classes)
        self.class_list = self.create_class_list(classes)
        self.package = package
        self.imports.clear()
        self.aliases.clear()
        self.resolve_imports()

    def sorted_imports(self) -> List[Package]:
        """Return a new sorted by name list of import packages."""
        return sorted(self.imports, key=lambda x: x.name)

    def sorted_classes(self) -> Iterator[Class]:
        """
        Return an iterator of classes property sorted for generation.

        Keep track of the class names and their target package name for
        future classes. Also apply type aliases for the given process
        run.
        """
        for name in self.class_list:
            obj = self.class_map.get(name)
            if obj is not None:
                self.add_package(obj)
                yield self.apply_aliases(obj)

    def apply_aliases(self, obj: Class) -> Class:
        """Walk the attributes tree and set the type aliases."""
        for attr in obj.attrs:
            attr.type_aliases = {
                type_name: self.aliases.get(type_name)
                for type_name in attr.types
                if self.aliases.get(type_name)
            }

        for inner in obj.inner:
            self.apply_aliases(inner)

        return obj

    def resolve_imports(self) -> None:
        """Walk all the import class names and add type aliases for name
        collisions with the given list of classes and build a list of import
        packages."""
        for ref in self.import_classes():
            prefix, name = split(ref)
            package = self.find_package(prefix, name)
            alias = ref if prefix and self.class_map.get(name) else None

            self.add_import(name=name, package=package, alias=alias)

    def add_import(
        self, name: str, package: str, alias: Optional[str]
    ) -> None:
        """Create and append an import package to the list of imports, collect
        a map of aliases for when we process the list of classes to
        generate."""
        if alias is not None:
            self.aliases[alias] = alias
        self.imports.append(Package(name=name, source=package, alias=alias))

    def add_package(self, obj: Class) -> None:
        """
        Add the given class to the map of processed items indexed with the
        qname of the class and the schema target namespace.

        eg {http://www.namespace/name}ClassName
        """
        qname = etree.QName(self.schema.target_namespace, obj.name)
        self.processed[qname.text] = self.package

    def find_package(self, prefix, name) -> str:
        """
        Use the schema namespaces map to find the package where the requested
        class belongs to.

        Example:
            * Schema nsmap {"common": "http://www.common/ns"}
            * Resolved processed {"{http://www.common/ns}address": "source.package"}
            * Request for (common, address) will return source.package
        """
        namespace = self.schema.nsmap.get(prefix)
        qname = etree.QName(namespace, name)
        return self.processed[qname.text]

    def import_classes(self):
        """Return a list of class that need to be imported."""
        return [name for name in self.class_list if name not in self.class_map]

    def create_class_list(self, classes: List[Class]):
        """Use topology sort to return a flat list for all the dependencies."""

        prefix = self.schema.target_prefix
        return toposort_flatten(
            {obj.name: self.collect_deps(obj, prefix) for obj in classes}
        )

    def collect_deps(self, obj: Class, prefix: Optional[str]) -> Set[str]:
        """
        Return a list of dependencies for the given class.

        Collect:
            * base classes
            * attribute types
            * recursively go through the inner classes
            * Ignore inner class references
            * Filter the standard xsd types
        """
        deps: Set[str] = set()
        for attr in obj.attrs:
            if not attr.forward_ref:
                deps.update(list(attr.types))

        deps.update(ext.name for ext in obj.extensions)
        for inner in obj.inner:
            deps.update(self.collect_deps(inner, prefix))

        return {
            text.strip_prefix(dep, prefix)
            for dep in deps
            if dep and not XSDType.get_enum(dep)
        }

    @staticmethod
    def create_class_map(classes: List[Class]):
        """Index the list of classes by name."""

        result: Dict[str, Class] = dict()
        for obj in classes:
            if obj.name in result:
                raise ValueError(f"Duplicate class name`{obj.name}`")
            result[obj.name] = obj

        return result
