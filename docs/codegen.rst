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

Specify where the target module(s) will be created inside the current working directory.
eg `--package api.models`

.. admonition:: Note
    :class: hint

    The cli is relying on the `os.path.commonpath` of the schemas locations to
    create the final package structure. If you prefer a more flat structure or
    you have circular import errors check the option :ref:`ns-struct`.


output
------

Specify the output format

* ``pydata``: Python lib `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_
* ``plantuml``: `PlantUML <https://plantuml.com/class-diagram>`_ class diagram


verbosity
---------

Specify the log level, default is ``INFO``

Available options: ``CRITICAL``, ``ERROR``, ``WARNING``, ``INFO`` or ``DEBUG``


wsdl
----

Generate models and services from a wsdl source.


.. admonition:: Experimental
    :class: danger

    This feature is experimental and only a small subset of features have been
    implemented, WSDL 1.1 & SOAP 1.1 bindings.


print
-----

Redirect generated code to stdOut instead of writing the output to the target files.


ns-struct
---------

Group classes by the target namespace they were defined. This option creates a more
flat package structure and solves many circular import errors.


.. admonition:: Examples
    :class: hint

    Check the :doc:`demos` and the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more ✨✨✨
