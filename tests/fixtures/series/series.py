from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate


@dataclass
class Country:
    class Meta:
        name = "country"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    timezone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Externals:
    class Meta:
        name = "externals"

    tvrage: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    thetvdb: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    imdb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Image:
    class Meta:
        name = "image"

    medium: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    original: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Previousepisode:
    class Meta:
        name = "previousepisode"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Rating:
    class Meta:
        name = "rating"

    average: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Schedule:
    class Meta:
        name = "schedule"

    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    days: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Self:
    class Meta:
        name = "self"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Links:
    class Meta:
        name = "_links"

    self_value: Optional[Self] = field(
        default=None,
        metadata={
            "name": "self",
            "type": "Element",
            "required": True,
        }
    )
    previousepisode: Optional[Previousepisode] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Network:
    class Meta:
        name = "network"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Series:
    class Meta:
        name = "series"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    genres: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    runtime: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    premiered: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    official_site: Optional[str] = field(
        default=None,
        metadata={
            "name": "officialSite",
            "type": "Element",
            "required": True,
        }
    )
    schedule: Optional[Schedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    rating: Optional[Rating] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    weight: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    network: Optional[Network] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    web_channel: Optional[object] = field(
        default=None,
        metadata={
            "name": "webChannel",
            "type": "Element",
        }
    )
    externals: Optional[Externals] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    image: Optional[Image] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    updated: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    links: Optional[Links] = field(
        default=None,
        metadata={
            "name": "_links",
            "type": "Element",
        }
    )
