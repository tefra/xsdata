from xsdata.codegen.mixins import HandlerInterface
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.exceptions import AnalyzerError
from xsdata.models.xsd import SimpleType


class AttributeMismatchHandler(HandlerInterface):
    """Normalize attributes that can not coexist together in the same class by
    moving them to an existing inner class or to a new one."""

    @classmethod
    def process(cls, target: Class):
        if target.is_enumeration or not any(
            attr.is_enumeration for attr in target.attrs
        ):
            return

        enumerations = []
        for attr in list(target.attrs):
            if attr.is_enumeration:
                target.attrs.remove(attr)
                enumerations.append(attr)

        if len(target.attrs) > 1:
            raise AnalyzerError("Mixed enumeration with more than one normal field.")

        enum_inner = next(
            (inner for inner in target.inner if inner.is_enumeration), None
        )
        if not enum_inner:
            enum_inner = Class(
                name="value",
                type=SimpleType,
                module=target.module,
                package=target.package,
                mixed=False,
                abstract=False,
                nillable=False,
            )
            target.attrs[0].types.append(AttrType(name="value", forward=True))
            target.inner.append(enum_inner)

        enum_inner.attrs.extend(enumerations)
