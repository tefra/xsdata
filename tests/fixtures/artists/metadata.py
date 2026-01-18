from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlPeriod

__NAMESPACE__ = "http://musicbrainz.org/ns/mmd-2.0#"


@dataclass(kw_only=True)
class Alias:
    class Meta:
        name = "alias"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    locale: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sort_name: str = field(
        metadata={
            "name": "sort-name",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    type_id: None | str = field(
        default=None,
        metadata={
            "name": "type-id",
            "type": "Attribute",
        },
    )
    primary: None | str = field(
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


@dataclass(kw_only=True)
class BeginArea:
    class Meta:
        name = "begin-area"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sort_name: str = field(
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Gender:
    class Meta:
        name = "gender"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Iso31661CodeList:
    class Meta:
        name = "iso-3166-1-code-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    iso_3166_1_code: str = field(
        metadata={
            "name": "iso-3166-1-code",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Iso31662CodeList:
    class Meta:
        name = "iso-3166-2-code-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    iso_3166_2_code: str = field(
        metadata={
            "name": "iso-3166-2-code",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LifeSpan:
    class Meta:
        name = "life-span"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    begin: XmlDate | XmlPeriod = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    end: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ended: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AliasList:
    class Meta:
        name = "alias-list"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    alias: list[Alias] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Area:
    class Meta:
        name = "area"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sort_name: str = field(
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        }
    )
    iso_3166_1_code_list: Iso31661CodeList = field(
        metadata={
            "name": "iso-3166-1-code-list",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EndArea:
    class Meta:
        name = "end-area"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sort_name: str = field(
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        }
    )
    iso_3166_2_code_list: Iso31662CodeList = field(
        metadata={
            "name": "iso-3166-2-code-list",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Artist:
    class Meta:
        name = "artist"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    type_id: str = field(
        metadata={
            "name": "type-id",
            "type": "Attribute",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sort_name: str = field(
        metadata={
            "name": "sort-name",
            "type": "Element",
            "required": True,
        }
    )
    disambiguation: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ipi: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ipi_list: None | IpiList = field(
        default=None,
        metadata={
            "name": "ipi-list",
            "type": "Element",
        },
    )
    isni_list: IsniList = field(
        metadata={
            "name": "isni-list",
            "type": "Element",
            "required": True,
        }
    )
    gender: None | Gender = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    country: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    area: Area = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    begin_area: BeginArea = field(
        metadata={
            "name": "begin-area",
            "type": "Element",
            "required": True,
        }
    )
    end_area: None | EndArea = field(
        default=None,
        metadata={
            "name": "end-area",
            "type": "Element",
        },
    )
    life_span: LifeSpan = field(
        metadata={
            "name": "life-span",
            "type": "Element",
            "required": True,
        }
    )
    alias_list: AliasList = field(
        metadata={
            "name": "alias-list",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Metadata:
    class Meta:
        name = "metadata"
        namespace = "http://musicbrainz.org/ns/mmd-2.0#"

    artist: Artist = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
