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


Changelog: 20.10 (2020-10-02)
-----------------------------
- Fixed generator adding multiple default value fields. `#249 <https://github.com/tefra/xsdata/issues/249>`_
- Fixed generator not applying nested container restrictions. `#263 <https://github.com/tefra/xsdata/issues/253>`_
- Fixed generator to avoid case insensitive class name conflicts. `#269 <https://github.com/tefra/xsdata/issues/269>`_
- Fixed generator rendering unused simple types.
- Fixed generator unsorted libraries imports.
- Fixed JsonParser trying to parse init=False fields. `#253 <https://github.com/tefra/xsdata/issues/253>`_
- Fixed NodeParser binding tail content more than once with mixed vars. `#256 <https://github.com/tefra/xsdata/issues/256>`_
- Added XmlWriter interface to decouple serialize from lxml. `#247 <https://github.com/tefra/xsdata/issues/247>`_
- Added native python xml content writer XmlEventWriter. ✨✨✨
- Added lxml based content writer: LxmlEventWriter.
- Added generator config with options to control naming cases and aliases. `#265 <https://github.com/tefra/xsdata/issues/265>`_
- Updated field xml type auto detection to be more flexible. `#246 <https://github.com/tefra/xsdata/issues/246>`_
- Updated EnumConverter to resort to canonical form matching as last resort. `#273 <https://github.com/tefra/xsdata/issues/273>`_
- Updated support for derived elements. `#267 <https://github.com/tefra/xsdata/issues/267>`_


This is my favorite release so far, maybe because xsdata reached one year of development
✨✨✨ or maybe because some of the last original components finally got the rewrite they
deserved.
