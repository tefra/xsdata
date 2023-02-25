from collections import Counter
from collections import defaultdict
from typing import Dict
from typing import List

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


class CreateCompoundFields(RelativeHandlerInterface):
    """Group attributes that belong in the same choice and replace them by
    compound fields."""

    __slots__ = "config"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)

        self.config = container.config.output.compound_fields

    def process(self, target: Class):
        if self.config.enabled:
            groups = group_by(target.attrs, get_restriction_choice)
            for choice, attrs in groups.items():
                if choice and len(attrs) > 1:
                    self.group_fields(target, attrs)

        for index in range(len(target.attrs)):
            self.reset_sequence(target, index)

    def group_fields(self, target: Class, attrs: List[Attr]):
        """Group attributes into a new compound field."""
        pos = target.attrs.index(attrs[0])
        choice = attrs[0].restrictions.choice
        sum_occurs = choice and choice.startswith("effective_")

        names = []
        choices = []
        min_occurs_groups: Dict[int, int] = defaultdict(int)
        max_occurs_groups: Dict[int, int] = defaultdict(int)
        for attr in attrs:
            ClassUtils.remove_attribute(target, attr)
            names.append(attr.local_name)

            key = self.attr_group_key(attr)
            min_occurs_groups[key] += attr.restrictions.min_occurs or 0
            max_occurs_groups[key] += attr.restrictions.max_occurs or 0

            choices.append(self.build_attr_choice(attr))

        name = self.choose_name(target, names)
        min_occurs = min_occurs_groups.values()
        max_occurs = max_occurs_groups.values()

        target.attrs.insert(
            pos,
            Attr(
                name=name,
                index=0,
                types=[AttrType(qname=str(DataType.ANY_TYPE), native=True)],
                tag=Tag.CHOICE,
                restrictions=Restrictions(
                    min_occurs=sum(min_occurs) if sum_occurs else min(min_occurs),
                    max_occurs=sum(max_occurs) if sum_occurs else max(max_occurs),
                ),
                choices=choices,
            ),
        )

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

    def build_reserved_names(self, target: Class, names: List[str]) -> set[str]:
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
            default=attr.default,
            types=attr.types,
            tag=attr.tag,
            help=attr.help,
            restrictions=restrictions,
        )

    @classmethod
    def attr_group_key(cls, attr: Attr) -> int:
        return attr.restrictions.group or attr.restrictions.sequence or id(attr)

    @classmethod
    def reset_sequence(cls, target: Class, index: int):
        """Reset the attribute at the given index if it has no siblings with
        the sequence restriction."""

        attr = target.attrs[index]
        before = target.attrs[index - 1] if index - 1 >= 0 else None
        after = target.attrs[index + 1] if index + 1 < len(target.attrs) else None

        if not attr.is_list:
            attr.restrictions.sequence = None

        if (
            attr.restrictions.sequence is None
            or (before and before.restrictions.sequence is not None)
            or (after and after.restrictions.sequence is not None and after.is_list)
        ):
            return

        attr.restrictions.sequence = None
