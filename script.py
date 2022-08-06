from tests.fixtures.books.fixtures import books
from xsdata.formats.dataclass.serializers.code import PycodeSerializer

serializer = PycodeSerializer()
print(serializer.render(books))
