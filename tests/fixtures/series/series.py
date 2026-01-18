from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass
class Country:
    class Meta:
        name = "country"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timezone: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Externals:
    class Meta:
        name = "externals"

    tvrage: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    thetvdb: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imdb: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Image:
    class Meta:
        name = "image"

    medium: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    original: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Previousepisode:
    class Meta:
        name = "previousepisode"

    href: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Rating:
    class Meta:
        name = "rating"

    average: None | float = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Schedule:
    class Meta:
        name = "schedule"

    time: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    days: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Self:
    class Meta:
        name = "self"

    href: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Links:
    class Meta:
        name = "_links"

    self_value: None | Self = field(
        default=None,
        metadata={
            "name": "self",
            "type": "Element",
            "required": True,
        },
    )
    previousepisode: None | Previousepisode = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Network:
    class Meta:
        name = "network"

    id: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    country: None | Country = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Series:
    class Meta:
        name = "series"

    id: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    genres: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    runtime: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    premiered: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    official_site: None | str = field(
        default=None,
        metadata={
            "name": "officialSite",
            "type": "Element",
            "required": True,
        },
    )
    schedule: None | Schedule = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rating: None | Rating = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    weight: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    network: None | Network = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    web_channel: None | object = field(
        default=None,
        metadata={
            "name": "webChannel",
            "type": "Element",
        },
    )
    externals: None | Externals = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    image: None | Image = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    summary: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    updated: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    links: None | Links = field(
        default=None,
        metadata={
            "name": "_links",
            "type": "Element",
        },
    )
