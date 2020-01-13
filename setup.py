from pathlib import Path

from setuptools import setup


def get_version(rel_path):
    for line in Path(rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            return line.split('"')[1]
    raise RuntimeError("Unable to find version string.")


setup(version=get_version("xsdata/__init__.py"))
