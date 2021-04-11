.. image:: https://github.com/tefra/xsdata/raw/master/docs/_static/logo.png
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

xsData is a complete XML and JSON data binding library for python allowing developers to
access and documents as simple objects rather than using DOM.

It ships with a code generator for XML schemas, WSDL definitions and XML documents. It
produces simple dataclasses with type hints and binding metadata.

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
    >>> xml_string = Path("tests/fixtures/primer/order.xml").read_text()
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
  - Directly from XML Documents
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


Changelog: 21.4 (2021-04-02)
----------------------------
- Split requirements to extras cli, soap and lxml `#419 <https://github.com/tefra/xsdata/issues/419>`_
- Fixed parser conflict when an attribute and element field have the same qualified name
- Added cli auto detection for source types, removed cli flag `--wsdl`
- Added cli support to generate code from raw xml documents
- Added cli entry point to allow pluggable output formats `#429 <https://github.com/tefra/xsdata/issues/429>`_
- Added cli short flags for all options and flags
- Added handler to set effective choice groups `#433 <https://github.com/tefra/xsdata/issues/433>`_
- Moved plantUML output format to a standalone `plugin <https://github.com/tefra/xsdata-plantuml>`_
- Updated xml parser to allow unions of primitive and class types
- Updated XmlDateTime parser to catch invalid cases with extra leading zeros
- Updated QName converter to validate uri/ncname when parsing string representations
- Updated JsonParser to allow parsing from filename string
- Updated cli option `--compound-fields` to a boolean flag
