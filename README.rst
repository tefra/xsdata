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


Changelog: 21.6 (2021-06-01)
----------------------------
- Fixed no args Dict annotation, raising an exception `#494 <https://github.com/tefra/xsdata/issues/494>`_
- Fixed original name case not working for field names `#498 <https://github.com/tefra/xsdata/issues/498>`_
- Fixed element type resolution with duplicate name conflicts `#503 <https://github.com/tefra/xsdata/issues/503>`_
- Added handler to flatten bare inner classes
- Added the ability for custom types to subclass named tuples
- Added keyword meta in the reserved words `#491 <https://github.com/tefra/xsdata/issues/491>`_
- Added new xml type `Ignore` to skip fields during binding `#504 <https://github.com/tefra/xsdata/issues/504>`_
- Updated generic model DerivedElement.substituted flag with xsi:type
- Updated core components to improve binding performance

  - Converted almost all internal dataclasses to simple objects with __slots__
  - Converted the internal xml date/time types to named tuples
  - Reduced models metadata lookup times and memory footprint

- Updated JSON parser `#495 <https://github.com/tefra/xsdata/issues/495>`_

  - Support failing on unknown properties
  - Support required properties
  - Support parser config
  - Stricter binding process
  - Enhance DerivedElement support
