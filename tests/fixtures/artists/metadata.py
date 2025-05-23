from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

__NAMESPACE__ = "http://musicbrainz.org/ns/mmd-2.0#"


@dataclass
class Alias:
    class Meta:
        name = "alias"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    locale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    type_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "type-id",
            "type": "Attribute",
        },
    )
    primary: Optional[str] = field(
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

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sort_name: Optional[str] = field(
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

    id: Optional[str] = field(
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

    iso_3166_1_code: Optional[str] = field(
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

    iso_3166_2_code: Optional[str] = field(
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

    begin: Optional[Union[XmlDate, XmlPeriod]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ended: Optional[bool] = field(
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

    count: Optional[int] = field(
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

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        },
    )
    iso_3166_1_code_list: Optional[Iso31661CodeList] = field(
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

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        },
    )
    iso_3166_2_code_list: Optional[Iso31662CodeList] = field(
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

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    type_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "type-id",
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        },
    )
    disambiguation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ipi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ipi_list: Optional[IpiList] = field(
        default=None,
        metadata={
            "name": "ipi-list",
            "type": "Element",
        },
    )
    isni_list: Optional[IsniList] = field(
        default=None,
        metadata={
            "name": "isni-list",
            "type": "Element",
            "required": True,
        },
    )
    gender: Optional[Gender] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    area: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    begin_area: Optional[BeginArea] = field(
        default=None,
        metadata={
            "name": "begin-area",
            "type": "Element",
            "required": True,
        },
    )
    end_area: Optional[EndArea] = field(
        default=None,
        metadata={
            "name": "end-area",
            "type": "Element",
        },
    )
    life_span: Optional[LifeSpan] = field(
        default=None,
        metadata={
            "name": "life-span",
            "type": "Element",
            "required": True,
        },
    )
    alias_list: Optional[AliasList] = field(
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

    artist: Optional[Artist] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
