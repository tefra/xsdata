============
DTD Modeling
============

The code generator supports processing external document type definitions (DTD).

.. code-block:: console

    $ xsdata --package tests.fixtures.dtd.models tests/fixtures/dtd/complete_example.dtd


.. tab:: DTD Definition

    .. literalinclude:: /../tests/fixtures/dtd/complete_example.dtd
       :language: dtd

.. tab:: Output

    .. literalinclude:: /../tests/fixtures/dtd/models/complete_example.py
       :language: python
