=====
Demos
=====

Definitive XML Schema
=====================

Historically this was the first integration test suite of xsdata and is still used to
make sure things still work between minor code changes.

It's based on the samples from the book
`Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_ by Priscilla Walmsley.

The samples cover most of the XML Schema language traits and the test suite is using the
:mod:`~xsdata.cli` with the :mod:`~xsdata.formats.dataclass` format to generate code and
demonstrate the current data binding capabilities for the
:mod:`~xsdata.formats.dataclass` by deserializing XML data to python content trees and
then converting them back to JSON and XML documents.


.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_ by Priscilla
    Walmsley (c) 2012 Prentice Hall PTR

.. toctree::
    :maxdepth: 1
    :glob:


    defxmlschema/*


W3C XML Schema Suite
====================

xsdata is constantly tested and measured against the
`W3C XML Schema 1.1 test suite <https://github.com/w3c/xsdtests>`_.

The suite is quite extensible and consist of more than 26k tests cases for both XML
Schema 1.0 and 1.1.

.. hint::

    Because of the size and time it takes to run the test runner is on it's own
    `repo <https://github.com/tefra/xsdata-w3c-tests>`_.

    At least until I can manage to reduce the total run time which is about 8 minutes
    without coverage.


Report
------

**45** failed, **14521** passed, **110** skipped @
`travis-ci <https://travis-ci.com/tefra/xsdata-w3c-tests>`_

✨✨✨✨

Methodology
-----------

- Invalid schema tests or no schema tests are ignored (~12k tests)
- Generate dataclasses for given schema.
  - **Fail** when cli raises exception or expected module::class is not found.
- Parse the given xml instance.
  - **Fail** when parser raises exception.
- Serialize to xml and validate against the schema.
  - **Fail** if final output is invalid.
  - **Skip** if original instance or schema also fail validation.


For all XML Schema definitions we use the
`xmlschema <https://pypi.org/project/xmlschema/>`_ to validate results.


.. hint::

    xsdata is an xml binding library not a schema validator.


**Try it out**

.. code-block:: console

    git clone git@github.com:tefra/xsdata-w3c-tests.git
    cd xsdata-w3c-tests
    pip install -r requirements.txt
    pytest -n 4 --tb short tests/  # | tee pytest.log
