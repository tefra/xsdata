.. image:: https://github.com/tefra/xsdata/raw/master/docs/_static/logo.svg
    :target: https://xsdata.readthedocs.io/

Naive XML Bindings for python
=============================

.. image:: https://github.com/tefra/xsdata/workflows/tests/badge.svg
    :target: https://github.com/tefra/xsdata/actions

.. image:: https://readthedocs.org/projects/xsdata/badge
    :target: https://xsdata.readthedocs.io/

.. image:: https://codecov.io/gh/tefra/xsdata/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/tefra/xsdata

.. image:: https://img.shields.io/github/languages/top/tefra/xsdata.svg
    :target: https://xsdata.readthedocs.io/

.. image:: https://www.codefactor.io/repository/github/tefra/xsdata/badge
   :target: https://www.codefactor.io/repository/github/tefra/xsdata

.. image:: https://img.shields.io/pypi/pyversions/xsdata.svg
    :target: https://pypi.org/pypi/xsdata/

.. image:: https://img.shields.io/pypi/v/xsdata.svg
    :target: https://pypi.org/pypi/xsdata/

--------

xsData is a complete data binding library for python allowing developers to access and
use XML and JSON documents as simple objects rather than using DOM.

It ships with a code generator for XML schemas, WSDL definitions, XML & JSON documents.
It produces simple dataclasses with type hints and simple binding metadata.

The included XML and JSON parser/serializer are highly optimized and adaptable, with
multiple handlers and configuration properties.

xsData is constantly tested against the
`W3C XML Schema 1.1 test suite <https://github.com/tefra/xsdata-w3c-tests>`_.

Getting started
---------------

.. code:: console

    $ # Install all dependencies
    $ pip install xsdata[cli,lxml,soap]

.. code:: console

    $ # Generate models
    $ xsdata tests/fixtures/primer/order.xsd --package tests.fixtures.primer

.. code:: python

    >>> # Parse XML
    >>> from pathlib import Path
    >>> from tests.fixtures.primer import PurchaseOrder
    >>> from xsdata.formats.dataclass.parsers import XmlParser
    >>>
    >>> xml_string = Path("tests/fixtures/primer/sample.xml").read_text()
    >>> parser = XmlParser()
    >>> order = parser.from_string(xml_string, PurchaseOrder)
    >>> order.bill_to
    Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=Decimal('95819'), country='US')


Check the `documentation <https://xsdata.readthedocs.io>`_ for more
✨✨✨

Features
--------

- Generate code from:

  - XML Schemas 1.0 & 1.1
  - WSDL 1.1 definitions with SOAP 1.1 bindings
  - Directly from XML and JSON Documents
  - Extensive configuration to customize output
  - Pluggable code writer for custom output formats

- Default Output:

  - Pure python dataclasses with metadata
  - Type hints with support for forward references and unions
  - Enumerations and inner classes
  - Support namespace qualified elements and attributes

- Data Binding:

  - XML and JSON parser, serializer
  - Handlers and Writers based on lxml and native xml python
  - Support wildcard elements and attributes
  - Support xinclude statements and unknown properties
  - Customize behaviour through config


Changelog: 21.7 (2021-07-01)
----------------------------

- Fixed docstrings backslash escaping `#518 <https://github.com/tefra/xsdata/pull/518>`_
- Fixed analyzer flattening bare types `#541 <https://github.com/tefra/xsdata/pull/541>`_
- Fixed multiple issues with compound fields and override fields `#533 <https://github.com/tefra/xsdata/pull/533>`_
- Fixed missing derived elements types during xml parsing `#541 <https://github.com/tefra/xsdata/pull/541>`_
- Added structure style: clusters for smaller packages `#509 <https://github.com/tefra/xsdata/pull/509>`_
- Added configuration to generate relative imports `#519 <https://github.com/tefra/xsdata/pull/519>`_
- Added configuration to toggle all dataclasses features `#529 <https://github.com/tefra/xsdata/pull/529>`_
- Added binding support for tuple typing annotations (frozen dataclasses) `#529 <https://github.com/tefra/xsdata/pull/529>`_
- Added support to bind data directly from xml/lxml Element and ElementTree `#531 <https://github.com/tefra/xsdata/pull/531>`_ `#546 <https://github.com/tefra/xsdata/pull/546>`_
- Updated analyzer to avoid same name for outer-inner classes `#511 <https://github.com/tefra/xsdata/pull/511>`_
- Updated cli to fail early if config file is invalid `#514 <https://github.com/tefra/xsdata/pull/514>`_
- Updated cli to remove setuptools from runtime dependencies `#515 <https://github.com/tefra/xsdata/pull/515>`_
- Updated analyzer to relax override field validations completely `#516 <https://github.com/tefra/xsdata/pull/516>`_
- Updated analyzer to sort classes before class name conflict resolution `#517 <https://github.com/tefra/xsdata/pull/517>`_
- Updated JSON parser to attempt binding against subclasses `#527 <https://github.com/tefra/xsdata/pull/527>`_
- Updated analyzer to guard against multiple substitution group runs `#538 <https://github.com/tefra/xsdata/pull/538>`_
- Updated code generation to use case sensitive reserved words `#545 <https://github.com/tefra/xsdata/pull/545>`_
