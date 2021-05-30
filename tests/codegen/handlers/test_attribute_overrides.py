import sys
from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeOverridesHandler
from xsdata.codegen.models import Status
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeOverridesHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.processor = AttributeOverridesHandler(container=self.container)

    @mock.patch.object(AttributeOverridesHandler, "resolve_conflict")
    @mock.patch.object(AttributeOverridesHandler, "validate_override")
    def test_process(self, mock_validate_override, mock_resolve_conflict):
        class_a = ClassFactory.create(
            status=Status.PROCESSING,
            attrs=[
                AttrFactory.create(name="el", tag=Tag.ELEMENT),
                AttrFactory.create(name="at", tag=Tag.ATTRIBUTE),
            ],
        )

        class_b = ClassFactory.elements(2, status=Status.PROCESSED)
        class_c = ClassFactory.create(status=Status.PROCESSED)

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

        # restrictions except choice, min/max occurs don't match
        attr_b.fixed = attr_a.fixed
        attr_a.restrictions.max_length = 10
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(1, len(target.attrs))

        # Restrictions are compatible again
        attr_b.restrictions.max_length = attr_a.restrictions.max_length

        attr_a.restrictions.min_occurs = 1
        attr_a.restrictions.max_occurs = 2
        attr_a.restrictions.choice = 3

        attr_b.restrictions.min_occurs = 4
        attr_b.restrictions.max_occurs = 5
        attr_b.restrictions.choice = 6
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(0, len(target.attrs))

        target.attrs.append(attr_a)
        attr_a.restrictions.min_occurs = None
        attr_a.restrictions.max_occurs = 10
        attr_b.restrictions.min_occurs = None
        attr_b.restrictions.max_occurs = None
        self.processor.validate_override(target, attr_a, attr_b)
        self.assertEqual(sys.maxsize, attr_b.restrictions.max_occurs)

    def test_resolve_conflicts(self):
        a = AttrFactory.create(name="foo", tag=Tag.ATTRIBUTE)
        b = a.clone()
        b.tag = Tag.ELEMENT
        self.processor.resolve_conflict(a, b)

        self.assertEqual("foo_Attribute", a.name)
        self.assertEqual("foo", b.name)
