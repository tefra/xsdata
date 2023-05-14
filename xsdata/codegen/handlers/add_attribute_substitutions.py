from collections import defaultdict
from typing import Dict
from typing import List
from typing import Optional

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import Tag
from xsdata.utils import collections


class AddAttributeSubstitutions(RelativeHandlerInterface):
    """Apply substitution attributes to the given class recursively."""

    __slots__ = "substitutions"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)
        self.substitutions: Optional[Dict[str, List[Attr]]] = None

    def process(self, target: Class):
        """
        Search and process attributes not derived from xs:enumeration or
        xs:any.

        Build the substitutions map if it's not initialized yet.
        """
        if self.substitutions is None:
            self.create_substitutions()

        for attr in list(target.attrs):
            if not (attr.is_enumeration or attr.is_wildcard):
                self.process_attribute(target, attr)

    def process_attribute(self, target: Class, attr: Attr):
        """
        Check if the given attribute matches any substitution class in order to
        clone it's attributes to the target class.

        The cloned attributes are placed below the attribute the are
        supposed to substitute.

        Guard against multiple substitutions in case of xs:groups.
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

                pos = collections.find(target.attrs, clone)
                index = pos + 1 if pos > -1 else index
                target.attrs.insert(index, clone)

                self.process_attribute(target, clone)

    def create_substitutions(self):
        """Create reference attributes for all the classes substitutions and
        group them by their fully qualified name."""

        self.substitutions = defaultdict(list)
        for obj in self.container:
            for qname in obj.substitutions:
                attr = self.create_substitution(obj)
                self.substitutions[qname].append(attr)

    @classmethod
    def prepare_substituted(cls, attr: Attr):
        attr.restrictions.min_occurs = 0
        if not attr.restrictions.choice:
            choice = id(attr)
            attr.restrictions.choice = choice
            attr.restrictions.path.append(("c", choice, 1, 1))

    @classmethod
    def create_substitution(cls, source: Class) -> Attr:
        """Create an attribute with type that refers to the given source class
        and namespaced qualified name."""

        return Attr(
            name=source.name,
            types=[AttrType(qname=source.qname)],
            tag=Tag.ELEMENT,
            namespace=source.namespace,
        )
