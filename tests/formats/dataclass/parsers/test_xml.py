from unittest import mock

from tests.fixtures.artists import Artist
from tests.fixtures.books import Books
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.parsers.nodes import PrimitiveNode, SkipNode
from xsdata.formats.dataclass.parsers.xml import UserXmlParser
from xsdata.models.enums import EventType
from xsdata.utils.testing import FactoryTestCase, XmlMetaFactory, XmlVarFactory


class UserXmlParserTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.parser = UserXmlParser()
        self.parser.objects = [(x, x) for x in "abcde"]

    @mock.patch.object(UserXmlParser, "emit_event")
    def test_start(self, mock_emit_event) -> None:
        attrs = {"a": "b"}
        queue = []

        self.parser.start(Books, queue, [], "{urn:books}books", attrs, {})
        self.assertEqual(1, len(queue))

        mock_emit_event.assert_called_once_with(
            EventType.START, "{urn:books}books", attrs=attrs
        )

    @mock.patch.object(UserXmlParser, "emit_event")
    def test_end(self, mock_emit_event) -> None:
        objects = []
        queue = []
        meta = XmlMetaFactory.create(clazz=Artist)
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, name="foo", types=(bool,))
        queue.append(PrimitiveNode(meta, var, {}, self.parser.config))

        result = self.parser.end(queue, objects, "enabled", "true", None)
        self.assertTrue(result)
        self.assertEqual(0, len(queue))
        self.assertEqual(("enabled", True), objects[-1])
        mock_emit_event.assert_called_once_with(EventType.END, "enabled", obj=result)

    @mock.patch.object(UserXmlParser, "emit_event")
    def test_end_with_no_result(self, mock_emit_event) -> None:
        objects = []
        queue = [SkipNode()]

        result = self.parser.end(queue, "author", "foobar", None, objects)
        self.assertFalse(result)
        self.assertEqual(0, len(objects))
        self.assertEqual(0, len(queue))
        self.assertEqual(0, mock_emit_event.call_count)

    def test_emit_event(self) -> None:
        mock_func = mock.Mock()
        self.parser.foo_bar_el = mock_func

        self.parser.emit_event("foo", "{tns}BarEl", a=1, b=2)

        mock_func.assert_called_once_with(a=1, b=2)
        self.assertEqual({("foo", "{tns}BarEl"): mock_func}, self.parser.hooks_cache)
