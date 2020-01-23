Data Binding
============

The suite is demonstrating the current data binding capabilities for the :mod:`~xsdata.formats.dataclass` by deserializing XML data to python content trees and then converting them back to JSON and XML documents.


**Modules**

- :class:`~xsdata.formats.dataclass.parsers.XmlParser`
- :class:`~xsdata.formats.dataclass.serializers.XmlSerializer`
- :class:`~xsdata.formats.dataclass.serializers.JsonSerializer`


**Results**

.. include:: ../../tests/fixtures/defxmlschema/binding.results.rst

Tests that finish without exceptions are marked as succesfull the actual output may contain errors, that we are trying to fix!


.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_ by Priscilla Walmsley (c) 2012 Prentice Hall PTR

.. toctree::
    :glob:

    binding/*
