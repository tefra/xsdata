from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class StrucDocBr:
    class Meta:
        name = "StrucDoc.Br"


@dataclass
class StrucDocCol:
    """
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar span:
    :ivar width:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "StrucDoc.Col"

    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    span: str = field(
        default="1",
        metadata=dict(
            type="Attribute"
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["StrucDocCol.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valign: Optional["StrucDocCol.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class StrucDocFootnoteRef:
    """
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar idref:
    """
    class Meta:
        name = "StrucDoc.FootnoteRef"

    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    idref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="IDREF",
            type="Attribute",
            required=True
        )
    )


class StrucDocListListType(Enum):
    """
    :cvar ORDERED:
    :cvar UNORDERED:
    """
    ORDERED = "ordered"
    UNORDERED = "unordered"


@dataclass
class StrucDocSub:
    """
    :ivar content:
    """
    class Meta:
        name = "StrucDoc.Sub"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class StrucDocSup:
    """
    :ivar content:
    """
    class Meta:
        name = "StrucDoc.Sup"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class StrucDocCaption:
    """
    :ivar content:
    :ivar link_html:
    :ivar sub:
    :ivar sup:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar id:
    :ivar language:
    :ivar style_code:
    """
    class Meta:
        name = "StrucDoc.Caption"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata=dict(
            name="linkHtml",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class StrucDocColgroup:
    """
    :ivar col:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar span:
    :ivar width:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "StrucDoc.Colgroup"

    col: List[StrucDocCol] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    span: str = field(
        default="1",
        metadata=dict(
            type="Attribute"
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["StrucDocColgroup.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valign: Optional["StrucDocColgroup.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class StrucDocTitleFootnote:
    """
    :ivar content_any:
    :ivar content:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar id:
    :ivar language:
    :ivar style_code:
    """
    class Meta:
        name = "StrucDoc.TitleFootnote"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List["StrucDocTitleContent"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class StrucDocRenderMultiMedia:
    """
    :ivar caption:
    :ivar referenced_object:
    :ivar id:
    :ivar language:
    :ivar style_code:
    """
    class Meta:
        name = "StrucDoc.RenderMultiMedia"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    referenced_object: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="referencedObject",
            type="Attribute",
            required=True,
            tokens=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class StrucDocTitleContent:
    """
    :ivar content_any:
    :ivar content:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar id:
    :ivar language:
    :ivar style_code:
    """
    class Meta:
        name = "StrucDoc.TitleContent"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List["StrucDocTitleContent"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote: List[StrucDocTitleFootnote] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class StrucDocParagraph:
    """
    :ivar content_any:
    :ivar caption:
    :ivar content:
    :ivar link_html:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar render_multi_media:
    :ivar id:
    :ivar language:
    :ivar style_code:
    """
    class Meta:
        name = "StrucDoc.Paragraph"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata=dict(
            name="linkHtml",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata=dict(
            name="renderMultiMedia",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class StrucDocTh:
    """
    :ivar content_any:
    :ivar content:
    :ivar link_html:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar render_multi_media:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar abbr:
    :ivar axis:
    :ivar headers:
    :ivar scope:
    :ivar rowspan:
    :ivar colspan:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "StrucDoc.Th"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata=dict(
            name="linkHtml",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata=dict(
            name="renderMultiMedia",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    abbr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    axis: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    headers: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
            tokens=True
        )
    )
    scope: Optional["StrucDocTh.Scope"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rowspan: str = field(
        default="1",
        metadata=dict(
            type="Attribute"
        )
    )
    colspan: str = field(
        default="1",
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["StrucDocTh.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valign: Optional["StrucDocTh.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Scope(Enum):
        """
        :cvar ROW:
        :cvar COL:
        :cvar ROWGROUP:
        :cvar COLGROUP:
        """
        ROW = "row"
        COL = "col"
        ROWGROUP = "rowgroup"
        COLGROUP = "colgroup"

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class StrucDocTitle:
    """
    :ivar content_any:
    :ivar content:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar media_type:
    """
    class Meta:
        name = "StrucDoc.Title"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List[StrucDocTitleContent] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote: List[StrucDocTitleFootnote] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    media_type: str = field(
        init=False,
        default="text/x-hl7-title+xml",
        metadata=dict(
            name="mediaType",
            type="Attribute"
        )
    )


@dataclass
class StrucDocTd:
    """
    :ivar content_any:
    :ivar content:
    :ivar link_html:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar render_multi_media:
    :ivar paragraph:
    :ivar list_value:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar abbr:
    :ivar axis:
    :ivar headers:
    :ivar scope:
    :ivar rowspan:
    :ivar colspan:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "StrucDoc.Td"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata=dict(
            name="linkHtml",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata=dict(
            name="renderMultiMedia",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    paragraph: List[StrucDocParagraph] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    list_value: List["StrucDocList"] = field(
        default_factory=list,
        metadata=dict(
            name="list",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    abbr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    axis: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    headers: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
            tokens=True
        )
    )
    scope: Optional["StrucDocTd.Scope"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rowspan: str = field(
        default="1",
        metadata=dict(
            type="Attribute"
        )
    )
    colspan: str = field(
        default="1",
        metadata=dict(
            type="Attribute"
        )
    )
    align: Optional["StrucDocTd.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valign: Optional["StrucDocTd.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Scope(Enum):
        """
        :cvar ROW:
        :cvar COL:
        :cvar ROWGROUP:
        :cvar COLGROUP:
        """
        ROW = "row"
        COL = "col"
        ROWGROUP = "rowgroup"
        COLGROUP = "colgroup"

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class StrucDocTr:
    """
    :ivar th:
    :ivar td:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "StrucDoc.Tr"

    th: List[StrucDocTh] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    td: List[StrucDocTd] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    align: Optional["StrucDocTr.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valign: Optional["StrucDocTr.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class StrucDocTbody:
    """
    :ivar tr:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "StrucDoc.Tbody"

    tr: List[StrucDocTr] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    align: Optional["StrucDocTbody.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valign: Optional["StrucDocTbody.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class StrucDocTfoot:
    """
    :ivar tr:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "StrucDoc.Tfoot"

    tr: List[StrucDocTr] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    align: Optional["StrucDocTfoot.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valign: Optional["StrucDocTfoot.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class StrucDocThead:
    """
    :ivar tr:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar align:
    :ivar char:
    :ivar charoff:
    :ivar valign:
    """
    class Meta:
        name = "StrucDoc.Thead"

    tr: List[StrucDocTr] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    align: Optional["StrucDocThead.Align"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    char: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charoff: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    valign: Optional["StrucDocThead.Valign"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Align(Enum):
        """
        :cvar LEFT:
        :cvar CENTER:
        :cvar RIGHT:
        :cvar JUSTIFY:
        :cvar CHAR:
        """
        LEFT = "left"
        CENTER = "center"
        RIGHT = "right"
        JUSTIFY = "justify"
        CHAR = "char"

    class Valign(Enum):
        """
        :cvar TOP:
        :cvar MIDDLE:
        :cvar BOTTOM:
        :cvar BASELINE:
        """
        TOP = "top"
        MIDDLE = "middle"
        BOTTOM = "bottom"
        BASELINE = "baseline"


@dataclass
class StrucDocTable:
    """
    :ivar caption:
    :ivar col:
    :ivar colgroup:
    :ivar thead:
    :ivar tfoot:
    :ivar tbody:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar summary:
    :ivar width:
    :ivar border:
    :ivar frame:
    :ivar rules:
    :ivar cellspacing:
    :ivar cellpadding:
    """
    class Meta:
        name = "StrucDoc.Table"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    col: List[StrucDocCol] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    colgroup: List[StrucDocColgroup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    thead: Optional[StrucDocThead] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    tfoot: Optional[StrucDocTfoot] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    tbody: List[StrucDocTbody] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    summary: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    border: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    frame: Optional["StrucDocTable.Frame"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rules: Optional["StrucDocTable.Rules"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Frame(Enum):
        """
        :cvar VOID:
        :cvar ABOVE:
        :cvar BELOW:
        :cvar HSIDES:
        :cvar LHS:
        :cvar RHS:
        :cvar VSIDES:
        :cvar BOX:
        :cvar BORDER:
        """
        VOID = "void"
        ABOVE = "above"
        BELOW = "below"
        HSIDES = "hsides"
        LHS = "lhs"
        RHS = "rhs"
        VSIDES = "vsides"
        BOX = "box"
        BORDER = "border"

    class Rules(Enum):
        """
        :cvar NONE_VALUE:
        :cvar GROUPS:
        :cvar ROWS:
        :cvar COLS:
        :cvar ALL:
        """
        NONE_VALUE = "none"
        GROUPS = "groups"
        ROWS = "rows"
        COLS = "cols"
        ALL = "all"


@dataclass
class StrucDocItem:
    """
    :ivar content_any:
    :ivar caption:
    :ivar content:
    :ivar link_html:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar render_multi_media:
    :ivar paragraph:
    :ivar list_value:
    :ivar table:
    :ivar id:
    :ivar language:
    :ivar style_code:
    """
    class Meta:
        name = "StrucDoc.Item"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata=dict(
            name="linkHtml",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    footnote: List["StrucDocFootnote"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata=dict(
            name="renderMultiMedia",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    paragraph: List[StrucDocParagraph] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    list_value: List["StrucDocList"] = field(
        default_factory=list,
        metadata=dict(
            name="list",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    table: List[StrucDocTable] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class StrucDocList:
    """
    :ivar caption:
    :ivar item:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar list_type:
    """
    class Meta:
        name = "StrucDoc.List"

    caption: Optional[StrucDocCaption] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3"
        )
    )
    item: List[StrucDocItem] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    list_type: StrucDocListListType = field(
        default=StrucDocListListType.UNORDERED,
        metadata=dict(
            name="listType",
            type="Attribute"
        )
    )


@dataclass
class StrucDocFootnote:
    """
    :ivar content_any:
    :ivar content:
    :ivar link_html:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar render_multi_media:
    :ivar paragraph:
    :ivar list_value:
    :ivar table:
    :ivar id:
    :ivar language:
    :ivar style_code:
    """
    class Meta:
        name = "StrucDoc.Footnote"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    link_html: List["StrucDocLinkHtml"] = field(
        default_factory=list,
        metadata=dict(
            name="linkHtml",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata=dict(
            name="renderMultiMedia",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    paragraph: List[StrucDocParagraph] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    list_value: List[StrucDocList] = field(
        default_factory=list,
        metadata=dict(
            name="list",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List[StrucDocTable] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class StrucDocLinkHtml:
    """
    :ivar content:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar name:
    :ivar href:
    :ivar rel:
    :ivar rev:
    :ivar title:
    :ivar id:
    :ivar language:
    :ivar style_code:
    """
    class Meta:
        name = "StrucDoc.LinkHtml"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote: List[StrucDocFootnote] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    href: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rel: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    rev: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class StrucDocContent:
    """
    :ivar content_any:
    :ivar content:
    :ivar link_html:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar render_multi_media:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar revised:
    """
    class Meta:
        name = "StrucDoc.Content"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List["StrucDocContent"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    link_html: List[StrucDocLinkHtml] = field(
        default_factory=list,
        metadata=dict(
            name="linkHtml",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote: List[StrucDocFootnote] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata=dict(
            name="renderMultiMedia",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    revised: Optional["StrucDocContent.Revised"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Revised(Enum):
        """
        :cvar INSERT:
        :cvar DELETE:
        """
        INSERT = "insert"
        DELETE = "delete"


@dataclass
class StrucDocText:
    """
    :ivar content_any:
    :ivar content:
    :ivar link_html:
    :ivar sub:
    :ivar sup:
    :ivar br:
    :ivar footnote:
    :ivar footnote_ref:
    :ivar render_multi_media:
    :ivar paragraph:
    :ivar list_value:
    :ivar table:
    :ivar id:
    :ivar language:
    :ivar style_code:
    :ivar media_type:
    """
    class Meta:
        name = "StrucDoc.Text"

    content_any: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List[StrucDocContent] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    link_html: List[StrucDocLinkHtml] = field(
        default_factory=list,
        metadata=dict(
            name="linkHtml",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sub: List[StrucDocSub] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    sup: List[StrucDocSup] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    br: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote: List[StrucDocFootnote] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    footnote_ref: List[StrucDocFootnoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="footnoteRef",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    render_multi_media: List[StrucDocRenderMultiMedia] = field(
        default_factory=list,
        metadata=dict(
            name="renderMultiMedia",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    paragraph: List[StrucDocParagraph] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    list_value: List[StrucDocList] = field(
        default_factory=list,
        metadata=dict(
            name="list",
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    table: List[StrucDocTable] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:hl7-org:v3",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    style_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="styleCode",
            type="Attribute",
            tokens=True
        )
    )
    media_type: str = field(
        init=False,
        default="text/x-hl7-text+xml",
        metadata=dict(
            name="mediaType",
            type="Attribute"
        )
    )
