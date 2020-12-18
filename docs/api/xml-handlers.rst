============
XML Handlers
============

XmlHandlers read the xml source and push build events to create the target class.
xsData ships with multiple handlers based on lxml and native python that vary in
performance and features.

.. currentmodule:: xsdata.formats.dataclass.parsers.handlers

.. autosummary::
    :toctree: reference
    :template: dataclass.rst
    :nosignatures:

    LxmlEventHandler
    LxmlSaxHandler
    XmlEventHandler
    XmlSaxHandler

.. currentmodule:: xsdata.formats.dataclass.parsers.mixins

.. autosummary::
    :toctree: reference
    :template: dataclass.rst
    :nosignatures:

    XmlHandler
