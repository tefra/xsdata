from docs.examples.json_parser_from_path import result
from xsdata.formats.dataclass.serializers import JsonSerializer

serializer = JsonSerializer(indent=2)
json = serializer.render(result)
assert json == """
{
  "items": {
    "product": [
      {
        "number": 557,
        "name": "Short-Sleeved Linen Blouse",
        "size": {
          "value": null,
          "system": null
        }
      }
    ]
  }
}
""".strip()
