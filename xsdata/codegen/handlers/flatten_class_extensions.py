from typing import Optional

from xsdata.codegen.mixins import RelativeHandlerInterface
from xsdata.codegen.models import Attr, AttrType, Class, Extension
from xsdata.codegen.utils import ClassUtils
from xsdata.logger import logger
from xsdata.models.enums import DataType, NamespaceType, Tag
from xsdata.utils.constants import DEFAULT_ATTR_NAME


class FlattenClassExtensions(RelativeHandlerInterface):
    """Reduce class extensions by copying or creating new attributes."""

    __slots__ = ()

    def process(self, target: Class):
        """Process a class' extensions.

        Args:
            target: The target class instance
        """
        for extension in list(target.extensions):
            self.process_extension(target, extension)

    def process_extension(self, target: Class, extension: Extension):
        """Process a class extension.

        Slit the process to native xsd extensions and user defined
        types.

        Args:
            target: The target class instance
            extension: The class extension instance
        """
        if extension.type.native:
            self.process_native_extension(target, extension)
        else:
            self.process_dependency_extension(target, extension)

    @classmethod
    def process_native_extension(cls, target: Class, extension: Extension):
        """Native type flatten handler.

        In case of enumerations copy the native data type to all enum
        members, otherwise add a default text attr with the
        extension attributes.

        Args:
            target: The target class instance
            extension: The class extension instance
        """
        if target.is_enumeration:
            cls.replace_attributes_type(target, extension)
        else:
            cls.add_default_attribute(target, extension)

    def process_dependency_extension(self, target: Class, extension: Extension):
        """Process user defined extension types.

        Case:
            - Extension source is missing
            - Target class is an enumeration
            - Extension source is a simple type or an enumeration
            - Extension source is a complex type

        Args:
            target: The target class instance
            extension: The class extension instance
        """
        source = self.find_dependency(extension.type)
        if not source:
            logger.warning("Missing extension type: %s", extension.type.name)
            target.extensions.remove(extension)
        elif target.is_enumeration:
            self.process_enum_extension(source, target, extension)
        elif not source.is_complex_type or source.is_enumeration:
            self.process_simple_extension(source, target, extension)
        else:
            self.process_complex_extension(source, target, extension)

    def process_enum_extension(
        self,
        source: Class,
        target: Class,
        extension: Optional[Extension],
    ):
        """Process an enumeration class extension.

        Cases:
            1. Source is an enumeration: merge them
            2. Source is a simple type: copy all source attr types
            3. Source is a complex type
                3.1 Target has a single member: Restrict default value
                3.2 Target has multiple members: unsupported reset enumeration

        Args:
            source: The source class instance
            target: The target class instance
            extension: The class extension instance
        """
        if source.is_enumeration:
            self.merge_enumerations(source, target)
        elif not source.is_complex_type:
            self.merge_enumeration_types(source, target)
        elif len(target.attrs) == 1:
            self.set_default_value(source, target)
        else:
            # We can't subclass and override the value field
            # the target enumeration, mypy doesn't play nicely.
            target.attrs.clear()

        if extension:
            if target.is_enumeration:
                target.extensions.remove(extension)
            else:
                extension.type.reference = source.ref

    @classmethod
    def merge_enumerations(cls, source: Class, target: Class):
        """Merge enumeration members from source to target class.

        Args:
            source: The source class instance
            target: The target class instance
        """
        source_attrs = {attr.name: attr for attr in source.attrs}
        target.attrs = [
            source_attrs[attr.name].clone() if attr.name in source_attrs else attr
            for attr in target.attrs
        ]

    def merge_enumeration_types(self, source: Class, target: Class):
        """Merge the enumeration attr types and restrictions.

        Args:
            source: The source class instance
            target: The target class instance
        """
        source_attr = source.attrs[0]
        for tp in source_attr.types:
            if tp.native:
                for target_attr in target.attrs:
                    target_attr.types.append(tp.clone())
                    target_attr.restrictions.merge(source_attr.restrictions)
            else:
                base = self.find_dependency(tp)
                # It's impossible to have a missing reference now, the
                # source class has passed through AttributeTypeHandler
                # and any missing types have been reset.
                assert base is not None
                self.process_enum_extension(base, target, None)

    @classmethod
    def set_default_value(cls, source: Class, target: Class):
        """Set the default value from the source single enumeration.

        When a simple type is a restriction of an enumeration with
        only one member, we can safely set its default value
        to that member value as fixed.

        Args:
            source: The source class instance
            target: The target class instance
        """
        new_attr = ClassUtils.find_value_attr(source).clone()
        new_attr.types = target.attrs[0].types
        new_attr.default = target.attrs[0].default
        new_attr.fixed = True
        target.attrs = [new_attr]

    @classmethod
    def process_simple_extension(cls, source: Class, target: Class, ext: Extension):
        """Process simple type extensions.

        Cases:
            1. If target is source: drop the extension.
            2. If source is enumeration and target isn't create default value attribute.
            3. If both source and target are enumerations copy all attributes.
            4. If target is enumeration: drop the extension.

        Args:
            source: The source class instance
            target: The target class instance
            ext: The extension class instance
        """
        if source is target:
            target.extensions.remove(ext)
        elif source.is_enumeration and not target.is_enumeration:
            cls.add_default_attribute(target, ext)
        elif source.is_enumeration == target.is_enumeration:
            ClassUtils.copy_attributes(source, target, ext)
        else:  # this is an enumeration
            target.extensions.remove(ext)

    @classmethod
    def process_complex_extension(cls, source: Class, target: Class, ext: Extension):
        """Process complex type extensions.

        Compare source and target classes and either remove the
        extension completely, copy all source attributes to the target
        class or leave the extension alone.

        Args:
            source: The source class instance
            target: The target class instance
            ext: The extension class instance
        """
        if cls.should_remove_extension(source, target, ext):
            target.extensions.remove(ext)
        elif cls.should_flatten_extension(source, target):
            ClassUtils.copy_attributes(source, target, ext)
        else:
            ext.type.reference = id(source)

    def find_dependency(self, attr_type: AttrType) -> Optional[Class]:
        """Find dependency for the given extension type with priority.

        Search priority: xs:SimpleType >  xs:ComplexType

        Args:
            attr_type: The attr type instance

        Returns:
            The class instance or None if it's undefined.
        """
        conditions = (
            lambda x: x.tag == Tag.SIMPLE_TYPE,
            lambda x: x.tag == Tag.COMPLEX_TYPE,
        )

        for condition in conditions:
            result = self.container.find(attr_type.qname, condition=condition)
            if result:
                return result

        return None

    @classmethod
    def should_remove_extension(
        cls,
        source: Class,
        target: Class,
        extension: Extension,
    ) -> bool:
        """Return whether the extension should be removed.

        Violations:
            - Circular Reference
            - Forward Reference
            - Unordered sequences
            - MRO Violation A(B), C(B) and extensions includes A, B, C

        Args:
            source: The source class instance
            target: The target class instance
            extension: The extension class instance
        """
        if (
            source is target
            or target in source.inner
            or cls.have_unordered_sequences(source, target, extension)
        ):
            return True

        # MRO Violation
        collision = {ext.type.qname for ext in target.extensions}
        return any(ext.type.qname in collision for ext in source.extensions)

    @classmethod
    def should_flatten_extension(cls, source: Class, target: Class) -> bool:
        """Return whether the extension should be flattened.

        Rules:
            1. Source doesn't have a parent class
            2. Source class is a simple type
            3. Source class has a suffix attr and target has its own attrs
            4. Target class has a suffix attr

        Args:
            source: The source class instance
            target: The target class instance
        """
        if not source.extensions and (
            not source.is_complex_type
            or target.has_suffix_attr
            or (source.has_suffix_attr and target.attrs)
        ):
            return True

        return False

    @classmethod
    def have_unordered_sequences(
        cls,
        source: Class,
        target: Class,
        extension: Extension,
    ) -> bool:
        """Validate overriding sequence attrs are in order.

        Dataclasses fields ordering follows the python mro pattern, the
        parent fields are always first, and they are updated if the
        subclass is overriding any of them but the overall ordering
        doesn't change!

        @todo This needs a complete rewrite and most likely it needs to
        @todo move way down in the process chain.

        Args:
            source: The source class instance
            target: The target class instance
            extension: The extension class instance
        """
        if extension.tag == Tag.EXTENSION or source.extensions:
            return False

        sequence = [
            attr.name
            for attr in target.attrs
            if attr.restrictions.sequence is not None and not attr.is_prohibited
        ]
        if len(sequence) > 1:
            compare = [attr.name for attr in source.attrs if attr.name in sequence]
            if compare and compare != sequence:
                return True

        return False

    @classmethod
    def replace_attributes_type(cls, target: Class, extension: Extension):
        """Replace all attrs types with the extension's type.

        The extension is a native xsd datatype.

        Args:
            target: The target class instance
            extension: The extension class instance
        """
        target.extensions.remove(extension)
        for attr in target.attrs:
            attr.types.clear()
            attr.types.append(extension.type.clone())

    @classmethod
    def add_default_attribute(cls, target: Class, extension: Extension):
        """Convert extension to a value text attr.

        If the extension type is xs:anyType convert the
        attr into a wildcard attr to match everything.

        Args:
            target: The target class instance
            extension: The extension class instance
        """
        if extension.type.datatype != DataType.ANY_TYPE:
            tag = Tag.EXTENSION
            name = DEFAULT_ATTR_NAME
            namespace = None
        else:
            tag = Tag.ANY
            name = "@any_element"
            namespace = NamespaceType.ANY_NS

        attr = cls.get_or_create_attribute(target, name, tag)
        attr.types.append(extension.type.clone())
        attr.restrictions.merge(extension.restrictions)
        attr.namespace = namespace
        target.extensions.remove(extension)

    @classmethod
    def get_or_create_attribute(cls, target: Class, name: str, tag: str) -> Attr:
        """Find or create an attr with the given name and tag.

        If the attr doesn't exist, create a new required
        attr and prepend it in the attrs list.

        Args:
            target: The target class instance
            name: The attr name
            tag: The attr tag name
        """
        attr = ClassUtils.find_attr(target, name)
        if attr is None:
            attr = Attr(name=name, tag=tag)
            attr.restrictions.min_occurs = 1
            attr.restrictions.max_occurs = 1
            target.attrs.insert(0, attr)

        return attr
