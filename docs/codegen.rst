Code Generator
==============


CLI Entry Point
---------------

.. command-output:: xsdata --help

SOURCES
--------

You can pass a list of definitions or a directory which includes the xml schemas you
want to process.


.. code-block:: console

    $ xsdata amadeus/schemas --package amadeus.models

    $ xsdata air_v48_0/AirReqRsp.xsd rail_v48_0/RailReqRsp.xsd --package travelport.models

    $ xsdata http://www.gstatic.com/localfeed/local_feed.xsd --package feeds --print


Although you can pass multiple sources, I am advising against that unless if you are
sure your sources are well written clean without namespace or naming conflicts.


Package
-------

The package option defines where the target module(s) will be created inside the
current working directory.

If the main xsd has any parent include or import you should adjust the target package.

.. admonition:: Note
    :class: hint

    The cli is relying on the `os.path.commonpath` to create the package structure and
    doesn't do any conflict resolution, which shouldn't be an issue if you use the cli
    with a single source (directory or remote/local file).


Output
------

The output option changes the generation format.

* ``pydata``: Python lib `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_
* ``plantuml``: `PlantUML <https://plantuml.com/class-diagram>`_ class diagram

Verbosity
---------

The verbosity option changes what messages will be printed.

Available options: ``CRITICAL``, ``ERROR``, ``WARNING``, ``INFO`` or ``DEBUG``

Print
-----

The print flag overwrites the verbosity level to `Error` and print to stdOut the output
result without writing to the target file.


.. admonition:: Examples
    :class: hint

    Check the :doc:`demos` and the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more ✨✨✨
