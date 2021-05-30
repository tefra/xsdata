from typing import Optional

from xsdata.codegen.mixins import ContainerHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.logger import logger


class AttributeDefaultValueHandler(ContainerHandlerInterface):
    """
    Sanitize attributes default values.

    Cases:
        1. Ignore enumerations.
        2. List fields can not have a fixed value.
        3. Optional fields or xsi:type can not have a default or fixed value.
        4. Convert string literal default value for enum fields.
    """

    __slots__ = ()

    def process(self, target: Class):
        for attr in target.attrs:
            self.process_attribute(target, attr)

    def process_attribute(self, target: Class, attr: Attr):

        if attr.is_enumeration:
            return

        if attr.is_optional or attr.is_xsi_type:
            attr.fixed = False
            attr.default = None

        if attr.default:
            self.process_attribute_default_enum(target, attr)

    def process_attribute_default_enum(self, target: Class, attr: Attr):
        """
        Convert string literal default value for enum fields.

        Loop through all attributes types and search for enum sources.
        If an enum source exist map the default string literal value to
        a qualified name. If the source class in inner promote it to
        root classes.
        """

        source_found = False

        assert attr.default is not None

        for attr_type in attr.types:
            source = self.find_enum(attr_type)
            if not source:
                continue

            source_found = True
            value_members = {x.default: x.name for x in source.attrs}
            name = value_members.get(attr.default)
            if name:
                attr.default = f"@enum@{source.qname}::{name}"
                return

            names = [
                value_members[token]
                for token in attr.default.split()
                if token in value_members
            ]
            if names:
                attr.default = f"@enum@{source.qname}::{'@'.join(names)}"
                return

        if source_found:
            logger.warning(
                "No enumeration member matched %s.%s default value `%s`",
                target.name,
                attr.local_name,
                attr.default,
            )
            attr.default = None

    def find_enum(self, attr_type: AttrType) -> Optional[Class]:
        """Find an enumeration class byte the attribute type."""
        if attr_type.native:
            return None

        return self.container.find(
            attr_type.qname, condition=lambda x: x.is_enumeration
        )
