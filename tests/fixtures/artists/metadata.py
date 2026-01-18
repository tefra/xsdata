from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlPeriod

__NAMESPACE__ = "http://musicbrainz.org/ns/mmd-2.0#"


@dataclass
class Alias:
    class Meta:
        name = "alias"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    locale: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sort_name: str | None = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    type_id: str | None = field(
        default=None,
        metadata={
            "name": "type-id",
            "type": "Attribute",
        },
    )
    primary: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class BeginArea:
    class Meta:
        name = "begin-area"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sort_name: str | None = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Gender:
    class Meta:
        name = "gender"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class IpiList:
    class Meta:
        name = "ipi-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    ipi: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class IsniList:
    class Meta:
        name = "isni-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    isni: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Iso31661CodeList:
    class Meta:
        name = "iso-3166-1-code-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    iso_3166_1_code: str | None = field(
        default=None,
        metadata={
            "name": "iso-3166-1-code",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Iso31662CodeList:
    class Meta:
        name = "iso-3166-2-code-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    iso_3166_2_code: str | None = field(
        default=None,
        metadata={
            "name": "iso-3166-2-code",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class LifeSpan:
    class Meta:
        name = "life-span"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    begin: XmlDate | XmlPeriod | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    end: XmlDate | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ended: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class AliasList:
    class Meta:
        name = "alias-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    count: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    alias: list[Alias] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Area:
    class Meta:
        name = "area"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sort_name: str | None = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        },
    )
    iso_3166_1_code_list: Iso31661CodeList | None = field(
        default=None,
        metadata={
            "name": "iso-3166-1-code-list",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class EndArea:
    class Meta:
        name = "end-area"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sort_name: str | None = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        },
    )
    iso_3166_2_code_list: Iso31662CodeList | None = field(
        default=None,
        metadata={
            "name": "iso-3166-2-code-list",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Artist:
    class Meta:
        name = "artist"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    type_id: str | None = field(
        default=None,
        metadata={
            "name": "type-id",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sort_name: str | None = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        },
    )
    disambiguation: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ipi: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ipi_list: IpiList | None = field(
        default=None,
        metadata={
            "name": "ipi-list",
            "type": "Element",
        },
    )
    isni_list: IsniList | None = field(
        default=None,
        metadata={
            "name": "isni-list",
            "type": "Element",
            "required": True,
        },
    )
    gender: Gender | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    country: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    area: Area | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    begin_area: BeginArea | None = field(
        default=None,
        metadata={
            "name": "begin-area",
            "type": "Element",
            "required": True,
        },
    )
    end_area: EndArea | None = field(
        default=None,
        metadata={
            "name": "end-area",
            "type": "Element",
        },
    )
    life_span: LifeSpan | None = field(
        default=None,
        metadata={
            "name": "life-span",
            "type": "Element",
            "required": True,
        },
    )
    alias_list: AliasList | None = field(
        default=None,
        metadata={
            "name": "alias-list",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Metadata:
    class Meta:
        name = "metadata"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    artist: Artist | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
