import sys
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

from xsdata.codegen.models import Attr, AttrType, Class, Extension, Restrictions
from xsdata.models.enums import DataType, Tag
from xsdata.models.mixins import ElementBase
from xsdata.models.xsd import (
    Attribute,
    AttributeGroup,
    ComplexType,
    Element,
    Group,
    Schema,
    SimpleType,
)
from xsdata.utils import collections, text
from xsdata.utils.namespaces import build_qname, is_default, prefix_exists

ROOT_CLASSES = (SimpleType, ComplexType, Group, AttributeGroup, Element, Attribute)


data_types = {
    "string": DataType.STRING,
    "number": DataType.FLOAT,
    "integer": DataType.INTEGER,
    "boolean": DataType.BOOLEAN,
    "any": DataType.ANY_TYPE,
}


class JsonSchemaMapper:
    """Map a schema instance to classes.

    This mapper is used to build classes from xsd documents.
    """

    @classmethod
    def map(cls, data: Dict, location: str) -> List[Class]:


        if "definitions" in data:
            return [
                cls.map_schema(name, data, location)
                for name, schema in data["definitions"].items()
            ]

        if "properties" in data:
            return [cls.map_schema(location, data, location)]


    @classmethod
    def map_schema(cls, qname: str, data: Dict, location: str, references: Dict) -> Class:

        required = set(data.get("required", []))

        attrs = []
        index = 0
        for name, prop in data["properties"].items():
            min_occurs = 0
            max_occurs = 1
            if name in required:
                min_occurs = 1

            tp = prop.get("type")
            if tp == "array":
                max_occurs = sys.maxsize
                if "type" in prop["items"]:
                    tp = prop["items"]["type"]
                else:
                    tp = prop["items"]["$ref"]
            elif tp is None and "$ref" in prop:
                tp = prop["$ref"]
            else:
                tp = "any"


            if tp.startswith("#"):
                tp = references[tp]
            else:
                tp = Path(tp).stem.replace(".schema", "")

            data_type = data_types.get(tp)
            if tp in data_types:
                attr_type = AttrType(qname=str(data_type), native=True)
            else:
                attr_type = AttrType(qname=tp)

            attr = Attr(
                index=index,
                name=name,
                tag=Tag.ELEMENT,
                help=prop.get("description"),
                types=[attr_type]
            )
            attr.restrictions.min_occurs = min_occurs
            attr.restrictions.max_occurs = max_occurs

            attrs.append(attr)
            index += 1




        return Class(
            qname=qname,
            tag=Tag.ELEMENT,
            help=data.get("description"),
            location=location,
            attrs=attrs
        )