from docformatter import format_code

from xsdata.models.render import Class


def arguments(data: dict):
    def quote(value):
        if isinstance(value, str) and not has_quotes(value):
            return '"{}"'.format(value.replace('"', "'"))
        return value

    return ",\n".join([f"{key}={quote(value)}" for key, value in data.items()])


def update(data: dict, more: dict):
    return dict(data, **more)


def docstring(obj: Class):
    lines = []
    if obj.help:
        lines.append(obj.help)

    for attr in obj.attrs:
        description = attr.help.strip() if attr.help else ""
        lines.append(f":ivar {attr.name}: {description}".strip())

    return (
        format_code('"""\n{}\n"""'.format("\n".join(lines))) if lines else ""
    )


def has_quotes(string: str):
    quote_types = ["'''", '"""', "'", '"']
    for quote in quote_types:
        if string.startswith(quote) and string.endswith(quote):
            return True
    return False
