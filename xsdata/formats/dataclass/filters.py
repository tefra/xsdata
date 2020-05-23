import functools
import math
import re
from decimal import Decimal
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from xml.sax.saxutils import quoteattr

from docformatter import format_code
from lxml.etree import QName

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.formats.converters import to_python
from xsdata.formats.dataclass import utils
from xsdata.models.enums import DataType
from xsdata.utils import text


@functools.lru_cache(maxsize=50)
def class_name(name: str) -> str:
    """Apply python conventions for class names."""
    return text.pascal_case(utils.safe_snake(name, "type"))


@functools.lru_cache(maxsize=50)
def attribute_name(name: str) -> str:
    """Apply python conventions for instance variable names."""
    return text.snake_case(utils.safe_snake(text.suffix(name)))


@functools.lru_cache(maxsize=50)
def constant_name(name: str) -> str:
    """Apply python conventions for constant names."""
    return text.snake_case(utils.safe_snake(name)).upper()


def type_name(attr_type: AttrType) -> str:
    """Return native python type name or apply class name conventions."""
    return attr_type.native_name or class_name(text.suffix(attr_type.name))


def attribute_metadata(attr: Attr, parent_namespace: Optional[str]) -> Dict:
    """Return a metadata dictionary for the given attribute."""
    metadata = dict(
        name=None
        if attr.is_nameless or attr.local_name == attribute_name(attr.name)
        else attr.local_name,
        type=attr.xml_type,
        namespace=attr.namespace
        if parent_namespace != attr.namespace or attr.is_attribute
        else None,
        **attr.restrictions.asdict(),
    )

    return {
        key: value
        for key, value in metadata.items()
        if value is not None and value is not False
    }


def format_arguments(data: Dict) -> str:
    """Format given dictionary as keyword arguments."""

    def prep(key: str, value: Any) -> str:
        if isinstance(value, str):
            value = f'''"{value.replace('"', "'")}"'''
            if key == "pattern":
                value = f"r{value}"
        return f"{key}={value}"

    return ",\n".join([prep(key, value) for key, value in data.items()])


def class_docstring(obj: Class, enum: bool = False) -> str:
    """Generate docstring for the given class and the constructor arguments."""
    lines = []
    if obj.help:
        lines.append(obj.help)

    var_type = "cvar" if enum else "ivar"
    name_func = constant_name if enum else attribute_name

    for attr in obj.attrs:
        description = attr.help.strip() if attr.help else ""
        lines.append(f":{var_type} {name_func(attr.name)}: {description}".strip())

    return format_code('"""\n{}\n"""'.format("\n".join(lines))) if lines else ""


def default_imports(output: str) -> str:
    """Generate the default imports for the given package output."""
    result = []

    if "Decimal" in output:
        result.append("from decimal import Decimal")

    if "(Enum)" in output:
        result.append("from enum import Enum")

    dataclasses = []
    if "@dataclass" in output:
        dataclasses.append("dataclass")
    if "field(" in output:
        dataclasses.append("field")

    if dataclasses:
        result.append(f"from dataclasses import {', '.join(dataclasses)}")

    if "QName" in output:
        result.append("from lxml.etree import QName")

    types = [tp for tp in ["Dict", "List", "Optional", "Union"] if f"{tp}[" in output]
    if types:
        result.append(f"from typing import {', '.join(types)}")

    return "\n".join(result)


def attribute_default(attr: Attr, ns_map: Optional[Dict] = None) -> Any:
    """Generate the field default value/factory for the given attribute."""
    if attr.is_list:
        return "list"
    if attr.is_map:
        return "dict"
    if not isinstance(attr.default, str):
        return attr.default

    data_types = {
        attr_type.native_code: attr_type.native_type
        for attr_type in attr.types
        if attr_type.native
    }

    local_types = list(set(data_types.values()))
    default_value = to_python(local_types, attr.default, ns_map, in_order=False)

    if isinstance(default_value, str):
        if DataType.NMTOKENS.code in data_types:
            default_value = quoteattr(
                " ".join(filter(None, map(str.strip, re.split(r"\s+", default_value))))
            )
        elif default_value.startswith("@enum@"):
            source, enumeration = default_value[6:].split("::", 1)
            attr_type = next(
                attr_type
                for attr_type in attr.types
                if text.suffix(attr_type.name) == source
            )
            if attr_type.alias:
                source = attr_type.alias

            default_value = f"{class_name(source)}.{constant_name(enumeration)}"
        else:
            default_value = quoteattr(default_value)
    elif isinstance(default_value, float) and math.isinf(default_value):
        default_value = f"float('{default_value}')"
    elif isinstance(default_value, Decimal):
        default_value = repr(default_value)
    elif isinstance(default_value, QName):
        default_value = (
            f'QName("{default_value.namespace}", "{default_value.localname}")'
        )
    return default_value


def attribute_type(attr: Attr, parents: List[str]) -> str:
    """Generate type hints for the given attribute."""

    type_names: List[str] = []
    for attr_type in attr.types:
        name = class_name(attr_type.alias) if attr_type.alias else type_name(attr_type)

        if attr_type.forward and attr_type.circular:
            outer_str = ".".join(map(class_name, parents))
            name = f'"{outer_str}"'
        elif attr_type.forward:
            outer_str = ".".join(map(class_name, parents))
            name = f'"{outer_str}.{name}"'
        elif attr_type.circular:
            name = f'"{name}"'

        if name not in type_names:
            type_names.append(name)

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


filters = {
    "attribute_name": attribute_name,
    "attribute_default": attribute_default,
    "attribute_metadata": attribute_metadata,
    "attribute_type": attribute_type,
    "class_name": class_name,
    "class_docstring": class_docstring,
    "constant_name": constant_name,
    "default_imports": default_imports,
    "format_arguments": format_arguments,
    "type_name": type_name,
}
