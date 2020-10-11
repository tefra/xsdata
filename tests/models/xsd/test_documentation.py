from unittest import TestCase

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.xsd import Documentation


class DocumentationTests(TestCase):
    def test_tostring(self):
        documentation = Documentation(
            elements=[
                "I am a ",
                AnyElement(
                    qname="p",
                    text="test",
                    tail="\n",
                    children=[AnyElement(qname="span", text="!")],
                ),
            ]
        )

        self.assertEqual("I am a <p>test<span>!</span></p>", documentation.tostring())
