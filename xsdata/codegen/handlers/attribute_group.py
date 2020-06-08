from dataclasses import dataclass

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.xsd import AttributeGroup
from xsdata.models.xsd import Group


@dataclass
class AttributeGroupHandler(HandlerInterface):
    """Replace attribute groups with the source class attributes."""

    container: ContainerInterface

    def process(self, target: Class):
        """
        Iterate over all group attributes and apply handler logic.

        Group attributes can refer to attributes or other group
        attributes, repeat until there is no group attribute left.
        """

        while any(attr.is_group for attr in target.attrs):
            for attr in list(target.attrs):
                if attr.is_group:
                    self.process_attribute(target, attr)

    def process_attribute(self, target: Class, attr: Attr):
        """
        Find the source class the attribute refers to and clone its attributes
        to the target class.

        The new attributes are placed in the position of original group
        attribute.
        """
        qname = target.source_qname(attr.name)
        source = self.container.find(
            qname, condition=lambda x: x.type in (AttributeGroup, Group)
        )

        if not source:
            raise AnalyzerValueError(f"Group attribute not found: `{qname}`")

        if source is target:
            target.attrs.remove(attr)
        else:
            ClassUtils.copy_group_attributes(source, target, attr)
