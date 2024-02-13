from collections import defaultdict
from typing import Dict, List, Optional

from xsdata.codegen.mixins import ContainerInterface, RelativeHandlerInterface
from xsdata.codegen.models import Attr, AttrType, Class
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import Tag
from xsdata.utils import collections


class AddAttributeSubstitutions(RelativeHandlerInterface):
    """Apply substitution attributes to the given class recursively.

    Args:
        container: The class container instance

    Attributes:
        substitutions: Mapping of type names to attr values
    """

    __slots__ = "substitutions"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)
        self.substitutions: Optional[Dict[str, List[Attr]]] = None

    def process(self, target: Class):
        """Process the given class attrs for substitution groups.

        This method will ignore attrs in the class derived from
        a xs:enumeration, xs:anyType and xs:any. If this is the
        first time we call the method, build the substitution
        map.

        Args:
            target: The target class instance
        """
        if self.substitutions is None:
            self.create_substitutions()

        for attr in list(target.attrs):
            if not (attr.is_enumeration or attr.is_wildcard):
                self.process_attribute(target, attr)

    def process_attribute(self, target: Class, attr: Attr):
        """Add substitution attrs that refer to the attr type.

        If the given attr is referenced in substitution groups
        clone all substitution attrs and place them bellow
        the original attr. Convert all the attrs of the group
        to repeatable choice elements.

        Guard against multiple substitutions in case of xs:groups.

        Args:
            target: The target class instance
            attr: The source attr instance to check and process
        """
        index = target.attrs.index(attr)
        assert self.substitutions is not None

        for attr_type in attr.types:
            if attr_type.substituted:
                continue

            attr_type.substituted = True
            for substitution in self.substitutions.get(attr_type.qname, []):
                self.prepare_substituted(attr)

                clone = ClassUtils.clone_attribute(substitution, attr.restrictions)
                clone.restrictions.min_occurs = 0
                clone.restrictions.max_occurs = attr.restrictions.max_occurs

                attr.substitution = clone.substitution = attr_type.name

                pos = collections.find(target.attrs, clone)
                index = pos + 1 if pos > -1 else index
                target.attrs.insert(index, clone)

                self.process_attribute(target, clone)

    def create_substitutions(self):
        """Build the substitutions mapping of type names to attr values.

        The values are simple reference attrs that we can easily
        clone later on demand.
        """
        self.substitutions = defaultdict(list)
        for obj in self.container:
            for qname in obj.substitutions:
                attr = self.create_substitution(obj)
                self.substitutions[qname].append(attr)

    @classmethod
    def prepare_substituted(cls, attr: Attr):
        """Prepare the original attr for substitutions.

        Effectively place the attr inside a xs:choice container
        with min occurs zero.
        """
        attr.restrictions.min_occurs = 0
        if not attr.restrictions.choice:
            choice = id(attr)
            attr.restrictions.choice = choice
            attr.restrictions.path.append(("c", choice, 1, 1))

    @classmethod
    def create_substitution(cls, source: Class) -> Attr:
        """Create a reference attr to the source class qname.

        Args:
            source: The source class to reference

        Returns:
            The reference to the source class attr.
        """
        return Attr(
            name=source.name,
            types=[AttrType(qname=source.qname)],
            tag=Tag.ELEMENT,
            namespace=source.namespace,
        )
