from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from io import StringIO
from typing import Any
from typing import List
from typing import Mapping
from typing import Set
from typing import TextIO
from typing import Type

from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.utils import collections
from xsdata.utils.objects import literal_value

spaces = "    "


unset = object()


@dataclass
class PycodeSerializer(AbstractSerializer):
    """
    Pycode serializer for dataclasses.

    Return a python representation code of a model instance.

    :param config: Serializer configuration
    :param context: Model context provider
    """

    config: SerializerConfig = field(default_factory=SerializerConfig)
    context: XmlContext = field(default_factory=XmlContext)

    def render(self, obj: object, var_name: str = "obj") -> str:
        """
        Convert and return the given object tree as python representation code.

        :param obj: The input dataclass instance
        :param var_name: The var name to assign the model instance
        """
        output = StringIO()
        self.write(output, obj, var_name)
        return output.getvalue()

    def write(self, out: TextIO, obj: Any, var_name: str):
        """
        Write the given object tree to the output text stream.

        :param out: The output stream
        :param obj: The input dataclass instance
        :param var_name: The var name to assign the model instance
        """
        types: Set[Type] = set()

        tmp = StringIO()
        for chunk in self.write_object(obj, 0, types):
            tmp.write(chunk)

        imports = self.build_imports(types)
        out.write(imports)
        out.write("\n\n")
        out.write(f"{var_name} = ")
        out.write(tmp.getvalue())
        out.write("\n")

    @classmethod
    def build_imports(cls, types: Set[Type]) -> str:
        imports = []
        for tp in types:
            module = tp.__module__
            name = tp.__qualname__
            if module != "builtins" and "." not in name:
                imports.append(f"from {module} import {name}\n")

        return "".join(sorted(imports))

    def write_object(self, obj: Any, level: int, types: Set[Type]):
        types.add(type(obj))
        if collections.is_array(obj):
            yield from self.write_array(obj, level, types)
        elif isinstance(obj, dict):
            yield from self.write_mapping(obj, level, types)
        elif self.context.class_type.is_model(obj):
            yield from self.write_class(obj, level, types)
        elif isinstance(obj, Enum):
            yield str(obj)
        else:
            yield literal_value(obj)

    def write_array(self, obj: List, level: int, types: Set[Type]):
        if not obj:
            yield str(obj)
            return

        next_level = level + 1
        yield "[\n"
        for val in obj:
            yield spaces * next_level
            yield from self.write_object(val, next_level, types)
            yield ",\n"

        yield f"{spaces * level}]"

    def write_mapping(self, obj: Mapping, level: int, types: Set[Type]):
        if not obj:
            yield str(obj)
            return

        next_level = level + 1
        yield "{\n"
        for key, value in obj.items():
            yield spaces * next_level
            yield from self.write_object(key, next_level, types)
            yield ": "
            yield from self.write_object(value, next_level, types)
            yield ",\n"

        yield f"{spaces * level}}}"

    def write_class(self, obj: Any, level: int, types: Set[Type]):
        yield f"{obj.__class__.__qualname__}(\n"

        next_level = level + 1
        index = 0
        for f in self.context.class_type.get_fields(obj):
            if not f.init:
                continue

            value = getattr(obj, f.name, types)
            default = self.context.class_type.default_value(f, default=unset)
            if default is not unset and (
                (callable(default) and default() == value) or default == value
            ):
                continue

            if index:
                yield f",\n{spaces * next_level}{f.name}="
            else:
                yield f"{spaces * next_level}{f.name}="

            yield from self.write_object(value, next_level, types)

            index += 1

        yield f"\n{spaces * level})"
