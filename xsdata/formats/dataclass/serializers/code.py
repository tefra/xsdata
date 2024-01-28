from dataclasses import dataclass, field
from enum import Enum
from io import StringIO
from typing import Any, Iterator, List, Mapping, Set, TextIO, Tuple, Type, Union

from xsdata.formats.bindings import AbstractSerializer
from xsdata.formats.dataclass.context import XmlContext
from xsdata.utils import collections
from xsdata.utils.objects import literal_value

spaces = "    "


unset = object()


@dataclass
class PycodeSerializer(AbstractSerializer):
    """Pycode serializer for data class instances.

    Generate python pretty representation code from a model instance.

    Args:
        context: The models context instance
    """

    context: XmlContext = field(default_factory=XmlContext)

    def render(self, obj: object, var_name: str = "obj") -> str:
        """Serialize the input model instance to python representation string.

        Args:
            obj: The input model instance to serialize
            var_name: The var name to assign the model instance

        Returns:
            The serialized representation string.
        """
        output = StringIO()
        self.write(output, obj, var_name)
        return output.getvalue()

    def write(self, out: TextIO, obj: Any, var_name: str):
        """Write the given object to the output text stream.

        Args:
            out: The output text stream
            obj: The input model instance to serialize
            var_name: The var name to assign the model instance
        """
        types: Set[Type] = set()

        tmp = StringIO()
        for chunk in self.repr_object(obj, 0, types):
            tmp.write(chunk)

        imports = self.build_imports(types)
        out.write(imports)
        out.write("\n\n")
        out.write(f"{var_name} = ")
        out.write(tmp.getvalue())
        out.write("\n")

    @classmethod
    def build_imports(cls, types: Set[Type]) -> str:
        """Build a list of imports from the given types.

        Args:
            types: A set of types

        Returns:
            The `from x import y` statements as string.
        """
        imports = set()
        for tp in types:
            module = tp.__module__
            name = tp.__qualname__
            if module != "builtins":
                if "." in name:
                    name = name.split(".")[0]

                imports.add(f"from {module} import {name}\n")

        return "".join(sorted(set(imports)))

    def repr_object(self, obj: Any, level: int, types: Set[Type]) -> Iterator[str]:
        """Write the given object as repr code.

        Args:
            obj: The input object to serialize
            level: The current object level
            types: The parent object types

        Yields:
            An iterator of the representation strings.
        """
        types.add(type(obj))
        if collections.is_array(obj):
            yield from self.repr_array(obj, level, types)
        elif isinstance(obj, dict):
            yield from self.repr_mapping(obj, level, types)
        elif self.context.class_type.is_model(obj):
            yield from self.repr_model(obj, level, types)
        elif isinstance(obj, Enum):
            yield str(obj)
        else:
            yield literal_value(obj)

    def repr_array(
        self,
        obj: Union[List, Set, Tuple],
        level: int,
        types: Set[Type],
    ) -> Iterator[str]:
        """Convert an iterable object to repr code.

        Args:
            obj: A list, set, tuple instance
            level: The current object level
            types: The parent object types

        Yields:
            An iterator of the representation strings.
        """
        if not obj:
            yield str(obj)
            return

        next_level = level + 1
        yield "[\n"
        for val in obj:
            yield spaces * next_level
            yield from self.repr_object(val, next_level, types)
            yield ",\n"

        yield f"{spaces * level}]"

    def repr_mapping(self, obj: Mapping, level: int, types: Set[Type]) -> Iterator[str]:
        """Convert a map object to repr code.

        Args:
            obj: A map instance
            level: The current object level
            types: The parent object types

        Yields:
            An iterator of the representation strings.
        """
        if not obj:
            yield str(obj)
            return

        next_level = level + 1
        yield "{\n"
        for key, value in obj.items():
            yield spaces * next_level
            yield from self.repr_object(key, next_level, types)
            yield ": "
            yield from self.repr_object(value, next_level, types)
            yield ",\n"

        yield f"{spaces * level}}}"

    def repr_model(self, obj: Any, level: int, types: Set[Type]) -> Iterator[str]:
        """Convert a data model instance to repr code.

        Args:
            obj: A map instance
            level: The current object level
            types: The parent object types

        Yields:
            An iterator of the representation strings.
        """
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

            yield from self.repr_object(value, next_level, types)

            index += 1

        yield f"\n{spaces * level})"
