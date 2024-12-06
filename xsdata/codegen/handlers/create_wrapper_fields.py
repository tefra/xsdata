from typing import Optional

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr, Class
from xsdata.codegen.utils import ClassUtils


class CreateWrapperFields(RelativeHandlerInterface):
    """Create wrapper fields.

    Args:
        container: The class container instance
    """

    def process(self, target: Class):
        """Process the given class attrs and choices.

        Args:
            target: The target class instance
        """
        if not self.container.config.output.wrapper_fields:
            return

        wrapped = False
        wrapped_inner = False
        for attr in target.attrs:
            if not self.validate_attr(attr):
                continue

            inner, source = self.find_source_attr(target, attr)
            if not source:
                continue

            self.wrap_field(source, attr, inner)
            wrapped = True
            wrapped_inner = wrapped_inner or inner

        if wrapped:
            ClassUtils.rename_duplicate_attributes(target)

            if inner:
                ClassUtils.clean_inner_classes(target)

    @classmethod
    def wrap_field(cls, source: Attr, attr: Attr, inner: bool):
        """Create a wrapper field.

        Clone the source attr and update its name, local name and wrapper
        attributes.

        Args:
            source: The source attr instance
            attr: The attr instance to wrap
            inner: Specify if the source is from an inner class
        """
        wrapper = attr.local_name

        attr.swap(source)
        attr.wrapper = wrapper
        attr.types[0].forward = False

    def find_source_attr(
        self, parent: Class, attr: Attr
    ) -> tuple[bool, Optional[Attr]]:
        """Find the source type for the given attr type instance.

        If it's a forward reference, look up the source in
        the parent class inners.

        Args:
            parent: The parent class instance
            attr: The attr instance to find a valid source attr

        Returns:
            A tuple of whether the source attr is inner and the source attr.
        """
        tp = attr.types[0]
        inner = False
        if tp.forward:
            source = self.container.find_inner(parent, tp.qname)
            inner = True
        else:
            source = self.container.first(tp.qname)

        if self.validate_source(source, attr.namespace):
            return inner, source.attrs[0]

        return inner, None

    @classmethod
    def validate_attr(cls, attr: Attr) -> bool:
        """Validate if the attr can be converted to a wrapper field.

        Rules:
            1. Must be an element
            2. Must have only one user type
            4. The element can't be optional
            5. The element can't be a list element

        Args:
            attr: The attr instance to validate

        Returns:
            Whether the attr can be converted to a wrapper.
        """
        return (
            attr.is_element
            and len(attr.types) == 1
            and not attr.types[0].native
            and not attr.is_list
            and not attr.is_optional
        )

    @classmethod
    def validate_source(cls, source: Class, namespace: Optional[str]) -> bool:
        """Validate if the source class can be converted to a wrapper field.

        Rules:
            1. It must not have any extensions
            2. It must contain exactly one type
            3. It must be derived from a xs:element
            4. It must not be optional
            5. It must not be a forward reference
            6. The source attr namespace must match the namespace

        Args:
            source: The source class instance to validate
            namespace: The processing attr namespace

        Returns:
            Whether the source class can be converted to a wrapper.
        """

        def ns_equal(a: Optional[str], b: Optional[str]):
            return (a or "") == (b or "")

        return (
            not source.extensions
            and len(source.attrs) == 1
            and source.attrs[0].is_element
            and not source.attrs[0].is_optional
            and not source.attrs[0].is_forward_ref
            and ns_equal(source.attrs[0].namespace, namespace)
        )
