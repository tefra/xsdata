from dataclasses import dataclass, field
from typing import List, Optional, Union
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
        }
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "type-id",
            "type": "Attribute",
        }
    )
    primary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
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
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
        }
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
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IpiList:
    class Meta:
        name = "ipi-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    ipi: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class IsniList:
    class Meta:
        name = "isni-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    isni: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
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
        }
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
        }
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
        }
    )
    end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ended: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
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
        }
    )
    alias: List[Alias] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
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
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
        }
    )
    iso_3166_1_code_list: Optional[Iso31661CodeList] = field(
        default=None,
        metadata={
            "name": "iso-3166-1-code-list",
            "type": "Element",
        }
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
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
        }
    )
    iso_3166_2_code_list: Optional[Iso31662CodeList] = field(
        default=None,
        metadata={
            "name": "iso-3166-2-code-list",
            "type": "Element",
        }
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
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "type-id",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sort_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sort-name",
            "type": "Element",
        }
    )
    disambiguation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ipi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ipi_list: Optional[IpiList] = field(
        default=None,
        metadata={
            "name": "ipi-list",
            "type": "Element",
        }
    )
    isni_list: Optional[IsniList] = field(
        default=None,
        metadata={
            "name": "isni-list",
            "type": "Element",
        }
    )
    gender: Optional[Gender] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    area: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    begin_area: Optional[BeginArea] = field(
        default=None,
        metadata={
            "name": "begin-area",
            "type": "Element",
        }
    )
    end_area: Optional[EndArea] = field(
        default=None,
        metadata={
            "name": "end-area",
            "type": "Element",
        }
    )
    life_span: Optional[LifeSpan] = field(
        default=None,
        metadata={
            "name": "life-span",
            "type": "Element",
        }
    )
    alias_list: Optional[AliasList] = field(
        default=None,
        metadata={
            "name": "alias-list",
            "type": "Element",
        }
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
        }
    )
