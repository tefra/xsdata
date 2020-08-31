Getting started
===============

Prerequisites
-------------

Make sure you have `python >= 3.6` and `pip` up and running.


.. command-output:: python --version

.. command-output:: pip --version


.. warning::

    In python 3.6 the typing module is flattening subclasses in unions, this
    may affect how values are converted.

    There is no official workaround because it's not very common, if you like monkey
    patching then take a look here :py:func:`typing._remove_dups_flatten`

    .. code-block::

        >>> from dataclasses import dataclass
        >>> from typing import Union, get_type_hints
        >>>
        >>> @dataclass
        ... class Example:
        ...     value: Union[int, bool, str, float]
        ...
        >>> get_type_hints(Example)
        {'value': typing.Union[int, str, float]}
        >>> issubclass(bool, int)
        True



----

Install xsData
--------------

Install xsData package using `pip`.

.. code-block:: bash

    pip install xsdata

Verify installation using the cli entry point.

.. command-output:: xsdata --help

----

.. admonition:: xsData relies on these awesome libraries
    :class: hint

    * `lxml <https://lxml.de/>`_ - XML parsing
    * `requests <https://requests.readthedocs.io/>`_ - Webservice Default Transport
    * `click <https://click.palletsprojects.com/>`_ - CLI entry point
    * `toposort <https://pypi.org/project/toposort/>`_ - Resolve class ordering
    * `jinja2 <https://jinja.palletsprojects.com/>`_ -  Code generation
    * `docformatter <https://pypi.org/project/docformatter/>`_ -  Code formatting
