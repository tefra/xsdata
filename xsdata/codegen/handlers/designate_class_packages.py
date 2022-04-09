import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import Set
from urllib.parse import urlparse

from toposort import toposort_flatten

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_location
from xsdata.codegen.models import get_target_namespace
from xsdata.exceptions import CodeGenerationError
from xsdata.models.config import ObjectType
from xsdata.models.config import StructureStyle
from xsdata.models.enums import COMMON_SCHEMA_DIR
from xsdata.utils import collections
from xsdata.utils.graphs import strongly_connected_components
from xsdata.utils.namespaces import to_package_name
from xsdata.utils.package import module_name


class DesignateClassPackages(ContainerHandlerInterface):
    """Designate classes to packages and modules based on the output structure
    style."""

    __slots__ = ()

    def run(self):
        structure_style = self.container.config.output.structure_style
        if structure_style == StructureStyle.NAMESPACES:
            self.group_by_namespace()
        elif structure_style == StructureStyle.SINGLE_PACKAGE:
            self.group_all_together()
        elif structure_style == StructureStyle.CLUSTERS:
            self.group_by_strong_components()
        elif structure_style == StructureStyle.NAMESPACE_CLUSTERS:
            self.group_by_namespace_clusters()
        else:
            self.group_by_filenames()

    def group_by_filenames(self):
        """Group uris by common path and auto assign package names to all
        classes."""
        package = self.container.config.output.package
        class_map = collections.group_by(self.container, key=get_location)
        groups = self.group_common_paths(class_map.keys())

        for keys in groups:
            if len(keys) == 1:
                common_path = os.path.dirname(keys[0])
            else:
                common_path = os.path.commonpath(keys)

            for key in keys:
                items = class_map[key]
                suffix = ".".join(Path(key).parent.relative_to(common_path).parts)

                package_name = f"{package}.{suffix}" if suffix else package
                self.assign(items, package_name, module_name(key))

    def group_by_namespace(self):
        """Group classes by their target namespace."""
        groups = collections.group_by(self.container, key=get_target_namespace)
        for namespace, classes in groups.items():
            parts = self.combine_ns_package(namespace)
            module = parts.pop()
            package = ".".join(parts)
            self.assign(classes, package, module)

    def group_all_together(self):
        """Group all classes together in the same module."""
        package_parts = self.container.config.output.package.split(".")
        module = package_parts.pop()
        package = ".".join(package_parts)

        self.assign(self.container, package, module)

    def group_by_strong_components(self):
        """Find circular imports and cluster their classes together."""
        package = self.container.config.output.package
        for group in self.strongly_connected_classes():
            classes = self.sorted_classes(group)
            module = classes[0].name
            self.assign(classes, package, module)

    def group_by_namespace_clusters(self):
        for group in self.strongly_connected_classes():
            classes = self.sorted_classes(group)
            if len(set(map(get_target_namespace, classes))) > 1:
                raise CodeGenerationError(
                    "Found strongly connected classes from different "
                    "namespaces, grouping them is impossible!"
                )

            parts = self.combine_ns_package(classes[0].target_namespace)
            module = classes[0].name
            self.assign(classes, ".".join(parts), module)

    def sorted_classes(self, qnames: Set[str]) -> List[Class]:
        edges = {
            qname: set(self.container.first(qname).dependencies()).intersection(qnames)
            for qname in qnames
        }
        return [self.container.first(qname) for qname in toposort_flatten(edges)]

    def strongly_connected_classes(self) -> Iterator[Set[str]]:
        edges = {obj.qname: list(set(obj.dependencies(True))) for obj in self.container}
        return strongly_connected_components(edges)

    @classmethod
    def assign(cls, classes: Iterable[Class], package: str, module: str):
        for obj in classes:
            obj.package = package
            obj.module = module
            cls.assign(obj.inner, package, module)

    @classmethod
    def group_common_paths(cls, paths: Iterable[str]) -> List[List[str]]:
        prev = ""
        index = 0
        groups = defaultdict(list)
        common_schemas_dir = COMMON_SCHEMA_DIR.as_uri()

        for path in sorted(paths):
            if path.startswith(common_schemas_dir):
                groups[0].append(path)
            else:
                path_parsed = urlparse(path)
                common_path = os.path.commonpath((prev, path))
                if not common_path or common_path == path_parsed.scheme:
                    index += 1

                prev = path
                groups[index].append(path)

        return list(groups.values())

    def combine_ns_package(self, namespace: Optional[str]) -> List[str]:
        result = self.container.config.output.package.split(".")

        if namespace:
            substitution = collections.first(
                re.sub(sub.search, sub.replace, namespace)
                for sub in self.container.config.substitutions.substitution
                if sub.type == ObjectType.PACKAGE
                and re.fullmatch(sub.search, namespace) is not None
            )
        else:
            substitution = None

        if substitution:
            result.extend(substitution.split("."))
        else:
            result.extend(to_package_name(namespace).split("."))

        return list(filter(None, result))
