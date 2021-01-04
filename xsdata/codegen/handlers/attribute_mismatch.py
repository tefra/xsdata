from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Attr
from xsdata.codegen.models import Class
from xsdata.models.enums import DataType


class AttributeMismatchHandler(HandlerInterface):
    """
    Sanitize cases where handling is currently unsupported.

    Cases:
        - Enumerations with list member values
        - Invalid lower case hex binary default values
    """

    @classmethod
    def process(cls, target: Class):
        for attr in target.attrs:
            cls.process_attr(attr)

    @classmethod
    def process_attr(cls, attr: Attr):
        """Reset attribute types and restrictions for unsupported cases."""
        is_enum = attr.is_enumeration
        for attr_type in attr.types:
            datatype = attr_type.datatype
            if is_enum and datatype in (DataType.NMTOKENS, DataType.IDREFS):
                attr_type.qname = str(DataType.STRING)
                attr.restrictions.tokens = False
            elif (
                (attr.fixed or is_enum)
                and datatype == DataType.HEX_BINARY
                and isinstance(attr.default, str)
                and not attr.default.isupper()
            ):
                attr_type.qname = str(DataType.STRING)
                attr.restrictions.format = None
