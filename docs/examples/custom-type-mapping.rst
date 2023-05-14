===================
Custom type mapping
===================

When managing a big collection of models, it sometimes is tricky to split them
into multiple python modules. Even more so if they depend on each other. For
the models to be serializable by xsdata, they need to be able to import all
other referenced models, which might not be possible due to circular imports.

One solution to get around this problem is to fence the imports within the
python modules by using :data:`python:typing.TYPE_CHECKING` and passing a
dedicated type-map dictionary to the
:class:`~xsdata.formats.dataclass.serializers.config.SerializerConfig`.


.. tab:: city.py

    .. literalinclude:: /../tests/models/typemapping/city.py
        :language: python

.. tab:: street.py

    .. literalinclude:: /../tests/models/typemapping/street.py
        :language: python

.. tab:: house.py

    .. literalinclude:: /../tests/models/typemapping/house.py
        :language: python


By fencing the imports, we are able to keep our models in different python
modules that are cleanly importable and considered valid by static type
checkers.

Passing the type-map dictionary, which maps the class/model-names directly to
imported objects, enables xsdata to serialize the models.


.. testcode::

    from xsdata.formats.dataclass.serializers import XmlSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig

    from tests.models.typemapping.city import City
    from tests.models.typemapping.house import House
    from tests.models.typemapping.street import Street


    city1 = City(name="footown")
    street1 = Street(name="foostreet")
    house1 = House(number=23)
    city1.streets.append(street1)
    street1.houses.append(house1)

    type_map = {"City": City, "Street": Street, "House": House}
    serializer_config = SerializerConfig(pretty_print=True, globalns=type_map)

    xml_serializer = XmlSerializer(config=serializer_config)
    serialized_house = xml_serializer.render(city1)
    print(serialized_house)


.. testoutput::
    :options: +NORMALIZE_WHITESPACE

    <?xml version="1.0" encoding="UTF-8"?>
    <City>
      <name>footown</name>
      <streets>
        <name>foostreet</name>
        <houses>
          <number>23</number>
        </houses>
      </streets>
    </City>
