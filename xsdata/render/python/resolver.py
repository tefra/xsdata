from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Set

from lxml import etree
from toposort import toposort_flatten

from xsdata.models.elements import Schema
from xsdata.models.enums import XSDType
from xsdata.models.render import Class, Object, Package


@dataclass
class ImportResolver:

    processed: Dict[str, str] = field(default_factory=dict)
    imports: List[Package] = field(default_factory=list)
    class_list: List[str] = field(init=False)
    class_map: Dict[str, Class] = field(init=False)
    schema: Schema = field(init=False)

    def current(self, classes: List[Class], schema: Schema):
        self.class_map = self.create_class_map(classes)
        self.class_list = self.create_class_list(classes)
        self.schema = schema

    def import_packages(self):
        len(self.imports) or self.resolve_imports()
        return self.imports

    def process_classes(self, package):
        for name in self.class_list:
            obj = self.class_map.get(name)
            if obj:
                qname = etree.QName(self.schema.target_namespace, obj.name)
                self.processed[qname.text] = package
                yield obj

    def type_overrides(self):
        len(self.imports) or self.resolve_imports()

        return {
            obj.alias: True
            for package in self.imports
            for obj in package.objects
            if obj.alias
        }

    def resolve_imports(self):
        tmp = defaultdict(list)
        for ref in self.import_classes():
            has_ns = ref.find(":") > -1

            prefix, name = ref.split(":") if has_ns else (None, ref)
            package = self.find_package(prefix, name)
            tmp[package].append(
                (name, ref) if has_ns and name in self.class_map else (name,)
            )

        self.imports = [
            Package(
                name=package,
                objects=[Object(*value) for value in sorted(tmp[package])],
            )
            for package in sorted(tmp.keys())
        ]

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
