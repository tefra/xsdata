from collections import Counter
from typing import Dict, List, Set, Tuple

from xsdata.codegen.mixins import ContainerInterface, RelativeHandlerInterface
from xsdata.codegen.models import Attr, Class, Restrictions, get_restriction_choice
from xsdata.codegen.utils import ClassUtils
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.enums import Tag
from xsdata.utils import collections
from xsdata.utils.collections import group_by

ALL = "a"
GROUP = "g"
SEQUENCE = "s"
CHOICE = "c"


class CreateCompoundFields(RelativeHandlerInterface):
    """Process attrs that belong in the same choice.

    Args:
        container: The class container instance

    Attributes:
        config: The compound fields configuration
    """

    __slots__ = "config"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)
        self.config = container.config.output.compound_fields

    def process(self, target: Class):
        """Process the attrs of class that belong in the same choice.

        If the compound fields configuration is enabled replace the
        attrs with a compound attr, otherwise recalculate the min
        occurs restriction for each of them.

        Args:
            target: The target class instance
        """
        groups = group_by(target.attrs, get_restriction_choice)
        for choice, attrs in groups.items():
            if choice and len(attrs) > 1:
                if self.config.enabled:
                    self.group_fields(target, attrs)
                else:
                    self.calculate_choice_min_occurs(attrs)

    @classmethod
    def calculate_choice_min_occurs(cls, attrs: List[Attr]):
        """Calculate the min occurs restriction of the attrs.

        If that attr has a path that includes a xs:choice
        with min occurs less than 1, update the attr min
        occurs restriction to zero, effectively marking
        it as optional.

        Args:
            attrs: A list of attrs that belong in the same xs:choice.
        """
        for attr in attrs:
            for path in attr.restrictions.path:
                name, index, mi, ma = path
                if name == CHOICE and mi <= 1:
                    attr.restrictions.min_occurs = 0

    @classmethod
    def update_counters(cls, attr: Attr, counters: Dict):
        """Update the counters dictionary with the attr min/max restrictions.

        This method builds a nested counters mapping per path.

        Example:
            {
                "min": [0, 1, 2]
                "max": [3, 4, 5],
                ("c", 1, 0, 1): {
                    "min": [6, 7, 8],
                    "max": [9, 10, 11],
                    ("g", 2, 0, 1): { ... }
                }
            }

        Args:
            attr: The source attr instance
            counters: The nested counters instance to update
        """
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
        """Group attributes into a new compound field.

        Args:
            target: The target class instance
            attrs: A list of attrs that belong to the same choice
        """
        pos = target.attrs.index(attrs[0])
        choice = attrs[0].restrictions.choice

        assert choice is not None

        names = []
        substitutions = []
        choices = []
        counters: Dict = {"min": [], "max": []}

        for attr in attrs:
            ClassUtils.remove_attribute(target, attr)
            names.append(attr.local_name)
            substitutions.append(attr.substitution)

            choices.append(self.build_attr_choice(attr))
            self.update_counters(attr, counters)

        min_occurs, max_occurs = self.sum_counters(counters)
        name = self.choose_name(target, names, list(filter(None, substitutions)))
        types = collections.unique_sequence(
            t.clone() for attr in attrs for t in attr.types
        )

        target.attrs.insert(
            pos,
            Attr(
                name=name,
                index=0,
                types=types,
                tag=Tag.CHOICE,
                restrictions=Restrictions(
                    min_occurs=sum(min_occurs),
                    max_occurs=max(max_occurs) if choice > 0 else sum(max_occurs),
                ),
                choices=choices,
            ),
        )

    def sum_counters(self, counters: Dict) -> Tuple[List[int], List[int]]:
        """Sum the min/max occurrences for the compound attr.

        Args:
            counters: The counters map of all the choice attrs
        """
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

    def choose_name(
        self,
        target: Class,
        names: List[str],
        substitutions: List[str],
    ) -> str:
        """Choose a name for the compound attr.

        If the attrs were placed in the same choice because of a single
        substitution group and the configuration `use_substitution_groups`
        is enabled, the group name will be used for the compound attr.

        Otherwise, the name will be the concatenation of the names of the
        attrs, if the length of the attrs is less than the `max_name_parts`
        config and the `force_default_name` is false,
        e.g. `hat_Or_bat_Or_bar`

        Otherwise, the name will the default from the config,
        e.g. `choice`

        If there are any name collisions with other class attrs, the system
        will add an integer suffix till the name is unique in the class
        e.g. `choice_1`, `choice_2`, `choice_3`

        Args:
            target: The target class
            names: The list of the attr names
            substitutions: The list of the substitution group names of the attrs
        """
        if self.config.use_substitution_groups and len(names) == len(substitutions):
            names = substitutions

        names = collections.unique_sequence(names)
        if self.config.force_default_name or len(names) > self.config.max_name_parts:
            name = self.config.default_name
        else:
            name = "_Or_".join(names)

        reserved = self.build_reserved_names(target, names)
        return ClassUtils.unique_name(name, reserved)

    def build_reserved_names(self, target: Class, names: List[str]) -> Set[str]:
        """Build a set of reserved attr names.

        The method will also check parent attrs.

        Args:
            target: The target class instance
            names: The potential names for the compound attr
        """
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
        """Build the choice attr from a normal attr.

        Steps:
            - Clone the original attr restrictions
            - Reset the min/max occurs
            - Remove the sequence reference
            - Build the new attr and maintain the basic attributes

        Args:
            attr: The source attr instance to use

        Returns:
            The new choice attr for the compound attr.
        """
        restrictions = attr.restrictions.clone()
        restrictions.min_occurs = None
        restrictions.max_occurs = None
        restrictions.sequence = None

        return Attr(
            name=attr.local_name,
            namespace=attr.namespace,
            types=[x.clone() for x in attr.types],
            tag=attr.tag,
            help=attr.help,
            restrictions=restrictions,
        )
