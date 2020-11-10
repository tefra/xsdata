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
bindings. It produces simple dataclasses with type hints that don't depend on the
library itself in order to reduce the learning curve for users that have to write the
binding models manually.

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


Changelog: 20.11 (2020-11-10)
-----------------------------
- Added sub command to download remote schemas and definitions. `#279 <https://github.com/tefra/xsdata/issues/279>`_
- Added new optional xml type `Elements` to maintain ordering for repeatable choices. `#296 <https://github.com/tefra/xsdata/issues/296>`_
- Added xsi:type lookup procedure for xs:anyType derived elements. `#306 <https://github.com/tefra/xsdata/issues/306>`_
- Updated simple type flattening detection. `#286 <https://github.com/tefra/xsdata/issues/286>`_
- Updated generator to allow namespace structure on schemas without target namespace.
- Updated generator to avoid writing min/max occurs metadata for implied values. `#297 <https://github.com/tefra/xsdata/issues/297>`_
- Update generator to use literal dictionary initialization.
- Updated parser security, disable lxml network and entities resolve.
- Fixed field types detection for elements with xs:alternative children. `#284 <https://github.com/tefra/xsdata/issues/284>`_
- Fixed file generation to enforce default charset UTF-8. `#302 <https://github.com/tefra/xsdata/issues/302>`_
- Fixed jinja2 undefined namespace var collision. `#298 <https://github.com/tefra/xsdata/issues/298>`_
- Fixed import class name collision. `#300 <https://github.com/tefra/xsdata/issues/300>`_
- Fixed restriction inheritance on xs:group elements. `#301 <https://github.com/tefra/xsdata/issues/301>`_
