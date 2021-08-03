**************************
Frequently Asked Questions
**************************



Why are all properties marked as optional?
------------------------------------------

We rely on the fields ordering for all binding procedures and due to the following
limitation we have to mark even required fields as optional.

..

    TypeError will be raised if a field without a default value follows a field
    with a default value. This is true whether this occurs in a single class, or as
    a result of class inheritance.

    Source: :mod:`python:dataclasses`

In Python 3.10 dataclasses introduced a new directive `kw_only` that resolves the above
limitation and xsdata handling. Read :ref:`more <Dataclasses Features>`

If you can't update just yet please check the `attrs <https://pypi.org/project/xsdata-attrs/>`_ plugin!


Why are elements out of order?
------------------------------

There are a few cases when elements can appear in any order. The default simplified
models don't have a way to store the original order of the elements in a document.

Repeatable choice elements is one of them.

.. literalinclude:: /../tests/fixtures/compound/schema.xsd
   :language: xml
   :lines: 1-9

In order to maintain the original order between roundtrip conversions you need to
enable compound fields. Compound fields are group fields and can be used to wrap
mixed context elements, repeatable choice elements or complex sequential elements.

Read :ref:`more <Compound Fields>`
