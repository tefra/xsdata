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
        cascade_default = not target.is_nillable and target.default
        for attr in target.attrs:
            if cascade_default:
                cls.cascade_default_value(target, attr)

            cls.reset_unsupported_types(attr)

    @classmethod
    def cascade_default_value(cls, target: Class, attr: Attr):
        """
        Set the text xml field default value from parent.

        At this stage all flattening and merging has finished, a class
        should only have one xml text field.
        """
        if not attr.xml_type and attr.default is None:
            attr.default = target.default
            attr.fixed = target.fixed

    @classmethod
    def reset_unsupported_types(cls, attr: Attr):
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
