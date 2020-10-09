import sys

from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.models import Restrictions


class ClassUtils:
    """General reusable utils methods that didn't fit anywhere else."""

    @classmethod
    def copy_attributes(cls, source: Class, target: Class, extension: Extension):
        """
        Copy the attributes and inner classes from the source class to the
        target class and remove the extension that links the two classes
        together.

        The new attributes are prepended in the list unless if they are
        supposed to be last in a sequence.
        """
        target.extensions.remove(extension)
        target_attr_names = {attr.name for attr in target.attrs}

        index = 0
        for attr in source.attrs:
            if attr.name not in target_attr_names:
                clone = cls.clone_attribute(attr, extension.restrictions)

                if attr.index == sys.maxsize:
                    target.attrs.append(clone)
                    continue

                target.attrs.insert(index, clone)
            index += 1

        cls.copy_inner_classes(source, target)

    @classmethod
    def copy_group_attributes(cls, source: Class, target: Class, attr: Attr):
        """Copy the attributes and inner classes from the source class to the
        target class and remove the group attribute that links the two classes
        together."""
        index = target.attrs.index(attr)
        target.attrs.pop(index)

        for source_attr in source.attrs:
            clone = cls.clone_attribute(source_attr, attr.restrictions)
            target.attrs.insert(index, clone)
            index += 1

        cls.copy_inner_classes(source, target)

    @classmethod
    def copy_extensions(cls, source: Class, target: Class, extension: Extension):
        """Copy the extensions from the source class to the target class and
        merge the restrictions from the extension that linked the two classes
        together."""
        for ext in source.extensions:
            clone = ext.clone()
            clone.restrictions.merge(extension.restrictions)
            target.extensions.append(clone)

    @classmethod
    def clone_attribute(cls, attr: Attr, restrictions: Restrictions) -> Attr:
        """Clone the given attribute and merge its restrictions with the given
        instance."""
        clone = attr.clone()
        clone.restrictions.merge(restrictions)
        return clone

    @classmethod
    def copy_inner_classes(cls, source: Class, target: Class):
        """
        Copy safely inner classes from source to target class.

        Checks:
            1. Inner is the target class, skip and mark as circular.
            2. Inner with same name exists, skip.
        """
        for inner in source.inner:
            if inner is target:
                cls.update_inner_circular(target, inner)
            elif not any(existing.name == inner.name for existing in target.inner):
                clone = inner.clone()
                clone.package = target.package
                clone.module = target.module
                target.inner.append(clone)

    @classmethod
    def update_inner_circular(cls, target: Class, inner: Class):

        """Find the target attributes with the inner type and mark them as
        circular."""
        for attr in target.attrs:
            for attr_type in attr.types:
                if attr_type.forward and attr_type.name == inner.name:
                    attr_type.circular = True
