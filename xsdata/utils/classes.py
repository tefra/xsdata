import sys
from typing import List
from typing import Optional

from xsdata.models.codegen import Attr
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.codegen import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import NamespaceType
from xsdata.models.enums import Tag
from xsdata.utils import text


class ClassUtils:

    INCLUDES_NONE = 0
    INCLUDES_SOME = 1
    INCLUDES_ALL = 2

    @classmethod
    def compare_attributes(cls, source: Class, target: Class) -> int:
        """Compare the attributes of the two classes and return whether the
        source includes all, some or none of the target attributes."""
        if source is target:
            return cls.INCLUDES_ALL

        if not target.attrs:
            return cls.INCLUDES_NONE

        source_attrs = {attr.name for attr in source.attrs}
        target_attrs = {attr.name for attr in target.attrs}
        difference = source_attrs - target_attrs

        if not difference:
            return cls.INCLUDES_ALL
        if len(difference) != len(source_attrs):
            return cls.INCLUDES_SOME

        return cls.INCLUDES_NONE

    @classmethod
    def copy_attributes(cls, source: Class, target: Class, extension: Extension):
        """
        Copy the attributes from the source class to the target class and
        remove the extension that links the two classes together.

        The new attributes are prepended in the list unless if they are
        supposed to be last in a sequence.
        """
        prefix = text.prefix(extension.type.name)
        target.extensions.remove(extension)
        target_attr_names = {text.suffix(attr.name) for attr in target.attrs}

        index = 0
        for attr in source.attrs:
            if text.suffix(attr.name) not in target_attr_names:
                clone = cls.clone_attribute(attr, extension.restrictions, prefix)

                if attr.index == sys.maxsize:
                    target.attrs.append(clone)
                    continue

                target.attrs.insert(index, clone)
            index += 1

        cls.copy_inner_classes(source, target)

    @classmethod
    def clone_attribute(
        cls, attr: Attr, restrictions: Restrictions, prefix: Optional[str] = None
    ) -> Attr:
        """
        Clone the given attribute and merge its restrictions with the given
        instance.

        Prepend the given namespace prefix to the attribute name if
        available.
        """
        clone = attr.clone()
        clone.restrictions.merge(restrictions)
        if prefix:
            for attr_type in clone.types:
                if not attr_type.native and attr_type.name.find(":") == -1:
                    attr_type.name = f"{prefix}:{attr_type.name}"

        return clone

    @classmethod
    def copy_inner_classes(cls, source: Class, target: Class):
        """
        Copy safely inner classes from source to target class.

        Checks:
            1. Inner is the target class, skip and mark as self reference
            2. Inner with same name exists, skip
        """
        for inner in source.inner:
            if inner is target:
                for attr in target.attrs:
                    for attr_type in attr.types:
                        if attr_type.forward and attr_type.name == inner.name:
                            attr_type.circular = True
            elif not any(existing.name == inner.name for existing in target.inner):
                clone = inner.clone()
                clone.package = target.package
                clone.module = target.module
                target.inner.append(clone)

    @classmethod
    def copy_extension_type(cls, target: Class, extension: Extension):
        """Add the given extension type to all target attributes types and
        remove it from the target class extensions."""

        for attr in target.attrs:
            attr.types.append(extension.type.clone())
        target.extensions.remove(extension)

    @classmethod
    def create_default_attribute(cls, item: Class, extension: Extension):
        """Add a default value field to the given class based on the extension
        type."""
        if extension.type.native_code == DataType.ANY_TYPE.code:
            attr = Attr(
                name="any_element",
                local_name="any_element",
                index=0,
                default=list if extension.restrictions.is_list else None,
                types=[extension.type.clone()],
                tag=Tag.ANY,
                namespace=NamespaceType.ANY.value,
                restrictions=extension.restrictions.clone(),
            )
        else:
            attr = Attr(
                name="value",
                local_name="value",
                index=0,
                default=None,
                types=[extension.type.clone()],
                tag=Tag.EXTENSION,
                restrictions=extension.restrictions.clone(),
            )

        item.attrs.insert(0, attr)
        item.extensions.remove(extension)

    @classmethod
    def find_attribute(cls, attrs: List[Attr], attr: Attr) -> int:
        """Return the position of the given attribute in the list."""
        try:
            return attrs.index(attr)
        except ValueError:
            return -1
