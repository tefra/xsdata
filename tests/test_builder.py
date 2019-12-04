from types import GeneratorType
from unittest.mock import PropertyMock, call, patch

from tests.factories import AttrFactory, ClassFactory, FactoryTestCase
from xsdata.builder import ClassBuilder
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
        for i in range(2):
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
                call(self.schema.complex_types[0], is_root=True),
                call(self.schema.complex_types[1], is_root=True),
                call(self.schema.elements[0], is_root=True),
                call(self.schema.elements[1], is_root=True),
            ]
        )

    @patch.object(ClassBuilder, "build_class_extensions")
    @patch.object(ClassBuilder, "build_class_attribute")
    @patch.object(ClassBuilder, "element_extensions")
    @patch.object(ClassBuilder, "element_children")
    @patch.object(Element, "display_help", new_callable=PropertyMock)
    @patch.object(Element, "real_name", new_callable=PropertyMock)
    def test_build_class(
        self,
        mock_real_name,
        mock_display_help,
        mock_element_children,
        mock_element_extensions,
        mock_build_class_attribute,
        mock_build_class_extensions,
    ):
        mock_real_name.return_value = "name"
        mock_build_class_extensions.return_value = ["foo", "bar"]
        mock_display_help.return_value = "sos"
        mock_element_children.return_value = [
            Attribute.create(name=x) for x in "ab"
        ]

        result = self.builder.build_class(Element.create())

        mock_build_class_attribute.assert_has_calls(
            [
                call(result, child)
                for child in mock_element_children.return_value
            ]
        )
        expected = ClassFactory.create(
            name="name", type=Element, extensions=["foo", "bar"], help="sos"
        )
        self.assertEqual(expected, result)

    @patch("xsdata.builder.logger.warning")
    @patch.object(ClassBuilder, "build_class_attribute", return_value=None)
    @patch.object(ClassBuilder, "element_children")
    @patch.object(Element, "display_help", new_callable=PropertyMock)
    @patch.object(Element, "extends", new_callable=PropertyMock)
    @patch.object(Element, "real_name", new_callable=PropertyMock)
    def test_build_class_with_no_extensions_and_attributes(
        self,
        mock_real_name,
        mock_extensions,
        mock_display_help,
        mock_element_children,
        mock_build_class_attribute,
        mock_warning,
    ):
        item = ClassFactory.create(
            type=Element,
            help="sos",
            attrs=[
                AttrFactory.create(
                    name="value",
                    default=None,
                    type=XSDType.STRING.code,
                    local_type=TagType.RESTRICTION.cname,
                    index=0,
                )
            ],
        )

        mock_real_name.return_value = item.name
        mock_extensions.return_value = []
        mock_display_help.return_value = "sos"
        mock_element_children.return_value = []

        element = Element.create()
        result = self.builder.build_class(element)

        mock_build_class_attribute.assert_not_called()
        mock_warning.assert_called_once_with(f"Empty class: `{item.name}`")

        self.assertEqual(item, result)

    def test_build_class_with_typed_element(self):
        result = self.builder.build_class(
            Attribute.create(type="foo", name="attr")
        )
        self.assertEqual(["foo"], result.extensions)

    @patch.object(ClassBuilder, "element_extensions")
    def test_build_class_extensions(self, mock_element_extensions):
        mock_element_extensions.return_value = [
            "bks:books",
            "xs:string",
            "title",
            "genre",
            None,
        ]
        obj = Element.create(type="bks:paper")

        expected = ["bks:books", "bks:paper", "genre", "title", "xs:string"]
        self.assertEqual(expected, self.builder.build_class_extensions(obj))

        self.builder.target_prefix = "bks:"
        expected = ["books", "genre", "paper", "title", "xs:string"]
        self.assertEqual(expected, self.builder.build_class_extensions(obj))

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

        complex_type = ComplexType.create(
            attributes=[Attribute.create() for i in range(2)],
            sequence=Sequence.create(
                elements=[Group.create(ref=x) for x in "abc"]
            ),
            simple_content=SimpleContent.create(
                restriction=Restriction.create(base="isAttribute")
            ),
            complex_content=ComplexContent.create(
                extension=Extension.create(base="ext")
            ),
        )

        children = self.builder.element_extensions(complex_type)
        expected = ["ext", "a", "b", "c"]

        self.assertIsInstance(children, GeneratorType)
        self.assertEqual(expected, list(children))

    @patch("xsdata.builder.logger.warning")
    @patch.object(ClassBuilder, "strip_target_namespace")
    @patch.object(ClassBuilder, "has_inner_type")
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
        mock_has_inner_type,
        mock_strip_target_namespace,
        mock_warning,
    ):
        item = ClassFactory.create()

        mock_real_name.return_value = item.name
        mock_real_type.return_value = "xs:int"
        mock_display_help.return_value = "sos"
        mock_namespace.return_value = "http://something/common"
        mock_get_restrictions.return_value = {"required": True}
        mock_has_inner_type.return_value = False
        mock_strip_target_namespace.side_effect = lambda x: x

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
        mock_has_inner_type.assert_called_once_with(attribute)
        mock_warning.assert_not_called()
        mock_strip_target_namespace.assert_called_once_with(
            mock_real_type.return_value
        )

    @patch.object(ClassBuilder, "build_inner_class")
    @patch.object(ClassBuilder, "has_inner_type")
    def test_build_class_attribute_with_inner_type(
        self, has_inner_type, build_inner_class,
    ):
        has_inner_type.return_value = True

        item = ClassFactory.create()
        attribute = Attribute.create(ref="foo")
        self.builder.build_class_attribute(item, attribute)

        self.assertEqual(True, item.attrs[0].forward_ref)
        has_inner_type.assert_called_once_with(attribute)
        build_inner_class.assert_called_once_with(item, attribute)

    def test_has_inner_type(self):
        self.assertFalse(self.builder.has_inner_type(Element.create()))
        self.assertFalse(
            self.builder.has_inner_type(Element.create(type="foo"))
        )
        self.assertTrue(
            self.builder.has_inner_type(
                Element.create(complex_type=ComplexType.create())
            )
        )

        attribute = Attribute.create()
        self.assertFalse(self.builder.has_inner_type(attribute))

    @patch.object(ClassBuilder, "build_class")
    def test_build_inner_class(self, mock_build_class):

        mock_build_class.return_value = ClassFactory.create()
        element = Element.create(name="foo", complex_type=ComplexType.create())
        parent = ClassFactory.create()

        self.builder.build_inner_class(parent, element)
        self.assertEqual(mock_build_class.return_value, parent.inner[0])

    def test_strip_target_namespace(self):
        self.schema.nsmap = {
            "bks": "urn:books",
            "foo": "bar",
            None: "http://namespace/other",
        }
        self.schema.target_namespace = "urn:books"
        builder = ClassBuilder(schema=self.schema)
        self.assertEqual("xs:int", builder.strip_target_namespace("xs:int"))
        self.assertEqual("int", builder.strip_target_namespace("bks:int"))
        self.assertEqual("int", builder.strip_target_namespace("int"))
