import abc
from typing import Callable
from typing import Iterator
from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.codegen.models import Class

Condition = Optional[Callable]


class ContainerInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def iterate(self) -> Iterator[Class]:
        raise NotImplementedError

    @abc.abstractmethod
    def find(self, qname: QName, condition: Condition = None) -> Optional[Class]:
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, item: Class):
        raise NotImplementedError

    @abc.abstractmethod
    def extend(self, items: List[Class]):
        raise NotImplementedError


class HandlerInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def process(self, target: Class):
        raise NotImplementedError
