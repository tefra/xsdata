from abc import ABC
from abc import abstractmethod
from pathlib import Path
from typing import Any
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template

from xsdata.formats.dataclass.utils import safe_snake
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Package
from xsdata.models.elements import Schema
from xsdata.resolver import DependenciesResolver
from xsdata.utils import text


class AbstractGenerator(ABC):
    templates_dir: Optional[Path] = None

    def __init__(self):
        if self.templates_dir is None:
            raise TypeError("Missing renderer templates directory")

        self.env = Environment(loader=FileSystemLoader(str(self.templates_dir)))
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

        curr_parents = parents + [obj.name]
        for inner in obj.inner:
            cls.process_class(inner, curr_parents)

        is_enum = obj.is_enumeration
        for attr in obj.attrs:
            if is_enum:
                cls.process_enumeration(attr, obj)
            else:
                cls.process_attribute(attr, curr_parents)

        for extension in obj.extensions:
            cls.process_extension(extension)

        return obj

    @classmethod
    def process_extension(cls, extension: AttrType):
        extension.name = cls.type_name(extension)

    @classmethod
    def process_attribute(cls, attr: Attr, parents: List[str]) -> None:
        """Normalize attribute properties."""
        attr.name = cls.attribute_name(attr.name)
        attr.display_type = cls.attribute_display_type(attr, parents)
        attr.local_name = text.split(attr.local_name)[1]
        attr.default = cls.attribute_default(attr)

    @classmethod
    def process_enumeration(cls, attr: Attr, parent: Class) -> None:
        """Normalize enumeration properties."""

        if len(parent.extensions) == 1 and parent.extensions[0].native:
            attr.types.append(parent.extensions[0])

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
    def type_name(cls, attr_type: AttrType) -> str:
        """Convert xsd types to python or apply class name conventions after
        stripping any reference prefix."""

        return attr_type.native_name or cls.class_name(text.suffix(attr_type.name))

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
    def attribute_display_type(cls, attr: Attr, parents: List[str]) -> str:
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
        for attr_type in attr.types:
            type_name = (
                cls.class_name(attr_type.alias)
                if attr_type.alias
                else cls.type_name(attr_type)
            )
            if attr_type.forward_ref:
                outer_str = ".".join(parents)
                type_name = f'"{outer_str}.{type_name}"'

            if type_name not in type_names:
                type_names.append(type_name)

        result = ", ".join(type_names)
        if len(type_names) > 1:
            result = f"Union[{result}]"

        if attr.is_list:
            result = f"List[{result}]"
        elif attr.is_map:
            result = f"Dict[{result}]"
        elif attr.default is None and "Dict" not in result:
            result = f"Optional[{result}]"

        return result

    @classmethod
    def attribute_default(cls, attr: Attr) -> Optional[Any]:
        """Normalize default value/factory by the attribute type."""
        if attr.is_list:
            return "list"
        if attr.is_map:
            return "dict"
        elif isinstance(attr.default, str):
            local_types = {
                attr_type.native_type for attr_type in attr.types if attr_type.native
            }

            if bool in local_types:
                if attr.default == "true":
                    return True
                if attr.default == "false" or len(local_types) == 1:
                    return False

            if int in local_types:
                try:
                    return int(attr.default)
                except ValueError:
                    pass

            if float in local_types:
                try:
                    return float(attr.default)
                except ValueError:
                    pass

            return f'"{attr.default}"'
        else:
            return attr.default
