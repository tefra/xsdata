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

## Changelog: 24.3.1 (2024-03-10)

**Fixes**

- Unnest class with circular reference
  ([#974](https://github.com/tefra/xsdata/pull/974))

## Changelog: 24.4 (2024-04-01)

**Features**

- Add xml and lxml tree serializers ([#975](https://github.com/tefra/xsdata/pull/975))
- Capture namespace prefixes in user dicts
  ([#978](https://github.com/tefra/xsdata/pull/978))
- Add cli option to generate wrapper fields
  ([#982](https://github.com/tefra/xsdata/pull/982))
- Support wrapper fields in JSON data bindings
  ([#982](https://github.com/tefra/xsdata/pull/982))
- Use abstract suffixes to resolve class name conflicts
  ([#985](https://github.com/tefra/xsdata/pull/985))
- Add the version number in the cli cache key
  ([#990](https://github.com/tefra/xsdata/pull/990))
- Use unicodedata.name for attrs with only special characters
  ([#993](https://github.com/tefra/xsdata/pull/993))
- Add src code excerpts on ruff errors
  ([#996](https://github.com/tefra/xsdata/pull/996))
- Detect circular imports and raise appropriate error
  ([#999](https://github.com/tefra/xsdata/pull/999))
- Add support for Python 3.13 ([#1001](https://github.com/tefra/xsdata/pull/1001))
- Add cli debug messages with performance stats

**Fixes**

- Use deepcopy to clone codegen models
  ([#980](https://github.com/tefra/xsdata/pull/980))
- Generate type hints for compound fields with token elements
  ([#997](https://github.com/tefra/xsdata/pull/997))
- Protect prohibited attrs from turning into lists
  ([#998](https://github.com/tefra/xsdata/pull/998))
- Convert child attr to list when parent is list
  ([#998](https://github.com/tefra/xsdata/pull/998))
