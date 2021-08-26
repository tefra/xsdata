================
Docstring styles
================

xsdata relies on `docformatter <https://pypi.org/project/docformatter/>`_  to follow
the `PEP 257 <https://www.python.org/dev/peps/pep-0257/>`_ -- docstring conventions and
offers the ability to switch between the most popular styles or disable them completely.

.. tab:: reStructuredText

    .. literalinclude:: /../tests/fixtures/docstrings/rst/schema.py
       :language: python
       :lines: 37-

.. tab:: NumPy

    .. literalinclude:: /../tests/fixtures/docstrings/numpy/schema.py
       :language: python
       :lines: 39-

.. tab:: Google

    .. literalinclude:: /../tests/fixtures/docstrings/google/schema.py
       :language: python
       :lines: 38-

.. tab:: Accessible

    This custom style sets the docstrings directly to enum members and fields
    metadata for runtime access.

    .. literalinclude:: /../tests/fixtures/docstrings/accessible/schema.py
       :language: python
       :lines: 39-

.. tab:: Blank

    Disable docstrings generation.

    .. literalinclude:: /../tests/fixtures/docstrings/blank/schema.py
       :language: python
       :lines: 25-
