from typing import List

from xsdata.codegen.mixins import ContainerInterface
from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import get_restriction_choice
from xsdata.codegen.models import get_slug
from xsdata.codegen.models import Restrictions
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.collections import group_by


class AttributeCompoundChoiceHandler(RelativeHandlerInterface):
    """Group attributes that belong in the same choice and replace them by
    compound fields."""

    __slots__ = "compound_fields"

    def __init__(self, container: ContainerInterface):
        super().__init__(container)

        self.compound_fields = container.config.output.compound_fields

    def process(self, target: Class):
        if self.compound_fields:
            groups = group_by(target.attrs, get_restriction_choice)
            for choice, attrs in groups.items():
                if (
                    choice
                    and len(attrs) > 1
                    and any(
                        attr.is_list or get_restriction_choice(attr) for attr in attrs
                    )
                ):
                    self.group_fields(target, attrs)

        for index in range(len(target.attrs)):
            self.reset_sequential(target, index)

    def group_fields(self, target: Class, attrs: List[Attr]):
        """Group attributes into a new compound field."""

        pos = target.attrs.index(attrs[0])
        choice = attrs[0].restrictions.choice
        sum_occurs = choice and choice.startswith("effective_")

        names = []
        choices = []
        min_occurs = []
        max_occurs = []
        for attr in attrs:
            target.attrs.remove(attr)
            names.append(attr.local_name)
            min_occurs.append(attr.restrictions.min_occurs or 0)
            max_occurs.append(attr.restrictions.max_occurs or 0)
            choices.append(self.build_attr_choice(attr))

        name = self.choose_name(target, names)

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
        reserved = set(map(get_slug, self.base_attrs(target)))
        reserved.update(map(get_slug, target.attrs))

        if len(names) > 3 or len(names) != len(set(names)):
            name = "choice"
        else:
            name = "_Or_".join(names)

        return ClassUtils.unique_name(name, reserved)

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
        restrictions.sequential = None

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
    def reset_sequential(cls, target: Class, index: int):
        """Reset the attribute at the given index if it has no siblings with
        the sequential restriction."""

        attr = target.attrs[index]
        before = target.attrs[index - 1] if index - 1 >= 0 else None
        after = target.attrs[index + 1] if index + 1 < len(target.attrs) else None

        if not attr.is_list:
            attr.restrictions.sequential = False

        if (
            not attr.restrictions.sequential
            or (before and before.restrictions.sequential)
            or (after and after.restrictions.sequential and after.is_list)
        ):
            return

        attr.restrictions.sequential = False
