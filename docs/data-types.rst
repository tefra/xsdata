==========
Data Types
==========


Mapping
=======

Below you can find the mapping of data types between python and xml schema.

.. include:: data-types-table.rst

Converters
==========

The build-in converters are used to bind data from and to xml documents. They are
also used partially for json data binding when the typing information is lost in
the literal representation like enumerations.

The converter will attempt to convert values according to the provided list of
possible types but in case of an error it will fall back to str, even if that
means violating the field typing definition.

A warning will also be raised in that case.

.. code-block::

    ConverterWarning: Failed to convert value `a` to one of [<class 'float'>]


You can register your custom type converters if you are working with user defined
models with types not supported from the default ones.


.. literalinclude:: examples/converter.py
   :lines: 9-
