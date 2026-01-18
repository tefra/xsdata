from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass
class Country:
    class Meta:
        name = "country"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    code: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timezone: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Externals:
    class Meta:
        name = "externals"

    tvrage: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    thetvdb: int | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imdb: str | None = field(
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

    medium: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    original: str | None = field(
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

    href: str | None = field(
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

    average: float | None = field(
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

    time: str | None = field(
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

    href: str | None = field(
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

    self_value: Self | None = field(
        default=None,
        metadata={
            "name": "self",
            "type": "Element",
            "required": True,
        },
    )
    previousepisode: Previousepisode | None = field(
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

    id: int | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    country: Country | None = field(
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

    id: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    url: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    language: str | None = field(
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
    status: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    runtime: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    premiered: XmlDate | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    official_site: str | None = field(
        default=None,
        metadata={
            "name": "officialSite",
            "type": "Element",
            "required": True,
        },
    )
    schedule: Schedule | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rating: Rating | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    weight: int | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    network: Network | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    web_channel: object | None = field(
        default=None,
        metadata={
            "name": "webChannel",
            "type": "Element",
        },
    )
    externals: Externals | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    image: Image | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    summary: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    updated: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    links: Links | None = field(
        default=None,
        metadata={
            "name": "_links",
            "type": "Element",
        },
    )
