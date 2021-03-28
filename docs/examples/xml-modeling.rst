============
XML Modeling
============


By using multiple samples you can create more complete models. The generator will merge
duplicate classes and their fields and their field types.


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
