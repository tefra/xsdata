from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from tests.factories import RestrictionsFactory
from xsdata.analyzer import ClassAnalyzer
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Restrictions
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
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
        self.analyzer = ClassAnalyzer()


class ClassAnalyzerTests(ClassAnalyzerBaseTestCase):
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
        gen_classes = ClassFactory.list(2)
        mock_fetch_classes_for_generation.return_value = gen_classes
        classes = ClassFactory.list(3, type=Element)

        self.assertEqual(gen_classes, self.analyzer.process(classes))

        mock_merge_redefined_classes.assert_called_once_with(classes)
        mock_create_class_qname_index.assert_called_once_with(classes)
        mock_mark_abstract_duplicate_classes.assert_called_once()
        mock_flatten_classes.assert_called_once_with()
        mock_fetch_classes_for_generation.assert_called_once_with()

    def test_create_class_qname_index(self):
        classes = [
            ClassFactory.create(type=Element, name="foo"),
            ClassFactory.create(type=ComplexType, name="foo"),
            ClassFactory.create(type=ComplexType, name="foobar"),
        ]

        expected = {
            "{xsdata}foo": classes[:2],
            "{xsdata}foobar": classes[2:],
        }

        self.analyzer.create_class_qname_index(classes)
        self.assertEqual(2, len(self.analyzer.class_index))
        self.assertEqual(expected, self.analyzer.class_index)

    def test_mark_abstract_duplicate_classes(self):
        one = ClassFactory.create(name="foo", abstract=True, type=Element)
        two = ClassFactory.create(name="foo", type=Element)
        three = ClassFactory.create(name="foo", type=ComplexType)
        four = ClassFactory.create(name="foo", type=SimpleType)

        five = ClassFactory.create(name="bar", abstract=True, type=Element)
        six = ClassFactory.create(name="bar", type=ComplexType)
        seven = ClassFactory.create(name="opa", type=ComplexType)

        self.analyzer.create_class_qname_index(
            [one, two, three, four, five, six, seven]
        )
        self.analyzer.mark_abstract_duplicate_classes()

        self.assertTrue(one.abstract)  # Was abstract already
        self.assertFalse(two.abstract)  # Is an element
        self.assertTrue(three.abstract)  # Marked as abstract
        self.assertFalse(four.abstract)  # Is common
        self.assertTrue(five.abstract)  # Was abstract already
        self.assertFalse(six.abstract)  # No element in group
        self.assertFalse(seven.abstract)  # Alone

    def test_fetch_classes_for_generation(self):
        classes = [
            ClassFactory.create(abstract=True, type=Element),
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

    def test_fetch_classes_for_generation_return_simple_when_no_complex_types(self):
        classes = ClassFactory.list(2, type=SimpleType)
        self.analyzer.create_class_qname_index(classes)

        actual = self.analyzer.fetch_classes_for_generation()
        self.assertEqual(classes, actual)

    @mock.patch.object(ClassAnalyzer, "flatten_class")
    def test_flatten_classes(self, mock_flatten_class):
        classes = ClassFactory.list(2)
        self.analyzer.create_class_qname_index(classes)
        self.analyzer.flatten_classes()
        mock_flatten_class.assert_has_calls(list(map(mock.call, classes)))

    @mock.patch.object(ClassAnalyzer, "flatten_class")
    def test_find_class(self, mock_flatten_class):
        qname = "foo"
        class_a = ClassFactory.create()
        class_b = ClassFactory.create()
        self.analyzer.class_index[qname] = [class_a, class_b]
        self.analyzer.processed[class_b.key] = True

        self.assertIsNone(self.analyzer.find_class("b"))

        actual = self.analyzer.find_class(
            qname, condition=lambda x: x.name == class_b.name
        )
        self.assertEqual(class_b, actual)

        actual = self.analyzer.find_class(qname, condition=None)
        self.assertEqual(class_a, actual)

        mock_flatten_class.assert_called_once_with(class_a)

    def test_is_self_referencing(self):
        item = ClassFactory.create()
        attr_type = AttrTypeFactory.create(name=item.name)
        attr = AttrFactory.create(types=[attr_type])
        item.attrs.append(attr)

        self.analyzer.create_class_qname_index([item])
        self.assertTrue(self.analyzer.is_attribute_self_reference(item, attr_type))

        attr_type.name = "foobar"
        self.assertFalse(self.analyzer.is_attribute_self_reference(item, attr_type))

    @mock.patch.object(ClassAnalyzer, "flatten_enumeration_unions")
    @mock.patch.object(ClassAnalyzer, "flatten_attribute")
    @mock.patch.object(ClassAnalyzer, "flatten_extension")
    def test_flatten_class(
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
                mock.call(obj, "c"),
                mock.call(obj, "b"),
                mock.call(obj.inner[0], "h"),
                mock.call(obj.inner[0], "g"),
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
    def test_test_flatten_when_target_is_not_common(
        self, mock_flatten_enumeration_unions
    ):
        obj = ClassFactory.create(type=Element)
        self.analyzer.flatten_class(obj)

        self.assertEqual(0, mock_flatten_enumeration_unions.call_count)

    @mock.patch.object(ClassAnalyzer, "create_default_attribute")
    def test_flatten_extension_with_native_type_and_target_not_enumeration(
        self, mock_create_default_attribute
    ):
        extension = ExtensionFactory.create(type=AttrTypeFactory.create(native=True))
        target = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ELEMENT),
            extensions=[extension],
        )

        self.analyzer.flatten_extension(target, extension)
        mock_create_default_attribute.assert_called_once_with(target, extension)

    @mock.patch.object(ClassAnalyzer, "flatten_extension_simple")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_flatten_extension_with_simple_source_extension(
        self, mock_find_class, mock_flatten_extension_simple
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()
        mock_find_class.return_value = source

        self.analyzer.flatten_extension(target, extension)

        type_qname = target.source_qname(extension.type.name)
        mock_find_class.assert_called_once_with(type_qname)
        mock_flatten_extension_simple.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "flatten_extension_complex")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_flatten_extension_with_complex_source_extension(
        self, mock_find_class, mock_flatten_extension_complex
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()
        mock_find_class.side_effect = [None, source]

        self.analyzer.flatten_extension(target, extension)
        type_qname = target.source_qname(extension.type.name)
        mock_find_class.assert_has_calls(
            [mock.call(type_qname), mock.call(type_qname, condition=None)]
        )
        mock_flatten_extension_complex.assert_called_once_with(
            source, target, extension
        )

    def test_flatten_extension_simple_when_target_is_source(self):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        self.analyzer.flatten_extension_simple(target, target, extension)
        self.assertEqual(0, len(target.extensions))

    @mock.patch.object(ClassAnalyzer, "create_default_attribute")
    def test_flatten_extension_simple_when_source_is_enumeration_and_target_is_not(
        self, mock_create_default_attribute
    ):
        source = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION)
        )
        target = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ELEMENT)
        )
        extension = ExtensionFactory.create()

        self.analyzer.flatten_extension_simple(source, target, extension)
        mock_create_default_attribute.assert_called_once_with(target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "create_default_attribute")
    def test_flatten_extension_simple_when_target_is_enumeration_and_source_is_not(
        self, mock_create_default_attribute, mock_copy_attributes
    ):
        extension = ExtensionFactory.create()
        source = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ELEMENT)
        )
        target = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ENUMERATION),
            extensions=[extension],
        )

        self.analyzer.flatten_extension_simple(source, target, extension)
        self.assertEqual(0, mock_create_default_attribute.call_count)
        self.assertEqual(0, mock_copy_attributes.call_count)
        self.assertEqual(0, len(target.extensions))

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    def test_flatten_extension_simple_when_source_and_target_are_enumerations(
        self, mock_copy_attributes
    ):
        source = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION)
        )
        target = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ENUMERATION)
        )
        extension = ExtensionFactory.create()

        self.analyzer.flatten_extension_simple(source, target, extension)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    def test_flatten_extension_simple_when_source_and_target_are_not_enumerations(
        self, mock_copy_attributes
    ):
        source = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ELEMENT)
        )
        target = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ELEMENT)
        )
        extension = ExtensionFactory.create()

        self.analyzer.flatten_extension_simple(source, target, extension)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    def test_flatten_extension_complex_when_target_is_source(self):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        self.analyzer.flatten_extension_complex(target, target, extension)
        self.assertEqual(0, len(target.extensions))

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    def test_flatten_extension_complex_when_source_and_target_equal(
        self, mock_copy_attributes
    ):
        source = ClassFactory.create(attrs=AttrFactory.list(2))
        target = source.clone()
        extension = ExtensionFactory.create()
        target.extensions.append(extension)

        self.analyzer.flatten_extension_complex(source, target, extension)
        self.assertEqual(0, len(target.extensions))
        self.assertEqual(0, mock_copy_attributes.call_count)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    def test_flatten_extension_complex_when_source_and_target_have_mixed_attributes(
        self, mock_copy_attributes
    ):
        source = ClassFactory.create(attrs=AttrFactory.list(2))
        target = source.clone()
        source.attrs.append(AttrFactory.create())
        target.attrs.append(AttrFactory.create())

        extension = ExtensionFactory.create()
        target.extensions.append(extension)

        self.analyzer.flatten_extension_complex(source, target, extension)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    def test_flatten_extension_complex_when_source_and_target_have_no_common_attributes(
        self, mock_copy_attributes
    ):
        source = ClassFactory.create(attrs=AttrFactory.list(2))
        target = ClassFactory.create(attrs=AttrFactory.list(2))
        extension = ExtensionFactory.create()
        target.extensions.append(extension)

        self.analyzer.flatten_extension_complex(source, target, extension)
        self.assertEqual(1, len(target.extensions))
        self.assertEqual(0, mock_copy_attributes.call_count)


class ClassAnalyzerHelpersTests(ClassAnalyzerBaseTestCase):
    def test_create_default_attribute(self):
        extension = ExtensionFactory.create()
        item = ClassFactory.create(extensions=[extension])

        ClassAnalyzer.create_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="value",
            index=0,
            default=None,
            types=[extension.type],
            local_type=TagType.EXTENSION,
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(0, len(item.extensions))
        self.assertEqual(expected, item.attrs[0])

    def test_create_default_attribute_with_any_type(self):
        extension = ExtensionFactory.create(
            type=AttrTypeFactory.create(name=DataType.ANY_TYPE.code, native=True),
            restrictions=Restrictions(min_occurs=1, max_occurs=1, required=True),
        )
        item = ClassFactory.create(extensions=[extension])

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
        self.assertEqual(0, len(item.extensions))
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
            type=AttrTypeFactory.create(name="common:c", index=111)
        )

        obj = ClassFactory.create(
            name="foo",
            extensions=[ext_b, ext_c],
            attrs=[AttrFactory.create(name=x, index=ord(x)) for x in "ab"],
        )

        ClassAnalyzer.copy_attributes(common_b, obj, ext_b)
        self.assertEqual(1, len(obj.extensions))

        ClassAnalyzer.copy_attributes(common_c, obj, ext_c)
        self.assertEqual(0, len(obj.extensions))

        attrs = [
            ("i", "i"),
            ("j", "other:j"),
            ("a", "string"),
            ("b", "string"),
            ("x", "common:x"),
            ("y", "other:y"),
        ]
        self.assertEqual(
            attrs,
            [
                (attr.name, " ".join([attr_type.name for attr_type in attr.types]))
                for attr in obj.attrs
            ],
        )


class ClassAnalyzerFlattenAttributeTests(ClassAnalyzerBaseTestCase):
    @mock.patch.object(ClassAnalyzer, "is_attribute_self_reference", return_value=False)
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_no_source_is_found(
        self, mock_find_class, mock_is_attribute_self_reference
    ):
        mock_find_class.return_value = None

        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create()
        attr = AttrFactory.create(name="a", types=[type_a])
        self.analyzer.flatten_attribute(parent, attr)

        self.assertEqual([type_a], attr.types)
        self.assertFalse(type_a.self_ref)
        mock_find_class.assert_called_once_with(parent.source_qname(type_a.name))
        mock_is_attribute_self_reference.assert_called_once_with(parent, type_a)

    @mock.patch.object(ClassAnalyzer, "is_attribute_self_reference", return_value=True)
    @mock.patch.object(ClassAnalyzer, "find_class", return_value=None)
    def test_when_is_attribute_self_reference(self, *args):
        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create()
        attr = AttrFactory.create(name="a", types=[type_a])
        self.analyzer.flatten_attribute(parent, attr)

        self.assertEqual([type_a], attr.types)
        self.assertTrue(type_a.self_ref)

    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_source_is_enumeration(self, mock_find_class):
        mock_find_class.return_value = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ENUMERATION)
        )

        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create(name="a")
        attr = AttrFactory.create(name="a", types=[type_a])
        self.analyzer.flatten_attribute(parent, attr)

        self.assertEqual([type_a], attr.types)
        mock_find_class.assert_called_once_with(parent.source_qname(type_a.name))

    @mock.patch.object(ClassAnalyzer, "copy_inner_classes")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_source_has_only_one_attribute(
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
        mock_find_class.assert_called_once_with(parent.source_qname(type_a.name))
        mock_copy_inner_classes.assert_called_once_with(common, parent)

    @mock.patch("xsdata.analyzer.logger.warning")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_when_source_has_more_than_one_attribute(
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
