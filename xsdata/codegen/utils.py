import sys
from typing import Iterator
from typing import List
from typing import Optional
from typing import Set

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.models import get_qname
from xsdata.codegen.models import get_slug
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.exceptions import CodeGenerationError
from xsdata.models.enums import DataType
from xsdata.utils import collections
from xsdata.utils import namespaces
from xsdata.utils import text


class ClassUtils:
    """General reusable utils methods that didn't fit anywhere else."""

    @classmethod
    def find_value_attr(cls, target: Class) -> Attr:
        """
        Find the text attribute of the class.

        :raise CodeGenerationError: If no text node/attribute exists
        """
        for attr in target.attrs:
            if not attr.xml_type:
                return attr

        raise CodeGenerationError(f"Class has no value attr {target.qname}")

    @classmethod
    def remove_attribute(cls, target: Class, attr: Attr):
        """Safely remove the given attr from the target class by check obj
        ids."""
        target.attrs = [at for at in target.attrs if id(at) != id(attr)]

    @classmethod
    def clean_inner_classes(cls, target: Class):
        """Check if there are orphan inner classes and remove them."""
        for inner in list(target.inner):
            if cls.is_orphan_inner(target, inner):
                target.inner.remove(inner)

    @classmethod
    def is_orphan_inner(cls, target: Class, inner: Class) -> bool:
        """Check if there is at least once valid attr reference to the given
        inner class."""
        for attr in target.attrs:
            for attr_type in attr.types:
                if attr_type.forward and attr_type.qname == inner.qname:
                    return False

        return True

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
                cls.copy_inner_classes(source, target, clone)

                if attr.index == sys.maxsize:
                    target.attrs.append(clone)
                    continue

                target.attrs.insert(index, clone)

            index += 1

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

            cls.copy_inner_classes(source, target, clone)

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
    def copy_inner_classes(cls, source: Class, target: Class, attr: Attr):
        """Iterate all attr types and copy any inner classes from source to the
        target class."""
        for attr_type in attr.types:
            cls.copy_inner_class(source, target, attr, attr_type)

    @classmethod
    def copy_inner_class(
        cls, source: Class, target: Class, attr: Attr, attr_type: AttrType
    ):
        """
        Check if the given attr type is a forward reference and copy its inner
        class from the source to the target class.

        Checks:
            1. Update type if inner class in a circular reference
            2. Copy inner class, rename it if source is a simple type.
        """
        if not attr_type.forward:
            return

        inner = ClassUtils.find_inner(source, attr_type.qname)
        if inner is target:
            attr_type.circular = True
        else:
            # In extreme cases this adds duplicate inner classes
            clone = inner.clone()
            clone.package = target.package
            clone.module = target.module
            clone.status = Status.RAW
            target.inner.append(clone)

    @classmethod
    def find_inner(cls, source: Class, qname: str) -> Class:
        for inner in source.inner:
            if inner.qname == qname:
                return inner

        raise CodeGenerationError(f"Missing inner class {source.qname}.{qname}")

    @classmethod
    def find_attr(cls, source: Class, name: str) -> Optional[Attr]:
        for attr in source.attrs:
            if attr.name == name:
                return attr

        return None

    @classmethod
    def flatten(cls, target: Class, location: str) -> Iterator[Class]:
        target.location = location

        while target.inner:
            yield from cls.flatten(target.inner.pop(), location)

        for attr in target.attrs:
            attr.types = collections.unique_sequence(attr.types, key="qname")
            for tp in attr.types:
                tp.forward = False

        yield target

    @classmethod
    def reduce_classes(cls, classes: List[Class]) -> List[Class]:
        result = []
        for group in collections.group_by(classes, key=get_qname).values():
            target = group[0].clone()
            target.attrs = cls.reduce_attributes(group)
            target.mixed = any(x.mixed for x in group)

            cls.cleanup_class(target)
            result.append(target)

        return result

    @classmethod
    def reduce_attributes(cls, classes: List[Class]) -> List[Attr]:
        result = []
        for attr in cls.sorted_attrs(classes):
            added = False
            optional = False
            for obj in classes:
                pos = collections.find(obj.attrs, attr)
                if pos == -1:
                    optional = True
                elif not added:
                    added = True
                    result.append(obj.attrs.pop(pos))
                else:
                    cls.merge_attributes(result[-1], obj.attrs.pop(pos))

            if optional:
                result[-1].restrictions.min_occurs = 0

        return result

    @classmethod
    def sorted_attrs(cls, classes: List[Class]) -> List[Attr]:
        attrs: List[Attr] = []
        classes.sort(key=lambda x: len(x.attrs), reverse=True)

        for obj in classes:
            i = 0
            obj_attrs = obj.attrs.copy()

            while obj_attrs:
                pos = collections.find(attrs, obj_attrs[i])
                i += 1

                if pos > -1:
                    insert = obj_attrs[: i - 1]
                    del obj_attrs[:i]
                    while insert:
                        attrs.insert(pos, insert.pop())

                    i = 0
                elif i == len(obj_attrs):
                    attrs.extend(obj_attrs)
                    obj_attrs.clear()

        return attrs

    @classmethod
    def merge_attributes(cls, target: Attr, source: Attr):
        target.types.extend(tp for tp in source.types if tp not in target.types)

        target.restrictions.min_occurs = min(
            target.restrictions.min_occurs or 0,
            source.restrictions.min_occurs or 0,
        )

        target.restrictions.max_occurs = max(
            target.restrictions.max_occurs or 1,
            source.restrictions.max_occurs or 1,
        )

        if source.restrictions.sequence is not None:
            target.restrictions.sequence = source.restrictions.sequence

    @classmethod
    def rename_attribute_by_preference(cls, a: Attr, b: Attr):
        """
        Decide and rename one of the two given attributes.

        When both attributes are derived from the same xs:tag and one of
        the two fields has a specific namespace prepend it to the name.
        Preferable rename the second attribute.

        Otherwise append the derived from tag to the name of one of the
        two attributes. Preferably rename the second field or the field
        derived from xs:attribute.
        """
        if a.tag == b.tag and (a.namespace or b.namespace):
            change = b if b.namespace else a
            assert change.namespace is not None
            change.name = f"{namespaces.clean_uri(change.namespace)}_{change.name}"
        else:
            change = b if b.is_attribute else a
            change.name = f"{change.name}_{change.tag}"

    @classmethod
    def rename_attributes_by_index(cls, attrs: List[Attr], rename: List[Attr]):
        """Append the next available index number to all the rename attributes
        names."""
        for index in range(1, len(rename)):
            reserved = set(map(get_slug, attrs))
            name = rename[index].name
            rename[index].name = cls.unique_name(name, reserved)

    @classmethod
    def unique_name(cls, name: str, reserved: Set[str]) -> str:
        if text.alnum(name) in reserved:
            index = 1
            while text.alnum(f"{name}_{index}") in reserved:
                index += 1

            return f"{name}_{index}"

        return name

    @classmethod
    def cleanup_class(cls, target: Class):
        for attr in target.attrs:
            attr.types = cls.filter_types(attr.types)

    @classmethod
    def filter_types(cls, types: List[AttrType]) -> List[AttrType]:
        """
        Remove duplicate and invalid types.

        Invalid:
            1. xs:error
            2. xs:anyType and xs:anySimpleType when there are other types present
        """
        types = collections.unique_sequence(types, key="qname")
        types = collections.remove(types, lambda x: x.datatype == DataType.ERROR)

        if len(types) > 1:
            types = collections.remove(
                types,
                lambda x: x.datatype in (DataType.ANY_TYPE, DataType.ANY_SIMPLE_TYPE),
            )

        if not types:
            types.append(AttrType(qname=str(DataType.STRING), native=True))

        return types
