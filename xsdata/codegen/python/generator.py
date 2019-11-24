from abc import ABC
from typing import Any, List, Optional

from xsdata.codegen.generator import AbstractGenerator
from xsdata.codegen.python.dataclass.utils import replace_words
from xsdata.models.codegen import Attr, Class, Package
from xsdata.models.enums import XSDType
from xsdata.utils import text


class PythonAbstractGenerator(AbstractGenerator, ABC):
    @classmethod
    def process_class(cls, obj: Class, parents: List[str] = None) -> Class:
        """Normalize all class instance fields, extensions, name and the inner
        classes recursively."""
        parents = parents or []
        obj.name = cls.class_name(obj.name)
        obj.extensions = [cls.type_name(ext) for ext in obj.extensions]

        curr_parents = parents + [obj.name]
        for inner in obj.inner:
            cls.process_class(inner, curr_parents)

        is_enum = obj.is_enumeration
        for attr in obj.attrs:
            if is_enum:
                cls.process_enumeration(attr)
            else:
                cls.process_attribute(attr, curr_parents)

        return obj

    @classmethod
    def process_attribute(cls, attr: Attr, parents) -> None:
        """Normalize attribute properties."""
        attr.name = cls.attribute_name(attr.name)
        attr.type = cls.attribute_type(attr, parents)
        attr.local_name = text.strip_prefix(attr.local_name)
        attr.default = cls.attribute_default(attr)

    @classmethod
    def process_enumeration(cls, attr: Attr, *args) -> None:
        """Normalize attribute properties."""
        attr.name = cls.enumeration_name(attr.name)
        attr.default = cls.attribute_default(attr)

    @classmethod
    def process_import(cls, package: Package) -> Package:
        """Normalize import package properties."""
        package.name = cls.class_name(package.name)
        if package.alias:
            package.alias = cls.class_name(package.alias)

        return package

    @classmethod
    def class_name(cls, name: str) -> str:
        """Convert class names to pascal case."""
        return text.pascal_case(name)

    @classmethod
    def type_name(cls, name: str) -> str:
        """Convert xsd types to python or apply class name conventions after
        stripping any reference prefix."""
        return XSDType.get_local(name) or cls.class_name(
            text.strip_prefix(name)
        )

    @classmethod
    def attribute_name(cls, name: str) -> str:
        """
        Strip reference prefix and turn to snake case.

        If the name is one of the python reserved words append the
        prefix _value
        """
        name = text.strip_prefix(name)
        return text.snake_case(replace_words.get(name.lower(), name))

    @classmethod
    def enumeration_name(cls, name: str) -> str:
        """
        Strip reference prefix and turn to snake case.

        If the name is one of the python reserved words append the
        prefix _value
        """
        return cls.attribute_name(name).upper()

    @classmethod
    def attribute_type(cls, attr: Attr, parents: List[str]) -> str:
        """
        Normalize attribute type.

        Steps:
            * If type alias is present use class name normalization
            * Otherwise use the type name normalization
            * Prepend outer class names and quote result for forward references
            * Wrap the result with List if the field accepts a list of values
            * Wrap the result with Optional if the field default value is None
        """
        result = (
            cls.class_name(attr.type_alias)
            if attr.type_alias
            else cls.type_name(attr.type)
        )

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
        """Normalize default value/factory by the attribute type."""
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
