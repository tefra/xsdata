Installation
============

Install using pip
-----------------

The recommended method is to use a virtual environment.

.. code-block:: console

    $ pip install xsdata[cli,lxml,soap]

.. hint::

     - Install the cli requirements for the code generator
     - Install the soap requirements for the builtin wsdl client
     - Install lxml if you want to use one of the lxml handlers/writers instead of
       the builtin python xml implementations.

xsdata has a monthly release cycle, in order to use the latest updates you can also
install directly from the git repo.

.. code-block:: console

    $ pip install xsdata[cli,lxml] @ git+https://github.com/tefra/xsdata


Install using conda
-------------------

.. code-block:: console

    $ conda install -c conda-forge xsdata

Verify installation
-------------------

Verify installation using the cli entry point.

.. cli:: xsdata --help


Requirements
------------

.. admonition:: xsData relies on these awesome libraries and supports `python >= 3.7`
    :class: hint

    * `lxml <https://lxml.de/>`_ - XML parsing
    * `requests <https://requests.readthedocs.io/>`_ - Webservice Default Transport
    * `click <https://click.palletsprojects.com/>`_ - CLI entry point
    * `toposort <https://pypi.org/project/toposort/>`_ - Resolve class ordering
    * `jinja2 <https://jinja.palletsprojects.com/>`_ -  Code generation
    * `docformatter <https://pypi.org/project/docformatter/>`_ -  Code formatting
