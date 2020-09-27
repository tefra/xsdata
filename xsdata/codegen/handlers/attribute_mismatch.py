from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import Class


class AttributeMismatchHandler(HandlerInterface):
    """
    Classes can not container attributes derived from xs:enumeration and any
    other schema element. Although very rare it can happen in silly cases when
    the author of the schema is trying to restrict the enum type with another
    xs:simpleType.

    Apart from visibility about the origin of the enumeration values it doesn't serve
    any other purpose. In this case simply drop non enum attributes

    .. code-block:: xml

        <xsd:simpleType name="ApplicableSizesType">
        <xsd:restriction>
          <xsd:simpleType>
            <xsd:list itemType="SizeType"/>
          </xsd:simpleType>
          <xsd:enumeration value="small medium large"/>
          <xsd:enumeration value="2 4 6 8 10 12 14 16 18"/>
        </xsd:restriction>
        </xsd:simpleType>
    """

    @classmethod
    def process(cls, target: Class):
        """Drop non enum attributes from enum classes."""

        enumerations = [attr for attr in target.attrs if attr.is_enumeration]
        if enumerations:
            target.attrs = enumerations
