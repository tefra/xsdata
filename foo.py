from enum import Enum

from xsdata.models.datatype import XmlDateTime, XmlDuration


class Foo(XmlDateTime, Enum):
    a = XmlDateTime.from_string("2010-09-20T13:00:00.000+01:00")


try:
    class YMdenumeration(XmlDuration, Enum):
        P1_Y = XmlDuration("P1Y")
        P1_Y3_M = XmlDuration("P1Y3M")
        P34_Y233_M = XmlDuration("-P34Y233M")
        P45_M = XmlDuration("P45M")
except TypeError as e:
    raise