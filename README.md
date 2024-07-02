[![image](https://github.com/tefra/xsdata/raw/main/docs/logo.svg)](https://xsdata.readthedocs.io/)

# Naive XML Bindings for python

[![image](https://github.com/tefra/xsdata/workflows/tests/badge.svg)](https://github.com/tefra/xsdata/actions)
[![image](https://readthedocs.org/projects/xsdata/badge)](https://xsdata.readthedocs.io/)
[![image](https://codecov.io/gh/tefra/xsdata/branch/main/graph/badge.svg)](https://codecov.io/gh/tefra/xsdata)
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
>>> from tests.fixtures.primer import PurchaseOrder
>>> from xsdata.formats.dataclass.parsers import XmlParser
>>>
>>> parser = XmlParser()
>>> order = parser.parse("tests/fixtures/primer/sample.xml", PurchaseOrder)
>>> order.bill_to
Usaddress(name='Robert Smith', street='8 Oak Avenue', city='Old Town', state='PA', zip=Decimal('95819'), country='US')
```

Check the [documentation](https://xsdata.readthedocs.io) for more ✨✨✨

## Features

**Code Generator**

- XML Schemas 1.0 & 1.1
- WSDL 1.1 definitions with SOAP 1.1 bindings
- DTD external definitions
- Directly from XML and JSON Documents
- Extensive configuration to customize output
- Pluggable code writer for custom output formats

**Default Output**

- Pure python dataclasses with metadata
- Type hints with support for forward references and unions
- Enumerations and inner classes
- Support namespace qualified elements and attributes

**Data Binding**

- XML and JSON parser, serializer
- PyCode serializer
- Handlers and Writers based on lxml and native xml python
- Support wildcard elements and attributes
- Support xinclude statements and unknown properties
- Customize behaviour through config

## Changelog: 24.6.1 (2024-06-28)

**Fixes**

- Ruff check command typo breaks generator with v0.5.0
  ([#1061](https://github.com/tefra/xsdata/pull/1061))

## Changelog: 24.6 (2024-06-24)

**Features**

- Add class and field info in parsing warnings
  ([#1036](https://github.com/tefra/xsdata/pull/1036))
- Remove whitespace from bytes encoded xml strings
  ([#1037](https://github.com/tefra/xsdata/pull/1037))
- Improve codegen performance ([#1043](https://github.com/tefra/xsdata/pull/1043))

**Fixes**

- JSON serializer fails on derived elements
  ([#1053](https://github.com/tefra/xsdata/pull/1053))
- Update typing-extensions minimum version
  ([#1039](https://github.com/tefra/xsdata/pull/1039))
- Avoid using not-threadsafe warnings.catch_warning
  ([#1042](https://github.com/tefra/xsdata/pull/1042))
- Unnest classes doesn't update inner classes recursively
  ([#1047](https://github.com/tefra/xsdata/pull/1047))
- Restore support for optional lists
  ([#1053](https://github.com/tefra/xsdata/pull/1053))
