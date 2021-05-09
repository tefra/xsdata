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
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
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
        }
    )
    original: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
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
        }
    )
    days: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SelfType:
    class Meta:
        name = "self"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Links:
    class Meta:
        name = "_links"

    self_value: Optional[SelfType] = field(
        default=None,
        metadata={
            "name": "self",
            "type": "Element",
        }
    )
    previousepisode: Optional[Previousepisode] = field(
        default=None,
        metadata={
            "type": "Element",
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
        }
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "type": "Element",
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
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    genres: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    runtime: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    premiered: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    official_site: Optional[str] = field(
        default=None,
        metadata={
            "name": "officialSite",
            "type": "Element",
        }
    )
    schedule: Optional[Schedule] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rating: Optional[Rating] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    weight: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    web_channel: Optional[object] = field(
        default=None,
        metadata={
            "name": "webChannel",
            "type": "Element",
        }
    )
    network: Optional[Network] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    externals: Optional[Externals] = field(
        default=None,
        metadata={
            "type": "Element",
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
        }
    )
    updated: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    links: Optional[Links] = field(
        default=None,
        metadata={
            "name": "_links",
            "type": "Element",
        }
    )
