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

Features
--------

- Generate data models from XML Schema 1.0 and 1.1 definitions.
- Supports qualified/unqualified elements and attributes
- Supports enumerations and inner classes
- Flattening strategies to keep the code as simple as possible.
- Preserve embedded documentation and references
- Pluggable code writer that supports different formats
- Output: Python Data Classes

  - PEP8 naming conventions and code output
  - Full support for type hints even with forward references
  - XML Parser & Serializer based on lxml
  - JSON Parser & Serializer

- Output: PlantUML class diagram

-------

.. image:: https://github.com/tefra/xsdata/raw/master/docs/_static/demo.svg

Check the documentation `test suites <https://xsdata.readthedocs.io/>`_ or our `W3C XML Schema 1.1  <https://github.com/tefra/xsdata-w3c-tests>`_ test runner and the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more ✨✨✨


Changelog: 20.5 (2020-05-02)
----------------------------
- Updated codegen cli to accept multiple definitions or directories as argument.
- Update ClassBuilder to recursively search for anonymous types.
- Updated XmlParser to be thread-safe.
- Added performance tweaks on XmlParser.
- Added parser config to fail or not on unknown properties.
- Fixed primitive types being marked as forward references.
- Fixed nested restrictions on xs:simpleType.
- Fixed ClassAnalyzer to recover/ignore missing types.
