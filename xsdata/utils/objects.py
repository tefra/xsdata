import math
from typing import Any
from xml.etree.ElementTree import QName


def update(obj: Any, **kwargs: Any):
    """Update an object from keyword arguments with dotted keys."""

    def attrsetter(obj: Any, attr: str, value: Any):
        names = attr.split(".")
        last = names.pop()
        for name in names:
            obj = getattr(obj, name)

        setattr(obj, last, value)

    for key, value in kwargs.items():
        attrsetter(obj, key, value)


def literal_value(value: Any) -> str:
    """Return the value for code generation."""
    if isinstance(value, float):
        return str(value) if math.isfinite(value) else f'float("{value}")'

    if isinstance(value, QName):
        return f'QName("{value.text}")'

    return repr(value)
