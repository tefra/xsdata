import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def load_entry_points(name: str):
    entry_points = importlib_metadata.entry_points()

    if hasattr(entry_points, "select"):
        plugins = entry_points.select(group=name)  # type: ignore
    else:
        plugins = entry_points.get(name, [])  # type: ignore

    for plugin in plugins:
        plugin.load()
