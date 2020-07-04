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

xsData comes with a code generator that can convert XML Schema 1.0 and 1.1 definitions
to simple dataclasses with type hints and as minimum footprint as possible. The
generated packages have no dependency on the library itself. So simple that you can
write the models on your own if you happen to use an XML document with no schema
available.

The XML Parser is highly optimized and uses lxml iterparse to bind the document data to
the target models. The parser accepts a configuration instance with various options
like `fail on unknown properties` and is also thread safe which means you can take
advantage of the internal model inspection caching context for even faster parsing.

The parser and serializer are constantly tested against the
`W3C XML Schema 1.1 test suite <https://github.com/tefra/xsdata-w3c-tests>`_ and
passes more than 99% of the valid instance cases.

.. image:: https://github.com/tefra/xsdata/raw/master/docs/_static/demo.svg

Check the documentation `demos <https://xsdata.readthedocs.io/en/latest/demos.html>`_ or
our `W3C XML Schema 1.1  <https://github.com/tefra/xsdata-w3c-tests>`_ test runner and
the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more ✨✨✨


Features
--------

- Generate data models from XML Schema 1.0 and 1.1 definitions.
- Supports qualified elements/attributes.
- Supports enumerations and inner classes.
- Flattening strategies to keep the code as simple as possible.
- Preserve embedded documentation and references
- Pluggable code writer that supports different formats
- Output: Python Data Classes
- Output: PlantUML class diagram

Changelog: 20.7 (2020-07-04)
----------------------------
- Updated analyzer to allow abstract types to be generated. `#199 <https://github.com/tefra/xsdata/issues/199>`_
- Removed support to generate code from multiple sources. `#172 <https://github.com/tefra/xsdata/issues/172>`_
- Fixed naming conflict with AttributeGroup analyzer handler. `#194 <https://github.com/tefra/xsdata/issues/194>`_
- Fixed analyzer to merge redefined attribute groups. `#196 <https://github.com/tefra/xsdata/issues/196>`_
- Fixed analyzer to block inheritance on xs:override derived types. `#198 <https://github.com/tefra/xsdata/issues/198>`_
- Refactored code to prepare for wsdl support.
