import operator
import os
from collections import defaultdict
from pathlib import Path
from typing import Iterable
from typing import List
from urllib.parse import urlparse

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Class
from xsdata.models.config import StructureStyle
from xsdata.models.enums import COMMON_SCHEMA_DIR
from xsdata.utils import collections
from xsdata.utils.package import module_name


class ClassAssignmentHandler(ContainerHandlerInterface):
    """Resolve class name conflicts depending the the output structure
    style."""

    __slots__ = ()

    def run(self):
        """Search for conflicts either by qualified name or local name
        depending the configuration and start renaming classes and
        dependencies."""

        structure_style = self.container.config.output.structure
        if structure_style == StructureStyle.NAMESPACES:
            self.assign_with_namespaces()
        elif structure_style == StructureStyle.SINGLE_PACKAGE:
            self.assign_with_package()
        else:
            self.assign_with_filenames()

    def assign_with_filenames(self):
        """Group uris by common path and auto assign package names to all
        classes."""
        package = self.container.config.output.package
        location_getter = operator.attrgetter("location")
        class_map = collections.group_by(self.container.iterate(), key=location_getter)
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

    def assign_with_namespaces(self):
        package = self.container.config.output.package
        namespace_getter = operator.attrgetter("target_namespace")
        groups = collections.group_by(self.container.iterate(), key=namespace_getter)
        for namespace, classes in groups.items():
            self.assign(classes, package, namespace or "")

    def assign_with_package(self):
        package_parts = self.container.config.output.package.split(".")
        module = package_parts.pop()
        package = ".".join(package_parts)

        self.assign(self.container.iterate(), package, module)

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
