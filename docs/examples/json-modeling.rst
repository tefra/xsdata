=============
JSON Modeling
=============


By using multiple samples you can create more complete models. The generator will merge
duplicate classes and their fields and their field types.


.. code-block:: console

    $ xsdata --package tests.fixtures.series tests/fixtures/series


.. tab:: Sample #1

    .. literalinclude:: /../tests/fixtures/series/show1.json
       :language: json

.. tab:: Sample #2

    .. literalinclude:: /../tests/fixtures/series/show2.json
       :language: json


.. tab:: Output

    .. literalinclude:: /../tests/fixtures/series/series.py
       :language: python
