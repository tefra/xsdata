Getting started
===============

Prerequisites
-------------

Make sure you have `python >= 3.7` and `pip` up and running.


.. command-output:: python --version

.. command-output:: pip --version


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
    * `click <https://click.palletsprojects.com/>`_ - CLI entry point
    * `toposort <https://pypi.org/project/toposort/>`_ - Resolve class ordering
    * `jinja2 <https://jinja.palletsprojects.com/>`_ -  Code generation
    * `docformatter <https://pypi.org/project/docformatter/>`_ -  Code formatting
