import sys
from unittest import mock

from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.analyzer import ClassAnalyzer
from xsdata.exceptions import AnalyzerError
from xsdata.models.codegen import Class
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import SimpleType
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace


class ClassAnalyzerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.target_namespace = "http://namespace/target"
        self.ns_map = {
            None: "http://namespace/foobar",
            "common": "http://namespace/common",
        }
        self.analyzer = ClassAnalyzer()

    @mock.patch.object(ClassAnalyzer, "fetch_classes_for_generation")
    @mock.patch.object(ClassAnalyzer, "sanitize_classes")
    @mock.patch.object(ClassAnalyzer, "flatten_classes")
    @mock.patch.object(ClassAnalyzer, "create_substitutions_index")
    @mock.patch.object(ClassAnalyzer, "handle_duplicate_classes")
    @mock.patch.object(ClassAnalyzer, "create_class_index")
    def test_process(
        self,
        mock_create_class_index,
        mock_handle_duplicates,
        mock_create_substitutions_index,
        mock_flatten_classes,
        mock_sanitize_classes,
        mock_fetch_classes_for_generation,
    ):
        gen_classes = ClassFactory.list(2)
        mock_fetch_classes_for_generation.return_value = gen_classes
        classes = ClassFactory.list(3, type=Element)

        self.assertEqual(gen_classes, self.analyzer.process(classes))

        mock_create_class_index.assert_called_once_with(classes)
        mock_handle_duplicates.assert_called_once()
        mock_create_substitutions_index.assert_called_once_with()
        mock_flatten_classes.assert_called_once_with()
        mock_sanitize_classes.assert_called_once_with()
        mock_fetch_classes_for_generation.assert_called_once_with()

    @mock.patch.object(ClassAnalyzer, "update_abstract_classes")
    @mock.patch.object(ClassAnalyzer, "merge_redefined_classes")
    @mock.patch.object(ClassAnalyzer, "remove_invalid_classes")
    def test_handle_duplicate_classes(
        self,
        mock_remove_invalid_classes,
        mock_merge_redefined_classes,
        mock_update_abstract_classes,
    ):
        first = ClassFactory.create()
        second = first.clone()
        third = ClassFactory.create()

        self.analyzer.create_class_index([first, second, third])
        self.analyzer.handle_duplicate_classes()

        mock_remove_invalid_classes.assert_called_once_with([first, second])
        mock_merge_redefined_classes.assert_called_once_with([first, second])
        mock_update_abstract_classes.assert_called_once_with([first, second])

    def test_remove_invalid_classes(self):
        first = ClassFactory.create(
            extensions=[
                ExtensionFactory.create(type=AttrTypeFactory.xs_bool()),
                ExtensionFactory.create(type=AttrTypeFactory.create(name="foo")),
            ]
        )
        second = ClassFactory.create(
            extensions=[ExtensionFactory.create(type=AttrTypeFactory.xs_bool()),]
        )
        third = ClassFactory.create()

        self.analyzer.create_class_index([first, second, third])

        classes = [first, second, third]
        self.analyzer.remove_invalid_classes(classes)
        self.assertEqual([second, third], classes)

    def test_create_class_index(self):
        classes = [
            ClassFactory.create(type=Element, name="foo"),
            ClassFactory.create(type=ComplexType, name="foo"),
            ClassFactory.create(type=ComplexType, name="foobar"),
        ]

        expected = {
            "{xsdata}foo": classes[:2],
            "{xsdata}foobar": classes[2:],
        }

        self.analyzer.create_class_index(classes)
        self.assertEqual(2, len(self.analyzer.class_index))
        self.assertEqual(expected, self.analyzer.class_index)

    @mock.patch.object(ClassAnalyzer, "create_reference_attribute")
    def test_create_substitutions_index(self, mock_create_reference_attribute):
        classes = [
            ClassFactory.create(substitutions=["foo", "bar"], abstract=True),
            ClassFactory.create(substitutions=["foo"], abstract=True),
        ]

        namespace = classes[0].source_namespace
        reference_attrs = AttrFactory.list(3)
        mock_create_reference_attribute.side_effect = reference_attrs

        self.analyzer.create_class_index(classes)
        self.analyzer.create_substitutions_index()

        expected = {
            QName(namespace, "foo"): [reference_attrs[0], reference_attrs[2]],
            QName(namespace, "bar"): [reference_attrs[1]],
        }
        self.assertEqual(expected, self.analyzer.substitutions_index)
        self.assertFalse(classes[0].abstract)
        self.assertFalse(classes[1].abstract)

        mock_create_reference_attribute.assert_has_calls(
            [
                mock.call(classes[0], classes[0].source_qname("foo")),
                mock.call(classes[0], classes[0].source_qname("bar")),
                mock.call(classes[1], classes[1].source_qname("foo")),
            ]
        )

    def test_fetch_classes_for_generation(self):
        classes = [
            ClassFactory.create(abstract=True, type=Element),
            ClassFactory.create(type=Element),
            ClassFactory.create(type=ComplexType),
            ClassFactory.create(type=SimpleType),
            ClassFactory.enumeration(2),
        ]
        self.analyzer.create_class_index(classes)

        expected = [
            classes[1],
            classes[2],
            classes[4],
        ]

        result = self.analyzer.fetch_classes_for_generation()
        self.assertEqual(expected, result)

    def test_fetch_classes_for_generation_when_no_complex_class_available(self):
        classes = [ClassFactory.enumeration(2), ClassFactory.create(type=SimpleType)]
        self.analyzer.create_class_index(classes)

        actual = self.analyzer.fetch_classes_for_generation()
        self.assertEqual(classes, actual)

    @mock.patch.object(ClassAnalyzer, "flatten_class")
    def test_flatten_classes(self, mock_flatten_class):
        classes = ClassFactory.list(2)
        self.analyzer.create_class_index(classes)
        self.analyzer.flatten_classes()
        mock_flatten_class.assert_has_calls(list(map(mock.call, classes)))

    @mock.patch.object(ClassAnalyzer, "flatten_class")
    def test_find_class(self, mock_flatten_class):
        qname = "foo"
        class_a = ClassFactory.create()
        class_b = ClassFactory.create()
        self.analyzer.class_index[qname] = [class_a, class_b]
        self.analyzer.processed.append(id(class_b))

        self.assertIsNone(self.analyzer.find_class("b"))

        actual = self.analyzer.find_class(
            qname, condition=lambda x: x.name == class_b.name
        )
        self.assertEqual(class_b, actual)

        actual = self.analyzer.find_class(qname, condition=None)
        self.assertEqual(class_a, actual)

        mock_flatten_class.assert_called_once_with(class_a)

    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_find_attr_type(self, mock_find_class):
        target = ClassFactory.create()
        type_a = AttrTypeFactory.create()
        source = ClassFactory.create()

        mock_find_class.return_value = source

        actual = self.analyzer.find_attr_type(target, type_a)
        self.assertEqual(source, actual)
        mock_find_class.assert_called_once_with(source.source_qname(type_a.name))

    def test_find_attr_simple_type(self):
        a = ClassFactory.enumeration(1, name="a")
        b = ClassFactory.elements(1, name="b", abstract=True)
        c = ClassFactory.elements(1, name="c")
        type_a = AttrTypeFactory.create(name="a")
        type_b = AttrTypeFactory.create(name="b")
        type_c = AttrTypeFactory.create(name="c")

        self.analyzer.create_class_index([a, b, c])

        self.assertIsNone(self.analyzer.find_attr_simple_type(a, type_a))  # Enumeration
        self.assertIsNone(self.analyzer.find_attr_simple_type(a, type_c))  # Complex
        self.assertIsNone(
            self.analyzer.find_attr_simple_type(b, type_b)
        )  # Source is target
        self.assertEqual(b, self.analyzer.find_attr_simple_type(a, type_b))

    def test_find_simple_class(self):
        a = ClassFactory.enumeration(1, name="a")
        b = ClassFactory.create(name="b", type=SimpleType)
        c = ClassFactory.elements(1, name="c", abstract=True)
        d = ClassFactory.elements(1, name="d")

        self.analyzer.create_class_index([a, b, c, d])

        self.assertEqual(a, self.analyzer.find_simple_class(a.source_qname()))
        self.assertEqual(b, self.analyzer.find_simple_class(b.source_qname()))
        self.assertEqual(c, self.analyzer.find_simple_class(c.source_qname()))
        self.assertIsNone(self.analyzer.find_simple_class(d.source_qname()))

    @mock.patch.object(ClassAnalyzer, "merge_duplicate_attributes")
    @mock.patch.object(ClassAnalyzer, "create_mixed_attribute")
    @mock.patch.object(ClassAnalyzer, "add_substitution_attrs")
    @mock.patch.object(ClassAnalyzer, "flatten_attribute_types")
    @mock.patch.object(ClassAnalyzer, "flatten_extension")
    @mock.patch.object(ClassAnalyzer, "expand_attribute_group")
    def test_flatten_class(
        self,
        mock_expand_attribute_group,
        mock_flatten_extension,
        mock_flatten_attribute_types,
        mock_add_substitution_attrs,
        mock_create_mixed_attribute,
        mock_merge_duplicate_attributes,
    ):
        inner = ClassFactory.list(2)
        extensions = ExtensionFactory.list(2)
        target = ClassFactory.elements(2, inner=inner, extensions=extensions)

        self.analyzer.flatten_class(target)

        mock_expand_attribute_group.assert_has_calls(
            [mock.call(target, target.attrs[0]), mock.call(target, target.attrs[1])]
        )

        mock_flatten_extension.assert_has_calls(
            [
                mock.call(target, target.extensions[1]),
                mock.call(target, target.extensions[0]),
            ]
        )

        mock_flatten_attribute_types.assert_has_calls(
            [mock.call(target, target.attrs[0]), mock.call(target, target.attrs[1])]
        )

        mock_add_substitution_attrs.assert_has_calls(
            [mock.call(target, target.attrs[0]), mock.call(target, target.attrs[1])]
        )

        mock_create_mixed_attribute.assert_has_calls(
            [mock.call(target), mock.call(inner[0]), mock.call(inner[1])]
        )

        mock_merge_duplicate_attributes.assert_has_calls(
            [mock.call(target), mock.call(inner[0]), mock.call(inner[1])]
        )

    @mock.patch.object(ClassAnalyzer, "flatten_extension_native")
    def test_flatten_extension_with_native_type(self, mock_flatten_extension_native):
        extension = ExtensionFactory.create(type=AttrTypeFactory.xs_string())
        target = ClassFactory.elements(1, extensions=[extension])

        self.analyzer.flatten_extension(target, extension)
        mock_flatten_extension_native.assert_called_once_with(target, extension)

    @mock.patch.object(ClassAnalyzer, "create_default_attribute")
    def test_flatten_extension_native(self, mock_create_default_attribute):
        extension = ExtensionFactory.create()
        target = ClassFactory.elements(1)

        self.analyzer.flatten_extension_native(target, extension)
        mock_create_default_attribute.assert_called_once_with(target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_extension_type")
    def test_flatten_extension_native_and_target_enumeration(
        self, mock_copy_extension_type
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.enumeration(1)

        self.analyzer.flatten_extension_native(target, extension)
        mock_copy_extension_type.assert_called_once_with(target, extension)

    @mock.patch.object(ClassAnalyzer, "flatten_extension_simple")
    @mock.patch.object(ClassAnalyzer, "find_simple_class")
    def test_flatten_extension_with_simple_source_extension(
        self, mock_find_simple_class, mock_flatten_extension_simple
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()
        mock_find_simple_class.return_value = source

        self.analyzer.flatten_extension(target, extension)

        type_qname = target.source_qname(extension.type.name)
        mock_find_simple_class.assert_called_once_with(type_qname)
        mock_flatten_extension_simple.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "flatten_extension_complex")
    @mock.patch.object(ClassAnalyzer, "find_simple_class")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_flatten_extension_with_complex_source_extension(
        self, mock_find_class, mock_find_simple_class, mock_flatten_extension_complex
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()
        mock_find_simple_class.return_value = None
        mock_find_class.return_value = source

        self.analyzer.flatten_extension(target, extension)
        type_qname = target.source_qname(extension.type.name)
        mock_find_simple_class.assert_called_once_with(type_qname)
        mock_find_class.assert_called_once_with(type_qname)
        mock_flatten_extension_complex.assert_called_once_with(
            source, target, extension
        )

    @mock.patch("xsdata.analyzer.logger.warning")
    def test_flatten_extension_with_unknown_extension_type(self, mock_logger_warning):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])

        self.analyzer.flatten_extension(target, extension)
        self.assertEqual(0, len(target.extensions))
        mock_logger_warning.assert_called_once_with(
            "Missing extension type: %s", extension.type.name
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
        source = ClassFactory.enumeration(2)
        target = ClassFactory.elements(1)
        extension = ExtensionFactory.create()

        self.analyzer.flatten_extension_simple(source, target, extension)
        mock_create_default_attribute.assert_called_once_with(target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "create_default_attribute")
    def test_flatten_extension_simple_when_target_is_enumeration_and_source_is_not(
        self, mock_create_default_attribute, mock_copy_attributes
    ):
        extension = ExtensionFactory.create()
        source = ClassFactory.elements(2)
        target = ClassFactory.enumeration(1, extensions=[extension])

        self.analyzer.flatten_extension_simple(source, target, extension)
        self.assertEqual(0, mock_create_default_attribute.call_count)
        self.assertEqual(0, mock_copy_attributes.call_count)
        self.assertEqual(0, len(target.extensions))

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    def test_flatten_extension_simple_when_source_and_target_are_enumerations(
        self, mock_copy_attributes
    ):
        source = ClassFactory.enumeration(2)
        target = ClassFactory.enumeration(1)
        extension = ExtensionFactory.create()

        self.analyzer.flatten_extension_simple(source, target, extension)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    def test_flatten_extension_simple_when_source_and_target_are_not_enumerations(
        self, mock_copy_attributes
    ):
        source = ClassFactory.elements(2)
        target = ClassFactory.elements(1)
        extension = ExtensionFactory.create()

        self.analyzer.flatten_extension_simple(source, target, extension)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "compare_attributes")
    def test_flatten_extension_complex_when_target_includes_all_source_attrs(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = self.analyzer.INCLUDES_ALL
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()

        self.analyzer.flatten_extension_complex(source, target, extension)

        self.assertEqual(0, len(target.extensions))

        mock_compare_attributes.assert_called_once_with(source, target)
        self.assertEqual(0, mock_copy_attributes.call_count)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "compare_attributes")
    def test_flatten_extension_complex_when_target_includes_some_source_attrs(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = self.analyzer.INCLUDES_SOME
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create()

        self.analyzer.flatten_extension_complex(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "compare_attributes")
    def test_flatten_extension_complex_when_target_includes_no_source_attrs(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = self.analyzer.INCLUDES_NONE
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()

        self.analyzer.flatten_extension_complex(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        self.assertEqual(0, mock_copy_attributes.call_count)
        self.assertEqual(1, len(target.extensions))

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "compare_attributes")
    def test_flatten_extension_complex_when_source_is_abstract(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = self.analyzer.INCLUDES_NONE
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create(abstract=True)

        self.analyzer.flatten_extension_complex(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "compare_attributes")
    def test_flatten_extension_complex_when_target_is_abstract(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = self.analyzer.INCLUDES_NONE
        extension = ExtensionFactory.create()
        target = ClassFactory.create(abstract=True)
        source = ClassFactory.create()

        self.analyzer.flatten_extension_complex(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "class_depends_on")
    @mock.patch.object(ClassAnalyzer, "compare_attributes")
    def test_flatten_extension_complex_when_source_has_suffix_attr(
        self, mock_compare_attributes, mock_class_depends_on_class, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = self.analyzer.INCLUDES_NONE
        mock_class_depends_on_class.return_value = False
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create()
        source.attrs.append(AttrFactory.create(index=sys.maxsize))

        self.analyzer.flatten_extension_complex(source, target, extension)
        self.assertEqual(0, len(target.attrs))

        target.attrs.append(AttrFactory.create())
        self.analyzer.flatten_extension_complex(source, target, extension)

        self.assertEqual(2, mock_compare_attributes.call_count)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "copy_attributes")
    @mock.patch.object(ClassAnalyzer, "class_depends_on")
    @mock.patch.object(ClassAnalyzer, "compare_attributes")
    def test_flatten_extension_complex_when_target_has_suffix_attr(
        self, mock_compare_attributes, mock_class_depends_on_class, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = self.analyzer.INCLUDES_NONE
        mock_class_depends_on_class.return_value = False
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create()
        target.attrs.append(AttrFactory.create(index=sys.maxsize))

        self.analyzer.flatten_extension_complex(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassAnalyzer, "clone_attribute")
    @mock.patch.object(ClassAnalyzer, "find_class")
    def test_expand_attribute_group(self, mock_find_class, mock_clone_attribute):
        source = ClassFactory.elements(2)
        group_attr = AttrFactory.attribute_group(name="foo:bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)

        mock_find_class.return_value = source
        mock_clone_attribute.side_effect = lambda x, y, z: x.clone()

        self.analyzer.expand_attribute_group(target, group_attr)

        self.assertEqual(2, len(target.attrs))
        self.assertIsNot(source.attrs[0], target.attrs[0])
        self.assertIsNot(source.attrs[1], target.attrs[1])
        self.assertNotIn(group_attr, target.attrs)

        mock_clone_attribute.assert_has_calls(
            [
                mock.call(source.attrs[0], group_attr.restrictions, "foo"),
                mock.call(source.attrs[1], group_attr.restrictions, "foo"),
            ]
        )

    def test_expand_attribute_group_with_unknown_source(self):
        group_attr = AttrFactory.attribute_group(name="foo:bar")
        target = ClassFactory.create()
        target.attrs.append(group_attr)

        with self.assertRaises(AnalyzerError) as cm:
            self.analyzer.expand_attribute_group(target, group_attr)

        self.assertEqual("Group attribute not found: `{foo}bar`", str(cm.exception))

    def test_flatten_attribute_types_when_type_is_native(self):
        xs_bool = AttrTypeFactory.xs_bool()
        xs_decimal = AttrTypeFactory.xs_decimal()
        attr = AttrFactory.create(types=[xs_bool, xs_decimal])
        target = ClassFactory.create()
        self.analyzer.flatten_attribute_types(target, attr)

        self.assertEqual([xs_bool, xs_decimal], attr.types)

        self.analyzer.flatten_attribute_types(target, attr)
        self.assertEqual([xs_bool, xs_decimal], attr.types)

    def test_flatten_attribute_types_with_restriction_pattern(self):
        xs_bool = AttrTypeFactory.xs_bool()
        xs_decimal = AttrTypeFactory.xs_decimal()
        attr = AttrFactory.create(types=[xs_bool, xs_decimal])
        target = ClassFactory.create()
        self.analyzer.flatten_attribute_types(target, attr)

        self.assertEqual([xs_bool, xs_decimal], attr.types)

        attr.restrictions.pattern = r"[0-1]"
        self.analyzer.flatten_attribute_types(target, attr)
        self.assertEqual([AttrTypeFactory.xs_string()], attr.types)

    @mock.patch.object(ClassAnalyzer, "flatten_attribute_type")
    def test_flatten_attribute_types_ignores_forward_types(
        self, mock_flatten_attribute_type
    ):
        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create()
        type_b = AttrTypeFactory.create(forward_ref=True)

        attr = AttrFactory.create(name="a", types=[type_a, type_b])
        self.analyzer.flatten_attribute_types(parent, attr)

        mock_flatten_attribute_type.assert_called_once_with(parent, attr, type_a)

    def test_flatten_attribute_types_filters_duplicate_types(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.xs_string(),
                        AttrTypeFactory.xs_string(),
                        AttrTypeFactory.xs_bool(),
                    ]
                )
            ]
        )
        self.analyzer.flatten_attribute_types(target, target.attrs[0])
        self.assertEqual(["string", "boolean"], [x.name for x in target.attrs[0].types])

    @mock.patch.object(ClassAnalyzer, "find_attr_type")
    @mock.patch.object(ClassAnalyzer, "merge_attribute_type")
    @mock.patch.object(ClassAnalyzer, "find_attr_simple_type")
    def test_flatten_attribute_type_with_simple_source(
        self, mock_find_attr_simple_type, mock_merge_attribute_type, mock_find_attr_type
    ):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create()
        source = ClassFactory.create()

        mock_find_attr_simple_type.return_value = source

        self.analyzer.flatten_attribute_type(target, attr, attr_type)
        self.assertEqual(0, mock_find_attr_type.call_count)
        mock_find_attr_simple_type.assert_called_once_with(target, attr_type)
        mock_merge_attribute_type.assert_called_once_with(
            source, target, attr, attr_type
        )

    @mock.patch.object(ClassAnalyzer, "class_depends_on")
    @mock.patch.object(ClassAnalyzer, "find_attr_type")
    @mock.patch.object(ClassAnalyzer, "merge_attribute_type")
    @mock.patch.object(ClassAnalyzer, "find_attr_simple_type")
    def test_flatten_attribute_type_with_complex_source(
        self,
        mock_find_attr_simple_type,
        mock_merge_attribute_type,
        mock_find_attr_type,
        mock_class_depends_on,
    ):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create()
        source = ClassFactory.create()

        mock_find_attr_simple_type.return_value = None
        mock_find_attr_type.return_value = source
        mock_class_depends_on.return_value = True

        self.analyzer.flatten_attribute_type(target, attr, attr_type)
        self.assertTrue(attr_type.self_ref)
        self.assertEqual(0, mock_merge_attribute_type.call_count)
        mock_find_attr_simple_type.assert_called_once_with(target, attr_type)
        mock_class_depends_on.assert_called_once_with(source, target)

    @mock.patch("xsdata.analyzer.logger.warning")
    def test_flatten_attribute_type_with_missing_source(self, mock_logger_warning):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create(name="foo")

        self.analyzer.flatten_attribute_type(target, attr, attr_type)
        self.assertEqual(DataType.STRING.code, attr_type.name)
        self.assertTrue(attr_type.native)
        self.assertFalse(attr_type.self_ref)
        self.assertFalse(attr_type.forward_ref)
        mock_logger_warning.assert_called_once_with("Missing type: %s", "foo")

    def test_flatten_attribute_type_with_self_reference(self):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create(name="foo", self_ref=True)

        self.analyzer.flatten_attribute_type(target, attr, attr_type)
        self.assertEqual("foo", attr_type.name)

    @mock.patch.object(ClassAnalyzer, "find_attribute")
    def test_add_substitution_attrs(self, mock_find_attribute):
        target = ClassFactory.elements(2)
        mock_find_attribute.side_effect = [-1, 2]

        first_attr = target.attrs[0]
        second_attr = target.attrs[1]
        first_attr.restrictions.max_occurs = 2

        attr_name = first_attr.name
        attr_qname = target.source_qname(attr_name)
        reference_attrs = AttrFactory.list(2)

        self.analyzer.substitutions_index[attr_qname] = reference_attrs
        self.analyzer.add_substitution_attrs(target, first_attr)

        self.assertEqual(4, len(target.attrs))

        self.assertEqual(reference_attrs[0], target.attrs[0])
        self.assertIsNot(reference_attrs[0], target.attrs[0])
        self.assertEqual(reference_attrs[1], target.attrs[3])
        self.assertIsNot(reference_attrs[1], target.attrs[3])
        self.assertEqual(2, target.attrs[0].restrictions.max_occurs)
        self.assertEqual(2, target.attrs[3].restrictions.max_occurs)

        self.analyzer.add_substitution_attrs(target, second_attr)
        self.assertEqual(4, len(target.attrs))

        self.analyzer.add_substitution_attrs(target, AttrFactory.enumeration())
        self.assertEqual(4, len(target.attrs))

    @mock.patch.object(ClassAnalyzer, "find_class")
    @mock.patch.object(Class, "dependencies")
    def test_class_depends_on(self, mock_dependencies, mock_find_class):
        source = ClassFactory.create()
        target = ClassFactory.create()
        another = ClassFactory.create()

        find_classes = {QName("a"): another, QName("b"): target}

        mock_find_class.side_effect = lambda x: find_classes.get(x)
        mock_dependencies.side_effect = [
            [QName(x) for x in "cde"],
            [QName(x) for x in "abc"],
            [QName(x) for x in "xy"],
        ]

        self.assertFalse(self.analyzer.class_depends_on(source, target))
        self.assertTrue(self.analyzer.class_depends_on(source, target))
        self.assertTrue(self.analyzer.class_depends_on(source, source))

        mock_find_class.assert_has_calls(
            [
                mock.call(QName("c")),
                mock.call(QName("d")),
                mock.call(QName("e")),
                mock.call(QName("a")),
                mock.call(QName("x")),
                mock.call(QName("y")),
                mock.call(QName("b")),
            ]
        )

    @mock.patch.object(ClassAnalyzer, "sanitize_class")
    def test_sanitize_classes(self, mock_sanitize_class):
        classes = ClassFactory.list(2)
        self.analyzer.create_class_index(classes)
        self.analyzer.sanitize_classes()
        mock_sanitize_class.assert_has_calls(list(map(mock.call, classes)))

    @mock.patch.object(ClassAnalyzer, "sanitize_duplicate_attribute_names")
    @mock.patch.object(ClassAnalyzer, "sanitize_attribute_sequence")
    @mock.patch.object(ClassAnalyzer, "sanitize_attribute_name")
    @mock.patch.object(ClassAnalyzer, "sanitize_attribute_restrictions")
    @mock.patch.object(ClassAnalyzer, "sanitize_attribute_default_value")
    def test_sanitize_class(
        self,
        mock_sanitize_attribute_default_value,
        mock_sanitize_attribute_restrictions,
        mock_sanitize_attribute_name,
        mock_sanitize_attribute_sequence,
        mock_sanitize_duplicate_attribute_names,
    ):
        target = ClassFactory.elements(2)
        inner = ClassFactory.elements(1)
        target.inner.append(inner)

        self.analyzer.sanitize_class(target)
        mock_sanitize_attribute_default_value.assert_has_calls(
            [
                mock.call(target.inner[0], target.inner[0].attrs[0]),
                mock.call(target, target.attrs[0]),
                mock.call(target, target.attrs[1]),
            ]
        )
        mock_sanitize_attribute_restrictions.assert_has_calls(
            [
                mock.call(target.inner[0].attrs[0]),
                mock.call(target.attrs[0]),
                mock.call(target.attrs[1]),
            ]
        )
        mock_sanitize_attribute_name.assert_has_calls(
            [
                mock.call(target.inner[0].attrs[0]),
                mock.call(target.attrs[0]),
                mock.call(target.attrs[1]),
            ]
        )
        mock_sanitize_attribute_sequence.assert_has_calls(
            [
                mock.call(target.inner[0].attrs, 0),
                mock.call(target.attrs, 0),
                mock.call(target.attrs, 1),
            ]
        )
        mock_sanitize_duplicate_attribute_names.assert_has_calls(
            [mock.call(target.inner[0].attrs), mock.call(target.attrs)]
        )

    def test_sanitize_attribute_default_value_with_list_field(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(fixed=True)
        attr.restrictions.max_occurs = 2
        self.analyzer.sanitize_attribute_default_value(target, attr)
        self.assertFalse(attr.fixed)

    def test_sanitize_attribute_default_value_with_optional_field(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(fixed=True, default=2)
        attr.restrictions.min_occurs = 0
        self.analyzer.sanitize_attribute_default_value(target, attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_sanitize_attribute_default_value_with_xsi_type(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(
            fixed=True, default=2, name="xsi:type", namespace=Namespace.XSI.uri
        )
        self.analyzer.sanitize_attribute_default_value(target, attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_sanitize_attribute_default_value_with_valid_case(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(fixed=True, default=2)
        self.analyzer.sanitize_attribute_default_value(target, attr)
        self.assertTrue(attr.fixed)
        self.assertEqual(2, attr.default)

    def test_sanitize_attribute_default_value_with_enumeration(self):
        miss = ClassFactory.elements(3, name="miss")
        hit = ClassFactory.enumeration(3, name="hit")
        hit.attrs[2].default = 2
        hit.attrs[2].name = "winner"

        self.analyzer.create_class_index([miss, hit])

        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(),
                AttrFactory.create(default=2),
                AttrFactory.create(
                    default=2, types=[AttrTypeFactory.create("foo", forward_ref=True)]
                ),
                AttrFactory.create(
                    default=2,
                    types=[
                        AttrTypeFactory.create("miss"),
                        AttrTypeFactory.create("hit"),
                    ],
                ),
            ]
        )

        actual = list()
        for attr in target.attrs:
            self.analyzer.sanitize_attribute_default_value(target, attr)
            actual.append(attr.default)

        self.assertEqual([None, 2, None, "@enum@hit.winner"], actual)

        attr = AttrFactory.create(
            default="missing", types=AttrTypeFactory.list(1, name="hit")
        )

        with self.assertRaises(AnalyzerError) as cm:
            self.analyzer.sanitize_attribute_default_value(target, attr)

        self.assertEqual("Unknown enumeration hit: missing", str(cm.exception))

    @mock.patch.object(ClassAnalyzer, "flatten_class")
    def test_class_depends_on_has_a_depth_limit(self, *args):
        one = ClassFactory.create(extensions=ExtensionFactory.list(1))
        two = ClassFactory.create(extensions=ExtensionFactory.list(1))
        three = ClassFactory.create(extensions=ExtensionFactory.list(1))
        four = ClassFactory.create(extensions=ExtensionFactory.list(1))
        five = ClassFactory.create(extensions=ExtensionFactory.list(1))

        one.extensions[0].type.name = two.name
        two.extensions[0].type.name = three.name
        three.extensions[0].type.name = four.name
        four.extensions[0].type.name = five.name
        five.extensions[0].type.name = one.name

        self.analyzer.create_class_index([one, two, three, four, five])
        self.assertTrue(self.analyzer.class_depends_on(five, one))
        self.assertTrue(self.analyzer.class_depends_on(two, one))

        self.assertFalse(self.analyzer.class_depends_on(two, one, depth=3))
        self.assertEqual(5, ClassAnalyzer.MAX_DEPENDENCY_CHECK_DEPTH)
