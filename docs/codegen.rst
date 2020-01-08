Code Generator
==============


CLI Entry Point
---------------

.. command-output:: xsdata --help

XSD Path
--------

The generator doesn't work with urls only with local files, if the given schema includes other schemas with urls the generator will fail. Every schema is evaluated once and in the order they are defined.

Circular dependencies will probably work just fine :)

Package
-------

The package option defines where the target module(s) will be created inside the current working directory.

If the main xsd has any parent include or import you should adjust the target package.

.. admonition:: Example
    :class: warning

    * Output directory ``./api/models``
    * Main xsd ``./api/air/AirReqRsp.xsd` that includes ``../common/CommonReqRsp.xsd``
    * Adjust the package from ``api.models`` to ``api.models.air`` because the generator has to also create the ``common.common_req_rsp`` module.

Renderer
--------

The renderer option changes the output format.

* ``pydata``: Python lib `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_
* ``plantuml``: `PlantUML <https://plantuml.com/class-diagram>`_ class diagram

Verbosity
---------

The verbosity option changes what messages will be printed.

Available options: ``CRITICAL``, ``ERROR``, ``WARNING``, ``INFO`` or ``DEBUG``

Print
-----

The print flag overwrites the verbosity level to `Error` and print to stdOut the output result without writing to the target file.

Examples
--------

Check the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more.


Basic
^^^^^

.. literalinclude:: examples/common.py
   :language: python
   :lines: 353-392


Enum
^^^^

.. literalinclude:: examples/common.py
   :language: python
   :lines: 1685-1702


Inner Class
^^^^^^^^^^^^

.. literalinclude:: examples/common.py
   :language: python
   :lines: 395-434
