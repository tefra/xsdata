from types import GeneratorType
from unittest.mock import PropertyMock, call, patch

from tests.factories import (
    AttrFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
)
from xsdata.builder import ClassBuilder
from xsdata.models.codegen import Attr
from xsdata.models.elements import (
    Attribute,
    AttributeGroup,
    ComplexContent,
    ComplexType,
    Element,
    Enumeration,
    Extension,
    Group,
    Restriction,
    Schema,
    Sequence,
    SimpleContent,
    SimpleType,
)
from xsdata.models.enums import TagType, XSDType


class ClassBuilderTests(FactoryTestCase):
    def setUp(self) -> None:
        super(ClassBuilderTests, self).setUp()
        self.schema = Schema.create()
        self.builder = ClassBuilder(schema=self.schema)

    @patch.object(ClassBuilder, "build_class")
    def test_process(self, mock_build_class):
        for _ in range(2):
            self.schema.simple_types.append(SimpleType.create())
            self.schema.attribute_groups.append(AttributeGroup.create())
            self.schema.groups.append(Group.create())
            self.schema.attributes.append(Attribute.create())
            self.schema.complex_types.append(ComplexType.create())
            self.schema.elements.append(Element.create())

        mock_build_class.side_effect = classes = ClassFactory.list(12)

        self.assertEqual(classes, self.builder.build())
        mock_build_class.assert_has_calls(
            [
                call(self.schema.simple_types[0]),
                call(self.schema.simple_types[1]),
                call(self.schema.attribute_groups[0]),
                call(self.schema.attribute_groups[1]),
                call(self.schema.groups[0]),
                call(self.schema.groups[1]),
                call(self.schema.attributes[0]),
                call(self.schema.attributes[1]),
                call(self.schema.complex_types[0]),
                call(self.schema.complex_types[1]),
                call(self.schema.elements[0]),
                call(self.schema.elements[1]),
            ]
        )

    @patch.object(ClassBuilder, "build_class_attributes")
    @patch.object(ClassBuilder, "build_class_extensions")
    @patch.object(Element, "is_abstract", new_callable=PropertyMock)
    @patch.object(Element, "display_help", new_callable=PropertyMock)
    @patch.object(Element, "real_name", new_callable=PropertyMock)
    def test_build_class(
        self,
        mock_real_name,
        mock_display_help,
        mock_is_abstract,
        mock_build_class_extensions,
        build_class_attributes,
    ):
        extensions = ExtensionFactory.list(2)
        mock_real_name.return_value = "name"
        mock_display_help.return_value = "sos"
        mock_is_abstract.return_value = True
        mock_build_class_extensions.return_value = extensions

        element = Element.create()
        result = self.builder.build_class(element)

        build_class_attributes.assert_called_once_with(element, result)

        expected = ClassFactory.create(
            name="name",
            type=Element,
            extensions=extensions,
            help="sos",
            is_abstract=True,
        )
        self.assertEqual(expected, result)

    @patch.object(ClassBuilder, "default_value_type")
    @patch.object(ClassBuilder, "build_class_attribute")
    def test_build_class_attributes_without_default_value_type(
        self, mock_build_class_attribute, default_value_type
    ):
        default_value_type.return_value = None
        element = Element.create(
            complex_type=ComplexType.create(
                attributes=[Attribute.create(), Attribute.create()]
            )
        )
        item = ClassFactory.create()

        self.builder.build_class_attributes(element, item)

        mock_build_class_attribute.assert_has_calls(
            [call(item, attr) for attr in element.complex_type.attributes]
        )

        self.assertEqual(0, len(item.attrs))

    @patch.object(ClassBuilder, "default_value_type")
    @patch.object(ClassBuilder, "build_class_attribute")
    def test_build_class_attributes_with_default_value_type(
        self, mock_build_class_attribute, default_value_type
    ):
        default_value_type.return_value = "xs:string"
        element = Element.create()
        item = ClassFactory.create()

        self.builder.build_class_attributes(element, item)

        mock_build_class_attribute.assert_not_called()

        expected = Attr(
            index=0,
            name="value",
            default=None,
            type=XSDType.STRING.code,
            local_type=TagType.EXTENSION.cname,
        )
        self.assertEqual(1, len(item.attrs))
        self.assertEqual(expected, item.attrs[0])

    @patch.object(ClassBuilder, "element_extensions")
    def test_build_class_extensions(self, mock_element_extensions):
        bar = ExtensionFactory.create(name="bar", index=3)
        bar_dub = ExtensionFactory.create(name="bar", index=2)
        foo = ExtensionFactory.create(name="foo", index=1)

        mock_element_extensions.return_value = [bar, bar_dub, foo]

        element = Element.create()
        actual = self.builder.build_class_extensions(element)

        self.assertEqual([bar_dub, foo], actual)

    def test_element_children(self):
        complex_type = ComplexType.create(
            attributes=[Attribute.create() for i in range(2)],
            sequence=Sequence.create(
                elements=[Element.create() for i in range(2)]
            ),
            simple_content=SimpleContent.create(
                restriction=Restriction.create()
            ),
            complex_content=ComplexContent.create(
                restriction=Restriction.create(
                    enumerations=[Enumeration.create(value=x) for x in "abc"]
                )
            ),
        )

        children = self.builder.element_children(complex_type)
        expected = [
            complex_type.simple_content.restriction,
            complex_type.complex_content.restriction.enumerations[0],
            complex_type.complex_content.restriction.enumerations[1],
            complex_type.complex_content.restriction.enumerations[2],
            complex_type.sequence.elements[0],
            complex_type.sequence.elements[1],
            complex_type.attributes[0],
            complex_type.attributes[1],
        ]
        self.assertIsInstance(children, GeneratorType)
        self.assertEqual(expected, list(children))

    def test_element_extensions(self):
        self.builder.target_prefix = "bk:"
        complex_type = ComplexType.create(
            attributes=[Attribute.create(index=i) for i in range(2)],
            sequence=Sequence.create(
                groups=[
                    Group.create(ref="a", index=3),
                    Group.create(ref="bk:b", index=4),
                    Group.create(ref="c", index=5),
                ]
            ),
            simple_content=SimpleContent.create(
                restriction=Restriction.create(base="isAttribute")
            ),
            complex_content=ComplexContent.create(
                extension=Extension.create(
                    base="bk:ext", index=7, type="Extension"
                )
            ),
        )

        children = self.builder.element_extensions(complex_type)
        expected = [
            ExtensionFactory.create(name="bk:ext", index=7, type="Extension"),
            ExtensionFactory.create(name="a", index=3, type="Group"),
            ExtensionFactory.create(name="bk:b", index=4, type="Group"),
            ExtensionFactory.create(name="c", index=5, type="Group"),
        ]

        self.assertIsInstance(children, GeneratorType)
        self.assertEqual(expected, list(children))

    def test_element_extensions_with_typed_parent(self):
        self.builder.target_prefix = "bk:"
        element = Element.create(type="bk:book", index=23)
        children = self.builder.element_extensions(element)
        expected = ExtensionFactory.list(
            1, name="bk:book", index=0, type="Element"
        )

        self.assertEqual(expected, list(children))

    @patch.object(ClassBuilder, "has_anonymous_class")
    @patch.object(Attribute, "get_restrictions")
    @patch.object(Attribute, "namespace", new_callable=PropertyMock)
    @patch.object(Attribute, "display_help", new_callable=PropertyMock)
    @patch.object(Attribute, "real_type", new_callable=PropertyMock)
    @patch.object(Attribute, "real_name", new_callable=PropertyMock)
    def test_build_class_attribute(
        self,
        mock_real_name,
        mock_real_type,
        mock_display_help,
        mock_namespace,
        mock_get_restrictions,
        has_anonymous_class,
    ):
        item = ClassFactory.create()

        mock_real_name.return_value = item.name
        mock_real_type.return_value = "xs:int"
        mock_display_help.return_value = "sos"
        mock_namespace.return_value = "http://something/common"
        mock_get_restrictions.return_value = {"required": True}
        has_anonymous_class.return_value = False

        attribute = Attribute.create(default="false", index=66)

        self.builder.build_class_attribute(item, attribute)
        expected = AttrFactory.create(
            name=mock_real_name.return_value,
            type=mock_real_type.return_value,
            local_type=Attribute.__name__,
            namespace=mock_namespace.return_value,
            help=mock_display_help.return_value,
            forward_ref=False,
            default="false",
            index=66,
            **mock_get_restrictions.return_value,
        )
        self.assertEqual(expected, item.attrs[0])
        has_anonymous_class.assert_called_once_with(attribute)

    @patch.object(ClassBuilder, "build_inner_class")
    @patch.object(ClassBuilder, "has_anonymous_class")
    def test_build_class_attribute_with_anonymous_class(
        self, has_inner_type, build_inner_class,
    ):
        has_inner_type.return_value = True

        item = ClassFactory.create()
        attribute = Attribute.create(ref="foo")
        self.builder.build_class_attribute(item, attribute)

        self.assertEqual(True, item.attrs[0].forward_ref)
        has_inner_type.assert_called_once_with(attribute)
        build_inner_class.assert_called_once_with(item, attribute)

    def test_has_anonymous_class(self):
        obj = Element.create()
        self.assertFalse(self.builder.has_anonymous_class(obj))

        obj = Element.create(type="foo")
        self.assertFalse(self.builder.has_anonymous_class(obj))

        obj = Element.create(complex_type=ComplexType.create())
        self.assertTrue(self.builder.has_anonymous_class(obj))

        obj = Attribute.create()
        self.assertFalse(self.builder.has_anonymous_class(obj))

    def test_has_anonymous_enumeration(self):
        for clazz in [Element, Attribute]:
            obj = clazz.create()
            self.assertFalse(self.builder.has_anonymous_enumeration(obj))

            obj = clazz.create(simple_type=SimpleType.create())
            self.assertFalse(self.builder.has_anonymous_enumeration(obj))

            obj.simple_type.restriction = Restriction.create()
            self.assertFalse(self.builder.has_anonymous_enumeration(obj))

            obj.simple_type.restriction.enumerations.append(
                Enumeration.create()
            )
            self.assertTrue(self.builder.has_anonymous_enumeration(obj))

            obj.type = "foo"
            self.assertFalse(self.builder.has_anonymous_enumeration(obj))

    @patch.object(ClassBuilder, "build_class")
    def test_build_inner_class(self, mock_build_class):

        mock_build_class.return_value = ClassFactory.create()
        element = Element.create(name="foo", complex_type=ComplexType.create())
        parent = ClassFactory.create()

        self.builder.build_inner_class(parent, element)
        self.assertEqual(mock_build_class.return_value, parent.inner[0])

    @patch.object(ClassBuilder, "build_class")
    def test_build_inner_enumeration(self, mock_build_class):

        mock_build_class.return_value = ClassFactory.create()
        simple_type = SimpleType.create(
            restriction=Restriction.create(
                enumerations=[Enumeration.create(name="a")]
            )
        )
        element = Element.create(name="foo", simple_type=simple_type)
        parent = ClassFactory.create()

        self.builder.build_inner_enumeration(parent, element)
        self.assertEqual(mock_build_class.return_value, parent.inner[0])
        self.assertIsNone(element.simple_type)
        self.assertEqual("foo", element.type)
        self.assertEqual("foo", simple_type.name)

    @patch("xsdata.builder.logger.warning")
    def test_default_value_type(self, mock_logger_warning):
        item = ClassFactory.create()
        self.assertEqual("xs:string", ClassBuilder.default_value_type(item))

        item = ClassFactory.create(extensions=ExtensionFactory.list(1))
        self.assertIsNone(ClassBuilder.default_value_type(item))

        item = ClassFactory.create(
            extensions=[
                ExtensionFactory.create(name="xs:int"),
                ExtensionFactory.create(name="xs:boolean"),
            ]
        )
        self.assertEqual(
            "xs:int xs:boolean", ClassBuilder.default_value_type(item)
        )
        self.assertEqual(0, len(item.extensions))

        item = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION.cname),
            extensions=ExtensionFactory.list(1, name="xs:int"),
        )

        self.assertIsNone(ClassBuilder.default_value_type(item))
        mock_logger_warning.assert_called_once_with("Empty class: `class_B`")
