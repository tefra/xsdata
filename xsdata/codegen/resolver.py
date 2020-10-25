import logging
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from toposort import toposort_flatten

from xsdata.codegen.models import Class
from xsdata.codegen.models import Import
from xsdata.exceptions import ResolverValueError
from xsdata.utils import collections
from xsdata.utils.namespaces import split_qname

logger = logging.getLogger(__name__)


@dataclass
class DependenciesResolver:
    packages: Dict[str, str] = field(default_factory=dict)
    aliases: Dict[str, str] = field(default_factory=dict)
    imports: List[Import] = field(default_factory=list)
    class_list: List[str] = field(init=False, default_factory=list)
    class_map: Dict[str, Class] = field(init=False, default_factory=dict)
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

    def sorted_imports(self) -> List[Import]:
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
                attr_type.alias = self.aliases.get(attr_type.qname)

        collections.apply(obj.inner, self.apply_aliases)

    def resolve_imports(self):
        """Walk the import qualified names, check for naming collisions and add
        the necessary code generator import instance."""
        local_names = {split_qname(qname)[1] for qname in self.class_map.keys()}
        for qname in self.import_classes():
            package = self.find_package(qname)
            local_name = split_qname(qname)[1]
            exists = local_name in local_names
            local_names.add(local_name)
            self.add_import(qname=qname, package=package, exists=exists)

    def add_import(self, qname: str, package: str, exists: bool = False):
        """Append an import package to the list of imports with any if
        necessary aliases if the import name exists in the local module."""
        alias = None
        local_name = split_qname(qname)[1]
        if exists:
            module = package.split(".")[-1]
            alias = f"{module}:{local_name}"
            self.aliases[qname] = alias

        self.imports.append(Import(name=local_name, source=package, alias=alias))

    def find_package(self, qname: str) -> str:
        """
        Return the package name for the given qualified class name.

        :raises ResolverValueError: if name doesn't exist.
        """
        if qname not in self.packages:
            raise ResolverValueError(f"Unknown dependency: {qname}")
        return self.packages[qname]

    def import_classes(self) -> List[str]:
        """Return a list of class that need to be imported."""
        return [qname for qname in self.class_list if qname not in self.class_map]

    @staticmethod
    def create_class_list(classes: List[Class]) -> List[str]:
        """Use topology sort to return a flat list for all the dependencies."""
        return toposort_flatten({obj.qname: set(obj.dependencies()) for obj in classes})

    @staticmethod
    def create_class_map(classes: List[Class]) -> Dict[str, Class]:
        """Index the list of classes by name."""

        result: Dict[str, Class] = {}
        for obj in classes:
            if obj.qname in result:
                raise ResolverValueError(f"Duplicate class: `{obj.name}`")
            result[obj.qname] = obj

        return result
