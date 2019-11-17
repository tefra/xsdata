from abc import ABC
from typing import Any, Dict, List, Optional

from toposort import toposort_flatten

from xsdata.models.enums import XSDType
from xsdata.models.render import Attr, Class
from xsdata.render.python.dataclass.utils import replace_words
from xsdata.render.renderer import Renderer
from xsdata.utils import text


class PythonRenderer(Renderer, ABC):
    @classmethod
    def process_class(
        cls, obj: Class, overrides: Dict[str, str], parents: List[str]
    ):
        obj.name = cls.class_name(obj.name)
        obj.extensions = [cls.type_name(ext) for ext in obj.extensions]

        for inner in obj.inner:
            cls.process_class(inner, overrides, parents + [obj.name])

        for attr in obj.attrs:
            attr.name = cls.attribute_name(attr.name)
            attr.type = cls.attribute_type(
                attr, overrides, parents + [obj.name]
            )
            attr.local_name = text.strip_prefix(attr.local_name)
            attr.default = cls.attribute_default(attr)

    @classmethod
    def class_name(cls, name: str) -> str:
        return text.pascal_case(name)

    @classmethod
    def type_name(cls, name: str) -> str:
        return XSDType.get_local(name) or cls.class_name(
            text.strip_prefix(name)
        )

    @classmethod
    def attribute_name(cls, name: str) -> str:
        name = text.strip_prefix(name)
        return text.snake_case(replace_words.get(name.lower(), name))

    @classmethod
    def attribute_type(cls, attr: Attr, overrides, parents: List[str]) -> str:
        result = overrides.get(attr.type) or cls.type_name(attr.type)
        if attr.forward_ref:
            outer_str = ".".join(parents)
            result = f'"{outer_str}.{result}"'
        if attr.is_list:
            result = f"List[{result}]"
        elif attr.default is None:
            result = f"Optional[{result}]"

        return result

    @classmethod
    def attribute_default(cls, attr: Attr) -> Optional[Any]:
        if attr.is_list:
            return "list"
        elif isinstance(attr.default, str):
            if attr.type == "bool":
                return attr.default == "true"
            if attr.type == "int":
                return int(attr.default)
            if attr.type == "float":
                return float(attr.default)
            return f'"{attr.default}"'
        else:
            return attr.default

    @classmethod
    def sort_classes(cls, classes: List[Class]) -> List[Class]:
        index = {obj.name: obj for obj in classes}
        deps = {obj.name: cls.collect_deps(obj) for obj in classes}

        return [index[name] for name in toposort_flatten(deps) if name in deps]

    @classmethod
    def list_dependencies(cls, classes: List[Class]) -> List[str]:
        return toposort_flatten(
            {obj.name: cls.collect_deps(obj) for obj in classes}
        )
