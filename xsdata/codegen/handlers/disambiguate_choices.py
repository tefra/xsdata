from collections import defaultdict
from typing import Iterator

from xsdata.codegen.mixins import ContainerInterface, RelativeHandlerInterface
from xsdata.codegen.models import Attr, AttrType, Class, Extension, Restrictions
from xsdata.models.enums import DataType, Tag
from xsdata.utils import collections, text
from xsdata.utils.constants import DEFAULT_ATTR_NAME
from xsdata.utils.namespaces import build_qname


class DisambiguateChoices(RelativeHandlerInterface):
    """Process choices with the same types and disambiguate them.

    Essentially, this handler creates intermediate simple and complex
    types to ensure not two elements in a compound field can have the
    same type.

    Args:
        container: The class container instance

    Attributes:
        unnest_classes: Specifies whether to create intermediate
            inner or outer classes.
    """

    __slots__ = "unnest_classes"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)
        self.unnest_classes = container.config.output.unnest_classes

    def process(self, target: Class):
        """Process the given class attrs if they contain choices.

        Args:
            target: The target class instance
        """
        for attr in target.attrs:
            if attr.choices:
                self.process_compound_field(target, attr)

    def process_compound_field(self, target: Class, attr: Attr):
        """Process a compound field.

        A compound field can be created by a mixed wildcard with
        explicit children, or because we enabled the configuration
        to group repeatable choices.

        Steps:
            1. Merge choices derived from xs:any elements
            2. Find ambiguous choices and create intermediate classes
            3. Reset the attr types if it's not a mixed wildcard.


        Args:
            target: The target class instance
            attr: An attr instance that contains choices
        """
        self.merge_wildcard_choices(attr)

        for choice in self.find_ambiguous_choices(attr):
            self.disambiguate_choice(target, choice)

        if attr.tag == Tag.CHOICE:
            types = (tp for choice in attr.choices for tp in choice.types)
            attr.types = collections.unique_sequence(x.clone() for x in types)

    @classmethod
    def merge_wildcard_choices(cls, attr: Attr):
        """Merge choices derived from xs:any elements.

        It's a compound field it doesn't make sense
        to have multiple wildcard choices. Merge them
        together.

        Args:
            attr: The attr instance that contains choices
        """
        choices = []
        namespaces = []
        min_occurs = 0
        max_occurs = 0
        has_wildcard = False
        for choice in attr.choices:
            if choice.is_wildcard:
                min_occurs += choice.restrictions.min_occurs or 0
                max_occurs += choice.restrictions.max_occurs or 0
                namespaces.append(choice.namespace)
                has_wildcard = True
            else:
                choices.append(choice)

        attr.choices = choices

        if has_wildcard:
            attr.choices.append(
                Attr(
                    name="content",
                    types=[AttrType(qname=str(DataType.ANY_TYPE), native=True)],
                    tag=Tag.ANY,
                    namespace=" ".join(
                        collections.unique_sequence(filter(None, namespaces))
                    ),
                    restrictions=Restrictions(
                        min_occurs=min_occurs, max_occurs=max_occurs
                    ),
                )
            )

    @classmethod
    def find_ambiguous_choices(cls, attr: Attr) -> Iterator[Attr]:
        """Find choices with the same types.

        Args:
            attr: The attr instance with the choices.

        Yields:
            An iterator of the ambiguous choices, except wildcards.
        """
        groups = defaultdict(list)
        for index, choice in enumerate(attr.choices):
            for tp in choice.types:
                dt = tp.datatype
                if dt:
                    groups[dt.type.__name__].append(index)
                else:
                    groups[tp.qname].append(index)

        ambiguous = set()
        for indexes in groups.values():
            if len(indexes) > 1:
                ambiguous.update(indexes)

        for index in ambiguous:
            choice = attr.choices[index]
            if not choice.is_wildcard:
                yield choice

    def disambiguate_choice(self, target: Class, choice: Attr):
        """Create intermediate class for the given choice.

        Scenarios:
            1. Choice is derived from xs:anyType
            2. Choice is derived from a xs:anySimpleType
            3. Choice is a reference to xs:complexType or element

        Args:
            target: The target class instance
            choice: The ambiguous choice attr instance
        """
        is_circular = choice.is_circular_ref
        inner = not self.unnest_classes and not is_circular
        ref_class = self.create_ref_class(target, choice, inner=inner)

        if choice.is_any_type:
            self.add_any_type_value(ref_class, choice)
        elif self.is_simple_type(choice):
            self.add_simple_type_value(ref_class, choice)
        else:
            self.add_extension(ref_class, choice)

        choice.restrictions = Restrictions(
            min_occurs=choice.restrictions.min_occurs,
            max_occurs=choice.restrictions.max_occurs,
        )

        ref_type = AttrType(
            qname=ref_class.qname,
            reference=id(ref_class),
            forward=inner,
            circular=is_circular,
        )
        choice.types = [ref_type]
        if not inner:
            self.container.add(ref_class)
        else:
            target.inner.append(ref_class)

    def is_simple_type(self, choice: Attr) -> bool:
        """Return whether the choice attr is a simple type reference."""
        if any(tp.native for tp in choice.types):
            return True

        source = self.container.find(choice.types[0].qname)
        if source and source.is_enumeration:
            return True

        return False

    def create_ref_class(self, source: Class, choice: Attr, inner: bool) -> Class:
        """Create an intermediate class  for the given choice.

        If the reference class is going to be inner, ensure the class name is
        unique, otherwise we will still end-up with ambiguous choices.

        Args:
            source: The source class instance
            choice: The ambiguous choice attr instance
            inner: Specifies if the reference class will be inner
        """
        name = choice.name
        if inner:
            name = self.next_available_name(source, name)

        return Class(
            qname=build_qname(choice.namespace, name),
            status=source.status,
            tag=Tag.ELEMENT,
            local_type=True,
            location=source.location,
            ns_map=source.ns_map,
            nillable=choice.restrictions.nillable or False,
        )

    @classmethod
    def next_available_name(cls, parent: Class, name: str) -> str:
        """Find the next available name for an inner class.

        Args:
            parent: The parent class instance
            name: The name of the inner class

        Returns:
            The next available class name by adding a integer suffix.
        """
        reserved = {text.alnum(inner.name) for inner in parent.inner}
        index = 0
        new_name = name
        while True:
            cmp = text.alnum(new_name)

            if cmp not in reserved:
                return new_name

            index += 1
            new_name = f"{name}_{index}"

    @classmethod
    def add_any_type_value(cls, reference: Class, choice: Attr):
        """Add a simple any type content value attr to the reference class.

        Args:
            reference: The reference class instance
            choice: The source choice attr instance
        """
        attr = Attr(
            name="content",
            types=[AttrType(qname=str(DataType.ANY_TYPE), native=True)],
            tag=Tag.ANY,
            namespace=choice.namespace,
            restrictions=Restrictions(min_occurs=1, max_occurs=1),
        )
        reference.attrs.append(attr)

    @classmethod
    def add_simple_type_value(cls, reference: Class, choice: Attr):
        """Add a simple type content value attr to the reference class.

        Args:
            reference: The reference class instance
            choice: The source choice attr instance
        """
        new_attr = Attr(
            tag=Tag.EXTENSION,
            name=DEFAULT_ATTR_NAME,
            namespace=None,
            restrictions=choice.restrictions.clone(
                min_occurs=1,
                max_occurs=1,
                path=[],
                nillable=False,
            ),
            types=[tp.clone() for tp in choice.types],
        )
        reference.attrs.append(new_attr)

    @classmethod
    def add_extension(cls, reference: Class, choice: Attr):
        """Add an extension to the reference class from the choice type.

        Args:
            reference: The reference class instance
            choice: The source choice attr instance
        """
        extension = Extension(
            tag=Tag.EXTENSION,
            type=choice.types[0].clone(forward=False, circular=False),
            restrictions=Restrictions(),
        )
        reference.extensions.append(extension)
