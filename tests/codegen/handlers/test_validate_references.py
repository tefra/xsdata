from xsdata.codegen.container import ClassContainer
from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.handlers import ValidateReferences
from xsdata.models.config import (
    GeneratorConfig,
)
from xsdata.utils.testing import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
)


class ValidateReferencesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()
        self.config = GeneratorConfig()
        self.container = ClassContainer(config=self.config)
        self.handler = ValidateReferences(container=self.container)

    def test_validate_unique_qualified_names(self):
        first = ClassFactory.create()
        second = first.clone()
        self.container.extend([first, second])

        with self.assertRaises(CodegenError):
            self.handler.run()

    def test_validate_unique_instances(self):
        first = ClassFactory.create()
        first.extensions.append(ExtensionFactory.create())
        second = ClassFactory.create()
        second.extensions = first.extensions
        self.container.extend([first, second])

        with self.assertRaises(CodegenError):
            self.handler.run()

    def test_validate_unresolved_references(self):
        first = ClassFactory.create()
        first.attrs.append(AttrFactory.create())
        first.attrs.append(AttrFactory.reference("foo"))
        self.container.add(first)

        with self.assertRaises(CodegenError):
            self.handler.run()

    def test_validate_misrepresented_references(self):
        first = ClassFactory.create()
        inner = ClassFactory.create()
        first.inner.append(inner)
        first.attrs.append(
            AttrFactory.create(
                types=[AttrTypeFactory.create(qname="foo", reference=inner.ref)]
            )
        )
        self.container.add(first)

        with self.assertRaises(CodegenError):
            self.handler.run()
