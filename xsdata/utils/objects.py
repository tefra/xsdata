from typing import Any


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
