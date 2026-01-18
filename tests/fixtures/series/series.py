from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class Country:
    class Meta:
        name = "country"

    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    code: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    timezone: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Externals:
    class Meta:
        name = "externals"

    tvrage: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    thetvdb: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imdb: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Image:
    class Meta:
        name = "image"

    medium: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    original: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Previousepisode:
    class Meta:
        name = "previousepisode"

    href: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Rating:
    class Meta:
        name = "rating"

    average: float = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Schedule:
    class Meta:
        name = "schedule"

    time: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    days: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Self:
    class Meta:
        name = "self"

    href: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Links:
    class Meta:
        name = "_links"

    self_value: Self = field(
        metadata={
            "name": "self",
            "type": "Element",
            "required": True,
        }
    )
    previousepisode: Previousepisode = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Network:
    class Meta:
        name = "network"

    id: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    country: Country = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Series:
    class Meta:
        name = "series"

    id: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    language: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    genres: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    status: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    runtime: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    premiered: XmlDate = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    official_site: str = field(
        metadata={
            "name": "officialSite",
            "type": "Element",
            "required": True,
        }
    )
    schedule: Schedule = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    rating: Rating = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    weight: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    network: Network = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    web_channel: None | object = field(
        default=None,
        metadata={
            "name": "webChannel",
            "type": "Element",
        },
    )
    externals: Externals = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    image: None | Image = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    summary: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    updated: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    links: None | Links = field(
        default=None,
        metadata={
            "name": "_links",
            "type": "Element",
        },
    )
