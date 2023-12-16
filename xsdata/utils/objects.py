import math
import re
from typing import Any
from xml.etree.ElementTree import QName
from xml.sax.saxutils import quoteattr


def update(obj: Any, **kwargs: Any):
    """Update an object from keyword arguments with dotted keys."""
    for key, value in kwargs.items():
        attrsetter(obj, key, value)


def attrsetter(obj: Any, attr: str, value: Any):
    names = attr.split(".")
    last = names.pop()
    for name in names:
        obj = getattr(obj, name)

    setattr(obj, last, value)


def literal_value(value: Any) -> str:
    if isinstance(value, str):
        return quoteattr(value.encode("unicode_escape").decode("ASCII"))

    if isinstance(value, float):
        return str(value) if math.isfinite(value) else f'float("{value}")'

    if isinstance(value, QName):
        return f'QName("{value.text}")'

    if isinstance(value, bytes):
        # Use the contents of the bytes verbatim, but ensure that it is
        # wrapped in double quotes
        return re.sub(r"b'(.*)'$", r'b"\g<1>"', repr(value))

    return repr(value).replace("'", '"')
