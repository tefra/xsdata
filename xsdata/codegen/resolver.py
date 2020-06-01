import logging
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from lxml.etree import QName
from toposort import toposort_flatten

from xsdata.codegen.models import Class
from xsdata.codegen.models import Package
from xsdata.exceptions import ResolverValueError

logger = logging.getLogger(__name__)


@dataclass
class DependenciesResolver:
    packages: Dict[QName, str] = field(default_factory=dict)
    aliases: Dict[QName, str] = field(default_factory=dict)
    imports: List[Package] = field(default_factory=list)
    class_list: List[QName] = field(init=False, default_factory=list)
    class_map: Dict[QName, Class] = field(init=False, default_factory=dict)
    package: str = field(init=False)

    def process(self, classes: List[Class]):
        """
        Resolve the dependencies for the given list of classes and the target
        package.

        Reset aliases and imports from any previous runs keep the record
        of the processed class names
        """
        self.imports.clear()
        self.aliases.clear()
        self.class_map = self.create_class_map(classes)
        self.class_list = self.create_class_list(classes)
        self.resolve_imports()

    def sorted_imports(self) -> List[Package]:
        """Return a new sorted by name list of import packages."""
        return sorted(self.imports, key=lambda x: x.name)

    def sorted_classes(self) -> List[Class]:
        """Return an iterator of classes property sorted for generation and
        apply import aliases."""

        result = []
        for name in self.class_list:
            obj = self.class_map.get(name)
            if obj is not None:
                self.apply_aliases(obj)
                result.append(obj)
        return result

    def apply_aliases(self, obj: Class):
        """Walk the attributes tree and set the type aliases."""
        for attr in obj.attrs:
            for attr_type in attr.types:
                attr_type_qname = obj.source_qname(attr_type.name)
                attr_type.alias = self.aliases.get(attr_type_qname)

        for inner in obj.inner:
            self.apply_aliases(inner)

    def resolve_imports(self):
        """Walk the import qualified names, check for naming collisions and add
        the necessary code generator import instance."""
        local_names = [qname.localname for qname in self.class_map.keys()]
        for qname in self.import_classes():
            package = self.find_package(qname)
            exists = qname.localname in local_names
            self.add_import(qname=qname, package=package, exists=exists)

    def add_import(self, qname: QName, package: str, exists: bool = False):
        """Append an import package to the list of imports with any if
        necessary aliases if the import name exists in the local module."""
        alias = None
        if exists:
            module = package.split(".")[-1]
            alias = f"{module}:{qname.localname}"
            self.aliases[qname] = alias

        self.imports.append(Package(name=qname.localname, source=package, alias=alias))

    def find_package(self, qname: QName) -> str:
        """
        Return the package name for the given qualified class name.

        :raises ResolverValueError: if name doesn't exist.
        """
        if qname not in self.packages:
            raise ResolverValueError(f"Unknown dependency: {qname.text}")
        return self.packages[qname]

    def import_classes(self) -> List[QName]:
        """Return a list of class that need to be imported."""
        return [qname for qname in self.class_list if qname not in self.class_map]

    @staticmethod
    def create_class_list(classes: List[Class]) -> List[str]:
        """Use topology sort to return a flat list for all the dependencies."""
        return toposort_flatten(
            {obj.source_qname(): set(obj.dependencies()) for obj in classes}
        )

    @staticmethod
    def create_class_map(classes: List[Class]) -> Dict[QName, Class]:
        """Index the list of classes by name."""

        result: Dict[QName, Class] = {}
        for obj in classes:
            qname = obj.source_qname()
            if qname in result:
                raise ResolverValueError(f"Duplicate class: `{obj.name}`")
            result[qname] = obj

        return result
