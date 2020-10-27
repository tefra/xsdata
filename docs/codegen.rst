============
Command Line
============


.. command-output:: xsdata --help


Code Generator
==============


.. command-output:: xsdata generate --help

Generate is the default subcommand of the command line interface and can be omitted.

.. code-block:: console

    $ xsdata amadeus/schemas --package amadeus.models

    $ xsdata air_v48_0/AirReqRsp.xsd rail_v48_0/RailReqRsp.xsd --package travelport.models

    $ xsdata http://www.gstatic.com/localfeed/local_feed.xsd --package feeds --print


SOURCE
------

You can pass the file path or uri to a schema or a whole directory with multiple
definitions.


config
------

Specify a configuration file with more advance options.


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


compound-fields
---------------

The generator by default will flatten repeating choice elements into simple fields.
The main disadvantage is that the original elements ordering is lost during marshalling.
With this option you can force the generator to create compound list fields to preserve
ordering.

See :ref:`Type: Elements`

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


Configuration
=============

Alternatively to the cli flags and options you can provide a project
:mod:`xsdata.models.config` document.

.. code-block:: console

    $ xsdata amadeus/schemas --config amadeus/.xsdata.xml

The configuration offers more advance options to further tail the output to your needs,
like naming conventions and aliases.


.. command-output:: xsdata init-config --help

.. command-output:: xsdata init-config --print


.. hint::

    The sample output has the default naming conventions and some example aliases.


Conventions
-----------


**Case schemes**

All schemes are using a processor that splits a string into words when it encounters
non alphanumerical characters or when an upper case letter follows a lower case letter.

.. include:: name_cases_table.rst


.. hint::

    The mixed case is joining the words without changing the original upper/lower case

    The mixed underscore case is joining the words with an underscore.

    The pascal/camel cases are using python's :func:`str.title` method!


**Safe Prefixes**

They are used to neutralize classes and fields names that match reserved keywords.

.. code-block::

    and, except, lambda, with, as, finally, nonlocal, while, assert, false, none,
    yield, break, for, not, class, from, or, continue, global, pass, def, if, raise,
    del, import, return, elif, in, true, else, is, try, str, int, bool, float, list,
    optional, dict, field


Aliases
-------

The aliases allow users to override global naming conventions for class, fields package
and module names. Each alias has a source attribute that refers to the original type
name in the schema definition and the target attribute for output name.


For package and module aliases the source refers to the schemas filenames or
target namespaces depending the output structure strategy selected.

.. danger::

    The generator doesn't validate user defined target names.


Download Schemas
================

.. command-output:: xsdata download --help


.. admonition:: Examples
    :class: hint

    Check the :doc:`demos` and the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more ✨✨✨
