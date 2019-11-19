from dataclasses import dataclass, field
from typing import Dict, List, Set

from lxml import etree
from toposort import toposort_flatten

from xsdata.models.codegen import Class, Package
from xsdata.models.elements import Schema
from xsdata.models.enums import XSDType


@dataclass
class ImportResolver:
    processed: Dict[str, str] = field(default_factory=dict)
    aliases: Dict[str, str] = field(default_factory=dict)
    imports: List[Package] = field(default_factory=list)
    class_list: List[str] = field(init=False)
    class_map: Dict[str, Class] = field(init=False)
    schema: Schema = field(init=False)
    package: str = field(init=False)

    def process(self, classes: List[Class], schema: Schema, package: str):
        self.class_map = self.create_class_map(classes)
        self.class_list = self.create_class_list(classes)
        self.schema = schema
        self.package = package
        self.imports.clear()
        self.resolve_imports()

    def sorted_imports(self):
        return sorted(self.imports, key=lambda x: x.name)

    def sorted_classes(self):
        for name in self.class_list:
            if name in self.class_map:
                obj = self.class_map.get(name)
                self.add_package(obj)
                self.apply_aliases(obj)
                yield self.apply_aliases(obj)

    def apply_aliases(self, obj: Class):
        for attr in obj.attrs:
            attr.type_alias = self.aliases.get(attr.type)

        for inner in obj.inner:
            self.apply_aliases(inner)

        return obj

    def resolve_imports(self):
        for ref in self.import_classes():
            has_ns = ref.find(":") > -1
            prefix, name = ref.split(":") if has_ns else (None, ref)
            package = self.find_package(prefix, name)
            alias = ref if has_ns and self.class_map.get(name) else None

            self.add_import(name, alias, package)

    def add_import(self, name, alias, package):
        if alias:
            self.aliases[alias] = alias
        self.imports.append(Package(name=name, alias=alias, source=package))

    def add_package(self, obj: Class):
        qname = etree.QName(self.schema.target_namespace, obj.name)
        self.processed[qname.text] = self.package

    def find_package(self, prefix, name):
        namespace = self.schema.nsmap.get(prefix)
        qname = etree.QName(namespace, name)
        return self.processed.get(qname.text)

    def import_classes(self):
        return [name for name in self.class_list if name not in self.class_map]

    def create_class_map(self, classes: List[Class]):
        return {obj.name: obj for obj in classes}

    def create_class_list(self, classes: List[Class]):
        return toposort_flatten(
            {obj.name: self.collect_deps(obj) for obj in classes}
        )

    def collect_deps(self, obj: Class) -> Set[str]:
        dependencies = {
            attr.type for attr in obj.attrs if not attr.forward_ref
        }
        if len(obj.extensions) > 0:
            dependencies.update(obj.extensions)
        for inner in obj.inner:
            dependencies.update(self.collect_deps(inner))

        return set(filter(self.filter_xsd_types, dependencies))

    def filter_xsd_types(self, code: str):
        return XSDType.get_enum(code) is None
