Why do I get a TypeError: requires a single type
================================================

The full error message looks something like this:

.. code-block::

    TypeError: typing.Optional requires a single type. Got Field(name=None,type=None,default=<dataclasses._MISSING_TYPE object at 0x7f79f4b0d700>,default_facto.

This error means the typing annotations for a model are ambiguous because they collide with a class field. If you use Python 3.7 or later, you can set :code:`PostponedAnnotations` to :code:`true` in the :ref:`GeneratorOutput` section of the :ref:`generator config <Generator Config>` to solve this issue. This will enable Postponed Evaluations of Annotations (`PEP 563 <https://www.python.org/dev/peps/pep-0563/>`_) and the generated bindings will be able to be imported without errors. This feature is not available for Python 3.6 because :code:`annotations` were added to the :code:`__future__` module in Python 3.7.0b1.

**Example**

.. literalinclude:: /../tests/fixtures/annotations/model.py
   :language: python
