============
Command Line
============


Make sure the cli requirements are installed.

.. code-block:: console

    $ pip install xsdata[cli]


.. command-output:: xsdata --help


Generate Code
=============

.. command-output:: xsdata generate --help

.. admonition:: See also
    :class: hint

    - :ref:`Compound fields <Type: Elements>`
    - :ref:`Docstring styles`


.. code-block:: console
    :caption: Scan directory for xsd, wsdl, xml files

    $ xsdata amadeus/schemas --package amadeus.models


.. code-block:: console
    :caption: Convert a local schema

    $ xsdata air_v48_0/AirReqRsp.xsd --package travelport.models


.. code-block:: console
    :caption: Convert a remote schema

    $ xsdata http://www.gstatic.com/localfeed/local_feed.xsd --package feeds --print

.. code-block:: console
    :caption: Convert a remote xml file

    $ xsdata https://musicbrainz.org/ws/2/artist/1f9df192-a621-4f54-8850-2c5373b7eac9 --print


Output plugins
--------------

- `PlantUML <https://github.com/tefra/xsdata-plantuml>`_ class diagrams


Circular imports
----------------

Python is vulnerable to xsd circular imports. xsData by default groups all classes
by the schema location they are defined. This works well for schemas that avoid circular
imports. If you get import errors you should try one of the alternative structure
styles.

**clusters**

This style will identify the strongly connected classes and will group them together,
creating as many modules as possible. The modules are named after the the main class
of the group.

.. code-block:: console

    $ xsdata schema.xsd --package models --structure-style clusters


**namespaces**

This style will group classes by the target namespace they were originally defined. It
works well when the types of a namespace are spread across multiple schemas eg.
type substitutions, redefines.

.. code-block:: console

    $ xsdata schema.xsd --package models --structure-style namespaces


**single-package**

This style will group all classes together into a single package eliminating imports
altogether.

.. code-block:: console

    $ xsdata schema.xsd --package models --structure-style single-package


.. warning::

    Auto :ref:`locating types <Unknown xml target type>` during parsing might not work since
    all classes are bundled together under the same module namespace.


Initialize Config
=================

Initialize a project configuration with more advanced features, see
:ref:`more <Generator Config>`.

.. command-output:: xsdata init-config --help

.. code-block:: console

    $ xsdata amadeus/schemas --config amadeus/.xsdata.xml


Download Schemas
================

.. command-output:: xsdata download --help

.. admonition:: Examples
    :class: hint

    Check the :doc:`examples` and the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more ✨✨✨
