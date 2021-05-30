from typing import List

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.collections import group_by


class AttributeCompoundChoiceHandler(HandlerInterface):
    """Group attributes that belong in the same choice and replace them by
    compound fields."""

    __slots__ = ()

    def process(self, target: Class):
        groups = group_by(target.attrs, lambda x: x.restrictions.choice)
        for choice, attrs in groups.items():
            if choice and len(attrs) > 1 and any(attr.is_list for attr in attrs):
                self.group_fields(target, attrs)

    @classmethod
    def group_fields(cls, target: Class, attrs: List[Attr]):
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
            choices.append(cls.build_attr_choice(attr))

        if len(names) > 3 or len(names) != len(set(names)):
            name = "choice"
        else:
            name = "_Or_".join(names)

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
