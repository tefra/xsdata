import sys
from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from tests.factories import RestrictionsFactory
from xsdata.analyzer import ClassAnalyzer
from xsdata.analyzer import simple_type
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Restrictions
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Schema
from xsdata.models.elements import SimpleType
from xsdata.models.enums import DataType
from xsdata.models.enums import TagType


class ClassAnalyzerBaseTestCase(FactoryTestCase):
    def setUp(self) -> None:
        super(ClassAnalyzerBaseTestCase, self).setUp()
        self.target_namespace = "http://namespace/target"
        self.nsmap = {
            None: "http://namespace/foobar",
            "common": "http://namespace/common",
        }
        self.schema = Schema.create(
            target_namespace=self.target_namespace, nsmap=self.nsmap
        )
        self.analyzer = ClassAnalyzer()
        self.analyzer.schema = self.schema


class ClassAnalyzerProcessTests(ClassAnalyzerBaseTestCase):
    @mock.patch.object(ClassAnalyzer, "fetch_classes_for_generation")
    @mock.patch.object(ClassAnalyzer, "flatten_classes")
    @mock.patch.object(ClassAnalyzer, "mark_abstract_duplicate_classes")
    @mock.patch.object(ClassAnalyzer, "create_class_qname_index")
    @mock.patch.object(ClassAnalyzer, "merge_redefined_classes")
    def test_process(
        self,
        mock_merge_redefined_classes,
        mock_create_class_qname_index,
        mock_mark_abstract_duplicate_classes,
        mock_flatten_classes,
        mock_fetch_classes_for_generation,
    ):
        self.analyzer.schema = None
        mock_fetch_classes_for_generation.return_value = "foo"
        classes = ClassFactory.list(3, type=Element)

        self.assertEqual("foo", self.analyzer.process(self.schema, classes))

        mock_merge_redefined_classes.assert_called_once_with(classes)
        mock_create_class_qname_index.assert_called_once_with(classes)
        mock_mark_abstract_duplicate_classes.assert_called_once()
        mock_flatten_classes.assert_called_once_with()
        mock_fetch_classes_for_generation.assert_called_once_with()
        self.assertEqual(self.schema, self.analyzer.schema)

    def test_create_class_qname_index(self):
        classes = [
            ClassFactory.create(type=Element, name="foo"),
            ClassFactory.create(type=ComplexType, name="foo"),
            ClassFactory.create(type=ComplexType, name="foobar"),
        ]

        expected = {
            "{http://namespace/target}foo": classes[:2],
            "{http://namespace/target}foobar": classes[2:],
        }

        self.analyzer.create_class_qname_index(classes)
        self.assertEqual(2, len(self.analyzer.class_index))
        self.assertEqual(expected, self.analyzer.class_index)

    def test_mark_abstract_duplicate_classes(self):
        one = ClassFactory.create(name="foo", is_abstract=True, type=Element)
        two = ClassFactory.create(name="foo", type=Element)
        three = ClassFactory.create(name="foo", type=ComplexType)
        four = ClassFactory.create(name="foo", type=SimpleType)

        five = ClassFactory.create(name="bar", is_abstract=True, type=Element)
        six = ClassFactory.create(name="bar", type=ComplexType)
        seven = ClassFactory.create(name="opa", type=ComplexType)

        self.analyzer.create_class_qname_index(
            [one, two, three, four, five, six, seven]
        )
        self.analyzer.mark_abstract_duplicate_classes()

        self.assertTrue(one.is_abstract)  # Was abstract already
        self.assertFalse(two.is_abstract)  # Is an element
        self.assertTrue(three.is_abstract)  # Marked as abstract
        self.assertFalse(four.is_abstract)  # Is common
        self.assertTrue(five.is_abstract)  # Was abstract already
        self.assertFalse(six.is_abstract)  # No element in group
        self.assertFalse(seven.is_abstract)  # Alone

    def test_fetch_classes_for_generation(self):
        classes = [
            ClassFactory.create(is_abstract=True, type=Element),
            ClassFactory.create(type=Element),
            ClassFactory.create(type=ComplexType),
            ClassFactory.create(type=SimpleType),
            ClassFactory.create(
                type=SimpleType,
                attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION),
            ),
        ]

        expected = [
            classes[1],
            classes[2],
            classes[4],
        ]

        self.analyzer.create_class_qname_index(classes)
        result = self.analyzer.fetch_classes_for_generation()
        self.assertEqual(expected, result)
        self.assertEqual(3, len(self.analyzer.common_types))

        expected = [
            "{http://namespace/target}" + classes[0].name,
            "{http://namespace/target}" + classes[3].name,
            "{http://namespace/target}" + classes[4].name,
        ]
        self.assertEqual(expected, list(self.analyzer.common_types.keys()))

    @mock.patch.object(ClassAnalyzer, "flatten_class")
    def test_flatten_classes(self, mock_flatten_class):
        classes = ClassFactory.list(2)
        self.analyzer.create_class_qname_index(classes)
        self.analyzer.flatten_classes()
        mock_flatten_class.assert_has_calls(list(map(mock.call, classes)))


class ClassAnalyzerFindClassTests(ClassAnalyzerBaseTestCase):
    def setUp(self) -> None:
        super(ClassAnalyzerFindClassTests, self).setUp()
        self.analyzer.schema = self.schema

    @mock.patch.object(ClassAnalyzer, "find_common_class")
    @mock.patch.object(ClassAnalyzer, "find_schema_class")
    def test_searches_in_class_index_and_common_types(
        self, mock_find_schema_class, mock_find_common_class
    ):
        mock_find_schema_class.side_effect = [None, "a"]
        mock_find_common_class.return_value = "b"

        dependency = AttrTypeFactory.create()
        qname = self.analyzer.qname(dependency.name)

        self.assertEqual("b", self.analyzer.find_class(dependency))
        self.assertEqual("a", self.analyzer.find_class(dependency))

        mock_find_schema_class.assert_has_calls(
            [
                mock.call(qname, condition=simple_type),
                mock.call(qname, condition=simple_type),
            ]
        )
        mock_find_common_class.assert_called_once_with(qname, condition=simple_type)

    @mock.patch.object(ClassAnalyzer, "flatten_class")
    def test_search_for_schema_class(self, mock_flatten_class):
        qname = "foo"
        class_a = ClassFactory.create()
        class_b = ClassFactory.create()
        self.analyzer.class_index[qname] = [class_a, class_b]
        self.analyzer.processed[class_b.key] = True

        self.assertIsNone(self.analyzer.find_schema_class("b"))

        actual = self.analyzer.find_schema_class(
            qname, condition=lambda x: x.name == class_b.name
        )
        self.assertEqual(class_b, actual)

        actual = self.analyzer.find_schema_class(qname, condition=None)
        self.assertEqual(class_a, actual)

        mock_flatten_class.assert_called_once_with(class_a)

    def test_search_for_common_class(self):
        qname = "foo"
        class_a = ClassFactory.create()
        self.analyzer.common_types[qname] = class_a

        self.assertIsNone(self.analyzer.find_common_class("b"))

        actual = self.analyzer.find_common_class(qname, condition=None)
        self.assertEqual(class_a, actual)

        actual = self.analyzer.find_common_class(
            qname, condition=lambda x: x.name == class_a.name
        )
        self.assertEqual(class_a, actual)

        actual = self.analyzer.find_common_class(
            qname, condition=lambda x: x.name == "$$$"
        )
        self.assertIsNone(actual)

    def test_is_self_referencing(self):
        item = ClassFactory.create()
        attr_type = AttrTypeFactory.create(name=item.name)
        attr = AttrFactory.create(types=[attr_type])
        item.attrs.append(attr)

        self.analyzer.create_class_qname_index([item])
        self.assertTrue(self.analyzer.is_self_referencing(item, attr_type))

        attr_type.name = "foobar"
        self.assertFalse(self.analyzer.is_self_referencing(item, attr_type))


class ClassAnalyzerFlattenClassTests(ClassAnalyzerBaseTestCase):
    @mock.patch.object(ClassAnalyzer, "flatten_enumeration_unions")
    @mock.patch.object(ClassAnalyzer, "flatten_attribute")
    @mock.patch.object(ClassAnalyzer, "flatten_extension")
    def test_basic(
        self,
        mock_flatten_extension,
        mock_flatten_attribute,
        mock_flatten_enumeration_unions,
    ):
        obj = ClassFactory.create(
            name="a",
            type=SimpleType,
            extensions=["b", "c"],
            attrs=[AttrFactory.create(name=x) for x in "de"],
            inner=[
                ClassFactory.create(
                    name="f",
                    type=SimpleType,
                    extensions=["g", "h"],
                    attrs=[AttrFactory.create(name=x) for x in "ij"],
                )
            ],
        )

        self.analyzer.flatten_class(obj)

        mock_flatten_enumeration_unions.assert_has_calls(
            [mock.call(obj), mock.call(obj.inner[0])]
        )

        mock_flatten_extension.assert_has_calls(
            [
                mock.call(obj, "b"),
                mock.call(obj, "c"),
                mock.call(obj.inner[0], "g"),
                mock.call(obj.inner[0], "h"),
            ]
        )
        mock_flatten_attribute.assert_has_calls(
            [
                mock.call(obj, obj.attrs[0]),
                mock.call(obj, obj.attrs[1]),
                mock.call(obj.inner[0], obj.inner[0].attrs[0]),
                mock.call(obj.inner[0], obj.inner[0].attrs[1]),
            ]
        )

    @mock.patch.object(ClassAnalyzer, "flatten_enumeration_unions")
    def test_skip_enumeration_unions_when_class_not_common(
        self, mock_flatten_enumeration_unions,
    ):
        obj = ClassFactory.create(type=Element)
        self.analyzer.flatten_class(obj)

        self.assertEqual(0, mock_flatten_enumeration_unions.call_count)


class ClassAnalyzerFlattenExtensionTests(ClassAnalyzerBaseTestCase):
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_no_common_is_found(self, mock_find_class):
        mock_find_class.return_value = None

        extension = ExtensionFactory.create()
        obj = ClassFactory.create(extensions=[extension])
        self.analyzer.flatten_extension(obj, extension)

        self.assertEqual(1, len(obj.extensions))
        mock_find_class.assert_called_once_with(extension.type)

    @mock.patch.object(ClassAnalyzer, "create_default_attribute")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_common_is_enumeration(
        self, mock_find_class, mock_create_default_attribute
    ):
        mock_find_class.return_value = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION)
        )

        extension = ExtensionFactory.create()
        obj = ClassFactory.create(extensions=[extension])

        self.analyzer.flatten_extension(obj, extension)

        self.assertEqual(0, len(obj.extensions))
        mock_create_default_attribute.assert_called_once_with(obj, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_class_is_not_enumeration(self, mock_find_class, mock_copy_attributes):
        common = ClassFactory.create(attrs=AttrFactory.list(2))
        mock_find_class.return_value = common

        extension = ExtensionFactory.create()
        obj = ClassFactory.create(extensions=[extension], attrs=AttrFactory.list(2))

        self.analyzer.flatten_extension(obj, extension)

        mock_copy_attributes.assert_called_once_with(common, obj, extension)
        self.assertEqual(0, len(obj.extensions))

    @mock.patch.object(ClassAnalyzer, "create_default_attribute")
    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_class_is_common(
        self, mock_find_class, mock_copy_attributes, mock_create_default_attribute
    ):
        item = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ELEMENT)
        )
        mock_find_class.return_value = item

        extension = ExtensionFactory.create()
        item.extensions.append(extension)

        self.analyzer.flatten_extension(item, extension)

        self.assertEqual(0, len(item.extensions))
        self.assertEqual(0, mock_copy_attributes.call_count)
        self.assertEqual(0, mock_create_default_attribute.call_count)

    @mock.patch.object(ClassAnalyzer, "create_default_attribute")
    def test_when_type_is_native(self, mock_create_default_attribute):
        extension = ExtensionFactory.create(type=AttrTypeFactory.create(native=True))
        item = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ELEMENT),
            extensions=[extension],
        )

        self.analyzer.flatten_extension(item, extension)
        self.assertEqual(0, len(item.extensions))
        mock_create_default_attribute.assert_called_once_with(item, extension)


class ClassAnalyzerHelpersTests(ClassAnalyzerBaseTestCase):
    def test_create_default_attribute(self):
        item = ClassFactory.create()
        extension = ExtensionFactory.create()

        ClassAnalyzer.create_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="value",
            index=0,
            default=None,
            types=[extension.type],
            local_type=TagType.EXTENSION,
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(expected, item.attrs[0])

    def test_create_default_attribute_with_any_type(self):
        item = ClassFactory.create()
        extension = ExtensionFactory.create(
            type=AttrTypeFactory.create(name=DataType.ANY_TYPE.code, native=True),
            restrictions=Restrictions(min_occurs=1, max_occurs=1, required=True),
        )

        ClassAnalyzer.create_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="##any_element",
            index=0,
            wildcard=True,
            default=None,
            types=[extension.type.clone()],
            local_type=TagType.ANY,
            restrictions=Restrictions(min_occurs=1, max_occurs=1, required=True),
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(expected, item.attrs[0])

    def test_create_default_attribute_with_any_type_defaults_to_list(self):
        item = ClassFactory.create()
        extension = ExtensionFactory.create(
            type=AttrTypeFactory.create(name=DataType.ANY_TYPE.code, native=True),
            restrictions=Restrictions(required=True),
        )

        ClassAnalyzer.create_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="##any_element",
            index=0,
            wildcard=True,
            default=list,
            types=[extension.type.clone()],
            local_type=TagType.ANY,
            restrictions=Restrictions(min_occurs=0, max_occurs=sys.maxsize),
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(expected, item.attrs[0])

    def test_copy_attributes(self):
        common_b = ClassFactory.create(
            attrs=[
                AttrFactory.create(name="i", types=AttrTypeFactory.list(1, name="i")),
                AttrFactory.create(
                    name="j", types=AttrTypeFactory.list(1, name="other:j")
                ),
            ]
        )
        common_c = ClassFactory.create(
            attrs=[
                AttrFactory.create(name="x", types=AttrTypeFactory.list(1, name="x")),
                AttrFactory.create(
                    name="y", types=AttrTypeFactory.list(1, name="other:y")
                ),
            ]
        )
        ext_b = ExtensionFactory.create(type=AttrTypeFactory.create(name="b", index=2))
        ext_c = ExtensionFactory.create(
            type=AttrTypeFactory.create(name="common:c", index=66)
        )

        obj = ClassFactory.create(
            name="foo",
            extensions=[ext_b, ext_c],
            attrs=[AttrFactory.create(name=x, index=ord(x)) for x in "ab"],
        )

        ClassAnalyzer.copy_attributes(common_b, obj, ext_b)
        ClassAnalyzer.copy_attributes(common_c, obj, ext_c)

        attrs = [
            ("i", "i"),
            ("j", "other:j"),
            ("x", "common:x"),
            ("y", "other:y"),
            ("a", "string"),
            ("b", "string"),
        ]
        self.assertEqual(
            attrs,
            [
                (attr.name, " ".join([attr_type.name for attr_type in attr.types]))
                for attr in obj.attrs
            ],
        )


class ClassAnalyzerFlattenAttributeTests(ClassAnalyzerBaseTestCase):
    @mock.patch.object(ClassAnalyzer, "is_self_referencing", return_value=False)
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_no_common_is_found(self, mock_find_class, mock_is_self_referencing):
        mock_find_class.return_value = None

        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create()
        attr = AttrFactory.create(name="a", types=[type_a])
        self.analyzer.flatten_attribute(parent, attr)

        self.assertEqual([type_a], attr.types)
        mock_find_class.assert_called_once_with(type_a)

    @mock.patch.object(ClassAnalyzer, "is_self_referencing", return_value=True)
    @mock.patch.object(ClassAnalyzer, "find_class", return_value=None)
    def test_when_attr_is_self_referencing(self, *args):
        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create()
        attr = AttrFactory.create(name="a", types=[type_a])
        self.analyzer.flatten_attribute(parent, attr)

        self.assertEqual([type_a], attr.types)
        self.assertTrue(type_a.self_ref)

    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_common_is_enumeration(self, mock_find_class):
        mock_find_class.return_value = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ENUMERATION)
        )

        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create(name="a")
        attr = AttrFactory.create(name="a", types=[type_a])
        self.analyzer.flatten_attribute(parent, attr)

        self.assertEqual([type_a], attr.types)
        mock_find_class.assert_called_once_with(type_a)

    @mock.patch.object(ClassAnalyzer, "copy_inner_classes")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_common_class_has_only_one_attribute(
        self, mock_find_class, mock_copy_inner_classes
    ):
        type_a = AttrTypeFactory.create(name="a")
        type_b = AttrTypeFactory.create(name="b")
        common = ClassFactory.create(
            name="bar",
            attrs=AttrFactory.list(
                1,
                name="b",
                types=[type_b],
                restrictions=RestrictionsFactory.create(required=True, min_occurs=2),
            ),
        )

        mock_find_class.return_value = common

        parent = ClassFactory.create()
        attr = AttrFactory.create(
            name="a",
            types=[type_a],
            restrictions=RestrictionsFactory.create(min_occurs=1),
        )

        self.analyzer.flatten_attribute(parent, attr)

        self.assertEqual([type_b], attr.types)
        self.assertEqual(
            {"required": True, "min_occurs": 1}, attr.restrictions.asdict()
        )
        mock_find_class.assert_called_once_with(type_a)
        mock_copy_inner_classes.assert_called_once_with(common, parent)

    @mock.patch("xsdata.analyzer.logger.warning")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_common_class_has_more_than_one_attribute(
        self, mock_find_class, mock_logger_warning
    ):
        type_a = AttrTypeFactory.create(name="a")
        type_str = AttrType(name=DataType.STRING.code, native=True)
        common = ClassFactory.create(name="bar", attrs=AttrFactory.list(2))
        mock_find_class.return_value = common

        parent = ClassFactory.create()
        attr = AttrFactory.create(name="a", types=[type_a])

        self.analyzer.flatten_attribute(parent, attr)

        self.assertEqual([type_str], attr.types)
        mock_logger_warning.assert_called_once_with(
            "Missing type implementation: %s", common.type.__name__
        )


class ClassAnalyzerFlattenEnumerationUnionsTests(ClassAnalyzerBaseTestCase):
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_merge_enumeration_into_the_target_class(self, mock_find_class):
        enum_a = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION)
        )
        enum_b = ClassFactory.create(
            attrs=AttrFactory.list(3, local_type=TagType.ENUMERATION)
        )

        mock_find_class.return_value = enum_b

        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    name="value",
                    types=[
                        AttrTypeFactory.create(name=enum_a.name, forward_ref=True),
                        AttrTypeFactory.create(name=enum_b.name),
                    ],
                )
            ],
            inner=[enum_a],
        )

        self.assertFalse(obj.is_enumeration)

        self.analyzer.flatten_enumeration_unions(obj)

        self.assertTrue(obj.is_enumeration)
        self.assertEqual(5, len(obj.attrs))
        self.assertEqual(
            ["attr_B", "attr_C", "attr_D", "attr_E", "attr_F"],
            [attr.name for attr in obj.attrs],
        )


class ClassAnalyzerMergeClassesTests(ClassAnalyzerBaseTestCase):
    def test_with_unique_classes(self):
        classes = ClassFactory.list(2)
        self.analyzer.merge_redefined_classes(classes)
        self.assertEqual(2, len(classes))

    def test_raises_exception_with_more_than_two_redefines(self):
        class_a = ClassFactory.create()
        class_b = class_a.clone()
        class_c = class_a.clone()

        classes = [class_a, class_b, class_c]
        with self.assertRaises(AnalyzerValueError) as cm:
            self.analyzer.merge_redefined_classes(classes)

        self.assertEqual("Redefined class `class_B` more than once.", str(cm.exception))

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    def test_copies_attributes(self, mock_copy_attributes):
        class_a = ClassFactory.create()
        class_b = ClassFactory.create()
        class_c = class_a.clone()

        ext_a = ExtensionFactory.create(type=AttrTypeFactory.create(name=class_a.name))
        ext_str = ExtensionFactory.create(type=AttrTypeFactory.create(name="foo"))
        class_c.extensions.append(ext_a)
        class_c.extensions.append(ext_str)
        classes = [class_a, class_b, class_c]

        self.analyzer.merge_redefined_classes(classes)
        self.assertEqual(2, len(classes))

        mock_copy_attributes.assert_called_once_with(class_a, class_c, ext_a)
        self.assertEqual([ext_str], class_c.extensions)

    def test_copies_extensions(self):
        class_a = ClassFactory.create()
        class_c = class_a.clone()

        type_int = AttrTypeFactory.create(name=DataType.INTEGER.code, native=True,)

        ext_a = ExtensionFactory.create(
            type=type_int,
            restrictions=Restrictions(max_inclusive=10, min_inclusive=1, required=True),
        )
        ext_c = ExtensionFactory.create(
            type=AttrTypeFactory.create(name=class_a.name),
            restrictions=Restrictions(max_inclusive=0, min_inclusive=-10),
        )

        class_a.extensions.append(ext_a)
        class_c.extensions.append(ext_c)
        classes = [class_a, class_c]
        expected = {"max_inclusive": 0, "min_inclusive": -10, "required": True}

        self.analyzer.merge_redefined_classes(classes)
        self.assertEqual(1, len(classes))
        self.assertEqual(1, len(classes[0].extensions))
        self.assertEqual(expected, classes[0].extensions[0].restrictions.asdict())
