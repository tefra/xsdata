from unittest import TestCase

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.xsd import Annotation
from xsdata.models.xsd import AnnotationBase
from xsdata.models.xsd import Documentation


class AnnotationBaseTest(TestCase):
    def test_property_dispaly_help(self):
        base = AnnotationBase()
        self.assertIsNone(base.display_help)

        base.annotations.append(Annotation(documentations=[Documentation()]))
        self.assertIsNone(base.display_help)

        base.annotations.append(
            Annotation(
                documentations=[
                    Documentation(
                        elements=[
                            "    I am a ",
                            AnyElement(
                                qname="p",
                                text="test",
                                tail="\n",
                                children=[AnyElement(qname="span", text="!")],
                            ),
                        ]
                    )
                ]
            )
        )
        self.assertEqual("I am a <p>test<span>!</span></p>", base.display_help)
