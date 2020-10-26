from typing import Dict
from typing import List
from typing import Optional

from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrChoice
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.collections import group_by

Substitutions = Optional[Dict[str, List[Attr]]]


class AttributeChoiceGroupHandler(HandlerInterface):
    """Group attributes from the same choice group to compound element
    fields."""

    def process(self, target: Class):
        """Group and process target attributes by the choice group."""

        groups = group_by(target.attrs, lambda x: x.restrictions.choice)
        for choice, attrs in groups.items():
            if choice and len(attrs) > 1 and any(attr.is_list for attr in attrs):
                self.group_attrs(target, attrs)

    def group_attrs(self, target: Class, attrs: List[Attr]):
        """Group attributes into a new compound field."""

        pos = target.attrs.index(attrs[0])
        names = []
        choices = []
        min_occurs = []
        max_occurs = []
        for attr in attrs:
            target.attrs.remove(attr)
            names.append(attr.local_name)
            min_occurs.append(attr.restrictions.min_occurs)
            max_occurs.append(attr.restrictions.max_occurs)
            choices.append(self.convert_attr(attr))

        name = "choice" if len(names) > 3 else "_Or_".join(names)
        target.attrs.insert(
            pos,
            Attr(
                name=name,
                local_name=name,
                index=0,
                types=[AttrType(qname=DataType.ANY_TYPE.qname, native=True)],
                tag=Tag.CHOICE,
                restrictions=Restrictions(
                    min_occurs=min((x for x in min_occurs if x is not None), default=0),
                    max_occurs=max((x for x in max_occurs if x is not None), default=0),
                ),
                choices=choices,
            ),
        )

    @classmethod
    def convert_attr(cls, attr: Attr) -> AttrChoice:
        """
        Converts the given attr to a choice.

        The most important part is the reset of certain restrictions
        that don't make sense as choice metadata like occurrences.
        """
        restrictions = attr.restrictions.clone()
        restrictions.min_occurs = None
        restrictions.max_occurs = None
        restrictions.sequential = None

        return AttrChoice(
            name=attr.local_name,
            namespace=attr.namespace,
            default=attr.default,
            types=attr.types,
            tag=attr.tag,
            restrictions=restrictions,
        )
