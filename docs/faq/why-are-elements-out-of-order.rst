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
