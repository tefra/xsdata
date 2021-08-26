============
XML Modeling
============

The code generator supports processing xml documents directly. That means even without
a schema you can easily create at the very least an initial draft of your models just
from samples. If you use a directory with multiple samples the transformer will merge
and flatten duplicate classes, fields and field types.

.. code-block:: console

    $ xsdata --package tests.fixtures.artists tests/fixtures/artists


.. tab:: Sample #1

    .. literalinclude:: /../tests/fixtures/artists/art001.xml
       :language: xml

.. tab:: Sample #2

    .. literalinclude:: /../tests/fixtures/artists/art002.xml
       :language: xml

.. tab:: Sample #3

    .. literalinclude:: /../tests/fixtures/artists/art003.xml
       :language: xml

.. tab:: Output

    .. literalinclude:: /../tests/fixtures/artists/metadata.py
       :language: python
