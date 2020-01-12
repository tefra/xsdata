Tests
======

The suite is based on the `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_ by Priscilla Walmsley xsd samples and tests only focus on code generation with the pydata format.

**Results**

.. include:: ../tests/fixtures/defxmlschema/results.rst

**Skip Reasons:**

- Incomplete fixture (Almost 50% of the skipped tests with missing definitions)
- XML Schema 1.1
- The generator didn't fail for illegal schema definitions
- Missing implementation: substitution groups, mixed content, any attributes, elements



http://www.datypic.com/books/defxmlschema/


.. toctree::
    :glob:

    tests/*/*
