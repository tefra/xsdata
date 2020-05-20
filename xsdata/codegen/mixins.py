import abc
from typing import Callable
from typing import Iterator
from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.models.codegen import Class


class ContainerInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def iterate(self) -> Iterator[Class]:
        raise NotImplementedError

    @abc.abstractmethod
    def find(
        self, qname: QName, condition: Optional[Callable] = None
    ) -> Optional[Class]:
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, item: Class):
        raise NotImplementedError

    @abc.abstractmethod
    def extend(self, items: List[Class]):
        raise NotImplementedError


class ClassHandlerInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def process(self, target: Class):
        raise NotImplementedError
