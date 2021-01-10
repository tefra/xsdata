from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import collections

Substitutions = Optional[Dict[str, List[Attr]]]


@dataclass
class AttributeSubstitutionHandler(HandlerInterface):
    """Apply substitution attributes to the given class recursively."""

    container: ContainerInterface
    substitutions: Substitutions = field(init=False, default=None)

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
        """
        index = target.attrs.index(attr)
        assert self.substitutions is not None

        for attr_type in attr.types:
            for substitution in self.substitutions.get(attr_type.qname, []):
                clone = ClassUtils.clone_attribute(substitution, attr.restrictions)

                pos = collections.find(target.attrs, clone)
                index = pos + 1 if pos > -1 else index
                target.attrs.insert(index, clone)

                self.process_attribute(target, clone)

    def create_substitutions(self):
        """Create reference attributes for all the classes substitutions and
        group them by their fully qualified name."""

        self.substitutions = defaultdict(list)
        for obj in self.container.iterate():
            for qname in obj.substitutions:
                attr = self.create_substitution(obj)
                self.substitutions[qname].append(attr)

    @classmethod
    def create_substitution(cls, source: Class) -> Attr:
        """Create an attribute with type that refers to the given source class
        and namespaced qualified name."""

        return Attr(
            name=source.name,
            types=[AttrType(qname=source.qname)],
            tag=source.tag,
            namespace=source.namespace,
        )
