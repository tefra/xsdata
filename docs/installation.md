# Installation

## Using pip

```console
pip install xsdata[cli,lxml,soap]
```

!!! hint

    - Install the cli requirements for the code generator
    - Install the soap requirements for the builtin wsdl client
    - Install lxml for enhanced performance and advanced features

## From repository

```console
pip install xsdata[cli,lxml] @ git+https://github.com/tefra/xsdata
```

## Using conda

```console
conda install -c conda-forge xsdata
```

## Verify installation

Verify installation using the cli entry point.

```console exec="1" source="console"
$ xsdata --help
```

## Requirements

!!! Note "xsData relies on these awesome libraries and supports `python >= 3.9`"

    - [lxml](https://lxml.de/) - XML advanced features
    - [requests](https://requests.readthedocs.io/) - Webservice Default Transport
    - [click](https://click.palletsprojects.com/) - CLI entry point
    - [toposort](https://pypi.org/project/toposort/) - Resolve class ordering
    - [jinja2](https://jinja.palletsprojects.com/) - Code generation
    - [ruff](https://pypi.org/project/ruff/) - Code formatting
    - [docformatter](https://pypi.org/project/docformatter/) - Docstring formatting
