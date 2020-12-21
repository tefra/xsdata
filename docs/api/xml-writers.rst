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


**Benchmarks**

.. code-block::

    Name (time in ms)                Min                   Max                  Mean                Median
    ------------------------------------------------------------------------------------------------------------
    LxmlEventWriter-100          12.3876 (1.0)         14.0231 (1.02)        12.7359 (1.00)        12.6545 (1.00)
    XmlEventWriter-100           12.4709 (1.01)        13.7136 (1.0)         12.7122 (1.0)         12.6516 (1.0)
    LxmlEventWriter-1000        121.3230 (9.79)       127.0393 (9.26)       123.3760 (9.71)       122.5806 (9.69)
    XmlEventWriter-1000         122.6532 (9.90)       125.3476 (9.14)       124.2966 (9.78)       124.6594 (9.85)
    LxmlEventWriter-10000     1,223.8570 (98.80)    1,234.0158 (89.98)    1,230.9853 (96.84)    1,232.9678 (97.46)
    XmlEventWriter-10000      1,228.0192 (99.13)    1,235.6687 (90.11)    1,232.3008 (96.94)    1,233.0478 (97.46)
    --------------------------------------------------------------------------------------------------------------
