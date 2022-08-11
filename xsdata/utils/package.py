import functools
import os
from pathlib import Path


@functools.lru_cache(maxsize=50)
def package_path(package: str) -> Path:
    """Join the current working path with the package name."""
    return Path.cwd().joinpath(package.replace(".", "/")).parent


@functools.lru_cache(maxsize=50)
def module_path(module: str) -> Path:
    """Join the current working path with the given module name."""
    return Path.cwd().joinpath(module.replace(".", "/"))


@functools.lru_cache(maxsize=50)
def module_name(source: str) -> str:
    module = source.split("/")[-1]
    name, extension = os.path.splitext(module)
    return name if extension in (".xsd", ".dtd", ".wsdl", ".xml", ".json") else module
