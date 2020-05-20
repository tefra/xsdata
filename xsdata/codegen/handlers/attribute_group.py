from dataclasses import dataclass

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.exceptions import AnalyzerError
from xsdata.models.codegen import Attr
from xsdata.models.codegen import Class
from xsdata.utils import text
from xsdata.utils.classes import ClassUtils


@dataclass
class AttributeGroupHandler(HandlerInterface):
    """Expand attribute groups with all source class attributes recursively."""

    container: ContainerInterface

    def process(self, target: Class):
        while any(attr.is_group for attr in target.attrs):
            for attr in list(target.attrs):
                if attr.is_group:
                    self.process_attribute(target, attr)

    def process_attribute(self, target: Class, attr: Attr):
        qname = target.source_qname(attr.name)
        source = self.container.find(qname)

        if not source:
            raise AnalyzerError(f"Group attribute not found: `{qname}`")

        if source is target:
            target.attrs.remove(attr)
        else:
            index = target.attrs.index(attr)
            target.attrs.pop(index)
            prefix = text.prefix(attr.name)

            for source_attr in source.attrs:
                clone = ClassUtils.clone_attribute(
                    source_attr, attr.restrictions, prefix
                )
                target.attrs.insert(index, clone)
                index += 1

            ClassUtils.copy_inner_classes(source, target)
