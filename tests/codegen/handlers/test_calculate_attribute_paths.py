from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import CalculateAttributePaths
from xsdata.codegen.handlers import CreateCompoundFields
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class CalculateAttributePathsTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        self.processor = CalculateAttributePaths()

    def test_process(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.enumeration(),
                AttrFactory.attribute(),
                AttrFactory.element(),
                AttrFactory.element(
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        path=[("s", 1, 1, 1), ("s", 2, 1, 2)],
                    )
                ),
                AttrFactory.element(
                    restrictions=Restrictions(
                        min_occurs=1, max_occurs=1, path=[("s", 1, 1, 1)]
                    )
                ),
                AttrFactory.element(
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        path=[("s", 1, 1, 1), ("g", 3, 1, 1), ("g", 4, 1, 2)],
                    )
                ),
                AttrFactory.element(
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        path=[("s", 1, 1, 1), ("g", 3, 1, 1)],
                    )
                ),
                AttrFactory.element(
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        path=[("s", 1, 1, 1), ("c", 4, 0, 1)],
                    )
                ),
                AttrFactory.element(
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        path=[("s", 1, 1, 1), ("c", 4, 0, 1)],
                    )
                ),
                AttrFactory.element(
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        path=[("s", 1, 1, 1), ("c", 5, 2, 2)],
                    )
                ),
                AttrFactory.element(
                    restrictions=Restrictions(
                        min_occurs=1,
                        max_occurs=1,
                        path=[("s", 1, 1, 1), ("c", 5, 2, 2)],
                    )
                ),
            ]
        )
        self.processor.process(target)

        actual = []
        for attr in target.attrs:
            restrictions = attr.restrictions
            actual.append(
                (
                    restrictions.sequence,
                    restrictions.group,
                    restrictions.min_occurs,
                    restrictions.max_occurs,
                )
            )

        expected = [
            (None, None, None, None),
            (None, None, None, None),
            (None, None, None, None),
            (1, None, 1, 2),
            (1, None, 1, 1),
            (1, 4, 1, 2),
            (1, 3, 1, 1),
            (1, None, 0, 1),
            (1, None, 0, 1),
            (1, None, 2, 2),
            (1, None, 2, 2),
        ]
        self.assertEqual(expected, actual)
