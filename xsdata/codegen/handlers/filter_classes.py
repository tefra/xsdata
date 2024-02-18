from typing import List

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Class
from xsdata.logger import logger


class FilterClasses(ContainerHandlerInterface):
    """Filter classes for code generation based on the configuration strategy."""

    __slots__ = ()

    def run(self):
        """Main entrypoint to filter the class container.

        In order for a class to be considered global it has
        to be derived from an element, complexType, a binding
        operation or message

        If no global types exist, all classes will be generated.
        """
        classes = self.filter_all_globals()
        if classes:
            self.container.set(classes)
        else:
            logger.warning("No global types exist, will generate all types.")

    def filter_all_globals(self) -> List[Class]:
        """Filter all globals and any referenced types.

        This filter is trying to remove unused simple
        types.

        Returns:
            The list of classes for generation.
        """
        occurs = set()
        for obj in self.container:
            if obj.is_complex_type:
                occurs.add(obj.ref)
                occurs.update(obj.references)

        return [obj for obj in self.container if obj.ref in occurs]
