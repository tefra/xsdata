from xsdata.codegen.mixins import ContainerInterface, RelativeHandlerInterface
from xsdata.codegen.models import Attr, Class
from xsdata.models.config import UnwrapListType
from typing import Iterable, Tuple


class UnwrapLists(RelativeHandlerInterface):
    """Remove list wrapper elements."""

    __slots__ = "mode"

    mode: UnwrapListType

    def __init__(self, container: ContainerInterface):
        super().__init__(container)
        self.mode = container.config.output.wrapped_lists

    def process(self, target: Class):
        if self.mode is UnwrapListType.KEEP:
            return
        for attr, attr_type in self.itter_attributes(target):
            if len(attr_type.attrs) == 1 and len(attr_type.inner) == 1 and attr_type.attrs[0].is_list:
                self.unwrap_list(target, attr, attr_type)

    def itter_attributes(self, target: Class) -> Iterable[Tuple[Attr, Class]]:
        inners = {inner.qname: inner for inner in target.inner}
        for attribute in target.attrs.copy():
            if len(attribute.types) != 1:
                # TODO Check this logic
                continue
            inner = inners.get(attribute.types[0].qname, None)
            if inner is not None:
                yield attribute, inner

    def unwrap_list(self, target: Class, attr: Attr, attr_type: Class) -> None:
        wrapped_attribute = attr_type.attrs[0]
        wrapped_attribute.wrapper = attr.local_name

        if self.mode is UnwrapListType.OUTER_NAME:
            wrapped_attribute.name = attr.name

        position = target.inner.index(attr_type)
        target.inner[position] = attr_type.inner[0]
        position = target.attrs.index(attr)
        target.attrs[position] = wrapped_attribute