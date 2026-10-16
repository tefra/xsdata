from unittest import TestCase

from tests.fixtures.references.model import Family
from tests.fixtures.references.sample import family
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


class XmlSerializerTests(TestCase):
    expected = """<?xml version="1.0" encoding="UTF-8"?>
<rel:family xmlns:rel="urn:relations" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <rel:members>
    <rel:member xsi:type="parent">
      <name>peter</name>
      <surname>fictional</surname>
      <children>
        <child>albert_fictional</child>
        <child>bertha_fictional</child>
      </children>
    </rel:member>
    <rel:member xsi:type="offspring">
      <name>albert</name>
      <surname>fictional</surname>
      <age>7</age>
    </rel:member>
    <rel:member xsi:type="parent">
      <name>deceased</name>
      <surname>fictional</surname>
      <children>
        <child>albert_fictional</child>
        <child>bertha_fictional</child>
      </children>
    </rel:member>
    <rel:member xsi:type="offspring">
      <name>bertha</name>
      <surname>fictional</surname>
      <age>5</age>
    </rel:member>
    <rel:member xsi:type="parent">
      <name>penny</name>
      <surname>fictional</surname>
      <children>
        <child>albert_fictional</child>
        <child>bertha_fictional</child>
      </children>
    </rel:member>
  </rel:members>
  <rel:favorite>albert_fictional</rel:favorite>
</rel:family>
"""

    def setUp(self) -> None:
        config = SerializerConfig(indent="  ")
        self.serializer = XmlSerializer(config=config)
        pconfig = ParserConfig()
        context = XmlContext()
        self.parser = XmlParser(config=pconfig, context=context)
        super().setUp()

    def test_render(self) -> None:
        result = self.serializer.render(
            family,
            ns_map={
                "rel": "urn:relations",
                "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            },
        )
        print(result)
        self.assertEqual(self.expected, result)

    def test_parse(self) -> None:
        result = self.parser.from_string(self.expected, Family)
        self.assertEqual(family, result)
        self.assertEqual(7, result.favorite.age)
