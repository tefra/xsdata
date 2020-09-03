.. image:: https://github.com/tefra/xsdata/raw/master/docs/_static/logo.png
    :target: https://xsdata.readthedocs.io/

Naive XML Bindings for python
=============================

.. image:: https://travis-ci.com/tefra/xsdata.svg?branch=master
    :target: https://travis-ci.com/tefra/xsdata

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

xsData is a complete XML data binding library for python allowing developers to access
and use XML documents as simple objects rather than using DOM.

It ships with a code generator for XML Schema definitions and WSDL 1.1 with SOAP 1.1
bindings. It produces simple dataclasses with type hints that don't depend on the
library itself in order to reduce the learning curve for users that have to write the
binding models manually.

The included parser is highly optimized and adaptable with 4 available handlers based
on native python and lxml. The parser configuration offers the ability to skip unknown
properties and to process xinclude statements.

The parser and serializer are constantly tested against the
`W3C XML Schema 1.1 test suite <https://github.com/tefra/xsdata-w3c-tests>`_ and
passes more than 99% of the valid instance cases.

.. image:: https://github.com/tefra/xsdata/raw/master/docs/_static/demo.svg

Check the documentation `demos <https://xsdata.readthedocs.io/en/latest/demos.html>`_ or
our `W3C XML Schema 1.1  <https://github.com/tefra/xsdata-w3c-tests>`_ test runner and
the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more ✨✨✨


Features
--------

- Generate data models for XML Schema 1.0 and 1.1 definitions.
- Generate data models for WSDL 1.1 and SOAP 1.1 bindings.
- Support qualified elements/attributes, enumerations and inner classes.
- Preserve embedded documentation and references.
- Data binding for XML and JSON documents.
- Pluggable code writer that supports python dataclasses and PlantUML class diagrams.


Changelog: 20.9 (2020-09-03)
----------------------------
- Added field metadata key `tokens` for xs:list or xs:NMTOKENS derived elements.
- Added datatype factory to register custom converters.
- Added XmlHandler interface to decouple parsing from lxml.
- Added lxml based content handlers: LxmlEventHandler, LxmlSaxHandler
- Added native python xml content handlers: XmlEventHandler, XmlSaxHandler
- Added support for python >= 3.6 `#241 <https://github.com/tefra/xsdata/issues/241>`_
- Added codegen for soap 1.1 fault messages.
- Fixed converting to enum members derived from xs:NMTOKENS.
- Fixed package level import naming conflicts. `#228 <https://github.com/tefra/xsdata/issues/206>`_
- Fixed xml serializing to allow empty strings in attribute values. `#230 <https://github.com/tefra/xsdata/issues/230>`_
- Fixed xml serializing for mixed content with non generics. `#238 <https://github.com/tefra/xsdata/issues/238>`_
