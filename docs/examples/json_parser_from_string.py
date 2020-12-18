from docs.examples.json_parser_from_path import parser, json_path
from tests.fixtures.defxmlschema.chapter05 import Order

result = parser.from_string(json_path.read_text(), Order)