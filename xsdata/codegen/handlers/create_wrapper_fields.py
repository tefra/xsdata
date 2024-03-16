from typing import Optional

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr, AttrType, Class


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

        for attr in target.attrs:
            if self.validate_attr(attr):
                self.process_attr(target, attr)

    def process_attr(self, target: Class, attr: Attr):
        """Process the given attr instance.

        Args:
            target: The parent class instance
            attr: The attr instance to process
        """
        source = self.find_source(target, attr.types[0])
        if self.validate_source(source, attr.namespace):
            self.wrap_field(source.attrs[0], attr)

    @classmethod
    def wrap_field(cls, source: Attr, attr: Attr):
        """Create a wrapper field.

        Clone the source attr and update its name, local name and wrapper
        attributes.

        Args:
            source: The source attr instance
            attr: The attr instance to wrap
        """
        wrapper = attr.local_name

        attr.swap(source)
        attr.wrapper = wrapper

    def find_source(self, parent: Class, tp: AttrType) -> Class:
        """Find the source type for the given attr type instance.

        If it's a forward reference, look up the source in
        the parent class inners.

        Args:
            parent: The parent class instance
            tp: The attr type instance to look up

        Returns:
            The source class instance that matches the attr type.
        """
        if tp.forward:
            return self.container.find_inner(parent, tp.qname)

        return self.container.first(tp.qname)

    @classmethod
    def validate_attr(cls, attr: Attr) -> bool:
        """Validate if the attr can be converted to a wrapper field.

        Rules:
            1. Must be an element
            2. Must have only one type
            3. It has to be a user type
            4. The element can't be optional


        Args:
            attr: The attr instance to validate

        Returns:
            Whether the attr can be converted to a wrapper.

        """
        return (
            attr.is_element
            and len(attr.types) == 1
            and not attr.types[0].native
            and not attr.is_optional
        )

    @classmethod
    def validate_source(cls, source: Class, namespace: Optional[str]) -> bool:
        """Validate if the source class can be converted to a wrapper field.

        Rules:
            1. It must not have any extensions
            2. It must contain exactly one type
            3. It must not be a forward reference
            4. The source attr namespace must match the namespace


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
            and not source.attrs[0].is_forward_ref
            and ns_equal(source.attrs[0].namespace, namespace)
        )
