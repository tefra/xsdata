Definitive XML Schema
=====================

The samples from the book covert most of the XML Schema language traits.

The test suite is using the :mod:`~xsdata.cli` with the :mod:`~xsdata.formats.dataclass` format to generate code and demostrate the current data binding capabilities for the :mod:`~xsdata.formats.dataclass` by deserializing XML data to python content trees and then converting them back to JSON and XML documents.


**Modules**

- :class:`~xsdata.formats.dataclass.parsers.XmlParser`
- :class:`~xsdata.formats.dataclass.serializers.XmlSerializer`
- :class:`~xsdata.formats.dataclass.serializers.JsonSerializer`


.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_ by Priscilla Walmsley (c) 2012 Prentice Hall PTR

.. toctree::
    :maxdepth: 1
    :glob:


    defxmlschema/*
