import sys
from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import ValidateAttributesOverrides
from xsdata.codegen.models import Status
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ValidateAttributesOverridesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.processor = ValidateAttributesOverrides(container=self.container)

    @mock.patch.object(ValidateAttributesOverrides, "resolve_conflict")
    @mock.patch.object(ValidateAttributesOverrides, "validate_override")
    def test_process(self, mock_validate_override, mock_resolve_conflict):
        class_a = ClassFactory.create(
            status=Status.FLATTENING,
            attrs=[
                AttrFactory.create(name="el", tag=Tag.ELEMENT),
                AttrFactory.create(name="at", tag=Tag.ATTRIBUTE),
            ],
        )

        class_b = ClassFactory.elements(2, status=Status.FLATTENED)
        class_c = ClassFactory.create(status=Status.FLATTENED)

        class_b.extensions.append(ExtensionFactory.reference(class_c.qname))
        class_a.extensions.append(ExtensionFactory.reference(class_b.qname))

        class_c.attrs.append(class_a.attrs[0].clone())
        class_c.attrs.append(class_a.attrs[1].clone())
        class_c.attrs[1].tag = Tag.ELEMENT

        self.container.extend((class_a, class_b, class_c))
        self.processor.process(class_a)

        mock_validate_override.assert_called_once_with(
            class_a, class_a.attrs[0], class_c.attrs[0]
        )
        mock_resolve_conflict.assert_called_once_with(
            class_a.attrs[1], class_c.attrs[1]
        )

    def test_process_remove_non_overriding_prohibited_attrs(self):
        target = ClassFactory.elements(1)
        target.attrs[0].restrictions.max_occurs = 0

        self.processor.process(target)
        self.assertEqual(0, len(target.attrs))

    def test_overrides(self):
        a = AttrFactory.create(tag=Tag.SIMPLE_TYPE)
        b = a.clone()

        self.assertTrue(self.processor.overrides(a, b))

        b.tag = Tag.EXTENSION
        self.assertTrue(self.processor.overrides(a, b))

        b.namespace = "foo"
        self.assertFalse(self.processor.overrides(a, b))

    def test_validate_override(self):
        attr_a = AttrFactory.create()
        attr_b = attr_a.clone()
        target = ClassFactory.create()
        target.attrs.append(attr_a)

        # 100 Match remove override attrs
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(0, len(target.attrs))

        # default doesn't match
        target.attrs.append(attr_a)
        attr_b.default = "1"
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(1, len(target.attrs))

        # mixed doesn't match
        attr_b.default = attr_a.default
        attr_b.mixed = True
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(1, len(target.attrs))

        # fixed doesn't match
        attr_b.mixed = attr_a.mixed
        attr_b.fixed = True
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(1, len(target.attrs))

        # Restrictions don't match
        attr_b.fixed = attr_a.fixed
        attr_a.restrictions.tokens = not attr_b.restrictions.tokens
        attr_a.restrictions.nillable = not attr_b.restrictions.nillable
        attr_a.restrictions.min_occurs = 0
        attr_b.restrictions.min_occurs = 1
        attr_a.restrictions.max_occurs = 0
        attr_b.restrictions.max_occurs = 1

        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(1, len(target.attrs))

        # Restrictions are compatible again
        attr_a.restrictions.tokens = attr_b.restrictions.tokens
        attr_a.restrictions.nillable = attr_b.restrictions.nillable
        attr_a.restrictions.min_occurs = attr_b.restrictions.min_occurs = 1
        attr_a.restrictions.max_occurs = attr_b.restrictions.max_occurs = 1
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(0, len(target.attrs))

        # Source is list, parent is not
        target.attrs.append(attr_a)
        attr_a.restrictions.min_occurs = None
        attr_a.restrictions.max_occurs = 10
        attr_b.restrictions.min_occurs = None
        attr_b.restrictions.max_occurs = None
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(sys.maxsize, attr_b.restrictions.max_occurs)

        # Parent is any type, source isn't, skip
        attr_a = AttrFactory.native(DataType.STRING)
        attr_b = AttrFactory.native(DataType.ANY_SIMPLE_TYPE)
        target = ClassFactory.create(attrs=[attr_a])

        self.processor.validate_override(target, attr_a.clone(), attr_b)
        self.assertEqual(attr_a, target.attrs[0])

    def test_resolve_conflicts(self):
        a = AttrFactory.create(name="foo", tag=Tag.ATTRIBUTE)
        b = a.clone()
        b.tag = Tag.ELEMENT
        self.processor.resolve_conflict(a, b)

        self.assertEqual("foo_Attribute", a.name)
        self.assertEqual("foo", b.name)
