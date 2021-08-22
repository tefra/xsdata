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
    ----------------------------------------------------------------------------------------------------------------
    XmlEventHandler-100           12.8919 (1.0)         15.9605 (1.0)         13.5307 (1.0)         13.2453 (1.0)
    LxmlEventHandler-100          13.8475 (1.07)        22.6515 (1.42)        14.6275 (1.08)        14.1368 (1.07)
    XmlEventHandler-1000         133.3028 (10.34)      140.0809 (8.78)       136.5462 (10.09)      136.9877 (10.34)
    LxmlEventHandler-1000        145.4640 (11.28)      160.6939 (10.07)      150.6386 (11.13)      150.8563 (11.39)
    XmlEventHandler-10000      1,356.8814 (105.25)   1,426.8625 (89.40)    1,388.2719 (102.60)   1,387.1983 (104.73)
    LxmlEventHandler-10000     1,432.3628 (111.11)   1,491.1179 (93.43)    1,451.6037 (107.28)   1,444.5362 (109.06)
    ----------------------------------------------------------------------------------------------------------------
