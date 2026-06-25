from unittest import TestCase

from tests.fixtures.references.sample import family
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

class XmlSerializerTests(TestCase):
    def setUp(self) -> None:
        config = SerializerConfig(indent="  ")
        self.serializer = XmlSerializer(config=config)
        super().setUp()

    def test_render(self) -> None:
        result = self.serializer.render(family, ns_map={"rel": "urn:relations", "xsi": "http://www.w3.org/2001/XMLSchema-instance"})
        print(result)
        expected = """<?xml version="1.0" encoding="UTF-8"?>
<rel:family xmlns:rel="urn:relations" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <rel:surname>fictional</rel:surname>
  <rel:members>
    <rel:member xsi:type="parent">
      <name>peter</name>
      <children>
        <child>albert</child>
        <child>bertha</child>
      </children>
    </rel:member>
    <rel:member xsi:type="child">
      <name>albert</name>
      <age>7</age>
    </rel:member>
    <rel:member xsi:type="child">
      <name>bertha</name>
      <age>5</age>
    </rel:member>
  </rel:members>
</rel:family>
"""
        self.assertEqual(expected, result)