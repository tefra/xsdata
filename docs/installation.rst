Getting started
===============

Install using pip
-----------------

The recommended method is to use a virtual environment

.. code-block:: bash

    $ pip install xsdata

Install using conda
-------------------

.. code-block:: bash

    $ conda install -c conda-forge xsdata

Verify installation
-------------------

Verify installation using the cli entry point.

.. command-output:: xsdata --help


Requirements
------------

.. admonition:: xsData relies on these awesome libraries and supports `python >= 3.6`
    :class: hint

    * `lxml <https://lxml.de/>`_ - XML parsing
    * `requests <https://requests.readthedocs.io/>`_ - Webservice Default Transport
    * `click <https://click.palletsprojects.com/>`_ - CLI entry point
    * `toposort <https://pypi.org/project/toposort/>`_ - Resolve class ordering
    * `jinja2 <https://jinja.palletsprojects.com/>`_ -  Code generation
    * `docformatter <https://pypi.org/project/docformatter/>`_ -  Code formatting

.. warning::

    In python 3.6 the typing module is flattening subclasses in unions, this
    may affect how values are converted.

    There is no official workaround because it's not very common, if you like monkey
    patching then take a look here :py:func:`typing._remove_dups_flatten`

    .. doctest::

        >>> from dataclasses import dataclass
        >>> from typing import Union, get_type_hints
        ...
        >>> @dataclass
        ... class Example:
        ...     value: Union[int, bool, str, float]
        ...
        >>> get_type_hints(Example)  # doctest: +SKIP
        {'value': typing.Union[int, str, float]}
        >>> issubclass(bool, int)  # doctest: +SKIP
        True
