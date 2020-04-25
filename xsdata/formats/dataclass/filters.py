from typing import Any
from typing import Dict
from typing import Optional

from docformatter import format_code

from xsdata.models.codegen import Attr
from xsdata.models.codegen import Class


def attr_metadata(attr: Attr, parent_namespace: Optional[str]) -> Dict:
    metadata = dict(
        name=attr.local_name,
        type=attr.xml_type,
        namespace=attr.namespace
        if parent_namespace != attr.namespace or attr.is_attribute
        else None,
    )
    metadata.update(attr.restrictions.asdict())

    return {
        key: value
        for key, value in metadata.items()
        if value is not None and value is not False
    }


def arguments(data: Dict) -> str:
    def prep(key: str, value: Any) -> str:
        if isinstance(value, str) and not has_quotes(value):
            value = '"{}"'.format(value.replace('"', "'"))
            if key == "pattern":
                value = f"r{value}"
        return f"{key}={value}"

    return ",\n".join([prep(key, value) for key, value in data.items()])


def docstring(obj: Class, enum: bool = False) -> str:
    lines = []
    if obj.help:
        lines.append(obj.help)

    var_type = "cvar" if enum else "ivar"
    for attr in obj.attrs:
        description = attr.help.strip() if attr.help else ""
        lines.append(f":{var_type} {attr.name}: {description}".strip())

    return format_code('"""\n{}\n"""'.format("\n".join(lines))) if lines else ""


def lib_imports(output: str) -> str:
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


def has_quotes(string: str) -> bool:
    quote_types = ["'''", '"""', "'", '"']
    for quote in quote_types:
        if string.startswith(quote) and string.endswith(quote):
            return True
    return False


filters = {
    "arguments": arguments,
    "docstring": docstring,
    "lib_imports": lib_imports,
    "attr_metadata": attr_metadata,
}
