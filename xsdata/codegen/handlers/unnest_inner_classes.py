from typing import Optional

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr, Class
from xsdata.utils.namespaces import build_qname


class UnnestInnerClasses(RelativeHandlerInterface):
    """Promote inner classes to root classes."""

    __slots__ = ()

    def process(self, target: Class):
        """Process entrypoint for classes.

        Process the target class inner classes recursively.

        All enumerations are promoted by default, otherwise
        only if the configuration is disabled the classes
        are ignored.

        Args:
            target: The target class instance to inspect
        """
        for inner in list(target.inner):
            if inner.is_enumeration or self.container.config.output.unnest_classes:
                self.promote(target, inner)

    def promote(self, target: Class, inner: Class):
        """Promote the inner class to root classes.

        Steps:
            - Replace forward references to the inner class
            - Remove inner class from target class
            - Copy the class to the global class container.

        Args:
            target: The target class
            inner: An inner class
        """
        target.inner.remove(inner)
        attr = self.find_forward_attr(target, inner.qname)
        if attr:
            clone = self.clone_class(inner, target.name)
            self.update_types(attr, inner.qname, clone)
            self.container.add(clone)

    @classmethod
    def clone_class(cls, inner: Class, name: str) -> Class:
        """Clone and prepare inner class for promotion.

        Clone the inner class, mark it as promoted and pref
        the qualified name with the parent class name.

        Args:
            inner: The inner class to clone and prepare
            name: The parent class name to use a prefix

        Returns:
            The new class instance
        """
        clone = inner.clone()
        clone.local_type = True
        clone.qname = build_qname(inner.target_namespace, f"{name}_{inner.name}")

        for attr in clone.attrs:
            for tp in attr.types:
                if tp.circular and tp.qname == inner.qname:
                    tp.qname = clone.qname
                    tp.reference = clone.ref

        return clone

    @classmethod
    def update_types(cls, attr: Attr, search: str, source: Class):
        """Update the references from an inner to a global class.

        Args:
            attr: The target attr to inspect and update
            search: The current inner class qname
            source: The new global class qname
        """
        for attr_type in attr.types:
            if attr_type.qname == search and attr_type.forward:
                attr_type.qname = source.qname
                attr_type.reference = source.ref
                attr_type.forward = False

    @classmethod
    def find_forward_attr(cls, target: Class, qname: str) -> Optional[Attr]:
        """Find the first attr that references the given inner class qname.

        Args:
            target: The target class instance
            qname: An inner class qualified name

        Returns:
            Attr: The first attr that references the given qname
            None: If no such attr exists, it can happen!
        """
        for attr in target.attrs:
            for attr_type in attr.types:
                if attr_type.forward and attr_type.qname == qname:
                    return attr

        return None
