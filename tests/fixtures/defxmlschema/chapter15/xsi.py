from dataclasses import dataclass

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema-instance"


@dataclass
class Nil:
    class Meta:
        name = "nil"
        namespace = "http://www.w3.org/2001/XMLSchema-instance"


@dataclass
class NoNamespaceSchemaLocation:
    class Meta:
        name = "noNamespaceSchemaLocation"
        namespace = "http://www.w3.org/2001/XMLSchema-instance"


@dataclass
class SchemaLocation:
    class Meta:
        name = "schemaLocation"
        namespace = "http://www.w3.org/2001/XMLSchema-instance"


@dataclass
class Type:
    class Meta:
        name = "type"
        namespace = "http://www.w3.org/2001/XMLSchema-instance"
