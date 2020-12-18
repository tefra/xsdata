from docs.examples.json_parser_from_path import result
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers.json import JsonEncoder

serializer = JsonSerializer(encoder=JsonEncoder)
json = serializer.render(result)
