from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import AnalyzerValueError


class FlattenAttributeGroups(RelativeHandlerInterface):
    """Replace groups and attGroups with the source class attributes."""

    __slots__ = ()

    def process(self, target: Class):
        """
        Iterate over all group attributes and apply handler logic.

        Group attributes can refer to attributes or other group
        attributes, repeat until there is no group attribute left.
        """
        repeat = False
        for attr in list(target.attrs):
            if attr.is_group:
                repeat = True
                self.process_attribute(target, attr)

        if repeat:
            self.process(target)

    def process_attribute(self, target: Class, attr: Attr):
        """
        Find the source class the attribute refers to and copy its attributes
        to the target class.

        :raises AnalyzerValueError: if source class is not found.
        """
        qname = attr.types[0].qname  # group attributes have one type only.
        source = self.container.find(qname, condition=lambda x: x.tag == attr.tag)

        if not source:
            raise AnalyzerValueError(f"Group attribute not found: `{qname}`")

        if source is target:
            ClassUtils.remove_attribute(target, attr)
        else:
            ClassUtils.copy_group_attributes(source, target, attr)
