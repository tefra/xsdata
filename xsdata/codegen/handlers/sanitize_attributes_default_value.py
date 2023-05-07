from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.formats.converter import converter
from xsdata.logger import logger
from xsdata.models.enums import DataType


class SanitizeAttributesDefaultValue(RelativeHandlerInterface):
    """
    Sanitize attributes default values.

    Cases:
        1. Ignore enumerations.
        2. List fields can not have a default value
        3. Optional choice/sequence fields can not have a default value
        4. xsi:type fields are ignored, mark them as optional
        5. Convert string literal default value for enum fields.
    """

    __slots__ = ()

    def process(self, target: Class):
        for attr in target.attrs:
            self.process_attribute(target, attr)

            for choice in attr.choices:
                self.process_attribute(target, choice)

    def process_attribute(self, target: Class, attr: Attr):
        if self.should_reset_required(attr):
            attr.restrictions.min_occurs = 0

        if self.should_reset_default(attr):
            attr.fixed = False
            attr.default = None

        if attr.default is not None:
            self.process_types(target, attr)
        elif attr.xml_type is None and str in attr.native_types:
            # String text nodes get an empty string as default!
            attr.default = ""

    def process_types(self, target: Class, attr: Attr):
        if self.is_valid_external_value(target, attr):
            return

        if self.is_valid_native_value(target, attr):
            return

        logger.warning(
            "Failed to match %s.%s default value `%s` to one of %s",
            target.name,
            attr.local_name,
            attr.default,
            [tp.qname for tp in attr.types],
        )

        self.reset_attribute_types(attr)

    def is_valid_external_value(self, target: Class, attr: Attr) -> bool:
        """Return whether the default value of the given attr can be mapped to
        user defined type like an enumeration or an inner complex content
        class."""

        for tp in attr.user_types:
            source = self.find_type(target, tp)
            if self.is_valid_inner_type(source, attr, tp):
                return True

            if self.is_valid_enum_type(source, attr):
                return True

        return False

    def find_type(self, target: Class, attr_type: AttrType) -> Class:
        if attr_type.forward:
            return self.container.find_inner(target, attr_type.qname)

        return self.container.first(attr_type.qname)

    @classmethod
    def is_valid_inner_type(
        cls, source: Class, attr: Attr, attr_type: AttrType
    ) -> bool:
        """Return whether the inner class can inherit the attr default value
        and swap them as well."""
        if attr_type.forward:
            for src_attr in source.attrs:
                if src_attr.xml_type is None:
                    src_attr.default = attr.default
                    src_attr.fixed = attr.fixed
                    attr.default = None
                    attr.fixed = False
                    return True
        return False

    @classmethod
    def is_valid_enum_type(cls, source: Class, attr: Attr) -> bool:
        """
        Convert string literal default values to enumeration members
        placeholders and return result.

        The placeholders will be converted to proper references from the
        generator filters.

        Placeholder examples: Single -> @enum@qname::member_name
        Multiple -> @enum@qname::first_member@second_member
        """
        assert attr.default is not None

        value_members = {x.default: x.name for x in source.attrs}
        name = value_members.get(attr.default)
        if name:
            attr.default = f"@enum@{source.qname}::{name}"
            return True

        names = [
            value_members[token]
            for token in attr.default.split()
            if token in value_members
        ]
        if names:
            attr.default = f"@enum@{source.qname}::{'@'.join(names)}"
            return True

        return False

    @classmethod
    def is_valid_native_value(cls, target: Class, attr: Attr) -> bool:
        """
        Return whether the default value of the given attribute can be
        converted successfully to and from xml.

        The test process for enumerations and fixed value fields are
        strict, meaning the textual representation also needs to match
        the original.
        """
        assert attr.default is not None

        types = converter.sort_types(attr.native_types)
        if not types:
            return False

        if attr.restrictions.tokens:
            tokens = attr.default.split()
        else:
            tokens = [attr.default]

        if len(tokens) == 1 and attr.is_enumeration and attr.restrictions.tokens:
            attr.restrictions.tokens = False

        # Enumerations are also fixed!!!
        strict = attr.fixed

        return all(
            converter.test(
                token,
                types,
                strict=strict,
                ns_map=target.ns_map,
                format=attr.restrictions.format,
            )
            for token in tokens
        )

    @classmethod
    def should_reset_required(cls, attr: Attr) -> bool:
        """
        Return whether the min occurrences for the attr needs to be reset.

        @Todo figure out if wildcards are supposed to be optional!
        """
        return (
            not attr.is_attribute
            and attr.default is None
            and object in attr.native_types
            and not attr.is_list
        )

    @classmethod
    def should_reset_default(cls, attr: Attr) -> bool:
        """
        Return whether we should unset the default value of the attribute.

        - Default value is not set
        - Attribute is xsi:type (ignorable)
        - Attribute is part of a choice
        """
        return attr.default is not None and (
            attr.is_xsi_type
            or attr.is_list
            or (not attr.is_attribute and attr.is_optional)
        )

    @classmethod
    def reset_attribute_types(cls, attr: Attr):
        attr.types.clear()
        attr.types.append(AttrType(qname=str(DataType.STRING), native=True))
        attr.restrictions.format = None
