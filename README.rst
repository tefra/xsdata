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

xsData is a complete XML data binding library for python allowing developers to access
and use XML documents as simple objects rather than using DOM.

It ships with a code generator for XML Schema definitions and WSDL 1.1 with SOAP 1.1
bindings. It produces simple dataclasses with type hints in order to reduce the learning
curve for users that have to write the binding models manually.

The included xml parser and serializer are highly optimized and adaptable with handlers
based on native python and lxml. The parser configuration offers the ability to skip
unknown properties and to process xinclude statements.

xsData is constantly tested against the
`W3C XML Schema 1.1 test suite <https://github.com/tefra/xsdata-w3c-tests>`_.

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


Changelog: 21.2 (2021-02-02)
----------------------------

- Added class name context for user naming schemes `#348 <https://github.com/tefra/xsdata/issues/348>`_
- Added mixed pascal naming scheme `#348 <https://github.com/tefra/xsdata/issues/348>`_
- Added access to element/attribute name generators `#381 <https://github.com/tefra/xsdata/issues/381>`_
- Added XmlHexBinary/XmlBase64Binary builtin data types `#387 <https://github.com/tefra/xsdata/issues/387>`_
- Added support for xs:anyType root elements `#399 <https://github.com/tefra/xsdata/issues/399>`_
- Updated JSON binding modules to use the fields local name `#389 <https://github.com/tefra/xsdata/issues/389>`_
- Updated enum classes generation
   - Promote all inner enums to root `#383 <https://github.com/tefra/xsdata/issues/383>`_
   - Fixed issues with producing invalid members `#385 <https://github.com/tefra/xsdata/issues/385>`_
   - Added support for list/tuple member values
- Updated parsers accuracy for Union types
- Updated dependency resolution accuracy
- Update base classes generation strategies
- Updated builtin data types with helper constructors/methods
- Fixed inner class names conflicts `#375 <https://github.com/tefra/xsdata/issues/375>`_
- Fixed issue not generating fields derived from xs:alternative elements `#393 <https://github.com/tefra/xsdata/issues/393>`_
- Fixed duplicate root class name regression from v20.12
- Fixed issue adding unused lib imports
- Fixed issue adding unused name properties to choice elements
