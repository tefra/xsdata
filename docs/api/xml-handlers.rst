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


**Benchmarks**

.. code-block::

    Name (time in ms)                 Min                   Max                  Mean                Median
    ----------------------------------------------------------------------------------------------------------------
    XmlEventHandler-100           15.5117 (1.0)         25.2867 (1.05)        18.1108 (1.03)        17.4573 (1.02)
    LxmlEventHandler-100          16.1423 (1.04)        24.5722 (1.02)        17.5419 (1.0)         17.1829 (1.0)
    LxmlSaxHandler-100            19.4828 (1.26)        24.5199 (1.02)        21.4798 (1.22)        21.4161 (1.25)
    XmlSaxHandler-100             22.0499 (1.42)        24.0960 (1.0)         22.7615 (1.30)        22.7022 (1.32)
    XmlEventHandler-1000         164.0717 (10.58)      174.3340 (7.23)       169.8387 (9.68)       170.5508 (9.93)
    LxmlEventHandler-1000        171.7118 (11.07)      183.6858 (7.62)       177.2971 (10.11)      177.2766 (10.32)
    LxmlSaxHandler-1000          201.8185 (13.01)      214.4356 (8.90)       208.1227 (11.86)      208.3414 (12.12)
    XmlSaxHandler-1000           223.9293 (14.44)      241.8015 (10.03)      234.8391 (13.39)      237.8538 (13.84)
    XmlEventHandler-10000      1,687.5738 (108.79)   1,717.7587 (71.29)    1,702.0942 (97.03)    1,704.4335 (99.19)
    LxmlEventHandler-10000     1,720.5759 (110.92)   1,763.5875 (73.19)    1,740.5879 (99.22)    1,738.3820 (101.17)
    LxmlSaxHandler-10000       2,105.8143 (135.76)   2,178.7946 (90.42)    2,143.9545 (122.22)   2,141.1028 (124.61)
    XmlSaxHandler-10000        2,321.4368 (149.66)   2,430.4984 (100.87)   2,370.5923 (135.14)   2,373.6413 (138.14)
    ----------------------------------------------------------------------------------------------------------------
