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

The code generator supports XML schemas, DTD, WSDL definitions, XML & JSON documents.
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
  - DTD external definitions
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
  - PyCode serializer
  - Handlers and Writers based on lxml and native xml python
  - Support wildcard elements and attributes
  - Support xinclude statements and unknown properties
  - Customize behaviour through config



Changelog: 23.5 (2023-05-21)
----------------------------
- Fixed XML meta var index conflicts.
- Fixed mixed content handling for DTD elements. (`#749 <https://github.com/tefra/xsdata/pull/749>`_, `#762 <https://github.com/tefra/xsdata/pull/762>`_)
- Fixed an issue with required attributes turning into optional ones.
- Fixed calculation of min/max occurs when parsing XML/JSON documents. (`#756 <https://github.com/tefra/xsdata/pull/756>`_)
- Fixed calculation of min/max occurs when parsing DTD choice content types. (`#760 <https://github.com/tefra/xsdata/pull/760>`_)
- Fixed an issue when parsing tail content for compound wildcard elements.
- Fixed an issue with the code analyzer not fully processing some classes.
- Fixed an issue with the code analyzer taking forever to process very large enumerations. (`#776 <https://github.com/tefra/xsdata/issue/776>`_)
- Fixed an issue in the JSON parser with optional choice elements.
- Updated the transformer to silently ignore malformed JSON files. (`#750 <https://github.com/tefra/xsdata/pull/750>`_)
- Updated the override attribute handler to fix naming conflicts.
- Updated the override attribute handler to allow wildcard overrides.
- Updated conditions on extensions flattening (over-flattening). (`#754 <https://github.com/tefra/xsdata/pull/754>`_)
- Updated Group, AttributeGroup handling, skipping a few cases.
- Updated how min/max occurs are calculated with nested containers.
- Updated handling of element substitutions to treat them as choices. (`#786 <https://github.com/tefra/xsdata/pull/786>`_)
- Updated Pycodeserializer to skip default field values.
- Updated flattening restriction base classes when sequence elements are out of order.
- Updated docformatter to v1.6.5.
- Added support to override compound fields.
- Added support for multiple sequential groups in a class.
- Added support for non-list compound fields.
- Added support to mix list and non-list fields with sequence groups.
- Added an option to include headers in generated files. (`#746 <https://github.com/tefra/xsdata/pull/746>`_)
- Added an option to cache the initial load and mapping of resources.
- Added support for regular expressions in config substitutions. (`#755 <https://github.com/tefra/xsdata/pull/755>`_)
- Added a pretty print indentation option in the serializer config. (`#780 <https://github.com/tefra/xsdata/pull/780>`_)
- Added an option to set the encoding in the SOAP Client. (`#773 <https://github.com/tefra/xsdata/pull/773>`_)
- Added a CLI flag to show debug messages.
- Added a debug message for possible circular references during code generation.
- Added support to generate prohibited fields when they restrict parent fields. (`#781 <https://github.com/tefra/xsdata/pull/781>`_)

This release is bigger than intended and includes many major changes,
that's why it took so long.
