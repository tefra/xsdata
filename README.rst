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


Changelog: 21.8 (2021-08-03)
----------------------------
- Deprecated JsonSerializer indent property, use SerializerConfig instead
- Fixed SchemaMapper assigning wrong namespace for imported unqualified elements
- Fixed AttributeTypeHandler to maintain occurs between any flattening
- Fixed missing required field metadata property
- Fixed nillable fields not being marked as optional
- Fixed fields ordering during class reduce process (Codegen from xml/json)
- Added support for xs:defaultOpenContent:appliesToEmpty attribute
- Added ParserConfig class factory option `#549 <https://github.com/tefra/xsdata/pull/549>`_
- Added SerializerConfig option to ignore optional default attributes `#555 <https://github.com/tefra/xsdata/pull/555>`_
- Added warning on unexpected duplicate types `#564 <https://github.com/tefra/xsdata/pull/564>`_
- Added GeneratorConfig support for kw_only and slots for python >= 3.10
- Added structure style namespace-clusters `#573 <https://github.com/tefra/xsdata/pull/573>`_
- Updated text fields default value to empty string and marked as required `#570 <https://github.com/tefra/xsdata/pull/570>`_
- Updated fields derived from xs:substitutionGroups to optional
- Updated fields derived from xs:any to optional
- Updated AttributeDefaultValueHandler to preserve acceptable default values
- Updated AttributeDefaultValueHandler to mark as optional any xsi:type attribute
- Updated xs:alternative handling to resemble xs:choice
- Updated mixed content handler to group all elements under wildcard
- Updated ElementMapper to detect nillable types
- Updated DictMapper to generate list of xs:anySimpleType for empty list nodes
- Updated the compatibility layer for dataclass style plugins
- Updated namespaces structure style to convert namespaces similar to jaxb

  - `http://www.w3.org/XML/1998/namespace` to `org.w3.XML.1998.namespace`

- Update binding process for nillable types and fields

  - nillable types can be initialized
  - nillable fields are initialized with None values
