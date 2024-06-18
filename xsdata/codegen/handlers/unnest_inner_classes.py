from collections import defaultdict
from typing import Iterator, List, Tuple

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import AttrType, Class
from xsdata.codegen.utils import ClassUtils
from xsdata.utils.namespaces import build_qname


class UnnestInnerClasses(RelativeHandlerInterface):
    """Promote inner classes to root classes."""

    __slots__ = ()

    def process(self, target: Class):
        """Promote all inner classes recursively.

        Args:
            target: The target class instance to process
        """
        inner_classes = {}
        inner_references = defaultdict(list)
        promote_all = self.container.config.output.unnest_classes
        for attr_type, source in self.find_forward_refs(target):
            inner = ClassUtils.find_nested(source, attr_type.qname)

            if not (promote_all or inner.is_enumeration):
                continue

            inner_classes[inner.ref] = inner
            inner_references[inner.ref].append(attr_type)

        for ref, inner in inner_classes.items():
            references = inner_references[ref]

            self.update_inner_class(inner)
            self.update_types(references, inner.qname)
            self.container.add(inner)

        self.remove_orphan_inner_classes(target, promote_all)

    @classmethod
    def remove_orphan_inner_classes(cls, target: Class, promote_all: bool):
        """Remove inner classes with no attr references.

        Args:
            target: The target class instance to process
            promote_all: Whether to remove all inner classes or just the enumerations
        """
        for inner in target.inner.copy():
            if promote_all or inner.is_enumeration:
                target.inner.remove(inner)

    @classmethod
    def find_forward_refs(cls, target: Class) -> Iterator[Tuple[AttrType, Class]]:
        """Find all forward references for all inner classes.

        Args:
            target: The target class instance to process

        Yields:
            A tuple of attr type and the parent class instance.
        """
        for attr in target.attrs:
            for tp in attr.types:
                if tp.forward and not tp.native:
                    yield tp, target

        for inner in target.inner:
            yield from cls.find_forward_refs(inner)

    @classmethod
    def update_inner_class(cls, target: Class):
        """Prepare the nested class to be added as root.

        Args:
            target: The target class
        """
        assert target.parent is not None
        name_parts = [target.parent.name, target.name]
        new_qname = build_qname(target.target_namespace, "_".join(name_parts))

        target.qname = new_qname

        assert target.parent is not None

        target.parent.inner.remove(target)
        target.parent = None
        target.local_type = True

    @classmethod
    def update_types(cls, types: List[AttrType], qname: str):
        """Search and replace forward references.

        Return the number changes.

        Args:
            types: The types to search and replace
            qname: The updated qname
        """
        for tp in types:
            tp.qname = qname
            tp.forward = False
