from typing import List

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Class
from xsdata.logger import logger
from xsdata.models.config import ClassFilterStrategy


class FilterClasses(ContainerHandlerInterface):
    """Filter classes for code generation based on the configuration strategy."""

    __slots__ = ()

    def run(self):
        """Main entrypoint to filter the class container.

        In order for a class to be considered global it has
        to be a non-abstract element, a complex type without
        simple content or a wsdl binding element.

        Strategies:
            - Filter all global classes and the referenced simple types.
            - Filter global classes with references to other global classes.
            - Filter all classes
        """
        classes = []
        filter_strategy = self.container.config.output.filter_strategy
        if filter_strategy == ClassFilterStrategy.ALL_GLOBALS:
            classes = self.filter_all_globals()
        elif filter_strategy == ClassFilterStrategy.REFERRED_GLOBALS:
            classes = self.filter_referred_globals()

        if classes:
            self.container.set(classes)
        elif filter_strategy != ClassFilterStrategy.ALL:
            logger.warning(
                "The filter strategy '%s' returned no classes,"
                " will generate all types.",
                filter_strategy.value,
            )

    def filter_all_globals(self) -> List[Class]:
        """Filter all globals and any referenced types.

        This filter is trying to remove unused simple
        types.

        Returns:
            The list of classes for generation.
        """
        occurs = set()
        for obj in self.container:
            if obj.is_global_type:
                occurs.add(obj.ref)
                occurs.update(obj.references)

        return [obj for obj in self.container if obj.ref in occurs]

    def filter_referred_globals(self) -> List[Class]:
        """Filter globals with any references.

        This filter is trying to remove unused global
        types.

        Returns:
            The list of classes for generation.
        """
        occurs = set()
        for obj in self.container:
            if obj.is_global_type:
                references = list(obj.references)
                occurs.update(references)
                if references:
                    occurs.add(obj.ref)

        return [obj for obj in self.container if obj.ref in occurs]
