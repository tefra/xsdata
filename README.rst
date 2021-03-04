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


Changelog: 21.3 (2021-03-04)
----------------------------
- Added constant name convention config `#407 <https://github.com/tefra/xsdata/issues/407>`_
- Added naming schemes screaming snake case and original case
- Updated xsi:lookup on xs:any derived elements `#315 <https://github.com/tefra/xsdata/issues/315>`_
- Updated fields restriction inheritance `#417 <https://github.com/tefra/xsdata/issues/417>`_
- Updated cli to allow package override from arguments `#416 <https://github.com/tefra/xsdata/issues/416>`_
- Updated code generation to merge duplicate global types earlier `#406 <https://github.com/tefra/xsdata/issues/406>`_
- Fixed docstrings issue breaking python syntax `#403 <https://github.com/tefra/xsdata/issues/403>`_
- Fixed bindings for nillable content without workarounds `#408 <https://github.com/tefra/xsdata/issues/408>`_
- Fixed resolver to apply aliases on extensions and choice fields `#414 <https://github.com/tefra/xsdata/issues/414>`_
- Fixed schema models limiting xs:appinfo occurrences `#420 <https://github.com/tefra/xsdata/issues/420>`_
- Decoupled core systems from click and lxml

**Notice**: In the next release installation profiles will be introduced that will turn
the cli, lxml and soap features **optional**.
