from collections import Counter
from typing import Dict
from typing import List
from typing import Set
from typing import Tuple

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_restriction_choice
from xsdata.codegen.models import Restrictions
from xsdata.codegen.utils import ClassUtils
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.collections import group_by

ALL = "a"
GROUP = "g"
SEQUENCE = "s"
CHOICE = "c"


class CreateCompoundFields(RelativeHandlerInterface):
    """Group attributes that belong in the same choice and replace them by
    compound fields."""

    __slots__ = "config"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)

        self.config = container.config.output.compound_fields

    def process(self, target: Class):
        groups = group_by(target.attrs, get_restriction_choice)
        for choice, attrs in groups.items():
            if choice and len(attrs) > 1:
                if self.config.enabled:
                    self.group_fields(target, attrs)
                else:
                    self.calculate_choice_min_occurs(attrs)

    @classmethod
    def calculate_choice_min_occurs(cls, attrs: List[Attr]):
        for attr in attrs:
            for path in attr.restrictions.path:
                name, index, mi, ma = path
                if name == CHOICE and mi <= 1:
                    attr.restrictions.min_occurs = 0

    @classmethod
    def update_counters(cls, attr: Attr, counters: Dict):
        started = False
        choice = attr.restrictions.choice
        for path in attr.restrictions.path:
            name, index, mi, ma = path
            if not started and name != CHOICE and index != choice:
                continue

            started = True
            if path not in counters:
                counters[path] = {"min": [], "max": []}
            counters = counters[path]

            if mi <= 1:
                attr.restrictions.min_occurs = 0

        counters["min"].append(attr.restrictions.min_occurs)
        counters["max"].append(attr.restrictions.max_occurs)

    def group_fields(self, target: Class, attrs: List[Attr]):
        """Group attributes into a new compound field."""
        pos = target.attrs.index(attrs[0])
        choice = attrs[0].restrictions.choice

        assert choice is not None

        names = []
        choices = []
        counters: Dict = {"min": [], "max": []}

        for attr in attrs:
            ClassUtils.remove_attribute(target, attr)
            names.append(attr.local_name)
            choices.append(self.build_attr_choice(attr))

            self.update_counters(attr, counters)

        min_occurs, max_occurs = self.sum_counters(counters)
        name = self.choose_name(target, names)

        target.attrs.insert(
            pos,
            Attr(
                name=name,
                index=0,
                types=[AttrType(qname=str(DataType.ANY_TYPE), native=True)],
                tag=Tag.CHOICE,
                restrictions=Restrictions(
                    min_occurs=sum(min_occurs),
                    max_occurs=max(max_occurs) if choice > 0 else sum(max_occurs),
                ),
                choices=choices,
            ),
        )

    def sum_counters(self, counters: Dict) -> Tuple[List[int], List[int]]:
        min_occurs = counters.pop("min", [])
        max_occurs = counters.pop("max", [])

        for path, counter in counters.items():
            mi, ma = self.sum_counters(counter)

            if path[0] == "c":
                min_occurs.append(min(mi))
                max_occurs.append(max(ma))
            else:
                min_occurs.append(sum(mi))
                max_occurs.append(sum(ma))

        return min_occurs, max_occurs

    def choose_name(self, target: Class, names: List[str]) -> str:
        if (
            self.config.force_default_name
            or len(names) > 3
            or len(names) != len(set(names))
        ):
            name = self.config.default_name
        else:
            name = "_Or_".join(names)

        reserved = self.build_reserved_names(target, names)
        return ClassUtils.unique_name(name, reserved)

    def build_reserved_names(self, target: Class, names: List[str]) -> Set[str]:
        names_counter = Counter(names)
        all_attrs = self.base_attrs(target)
        all_attrs.extend(target.attrs)

        return {
            attr.slug
            for attr in all_attrs
            if attr.xml_type != XmlType.ELEMENTS
            or Counter([x.local_name for x in attr.choices]) != names_counter
        }

    @classmethod
    def build_attr_choice(cls, attr: Attr) -> Attr:
        """
        Converts the given attr to a choice.

        The most important part is the reset of certain restrictions
        that don't make sense as choice metadata like occurrences.
        """
        restrictions = attr.restrictions.clone()
        restrictions.min_occurs = None
        restrictions.max_occurs = None
        restrictions.sequence = None

        return Attr(
            name=attr.local_name,
            namespace=attr.namespace,
            types=attr.types,
            tag=attr.tag,
            help=attr.help,
            restrictions=restrictions,
        )
