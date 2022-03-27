Why do I get a TypeError: requires a single type
================================================

The full error message looks something like this:

.. code-block::

    TypeError: typing.Optional requires a single type. Got Field(name=None,type=None,default=<dataclasses._MISSING_TYPE object at 0x7f79f4b0d700>,default_facto.

This error means the typing annotations for a model are ambiguous because they
collide with a class field. In order to resolve this issue you have to enable
code:`PostponedAnnotations` in the :ref:`generator config <Generator Config>`.


.. hint::
    Postponed Evaluations of Annotations (`PEP 563 <https://www.python.org/dev/peps/pep-0563/>`_).


**Example**

.. literalinclude:: /../tests/fixtures/annotations/model.py
   :language: python
