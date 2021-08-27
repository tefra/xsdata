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
    XmlEventHandler

.. currentmodule:: xsdata.formats.dataclass.parsers.mixins

.. autosummary::
    :toctree: reference
    :template: dataclass.rst
    :nosignatures:

    XmlHandler


**Benchmarks**

.. code-block::

    Name (time in ms)                 Min                   Max                  Mean                Median
    ----------------------------------------------------------------------------------------------------------------
    XmlEventHandler-100           15.5117 (1.0)         25.2867 (1.05)        18.1108 (1.03)        17.4573 (1.02)
    LxmlEventHandler-100          16.1423 (1.04)        24.5722 (1.02)        17.5419 (1.0)         17.1829 (1.0)
    XmlEventHandler-1000         164.0717 (10.58)      174.3340 (7.23)       169.8387 (9.68)       170.5508 (9.93)
    LxmlEventHandler-1000        171.7118 (11.07)      183.6858 (7.62)       177.2971 (10.11)      177.2766 (10.32)
    XmlEventHandler-10000      1,687.5738 (108.79)   1,717.7587 (71.29)    1,702.0942 (97.03)    1,704.4335 (99.19)
    LxmlEventHandler-10000     1,720.5759 (110.92)   1,763.5875 (73.19)    1,740.5879 (99.22)    1,738.3820 (101.17)
    ----------------------------------------------------------------------------------------------------------------
