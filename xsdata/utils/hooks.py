import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def load_entry_points(name: str):
    eps = importlib_metadata.entry_points()
    if name in eps:
        for ep in eps[name]:
            ep.load()
