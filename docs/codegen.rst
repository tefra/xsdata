Code Generator
==============


CLI Entry Point
---------------

.. command-output:: xsdata --help

SOURCE
------

You can pass the file path or uri to a schema or a whole directory with multiple
definitions.


.. code-block:: console

    $ xsdata amadeus/schemas --package amadeus.models

    $ xsdata air_v48_0/AirReqRsp.xsd rail_v48_0/RailReqRsp.xsd --package travelport.models

    $ xsdata http://www.gstatic.com/localfeed/local_feed.xsd --package feeds --print


package
-------

The package option specifies where the target module(s) will be created inside the
current working directory.

.. admonition:: Note
    :class: hint

    The cli is relying on the `os.path.commonpath` of the schemas locations to
    create the final package structure. If you prefer a more flat structure or
    you have circular import errors check the option :ref:`ns-struct`.


output
------

The output option changes the generation format.

* ``pydata``: Python lib `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_
* ``plantuml``: `PlantUML <https://plantuml.com/class-diagram>`_ class diagram


verbosity
---------

The verbosity option changes what messages will be printed.

Available options: ``CRITICAL``, ``ERROR``, ``WARNING``, ``INFO`` or ``DEBUG``


wsdl
----

Generate models and services from a wsdl source.


.. admonition:: Experimental
    :class: danger

    This feature is experimental and only a small subset of features has been
    implemented, WSDL 1.1 & SOAP 1.1 bindings.


print
-----

The print flag overwrites the verbosity level to `Error` and print to stdOut the output
result without writing to the target file.


ns-struct
---------

The ns-struct flag bypasses the default behavior and groups classes by the target
namespace they were defined. This option creates a more flat package structure and
solves any circular import errors.


.. admonition:: Examples
    :class: hint

    Check the :doc:`demos` and the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more ✨✨✨
