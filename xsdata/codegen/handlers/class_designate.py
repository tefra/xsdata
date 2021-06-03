import os
from collections import defaultdict
from operator import attrgetter
from pathlib import Path
from typing import Iterable
from typing import List
from urllib.parse import urlparse

from toposort import toposort_flatten

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Class
from xsdata.models.config import StructureStyle
from xsdata.models.enums import COMMON_SCHEMA_DIR
from xsdata.utils import collections
from xsdata.utils.graphs import strongly_connected_components
from xsdata.utils.package import module_name


class ClassDesignateHandler(ContainerHandlerInterface):
    """Designate classes to packages and modules based on the output structure
    style."""

    __slots__ = ()

    def run(self):
        structure_style = self.container.config.output.structure
        if structure_style == StructureStyle.NAMESPACES:
            self.group_by_namespace()
        elif structure_style == StructureStyle.SINGLE_PACKAGE:
            self.group_all_together()
        elif structure_style == StructureStyle.CLUSTERS:
            self.group_by_strong_components()
        else:
            self.group_by_filenames()

    def group_by_filenames(self):
        """Group uris by common path and auto assign package names to all
        classes."""
        package = self.container.config.output.package
        class_map = collections.group_by(self.container, key=attrgetter("location"))
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
        package = self.container.config.output.package
        namespace_getter = attrgetter("target_namespace")
        groups = collections.group_by(self.container, key=namespace_getter)
        for namespace, classes in groups.items():
            self.assign(classes, package, namespace or "")

    def group_all_together(self):
        """Group all classes together in the same module."""
        package_parts = self.container.config.output.package.split(".")
        module = package_parts.pop()
        package = ".".join(package_parts)

        self.assign(self.container, package, module)

    def group_by_strong_components(self):
        """Find circular imports and cluster their classes together."""
        edges = {}
        class_map = {}
        for obj in self.container:
            edges[obj.qname] = set(obj.dependencies(True))
            class_map[obj.qname] = obj

        groups = strongly_connected_components(edges)
        package = self.container.config.output.package

        for group in groups:
            group_edges = {
                qname: set(class_map[qname].dependencies()).intersection(group)
                for qname in group
            }
            classes = [class_map[qname] for qname in toposort_flatten(group_edges)]
            module = classes[0].name

            self.assign(classes, package, module)

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
