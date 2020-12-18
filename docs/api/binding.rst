===========
Binding API
===========

The configuration offers more advance options to further tail the output to your needs,
like naming conventions and aliases.


Globals
-------

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    xsdata.formats.dataclass.context.XmlContext


Parsers
-------

.. currentmodule:: xsdata.formats.dataclass.parsers

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    XmlParser
    JsonParser
    config.ParserConfig


Generic Objects
---------------

.. currentmodule:: xsdata.formats.dataclass.models.generics

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    AnyElement
    DerivedElement


Parsing XML Nodes
-----------------

.. currentmodule:: xsdata.formats.dataclass.parsers.nodes

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    XmlNode
    ElementNode
    AnyTypeNode
    WildcardNode
    UnionNode
    PrimitiveNode


Serializers
-----------

.. currentmodule:: xsdata.formats.dataclass.serializers

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    XmlSerializer
    JsonSerializer
    config.SerializerConfig


Xml Handlers
------------

.. currentmodule:: xsdata.formats.dataclass.parsers.handlers

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    LxmlEventHandler
    LxmlSaxHandler
    XmlEventHandler
    XmlSaxHandler

.. currentmodule:: xsdata.formats.dataclass.parsers.mixins

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    XmlHandler


Xml Writers
------------

.. currentmodule:: xsdata.formats.dataclass.serializers.writers

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    LxmlEventWriter
    XmlEventWriter

.. currentmodule:: xsdata.formats.dataclass.serializers.mixins

.. autosummary::
    :toctree: ../reference
    :template: dataclass.rst
    :nosignatures:

    XmlWriter
