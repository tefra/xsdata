=============
JSON Modeling
=============


The code generator supports processing json documents directly. That means even without
a schema you can easily create at the very least an initial draft of your models just
from samples. If you use a directory with multiple samples the transformer will merge
and flatten duplicate classes, fields and field types.


.. code-block:: console

    $ xsdata --package tests.fixtures.series tests/fixtures/series/samples


.. tab:: Sample #1

    .. literalinclude:: /../tests/fixtures/series/samples/show1.json
       :language: json

.. tab:: Sample #2

    .. literalinclude:: /../tests/fixtures/series/samples/show2.json
       :language: json


.. tab:: Output

    .. literalinclude:: /../tests/fixtures/series/series.py
       :language: python
