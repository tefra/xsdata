import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

meta = dict()  # type: dict
with open(os.path.join(here, "xsdata", "version.py"), encoding="utf-8") as f:
    exec(f.read(), meta)

if __name__ == "__main__":
    setup(
        packages=find_packages(),
        version=meta["version"],
        install_requires=["lxml", "click", "click_completion", "toposort"],
        extras_require={
            "dev": ["pre-commit", "pytest", "pytest-cov", "codecov", "tox"]
        },
        entry_points={"console_scripts": ["xsdata=xsdata:cli"]},
    )
