from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr, Class
from xsdata.codegen.utils import ClassUtils


class FlattenAttributeGroups(RelativeHandlerInterface):
    """Replace groups and attGroups with the source class attributes."""

    __slots__ = ()

    def process(self, target: Class):
        """Iterate over all group attributes and apply handler logic.

        Group attributes can refer to attributes or other group
        attributes, repeat until there is no group attribute left.

        Args:
            target: The target class instance to inspect and process
        """
        repeat = False
        for attr in list(target.attrs):
            if attr.is_group:
                repeat = True
                self.process_attribute(target, attr)

        if repeat:
            self.process(target)

    def process_attribute(self, target: Class, attr: Attr):
        """Process a group/attributeGroup attr.

        Steps:
            1. Find the source class by the attr type and tag
            2. If the attr is circular reference, remove the attr
            3. Otherwise, copy all source attrs to the target class

        Args:
            target: The target class instance
            attr: The group attr to flatten

        Raises:
            AnalyzerValueError: if source class is not found.
        """
        qname = attr.types[0].qname  # group attributes have one type only.
        source = self.container.find(qname, condition=lambda x: x.tag == attr.tag)

        if not source:
            raise CodegenError("Unknown group reference", tag=attr.tag, qname=qname)

        if source is target:
            ClassUtils.remove_attribute(target, attr)
        else:
            ClassUtils.copy_group_attributes(source, target, attr)
