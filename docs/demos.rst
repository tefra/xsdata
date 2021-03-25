=====
Demos
=====

Definitive XML Schema
=====================

Historically this was the first integration test suite of xsdata and is still being
used to make sure things still work between minor code changes.

It's based on the samples from the book
`Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
by Priscilla Walmsley that cover most of the basic XML Schema language traits

The test suite is using the auto generated models to parse the sample documents
and serializes them back to JSON and XML documents.

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

The suite is quite extensible and consist of more than 14k valid tests cases for both
XML and JSON Binding.

.. hint::

    Because of the size and time it takes to run the test runner is on it's own
    `repo <https://github.com/tefra/xsdata-w3c-tests>`_.

    At least until I can manage to reduce the total run time which is about 8 minutes
    without coverage.


XSD Results: **10** failed, **14576** passed, **89** skipped, **16** warnings

XML Results: **13** failed, **14573** passed, **90** skipped, **15** warnings

JSON Results: **113** failed, **14562** passed, **1** warnings


✨✨✨✨


.. hint::

    The `xmlschema <https://pypi.org/project/xmlschema/>`_ is used to validate xml
    output.

    The json mode performs roundtrip conversions and compares the initial and final
    outputs

    The xml mode is using the document instances instead of the schemas to generate
    the binding models.


Docstring styles
================

Choose the style of the generated docstrings.

The accessible is a custom style offering easy access to the docstrings
of a dataclass' fields or an enum' members for doc/api generators.

.. tab:: reStructuredText

    .. literalinclude:: /../tests/fixtures/docstrings/rst/schema.py
       :language: python
       :lines: 37-

.. tab:: NumPy

    .. literalinclude:: /../tests/fixtures/docstrings/numpy/schema.py
       :language: python
       :lines: 39-

.. tab:: Google

    .. literalinclude:: /../tests/fixtures/docstrings/google/schema.py
       :language: python
       :lines: 38-

.. tab:: Accessible

    .. literalinclude:: /../tests/fixtures/docstrings/accessible/schema.py
       :language: python
       :lines: 38-
