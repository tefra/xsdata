Why I get a TypeError: requires a single type
=============================================

The full error message looks something like this:

.. code-block::

    TypeError: typing.Optional requires a single type. Got Field(name=None,type=None,default=<dataclasses._MISSING_TYPE object at 0x7f79f4b0d700>,default_facto.

The error means the dataclass wrapper can't build the typing annotations for a model
because the field type is ambiguous. If you are using the code generator make sure you
are not using the same convention for both field and class names.

**Example**

.. code-block:: python

    @dataclass
    class unit:
        pass


    @dataclass
    class element:
        unit: Optional[unit] = field()


Read :ref:`more <Generator Config>`
