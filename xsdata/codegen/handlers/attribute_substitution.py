from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional

from lxml.etree import QName

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils


Substitutions = Optional[Dict[QName, List[Attr]]]


@dataclass
class AttributeSubstitutionHandler(HandlerInterface):
    """
    Apply substitution attributes to the given class recursively.

    Substitution attributes are placed below the attribute the are
    supposed to substitute. Exclude enumerations and wildcard attributes
    from the process.
    """

    container: ContainerInterface
    substitutions: Substitutions = field(init=False, default=None)

    def process(self, target: Class):
        if self.substitutions is None:
            self.create_substitutions()

        for attr in list(target.attrs):
            if not (attr.is_enumeration or attr.is_wildcard):
                self.process_attribute(target, attr)

    def process_attribute(self, target: Class, attr: Attr):
        index = target.attrs.index(attr)
        qname = target.source_qname(attr.name)

        assert self.substitutions is not None

        for substitution in self.substitutions.get(qname, []):
            pos = ClassUtils.find_attribute(target.attrs, substitution)
            index = pos + 1 if pos > -1 else index

            clone = substitution.clone()
            clone.restrictions.merge(attr.restrictions)
            target.attrs.insert(index, clone)

            self.process_attribute(target, clone)

    def create_substitutions(self):
        """Create reference attributes for all the classes substitutions and
        group them by their fully qualified name."""

        self.substitutions = defaultdict(list)
        for obj in self.container.iterate():
            for substitution in obj.substitutions:
                obj.abstract = False
                qname = obj.source_qname(substitution)
                attr = self.create_substitution(obj, qname)
                self.substitutions[qname].append(attr)

    @classmethod
    def create_substitution(cls, source: Class, qname: QName) -> Attr:
        """Create an attribute with type that refers to the given source class
        and namespaced qualified name."""
        prefix = None
        if qname.namespace != source.source_namespace:
            prefix = source.source_prefix

        reference = f"{prefix}:{source.name}" if prefix else source.name
        return Attr(
            name=source.name,
            local_name=source.name,
            index=0,
            default=None,
            types=[AttrType(name=reference)],
            tag=source.type.__name__,
            namespace=source.namespace,
        )
