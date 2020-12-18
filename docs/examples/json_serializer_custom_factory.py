from typing import Tuple, Dict

from docs.examples.json_parser_from_path import result
from xsdata.formats.dataclass.serializers import JsonSerializer


def filter_none(x: Tuple) -> Dict:
    return {k: v for k, v in x if v is not None}


serializer = JsonSerializer(indent=2, dict_factory=filter_none)
json = serializer.render(result)
assert json == """
{
  "items": {
    "product": [
      {
        "number": 557,
        "name": "Short-Sleeved Linen Blouse",
        "size": {}
      }
    ]
  }
}
""".strip()
