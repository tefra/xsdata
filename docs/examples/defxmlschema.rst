=====================
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


~~~~~~


#08 - Simple types
==================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter08.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter08.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter08.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter08.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter08.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#12 - Complex types
===================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter12.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter12.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter12.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter12.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter12.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#01 - Schemas: An introduction
==============================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter01.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter01.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter01.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter01.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter01.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#03 - Namespaces
================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter03.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter03.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter03.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter03.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter03.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#16 - Substitution groups
=========================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter16.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter16.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter16.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter16.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter16.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#04 - Schema composition
========================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter04.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter04.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter04.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter04.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter04.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#17 - Identity constraints
==========================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter17.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter17.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter17.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter17.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter17.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#15 - Named groups
==================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter15.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter15.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter15.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter15.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter15.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#13 - Deriving complex types
============================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter13.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter13.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter13.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter13.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter13.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#05 - Instances and schemas
===========================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter05.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter05.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter05.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter05.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter05.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR


#10 - Union and list types
==========================


**Code Generation**

.. tab:: Schema

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter10.xsd
       :language: xml
       :lines: 2-

.. tab:: Models

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter10.py
       :language: python

**Data Binding**

.. tab:: Original XML Document

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter10.xml
       :language: xml
       :lines: 2-

.. tab:: xsData XML Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter10.xsdata.xml
       :language: xml
       :lines: 2-

.. tab:: xsData JSON Output

    .. literalinclude:: /../tests/fixtures/defxmlschema/chapter10.json
       :language: json

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR
