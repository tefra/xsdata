===========
XML Writers
===========

xsData ships with multiple writers based on lxml and native python that may vary
in performance in some cases. The output of all them is consistent with a few
exceptions when handling mixed content with ``pretty_print=True``.

.. currentmodule:: xsdata.formats.dataclass.serializers.writers

.. autosummary::
    :toctree: reference
    :template: dataclass.rst
    :nosignatures:

    LxmlEventWriter
    XmlEventWriter

.. currentmodule:: xsdata.formats.dataclass.serializers.mixins

.. autosummary::
    :toctree: reference
    :template: dataclass.rst
    :nosignatures:

    XmlWriter
