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
    --------------------------------------------------------------------------------------------------------------
    LxmlEventWriter-100          19.5958 (1.0)         44.7400 (1.0)         21.9167 (1.0)         20.8375 (1.0)
    XmlEventWriter-100           20.0230 (1.02)        60.4467 (1.35)        23.9251 (1.09)        22.2102 (1.07)
    XmlEventWriter-1000         202.7945 (10.35)      219.1466 (4.90)       207.3766 (9.46)       204.9455 (9.84)
    LxmlEventWriter-1000        208.1190 (10.62)      238.5222 (5.33)       218.3315 (9.96)       210.8077 (10.12)
    LxmlEventWriter-10000     1,982.3172 (101.16)   2,075.0310 (46.38)    2,039.1569 (93.04)    2,038.3305 (97.82)
    XmlEventWriter-10000      2,041.9899 (104.21)   2,123.2829 (47.46)    2,073.9406 (94.63)    2,069.6950 (99.33)
    --------------------------------------------------------------------------------------------------------------
