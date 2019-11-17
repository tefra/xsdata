from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterator, List, Set, Tuple

from xsdata.models.elements import Schema
from xsdata.models.enums import XSDType
from xsdata.models.render import Class


class Renderer(ABC):
    @abstractmethod
    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str]]:
        pass

    @classmethod
    def collect_deps(cls, obj: Class) -> Set[str]:
        dependencies = {
            attr.type for attr in obj.attrs if not attr.forward_ref
        }
        if len(obj.extensions) > 0:
            dependencies.update(obj.extensions)
        for inner in obj.inner:
            dependencies.update(cls.collect_deps(inner))

        return set(filter(cls.filter_xsd_types, dependencies))

    @classmethod
    def filter_xsd_types(cls, code: str):
        return XSDType.get_enum(code) is None
