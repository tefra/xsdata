from dataclasses import dataclass
from typing import Optional
from typing import Set

from xsdata.codegen.mixins import ClassHandlerInterface
from xsdata.codegen.mixins import ContainerInterface
from xsdata.logger import logger
from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.utils.classes import ClassUtils
from xsdata.utils.collections import unique_sequence


def simple_cond(candidate: Class) -> bool:
    return (
        not candidate.is_enumeration
        and not candidate.is_complex
        and len(candidate.attrs) < 2
    )


@dataclass
class AttributeTypeClassHandler(ClassHandlerInterface):
    """
    Reduce attribute types by merging simple types in order to reduce
    complexity at the cost of repeating definitions.

    Fix circular de

    Notes:
        * xs:pattern is not yet supported reset all native types to xs:string.
        * skip over forward references aka inner classes.
        * Copy all parent extensions if class is enumeration.
    """

    container: ContainerInterface

    def process(self, target: Class):
        for attr in list(target.attrs):
            self.process_attribute(target, attr)

    def process_attribute(self, target: Class, attr: Attr):
        """
        Iterate over the given attribute types and process only external
        references.

        Notes:
            1. native types should be left alone.
            2. xs:pattern is not yet supported reset type to xs:string.
            3. skip forward references aka inner classes.
            4. filter duplicate types by name.
        """

        for current_type in list(attr.types):
            if current_type.native:
                if attr.restrictions.pattern:
                    ClassUtils.reset_attribute_type(current_type)
            elif not current_type.forward:
                self.process_attribute_type(target, attr, current_type)

        attr.types = unique_sequence(attr.types, key="name")

    def process_attribute_type(self, target: Class, attr: Attr, attr_type: AttrType):
        """Flatten attribute type if it's a simple type otherwise check for
        circular reference or missing type."""

        qname = target.source_qname(attr_type.name)
        circular = attr_type.circular
        simple_source = None if circular else self.container.find(qname, simple_cond)
        complex_source = None if simple_source else self.container.find(qname)

        if simple_source:
            self.merge_attribute_type(simple_source, target, attr, attr_type)
        elif complex_source:
            attr_type.circular = self.is_circular_dependency(complex_source, target)
        elif not circular:
            logger.warning("Missing type: %s", attr_type.name)
            ClassUtils.reset_attribute_type(attr_type)

    def is_circular_dependency(
        self, source: Class, target: Class, seen: Optional[Set] = None
    ) -> bool:
        """Check if any source dependencies recursively match the target
        class."""

        if source is target:
            return True

        seen = seen or set()
        for qname in source.dependencies():

            if qname in seen:
                continue

            seen.add(qname)
            check = self.container.find(qname)
            if check and self.is_circular_dependency(check, target, seen):
                return True

        return False

    @classmethod
    def merge_attribute_type(
        cls, source: Class, target: Class, attr: Attr, attr_type: AttrType
    ):
        """
        Replace the given attribute type with the types of the single field
        source class.

        If the source class has more than one or no fields a warning
        will be logged and the target attribute type will change to
        simple string.
        """
        if len(source.attrs) != 1:
            logger.warning("Missing implementation: %s", source.type.__name__)
            ClassUtils.reset_attribute_type(attr_type)
        else:
            source_attr = source.attrs[0]
            index = attr.types.index(attr_type)
            attr.types.pop(index)

            for source_attr_type in source_attr.types:
                clone_type = source_attr_type.clone()
                attr.types.insert(index, clone_type)
                index += 1

            restrictions = source_attr.restrictions.clone()
            restrictions.merge(attr.restrictions)
            attr.restrictions = restrictions
            ClassUtils.copy_inner_classes(source, target)
