import sys

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.utils import ClassUtils
from xsdata.utils import collections
from xsdata.utils.text import alnum


class AttributeOverridesHandler(ContainerHandlerInterface):
    """
    Check override attributes are valid.

    Steps:
        1. The attribute is a valid override, leave it alone
        2. The attribute is unnecessary remove it
        3. The attribute is an invalid override, rename one of them
    """

    __slots__ = ()

    def process(self, target: Class):
        for extension in target.extensions:
            self.process_extension(target, extension)

    def process_extension(self, target: Class, extension: Extension):
        source = self.container.find(extension.type.qname)
        assert source is not None

        for attr in list(target.attrs):
            search = alnum(attr.name)
            source_attr = collections.first(
                source_attr
                for source_attr in source.attrs
                if alnum(source_attr.name) == search
            )

            if not source_attr:
                continue

            if attr.tag == source_attr.tag:
                self.validate_override(target, attr, source_attr)
            else:
                self.resolve_conflict(attr, source_attr)

        for extension in source.extensions:
            self.process_extension(target, extension)

    @classmethod
    def validate_override(cls, target: Class, attr: Attr, source_attr: Attr):
        if attr.is_list and not source_attr.is_list:
            # Hack much??? idk but Optional[str] can't override List[str]
            source_attr.restrictions.max_occurs = sys.maxsize

        if (
            attr.default == source_attr.default
            and attr.fixed == source_attr.fixed
            and attr.mixed == source_attr.mixed
            and attr.restrictions == source_attr.restrictions
        ):
            ClassUtils.remove_attribute(target, attr)

    @classmethod
    def resolve_conflict(cls, attr: Attr, source_attr: Attr):
        ClassUtils.rename_attribute_by_preference(attr, source_attr)
