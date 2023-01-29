import json
from pathlib import Path
from typing import Any


def dump(obj: Any):
    """
    Write any object into a dump json file.

    For internal troubleshooting purposes only!!!
    """
    with Path.cwd().joinpath("xsdata_dump.json").open("w+") as f:
        json.dump(convert(obj), f, indent=4)


def convert(obj: Any) -> Any:
    """Dump any obj into a readable dictionary."""
    if not obj:
        return obj

    if isinstance(obj, list):
        return list(map(convert, obj))

    if isinstance(obj, dict):
        return {key: convert(value) for key, value in obj.items()}

    if hasattr(obj, "__slots__") and obj.__slots__:
        return {name: convert(getattr(obj, name)) for name in obj.__slots__}

    return str(obj)
