from abc import ABC
from typing import Any, Dict, List, Optional

from xsdata.codegen.generator import AbstractGenerator
from xsdata.codegen.python.dataclass.utils import replace_words
from xsdata.models.codegen import Attr, Class, Package
from xsdata.models.enums import XSDType
from xsdata.utils import text


class PythonAbstractGenerator(AbstractGenerator, ABC):
    @classmethod
    def process_class(
        cls, obj: Class, overrides: Dict[str, str], parents: List[str] = None
    ):
        parents = parents or []
        obj.name = cls.class_name(obj.name)
        obj.extensions = [cls.type_name(ext) for ext in obj.extensions]

        if obj.inner and obj.extensions and obj.attrs:
            pass

        for inner in obj.inner:
            cls.process_class(inner, overrides, parents + [obj.name])

        for attr in obj.attrs:
            attr.name = cls.attribute_name(attr.name)
            attr.type = cls.attribute_type(
                attr, overrides, parents + [obj.name]
            )
            attr.local_name = text.strip_prefix(attr.local_name)
            attr.default = cls.attribute_default(attr)

        return obj

    @classmethod
    def process_import(cls, pck: Package):
        for obj in pck.objects:
            obj.name = cls.class_name(obj.name)
            if obj.alias:
                obj.alias = cls.class_name(obj.alias)

        return pck

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

        if attr.type in overrides:
            result = cls.class_name(attr.type)
        else:
            result = cls.type_name(attr.type)

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
