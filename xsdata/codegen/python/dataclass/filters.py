from docformatter import format_code

from xsdata.models.codegen import Class


def arguments(data: dict):
    def prep(key, value):
        if isinstance(value, str) and not has_quotes(value):
            value = '"{}"'.format(value.replace('"', "'"))
            if key == "pattern":
                value = f"r{value}"
        return f"{key}={value}"

    return ",\n".join(
        [prep(key, value) for key, value in data.items() if value is not None]
    )


def docstring(obj: Class, enum=False):
    lines = []
    if obj.help:
        lines.append(obj.help)

    var_type = "cvar" if enum else "ivar"
    for attr in obj.attrs:
        description = attr.help.strip() if attr.help else ""
        lines.append(f":{var_type} {attr.name}: {description}".strip())

    return (
        format_code('"""\n{}\n"""'.format("\n".join(lines))) if lines else ""
    )


def has_quotes(string: str):
    quote_types = ["'''", '"""', "'", '"']
    for quote in quote_types:
        if string.startswith(quote) and string.endswith(quote):
            return True
    return False


filters = {
    "arguments": arguments,
    "docstring": docstring,
}
