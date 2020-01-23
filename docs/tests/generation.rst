Code Generation
===============

The test suite is using the :mod:`~xsdata.cli` with the :mod:`~xsdata.formats.dataclass` format to generate code from simple examples that cover most of the XML Schema language traits.

The primary goal of this suite is to keep track of the XSD features not yet supported and to monitor changes in the current implementation.


**Results**

.. include:: ../../tests/fixtures/defxmlschema/generation.results.rst

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_ by Priscilla Walmsley (c) 2012 Prentice Hall PTR

.. toctree::
    :glob:

    generation/*
