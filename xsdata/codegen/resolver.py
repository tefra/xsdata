import logging
import re
from typing import Dict, List

from toposort import toposort_flatten

from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.models import Class, Import, get_slug
from xsdata.utils import collections

logger = logging.getLogger(__name__)


class DependenciesResolver:
    """The dependencies resolver class.

    Calculate what classes need to be imported
    per package, with aliases support.

    Args:
        registry: The full class qname-module map.

    Attributes:
        aliases: The generated aliases dictionary
        imports: The list of generated imports
        class_list: The topo-sorted list of class qnames
        class_map: A qname-class map

    """

    __slots__ = "registry", "aliases", "imports", "class_list", "class_map"

    def __init__(self, registry: Dict[str, str]):
        self.registry = registry
        self.aliases: Dict[str, str] = {}
        self.imports: List[Import] = []
        self.class_list: List[str] = []
        self.class_map: Dict[str, Class] = {}

    def process(self, classes: List[Class]):
        """Resolve the dependencies for the given class list.

        Reset previously resolved imports and aliases.

        Args:
            classes: A list of classes that belong to the same target module
        """
        self.imports.clear()
        self.aliases.clear()
        self.class_map = self.create_class_map(classes)
        self.class_list = self.create_class_list(classes)
        self.resolve_imports()

    def sorted_imports(self) -> List[Import]:
        """Return a new sorted by name list of import instances."""
        return sorted(self.imports, key=lambda x: x.name)

    def sorted_classes(self) -> List[Class]:
        """Apply aliases and return the sorted the generated class list."""
        result = []
        for name in self.class_list:
            obj = self.class_map.get(name)
            if obj is not None:
                self.apply_aliases(obj)
                result.append(obj)
        return result

    def apply_aliases(self, target: Class):
        """Apply import aliases to the target class.

        Update attr and extension types to point to the
        new class aliases. Process inner classes too!

        Args:
            target: The target class instance to process
        """
        for attr in target.attrs:
            for attr_type in attr.types:
                attr_type.alias = self.aliases.get(attr_type.qname)

            for choice in attr.choices:
                for choice_type in choice.types:
                    choice_type.alias = self.aliases.get(choice_type.qname)

        for ext in target.extensions:
            ext.type.alias = self.aliases.get(ext.type.qname)

        collections.apply(target.inner, self.apply_aliases)

    def resolve_imports(self):
        """Build the list of class imports and set aliases if necessary."""
        self.imports = [
            Import(qname=qname, source=self.get_class_module(qname))
            for qname in self.import_classes()
        ]
        protected = {obj.slug for obj in self.class_map.values()}
        self.resolve_conflicts(self.imports, protected)
        self.set_aliases()

    def set_aliases(self):
        """Store generated aliases."""
        self.aliases = {imp.qname: imp.alias for imp in self.imports if imp.alias}

    @classmethod
    def resolve_conflicts(cls, imports: List[Import], protected: set):
        """Find naming conflicts between imports and generate aliases.

        Example:
            from foo.bar import MyType as BarMyType
            from bar.foo import MyType as FooMyType

        Args:
            imports: The list of class import instances
            protected: The set of protected class names from the module
        """
        for slug, group in collections.group_by(imports, key=get_slug).items():
            if len(group) == 1:
                if slug in protected:
                    imp = group[0]
                    module = imp.source.split(".")[-1]
                    imp.alias = f"{module}:{imp.name}"
                continue

            for index, cur in enumerate(group):
                cmp = group[index + 1] if index == 0 else group[index - 1]
                parts = re.split("[_.]", cur.source)
                diff = set(parts) - set(re.split("[_.]", cmp.source))

                add = "_".join(part for part in parts if part in diff)
                cur.alias = f"{add}:{cur.name}"

    def get_class_module(self, qname: str) -> str:
        """Return the module for the given qualified class name.

        Args:
            qname: The namespace qualified name of the class

        Raises:
            CodeGenerationError: if name doesn't exist.
        """
        if qname not in self.registry:
            raise CodegenError("Failed to resolve dependency", qname=qname)
        return self.registry[qname]

    def import_classes(self) -> List[str]:
        """Return a list of class qnames that need to be imported."""
        return [qname for qname in self.class_list if qname not in self.class_map]

    @staticmethod
    def create_class_list(classes: List[Class]) -> List[str]:
        """Use topology sort to return a flat list for all the dependencies."""
        return toposort_flatten({obj.qname: set(obj.dependencies()) for obj in classes})

    @staticmethod
    def create_class_map(classes: List[Class]) -> Dict[str, Class]:
        """Index the list of classes by their qualified names.

        Raises:
            CodeGenerationError: If two classes have the same qname.

        Returns:
            A qname-class map.
        """
        result: Dict[str, Class] = {}
        for obj in classes:
            if obj.qname in result:
                raise CodegenError("Duplicate class during resolve", qname=obj.qname)
            result[obj.qname] = obj

        return result
