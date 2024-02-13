from importlib import metadata


def load_entry_points(name: str):
    """Load the plugins for the given hook name."""
    entry_points = metadata.entry_points()

    if hasattr(entry_points, "select"):
        plugins = entry_points.select(group=name)  # type: ignore
    else:
        plugins = entry_points.get(name, [])  # type: ignore

    for plugin in plugins:
        plugin.load()
