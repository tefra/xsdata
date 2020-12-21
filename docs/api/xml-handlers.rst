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

    Name (time in ms)               Min                   Max                  Mean                Median
    --------------------------------------------------------------------------------------------------------------
    LxmlEventHandler-100         9.1831 (1.0)         10.0212 (1.0)          9.3678 (1.0)          9.3246 (1.0)
    XmlEventHandler-100          9.3700 (1.02)        10.4110 (1.04)         9.5449 (1.02)         9.4944 (1.02)
    LxmlSaxHandler-100          10.9592 (1.19)        12.4429 (1.24)        11.1885 (1.19)        11.0935 (1.19)
    XmlSaxHandler-100           13.1215 (1.43)        14.0672 (1.40)        13.4060 (1.43)        13.3534 (1.43)
    LxmlEventHandler-1000       91.5178 (9.97)        93.6739 (9.35)        92.3735 (9.86)        92.1866 (9.89)
    XmlEventHandler-1000        92.7241 (10.10)       97.5819 (9.74)        94.0311 (10.04)       93.7171 (10.05)
    LxmlSaxHandler-1000        106.6704 (11.62)      110.6747 (11.04)      108.3380 (11.56)      108.2407 (11.61)
    XmlSaxHandler-1000         131.2831 (14.30)      133.0032 (13.27)      132.3303 (14.13)      132.4381 (14.20)
    LxmlEventHandler-10000     926.6736 (100.91)     938.2561 (93.63)      931.3415 (99.42)      930.3376 (99.77)
    XmlEventHandler-10000      936.2768 (101.96)     944.1380 (94.21)      939.8639 (100.33)     938.3422 (100.63)
    LxmlSaxHandler-10000     1,096.1053 (119.36)   1,109.3193 (110.70)   1,103.2988 (117.78)   1,104.0933 (118.41)
    XmlSaxHandler-10000      1,338.3855 (145.75)   1,350.9106 (134.81)   1,347.0401 (143.79)   1,348.2108 (144.59)
    --------------------------------------------------------------------------------------------------------------
