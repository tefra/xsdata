import functools
from pathlib import Path


@functools.lru_cache(maxsize=50)
def package_path(package: str) -> Path:
    return Path.cwd().joinpath(package.replace(".", "/")).parent


@functools.lru_cache(maxsize=50)
def module_path(package: str) -> Path:
    return Path.cwd().joinpath(package.replace(".", "/"))
