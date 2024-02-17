[![image](https://github.com/tefra/xsdata/raw/main/docs/logo.svg)](https://xsdata.readthedocs.io/)

# Naive XML Bindings for python

[![image](https://github.com/tefra/xsdata/workflows/tests/badge.svg)](https://github.com/tefra/xsdata/actions)
[![image](https://readthedocs.org/projects/xsdata/badge)](https://xsdata.readthedocs.io/)
[![image](https://codecov.io/gh/tefra/xsdata/branch/main/graph/badge.svg)](https://codecov.io/gh/tefra/xsdata)
[![image](https://img.shields.io/github/languages/top/tefra/xsdata.svg)](https://xsdata.readthedocs.io/)
[![image](https://www.codefactor.io/repository/github/tefra/xsdata/badge)](https://www.codefactor.io/repository/github/tefra/xsdata)
[![image](https://img.shields.io/pypi/pyversions/xsdata.svg)](https://pypi.org/pypi/xsdata/)
[![image](https://img.shields.io/pypi/v/xsdata.svg)](https://pypi.org/pypi/xsdata/)

---

xsData is a complete data binding library for python allowing developers to access and
use XML and JSON documents as simple objects rather than using DOM.

The code generator supports XML schemas, DTD, WSDL definitions, XML & JSON documents. It
produces simple dataclasses with type hints and simple binding metadata.

The included XML and JSON parser/serializer are highly optimized and adaptable, with
multiple handlers and configuration properties.

xsData is constantly tested against the
[W3C XML Schema 1.1 test suite](https://github.com/tefra/xsdata-w3c-tests).

## Getting started

```console
$ # Install all dependencies
$ pip install xsdata[cli,lxml,soap]
```

```console
$ # Generate models
$ xsdata tests/fixtures/primer/order.xsd --package tests.fixtures.primer
```

```python
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
```

Check the [documentation](https://xsdata.readthedocs.io) for more ✨✨✨

## Features

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

## Changelog: 24.2 (2024-02-17)

- Added Dict encoder/decoder ([#921](https://github.com/tefra/xsdata/pull/921))
- Deprecated Serializer config pretty_print/pretty_print_indentation
  ([#942](https://github.com/tefra/xsdata/pull/942))
- Fixed lxml event writer to respect the encoding configuration
  ([#940](https://github.com/tefra/xsdata/pull/940))
- Migrated documentation to mkdocs with markdown
- Refactored project docstrings
