from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.formats.dataclass.filters import class_docstring


class ClassDocstringTests(FactoryTestCase):
    def test_class_docstring(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(help="help"),
                AttrFactory.element(help="Foo\nBar"),
                AttrFactory.element(),
            ]
        )

        expected = '''"""
:ivar attr_b: help
:ivar attr_c: Foo
Bar
:ivar attr_d:
"""'''
        self.assertEqual(expected, class_docstring(target))

    def test_class_docstring_with_class_help(self):
        target = ClassFactory.elements(2, help="Help Me!")

        expected = '''"""Help Me!

:ivar attr_b:
:ivar attr_c:
"""'''
        self.assertEqual(expected, class_docstring(target))

    def test_class_docstring_with_enumeration(self):
        target = ClassFactory.enumeration(2, help="Help Me!")

        expected = '''"""Help Me!

:cvar ATTR_B:
:cvar ATTR_C:
"""'''
        self.assertEqual(expected, class_docstring(target, enum=True))
