from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Iterator, List, Optional, Tuple

from jinja2 import Environment, FileSystemLoader, Template

from xsdata.formats.dataclass.utils import safe_snake
from xsdata.models.codegen import Attr, Class, Package
from xsdata.models.elements import Schema
from xsdata.models.enums import XSDType
from xsdata.resolver import DependenciesResolver
from xsdata.utils import text


class AbstractGenerator(ABC):
    templates_dir: Optional[Path] = None

    def __init__(self):
        if self.templates_dir is None:
            raise TypeError("Missing renderer templates directory")

        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir))
        )
        self.resolver = DependenciesResolver()

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.jinja2".format(name))

    @abstractmethod
    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str]]:
        pass


class PythonAbstractGenerator(AbstractGenerator, ABC):
    @classmethod
    def process_class(cls, obj: Class, parents: List[str] = None) -> Class:
        """Normalize all class instance fields, extends, name and the inner
        classes recursively."""
        parents = parents or []
        obj.name = cls.class_name(obj.name)

        for extension in obj.extensions:
            extension.name = cls.type_name(extension.name)

        curr_parents = parents + [obj.name]
        for inner in obj.inner:
            cls.process_class(inner, curr_parents)

        is_enum = obj.is_enumeration
        for attr in obj.attrs:
            if is_enum:
                cls.process_enumeration(attr, obj)
            else:
                cls.process_attribute(attr, curr_parents)

        return obj

    @classmethod
    def process_attribute(cls, attr: Attr, parents: List[str]) -> None:
        """Normalize attribute properties."""
        attr.name = cls.attribute_name(attr.name)
        attr.type = cls.attribute_type(attr, parents)
        attr.local_name = text.split(attr.local_name)[1]
        attr.default = cls.attribute_default(attr)

    @classmethod
    def process_enumeration(cls, attr: Attr, parent: Class) -> None:
        """Normalize enumeration properties."""
        valid_types = ("str", "int", "float", "bool")

        attr.type = (
            parent.extensions[0].name
            if len(parent.extensions) == 1
            and parent.extensions[0].name in valid_types
            else "str"
        )
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
        return XSDType.get_local(name) or cls.class_name(text.split(name)[1])

    @classmethod
    def attribute_name(cls, name: str) -> str:
        """
        Strip reference prefix and turn to snake case.

        If the name is one of the python reserved words append the
        prefix _value
        """
        local_name = text.split(name)[1]
        return text.snake_case(safe_snake(local_name))

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

        type_names: List[str] = []
        for name in attr.types:
            type_name = (
                cls.class_name(attr.type_aliases[name])
                if name in attr.type_aliases
                else cls.type_name(name)
            )
            if type_name not in type_names:
                type_names.append(type_name)

        result = ", ".join(type_names)
        if attr.forward_ref:
            outer_str = ".".join(parents)
            result = f'"{outer_str}.{result}"'
        elif len(type_names) > 1:
            result = f"Union[{result}]"

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
