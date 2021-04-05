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

    $ xsdata air_v48_0/AirReqRsp.xsd rail_v48_0/RailReqRsp.xsd --package travelport.models


.. code-block:: console
    :caption: Convert a remote schema

    $ xsdata http://www.gstatic.com/localfeed/local_feed.xsd --package feeds --print

.. code-block:: console
    :caption: Convert a remote xml file

    $ xsdata https://musicbrainz.org/ws/2/artist/1f9df192-a621-4f54-8850-2c5373b7eac9 --print


Output plugins
--------------

- `PlantUML <https://github.com/tefra/xsdata-plantuml>`_ class diagrams


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
